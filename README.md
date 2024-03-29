# *Python API Automation Framework*

![image](https://github.com/shivam9870/Py1xAPIAutomation/assets/65064937/232c1393-9165-4fe9-bf76-4eba3c86736a)

Hybrid Custom Framework to Test REST APIs

### Tech Stack

1. Python 3.11
2. Requests - HTTP Request
3. PyTest- Testing Framework
4. Reporting - Allure Reports, PyTest HTML
5. Test Data - CSV, JSON, Excel
6. Parallel Execution - x Distribute

## How to install Packages

`` pip install request pytest pytest-html faker allure-pytest jsonschema ``

## To freeze your Package version

`` pip freeze > requirments.txt``

## To install the freeze version

``pip install -r requirments.txt``

### For parallel test_case execution = ``pip install pytest-xdist``

### Code running command =``pytest -n auto tests/integration_test/test_create_booking.py -s -v``

### To work with excel file = ``pip install openpyxl``

### To run the allure reports

> ``pytest tests/datadriventesting/test_ddt.py -s -v --alluredir=./reports``

### To work with JSON SCHEMA
``pip install jsonschema``
