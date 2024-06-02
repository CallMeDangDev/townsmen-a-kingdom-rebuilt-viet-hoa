import openpyxl

# Load the Excel file
workbook = openpyxl.load_workbook('en.xlsx')
sheet = workbook.active

# Open the output file
output_file = open('pre-en.strings', 'w', encoding='utf-8')

# Iterate through each row in the sheet
for row in sheet.iter_rows(values_only=True):
    if len(row) >= 2:
        key = row[0]
        value = row[1]
        output_file.write(f'"{key}" = "{value}";\n')

# Close the output file
output_file.close()