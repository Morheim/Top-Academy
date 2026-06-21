import csv

data = [
	["Name", "Age", "City"],
	["Alice", 30, "New York"],
	["Bob", 25, "Los Angeles"],
	["Charlie", 35, "Chicago"],
]
with open("output.csv", "w", newline="", encoding = "utf-8") as file:
	writer = csv.writer(file, delimiter=";")
	writer.writerows(data)

with open("output.csv", "r", encoding="utf-8") as file:
	content = csv.reader(file, delimiter=";")
	for c in list(content):
		print(c)



import json

data_js = {
	"Name": "Alice",
	"Age": "30",
	"Skills": ["Python", "Data Analysis"],
}
with open("example.json", "w", encoding="utf-8") as file:
	json.dump(obj=data_js,
	          fp=file,
	          indent=4
	)


data_product = [["product", "quantity", "price"],
				["Laptop", 7, 1020],
				["Smartphone", 12, 750],
				["Tablet", 17, 301]
]

with open("product.csv", "w", newline="", encoding="utf-8") as file:
	writer = csv.writer(file, delimiter=";")
	writer.writerows(data_product)

list_kazh = {}
def analyze_sales(file_path):
	total = 0
	with open(file_path, mode="r")as file:
		reader = csv.DictReader(file, delimiter=";")
		for row in reader:
			quantity = int(row["quantity"])
			price = float(row["price"])
			list_kazh[row["product"]] = quantity * price
			total += quantity * price
	return total


print(analyze_sales("product.csv"))
for i in list_kazh:
	print(i, list_kazh[i])


















