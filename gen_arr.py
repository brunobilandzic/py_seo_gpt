import csv

def parse_txt(data_path='data/final_export.csv'):

    products = []

    with open(data_path, "r", encoding="utf-8-sig") as file:
        reader = csv.reader(file, delimiter=';')

        for row in reader:
            products.append(row)

    return products

def get_headers(data_path='data/final_export.csv'):
    with open(data_path, "r", encoding="utf-8-sig") as file:
        reader = csv.reader(file, delimiter=';')

        return next(reader)  
if __name__ == '__main__':
    products = parse_txt()
    headers = get_headers()
    
    print(headers)
