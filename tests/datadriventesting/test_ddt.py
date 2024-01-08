# Read the Excel or CSV file
# We create a function that takes the value from the Excel/CSV file
# and at the end verify the expected result

# Read the Excel file - library ->> openpyxl
import openpyxl

import requests
import pytest

# Read a file and add into a [array]