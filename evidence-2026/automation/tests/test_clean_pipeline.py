import csv
import json
import sys
from pathlib import Path
import pytest
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from clean_pipeline import normalize_record, run

VALID = {'record_id':'abc-2','full_name':' Mary  Jones ', 'email':'  Mary@Example.com  ', 'source':'Web', 'priority':'HIGH'}

def test_normalizes_fields():
    good,error = normalize_record(VALID)
    assert error is None
    assert good == {'record_id':'ABC-2','full_name':'Mary Jones','email':'mary@example.com','source':'web','priority':'high'}

@pytest.mark.parametrize('change,reason',[
    ({'record_id':''},'missing_record_id'),
    ({'full_name':' '},'missing_name'),
    ({'email':'not-an-email'},'invalid_email'),
    ({'source':'mail'},'unsupported_source'),
    ({'priority':'urgent'},'invalid_priority'),
])
def test_rejects_invalid_values(change,reason):
    v={**VALID,**change}
    assert normalize_record(v)[1]==reason

def test_deduplicates_and_preserves_first(tmp_path):
    sample = tmp_path/'data.csv'
    with sample.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(VALID));w.writeheader()
        w.writerow(VALID);w.writerow({**VALID,'email':'other@example.com','record_id':'ABC-2'})
    result=run(sample,tmp_path/'out')
    assert result['accepted_rows']==1
    assert result['quarantined_rows']==1
    assert result['reasons']=={'duplicate_record_id':1}
    assert 'mary@example.com' in (tmp_path/'out'/'cleaned.csv').read_text()


def test_missing_columns_fail(tmp_path):
    p=tmp_path/'bad.csv';p.write_text('record_id,name\nA,John\n')
    with pytest.raises(ValueError,match='columns'):
        run(p,tmp_path/'out')


def test_blank_data_is_not_a_false_success(tmp_path):
    p=tmp_path/'empty.csv';p.write_text(','.join(VALID)+'\n')
    result=run(p,tmp_path/'out')
    assert result['total_rows']==0
    assert result['acceptance_rate']==0


def test_json_report_matches_csv_rows(tmp_path):
    data=Path(__file__).resolve().parents[1]/'data'/'sample_leads.csv'
    report=run(data,tmp_path/'results')
    saved=json.loads((tmp_path/'results'/'qa_report.json').read_text())
    assert report==saved
    assert report['total_rows']==report['accepted_rows']+report['quarantined_rows']