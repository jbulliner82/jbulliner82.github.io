# Technical evidence and project case studies

**Owner:** Joseph Bulliner · **Date:** October 18, 2026  
All new demos in this package use **fictional or synthetic data only**.

## 1. Parcel Evidence Lab — interactive research triage
**Problem:** Parcel listing details are frequently incomplete or inconsistent. Buyers need a visible way to separate claims from missing documents and identify the next source to check.

**Implementation:** Browser-only responsive HTML/CSS/JavaScript. Eight fictional parcels, free-text filtering, acreage/price controls, selected-record view, six evidence criteria, deterministic gap score, saved selection via localStorage, and JSON export.

**Scoring:** Access 25, well 10, septic 15, electric 10, flood 25, deed/title 15 points. A flag is added for values `unknown`, `claimed`, `needs-review` or `elevated-demo`. Weight sum is 100. The number **measures unresolved diligence indicators in sample data**, not market value or actual risk.

**What it demonstrates:** state management, provenance awareness, business-rule transparency, UX for a complex decision, export, and boundary-aware product language.

**Limitations:** No live GIS, source API integration, appraisal, title review, field inspection, actual flood analysis, or AI integration. The parcel data is entirely synthetic and should not be used for purchasing decisions.

**Next tests:** browser accessibility audit, cross-browser regression, fixture coverage for scoring rules, pagination and offline state, live-data adapters with source freshness and confidence labeling.

## 2. CSV Data Quality Pipeline — repeatable automation
**Problem:** Structured records have inconsistent casing, invalid emails, unsupported categories, and duplicate IDs.

**Implementation:** Python standard library script, CSV input, field normalization, invalid-row quarantine, first-valid-ID deduplication, JSON quality report, and pytest suite.

**Local run at package creation:** 240 deterministic synthetic rows; 187 accepted; 53 quarantined. Reasons: 7 duplicate IDs, 22 invalid emails, 11 invalid priorities, 13 unsupported sources. 10 unit tests passed in a local run.

**Test controls:** seeded deterministic synthetic dataset; acceptance rate reported; output reconciles `accepted + quarantined = input`. One automated unit test checks this reconciliation.

**Limitations:** demonstration email validation rather than RFC-complete validation; no streaming, logging/observability service, database, message queue, user authentication, CI run, or employer deployment. Do not claim saved hours or economic impact.

**Reproduction:** from `automation/`, run `python clean_pipeline.py --out results`, then `python -m pytest -q` (pytest required only for tests).

## 3. ShowUp — existing independent ML repository
**Repository:** https://github.com/jbulliner82/showup-appointment-predictor  
**Observed from public README:** Python/FastAPI/SQLite/scikit-learn, sample-data generation, web dashboard, risk scoring and reported synthetic dataset metrics (e.g., 225 sample appointments and a reported 86.7% accuracy figure).

**Important accuracy note:** The README's marketing claims of '30–40% fewer no-shows' are **not validated clinical or business outcomes**; synthetic offline predictions cannot prove a reduction in cancellations. No live clinical validation or deployment was verified in this portfolio build. Before applying for regulated ML roles, audit the train/test splitting, leakage, class balance, calibration, privacy and data lineage.

## 4. Leadership Under Pressure — interactive instructional design
See `LEARNING_DESIGN_CASE_STUDY.md`. The code is functional, but there is no human-learning outcomes study yet.

## Evidence status ladder
- **Code exists:** the code is included in the package or a GitHub repo.
- **Works locally:** executed using the bundled fixtures.
- **Tested:** automated or browser interaction checks have recorded pass/fail outcomes.
- **Hosted live:** URL opens and the latest version is confirmed.
- **Production-validated:** real users/clients, real data, actual outcomes and independent review. **Not established** for the portfolio demos.