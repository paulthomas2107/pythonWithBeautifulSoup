from bs4 import BeautifulSoup
import requests
import re

with open("index.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")

print(doc.prettify())

tag = doc.title
print(tag)
print(tag.string)

tag.string = "Paul's File"
print(tag)

tag = doc.find("a")
print (tag)

tag = doc.find_all("p")
print (tag)
print (tag[0])

tag = doc.find_all("b")
print (tag)
print (tag[0])


url = "https://www.newegg.ca/gigabyte-geforce-rtx-3080-ti-gv-n308tgaming-oc-12gd/p/N82E16814932436?Description=3080&cm_re=3080-_-14-932-436-_-Product"
result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")
prices = doc.find_all(text="$")
parent = prices[0].parent
strong = parent.find("strong")
print(strong)
print(strong.string)


with open("index2.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")

tag = doc.find("option")
tag['value'] = 'new value'
print(tag)

tags = doc.find_all(["p", "div", "li"])
print(tags)

tags = doc.find_all(["option"], text="Undergraduate")
print(tags)

tags = doc.find_all(["option"], text="Undergraduate", value="undergraduate")
print(tags)

tags = doc.find_all(class_="btn-item")
print(tags)

tags = doc.find_all(text=re.compile("\$.*"))
for tag in tags:
    print(tag.strip())

tags = doc.find_all(text=re.compile("\$.*"), limit=1)
for tag in tags:
    print(tag.strip())

tags = doc.find_all("input", type="text")
for tag in tags:
    tag['placeholder'] = 'I changed You !'
with open("changed.html", "w") as file:
    file.write(str(doc))




