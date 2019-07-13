## Main documentation: https://pytest-cov.readthedocs.io/

### pytest --cov=account account/tests/test_models.py

    --cov=account                   - It will give coverage of account folder

    account/tests/test_models.py    - It will give coverage of this test file

### pytest --cov-report=html --cov=account account/tests/test_models.py

    --cov-report=html               - Give report in html format. Will create a directory named 'htmlcov' in the folder from where run pytest. Inside 'htmlcov' folder there is a file 'index.html', when we open this file in browser we can see the test coverage report.

### pytest --cov-report=term --cov=account account/tests/test_models.py

    --cov-report=term               - Will print report in terminal.

### pytest --cov-report=term-missing --cov=account account/tests/test_models.py

    --cov-report=term-missing       - Will print report in terminal with missing lines.

### pytest --cov-report=term:skip-covered --cov=account account/tests/test_models.py

    --cov-report=term:skip-covered  - Will skip 100% covered files in report.

### pytest --cov-report=html --cov-report=xml --cov=account account/tests/test_models.py

    This is also a valid command. It will generate report in two format.
    --cov-report=html               - Will generate report in 'htmlcov' directory
    --cov-report=xml                - Will generate report in 'coverage.xml' file in xml format.
