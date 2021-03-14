import csv
f=open("fruits.csv","w")
writer=csv.DictWriter(f,fieldnames=["fruit","count"])
writer.writeheader()#writeheader() write headers to the csvfile
writer.writerow({"fruit":"Apple","count":"1"})
writer.writerow({"fruit":"Banana","count":"2"})
f.close()
c=0
f=open("fruits.csv")
reader=csv.DictReader(f)
for row in reader:
    if c==0:
        print(f'{" ".join(row)}')
    print(f'{row["fruit"]},{row["count"]}')
f.close()