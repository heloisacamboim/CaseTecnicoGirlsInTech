import json
from pprint import pprint
from collections import defaultdict

with open("data.json") as fin:
    data = json.load(fin)

saida = {}

for establishment in data["establishments"]:
    sum = 0
    count = 0
    est = "establishment " + establishment["name"]
    for product in data["products"]:
        prod = "product " + product["name"]
        for category in data["categories"]:
            cat = "category " + category["name"]
            if product["id"] in establishment["productsId"] and category["id"] in product["categoriesId"]:
                if est not in saida: saida[est] = {}
                if cat not in saida[est]: saida[est][cat] = {}
                # if prod not in saida[est][cat]: saida[est][cat][prod] = {}
                price = float(product["price"])/100
                saida[est][cat][prod] = {"price": format(price, '.2f')}
                sum += price
                count += 1
                saida[est]["avgPrice"] = format((sum / count), '.2f')

with open("output.json","w") as fout:
    json.dump(saida, fout, indent=2, sort_keys=True)
pprint(saida)