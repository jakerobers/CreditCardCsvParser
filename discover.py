import csv
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]
results = []

with open(input_file, 'rb') as csvfile:
  reader = csv.DictReader(csvfile)
  for row in reader:
    if float(row['Amount']) < 0:
      continue
    row['Description'] = row['Description'][:20]
    results.append(row)

with open(output_file, 'w') as csvfile:
  fieldnames = ['Post Date', 'Trans. Date', 'Amount', 'Description', 'Category']
  writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
  writer.writeheader()
  for row in results:
    writer.writerow(row)


print("done")
