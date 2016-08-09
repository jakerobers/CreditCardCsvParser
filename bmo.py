import csv
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]
results = []

with open(input_file, 'rb') as csvfile:
  reader = csv.DictReader(csvfile)
  for row in reader:
    new_row = {}
  
    if row['Billing Amount'][0] == '(':
      continue

    new_row['Description'] = row['Merchant'][:20]
    new_row['Trans. Date'] = row['Transaction Date']
    new_row['Post Date'] = row['Posting Date']
    new_row['Amount'] = row['Billing Amount'][1:]

    results.append(new_row)

with open(output_file, 'w') as csvfile:
  fieldnames = ['Post Date', 'Trans. Date', 'Amount', 'Description']
  writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
  writer.writeheader()
  for row in results:
    print(row)
    writer.writerow(row)


print("done")
