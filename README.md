# Mathematics

Linear algebra, linear regression, statistics and the math behind deep learning, worked in Python.

## Running it

Python 3.15. One `requirements.txt` covers every folder:

```bash
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
cd Linear_Regression && ../.venv/bin/python predict_life_expectancy.py
```

Run each script from its own folder; the scripts read their data files from there. CI runs every script and the
notebook's code cells on each push and pull request, and Dependabot keeps the packages and actions current.
