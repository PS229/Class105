import csv
import math
import statistics

with open("class2.csv", newline = "") as f:
    reader = csv.reader(f)
    fileData = list(reader)
fileData.pop(0)

totalMarks = 0
totalEntries = len(fileData)

for i in fileData:
    totalMarks = float(i[1]) + totalMarks
mean = totalMarks/totalEntries
add1 = 0
for i in fileData:
    sub = float(i[1]) - mean
    sqr = sub**2
    add1 = sqr + add1
step2 = add1/totalEntries
st_dev = math.sqrt(step2)
print(st_dev)

st = []

for i in fileData:
    st.append(float(i[1]))

stan = statistics.stdev(st)
print(stan)