# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 13:07:10 2019

@author: 105028218
"""
#############################################################################
#
# An example of converting a Pandas dataframe to an xlsx file
# with column formats using Pandas and XlsxWriter.
#
# Copyright 2013-2019, John McNamara, jmcnamara@cpan.org
#

import pandas as pd

# Create a Pandas dataframe from some data.
df = pd.DataFrame({'Numbers':    [1010, 2020, 3030, 2020, 1515, 3030, 4545],
                   'Percentage': [.1,   .2,   .33,  .25,  .5,   .75,  .45 ],
})

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter("pandas_column_formats.xlsx", engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer, sheet_name='Sheet1')

# Get the xlsxwriter workbook and worksheet objects.
workbook  = writer.book
worksheet = writer.sheets['Sheet1']

# Add some cell formats.
format1 = workbook.add_format({'num_format': '#,##0.00'})
format2 = workbook.add_format({'num_format': '0%','bold': True,'color':'red'})
format3 = workbook.add_format({'num_format': '0%','bold': True,'color':'red'})
worksheet.set_column('B:B', 18, format1)
worksheet.set_column('C:C', None, format2)
writer.save()