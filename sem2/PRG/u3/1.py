import pandas, openpyxl

excelDataDF = pandas.read_excel('vegetable.xlsx', sheet_name='summer')
print(excelDataDF)