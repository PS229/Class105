import csv
import pandas as pd
import plotly.express as px
with open("class1.csv", newline = "") as f:
    reader = csv.reader(f)
    fileData = list(reader)
fileData.pop(0)

totalMarks = 0
totalEntries = len(fileData)
for i in fileData:
    totalMarks = float(i[1]) + totalMarks
mean = totalMarks/totalEntries
print(mean)

df = pd.read_csv("class1.csv")
fig = px.scatter(df, x = "Student", y = "Marks")
fig.update_layout(shapes = [
    dict(type = "line", y0 = mean, y1 = mean, x0 = 0, x1 = totalEntries)
])
fig.update_yaxes(rangemode = "tozero")
fig.show()