# This TabPy code will use Sample Supertore data and create a wrapped version of Product Name
import pandas as pd
import textwrap

# Max Length of each line of the wrapped string.
maxLength = 25


# Create a wrapped string of "maxLength" and return it.
def wrap_string(stringToWrap):
    return textwrap.fill(stringToWrap, maxLength)


# Create a new field with the wrapped Product Name.
# Note: "apply" calls the specified function for each row in the data frame.
def wrap_product(input):
    return pd.DataFrame({
        'Row ID'            : input['Row ID'],
        'Order ID'          : input['Order ID'],
        'Order Date'        : input['Order Date'],
        'Ship Date'         : input['Ship Date'],
        'Ship Mode'         : input['Ship Mode'],
        'Customer ID'       : input['Customer ID'],
        'Customer Name'     : input['Customer Name'],
        'Segment'           : input['Segment'],
        'Country/Region'    : input['Country/Region'],
        'City'              : input['City'],
        'State/Province'    : input['State/Province'],
        'Postal Code'       : input['Postal Code'],
        'Region'            : input['Region'],
        'Product ID'        : input['Product ID'],
        'Category'          : input['Category'],
        'Sub-Category'      : input['Sub-Category'],
        'Product Name'      : input['Product Name'],
        'Product Name Wrap' : input['Product Name'].apply(wrap_string),
        'Sales'             : input['Sales'],
        'Quantity'          : input['Quantity'],
        'Discount'          : input['Discount'],
        'Profit'            : input['Profit'],
    })


# Define the Output Schema.
def get_output_schema():
    return pd.DataFrame({
        'Row ID'            : prep_int(),
        'Order ID'          : prep_string(),
        'Order Date'        : prep_string(),
        'Ship Date'         : prep_string(),
        'Ship Mode'         : prep_string(),
        'Customer ID'       : prep_string(),
        'Customer Name'     : prep_string(),
        'Segment'           : prep_string(),
        'Country/Region'    : prep_string(),
        'City'              : prep_string(),
        'State/Province'    : prep_string(),
        'Postal Code'       : prep_string(),
        'Region'            : prep_string(),
        'Product ID'        : prep_string(),
        'Category'          : prep_string(),
        'Sub-Category'      : prep_string(),
        'Product Name'      : prep_string(),
        'Product Name Wrap' : prep_string(),
        'Sales'             : prep_decimal(),
        'Quantity'          : prep_int(),
        'Discount'          : prep_decimal(),
        'Profit'            : prep_decimal(),
    })