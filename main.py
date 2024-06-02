import csv

# open the text file in read, using UTF-8 encoding
text_file = open('en.strings', 'r', encoding='utf-8')

# open a csv file in write
csv_file = open('output.csv', 'w', newline='', encoding='utf-8')

# create a csv writer object
csv_writer = csv.writer(csv_file)

# write the header
csv_writer.writerow(["Key", "Value"])

for line in text_file:
    # split the line into key and value, remove the quotes and the ending semicolon
    key, value = line.split(" = ", 1)
    key = key.strip('"')
    value = value.strip('";\n')

    # write the key and value to the CSV file
    csv_writer.writerow([key, value])

# close the files
text_file.close()
csv_file.close()

print("Conversion to CSV completed.")