import requests
import csv
import curlconverter


def get_category():
    url = "https://catalog.wb.ru/catalog/electronic14/catalog?TestGroup=control&TestID=385&appType=1&cat=9468&curr=rub&dest=-3339992&sort=popular&spp=27&uclusters=1"

    headers = {
        "Accept": "*/*",
        "Accept-Language": "ru,en;q=0.9",
        "Connection": "keep-alive",
        "Origin": "https://www.wildberries.ru",
        "Referer": "https://www.wildberries.ru/catalog/elektronika/igry-i-razvlecheniya/aksessuary/garnitury",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "cross-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.731 YaBrowser/23.11.1.731 Yowser/2.5 Safari/537.36",
        "sec-ch-ua": 'Chromium";v="118", "YaBrowser";v="23", "Not=A?Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": 'Windows'
    }

    response = requests.get(url=url, headers=headers)
    return response.json()


def prepare_items(response):
    products = []

    products_raw = response.get('data', {}).get('products', None)
    if products_raw is not None and len(products_raw) > 0:
        for product in products_raw:
            products.append({
                'brand': product.get('brand', None),
                'name': product.get('name', None),
                'sale': product.get('sale', None),
                'priceU': float(product.get('priceU', None)) / 100,
                'salePriceU': float(product.get('salePriceU', None)) / 100,
            })
    return products


def write_csv(products):
    with open("wb_parce.csv", "a") as f:
        names = ['brand', 'name', 'sale', 'priceU', 'salePriceU']
        write = csv.DictWriter(f, delimiter=",", lineterminator="\n", fieldnames=names)
        write.writeheader()
        for item in products:
            write.writerow(item)
            # (products['brand'], products['name'], products['sale'], products['priceU'], products['salePriceU'])


def main():
    response = get_category()
    products = prepare_items(response)
    write_csv(products)


if __name__ == '__main__':
    main()
