# simple example of matching data sets
import csv

def read_file(name):
    with open(name, 'r') as input_file:
        reader = csv.DictReader(input_file, delimiter = '|')
        data = []
        for row in reader:
            data.append(row)
            
    return data

data_files = [ 
    '/Users/alitopaloglu/Downloads/pythonlab-classes-master/name-address.psv',
    '/Users/alitopaloglu/Downloads/pythonlab-classes-master/name-bank-email.psv'
]
# the path I mentioned in the summary is in the example list above. 

#dict = {'name': 'Rami',
#       'address': 'None of your business'}

data_sets = {}

for filename in data_files:
    contents = read_file(filename)
    data_sets[filename] = contents #we put in contets of that file to our empty dicitionary
    
joined_data = {}
for data_set_name in data_sets:
    data_set = data_sets[data_set_name]
    for row in data_set:
        key = row['name']
        key = key.strip()
        key = key.lower()
        if key not in joined_data:
            joined_data[key] = row
        else:
            data = joined_data[key]
            data.update(row)

for row in joined_data.values():
    raw_data = row.values()
    print "\t".join(raw_data)
