# Joseph Bulliner — Evidence Portfolio / October 2026

This package is an applicant-owned, reproducible set of **independent demonstration projects** for recruiters and technical reviewers. It complements Joseph Bulliner's existing public GitHub profile and hiring portfolio.

## Start here

1. Open `index.html` in Chrome, Safari, Firefox, or Edge (or serve the folder locally with `python -m http.server 8000`).
2. Explore `parcel-lab.html` and `learning-lab.html` without credentials.
3. From the `automation/` directory, execute:

   ```sh
   python clean_pipeline.py --out results
   python -m pytest -q
   ```

4. Review `docs/TECHNICAL_CASE_STUDIES.md`, `docs/LEARNING_DESIGN_CASE_STUDY.md`, screenshots and the tailored resume files.

## Verified in this build
- The standalone Python data-quality pipeline completed a controlled run against 240 seeded, artificial records.
- Ten pytest tests passed in the local environment.
- Browser screenshots were captured from executable demo HTML via headless Chromium (see `local package: assets/screenshots`).

## No invented outcomes
No business revenue, payroll savings, enterprise deployment, customer adoption, employee learning gains, clinical outcomes, or live property validation is represented by this kit. Its metrics are sample/test outcomes. Existing GitHub work is separate and is not rewritten as client work.

## Public profile
- GitHub: https://github.com/jbulliner82
- Existing hiring site: https://jbulliner82.github.io/hire-joseph-bulliner/
- Existing ML demonstration: https://github.com/jbulliner82/showup-appointment-predictor

## Safe publication
Avoid adding personal addresses, phone numbers, credentials, API keys, employer records, real customers' private data or healthcare data to a public repository. This package uses fictional examples and can be republished safely after manual review.
## Public interactive demos
- [Portfolio homepage](https://jbulliner82.github.io/evidence-2026/)
- [Leadership scenario course](https://jbulliner82.github.io/evidence-2026/learning-lab.html)
- [Parcel evidence demonstration](https://jbulliner82.github.io/evidence-2026/parcel-lab.html)

## Reproducible source
Run `python -m pytest -q` from the `automation` folder after installing pytest. All data is synthetic and no employer outcomes are claimed.
