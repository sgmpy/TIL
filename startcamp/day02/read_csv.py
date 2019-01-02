import csv
with open('lunch.csv','r',encoding='utf8') as f:
    #lines = f.readlines()
    items = csv.reader(f)
    for item in items:
        print(item)