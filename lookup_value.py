# -*- coding: utf-8 -*-
"""
Complete the function, lookup_value(col_name, row_id, header, data_rows), to look up a particular value in the data when stored as shown above. In particular, the parameters of the function are

col_name: Name of the column, e.g., 'school', 'address', 'freetime'.
row_id: The desired row number, starting at 0 (the first data row).
header, data_rows: The list of column names and data rows, respectively.
For example, consider the math data shown above. Then,

    lookup_value('age', 0, math_header, math_data_rows) == '18'
    lookup_value('G2', 3, math_header, math_data_rows) == '14'
"""

def read_csv(filename):
    with open(filename) as fp:
        from csv import reader
        data_rows = list(reader(fp))
    header = data_rows.pop(0)
    return (header, data_rows)

# Read the math class data
math_header, math_data_rows = read_csv('student-mat.csv')

# Read the Portuguese class data
port_header, port_data_rows = read_csv('student-por.csv')
#print math_header


def lookup_value(col_name, row_id, header, data_rows):
 #   assert col_name in header, "{} not in {}".format(col_name, header)
 #   assert 0 <= row_id < len(data_rows)
    col_i=math_header.index(col_name)
    return data_rows[row_id][col_i]
    
lookup_value('age', 0, math_header, math_data_rows) 

''' Suppose we wish to extract a list of all values stored in a given column of the table. Complete the function, lookup_column_values(col, header, data_rows), which takes as input the column name col, list of column names header, and rows data_rows, and returns a list of all the values stored in that column.

For example, the first five entries of the returned list when reference the 'age' column of the math class data should satisfy:

  values = lookup_column_values('age', math_header, math_data_rows)
  assert values[:5] == ['18', '17', '15', '15', '16']''' 

def lookup_column_values(col, header, data_rows):
    assert col in header
    col_i=math_header.index(col_name)
    return data_rows[][col_i]

def lookup_column_values(col, header, data_rows):
    assert col in header
    col_i=header.index(col)
    cols=[data[col_i] for data in data_rows]
    cols=[]
    for data in data_rows:
        cols.append(data[col_i])
    return cols
    