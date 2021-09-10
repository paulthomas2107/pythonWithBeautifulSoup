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


url ="https://coinmarketcap.com/"
result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")

# Get crypto prices
tbody = doc.tbody
trs = tbody.contents

prices = {}

for tr in trs[:10]:
    name, price = tr.contents[2:4]
    fixed_name = name.p.string
    fixed_price = price.a.string
    prices[fixed_name] = fixed_price

print(prices)

search_term = '3070'
url = f"https://www.newegg.ca/p/pl?d={search_term}&N=4131"
page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")

page_text = doc.find(class_="list-tool-pagination-text").strong
pages = int(str(page_text).split("/")[-2].split(">")[-1][:-1])
items_found = {}

print("_____________________________________________________________________")
for page in range(1, pages + 1):
    url = f"https://www.newegg.ca/p/pl?d={search_term}&N=4131&page={page}"
    page = requests.get(url).text
    doc = BeautifulSoup(page, "html.parser")
    div = doc.find(class_="item-cells-wrap border-cells items-grid-view four-cells expulsion-one-cell")
    items = div.find_all(text=re.compile(search_term))
    for item in items:
        parent = item.parent
        if parent.name != "a":
            continue
        link = parent["href"]
        next_parent = item.find_parent(class_="item-container")
        try:
            price = next_parent.find(class_="price-current").find("strong").string
            items_found[item] = {"price": int(price.replace(",", "")), "link": link}
        except:
            pass


sorted_items = sorted(items_found.items(), key=lambda x: x[1]['price'])

for item in sorted_items:
    print(item[0])
    print(f"${item[1]['price']}")
    print(item[1]['link'])
    print("_____________________________")







