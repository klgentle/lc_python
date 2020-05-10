import sys

data = ""
with open("star_data.txt","r") as f:
    data = f.readlines()
for row in map(lambda x: x.rstrip().split(":"), data):
    #print("<tr><td>" + "</td><td>".join(row) + "</td></tr>")
    print("<tr><td>" + "</td><td>".join([i.rstrip() for i in row]) + "</td></tr>")
