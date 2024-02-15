import csv
with open("filepath here") as file:
    reader = csv.reader(file, delimiter=',')
    for line in reader:
        print(line)
        
