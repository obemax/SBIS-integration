import random

import requests
# from products.models import ProductCategory, Product

json = {
    "app_client_id": "3782400122376855",
    "app_secret": "IQT0NZMS5D0JQUVDKVYMQKI5",
    "secret_key": "s8I4bdHqH5DTU49OLs7sInUPxUGht2xYA22WgbaJIoL6bgloFyuVbrpwNKwsT4Fyt9ocVZ47K3wNV92kv7wLBG5gfd6GIJPmbC2JFMadbDkVnVjSUBeMji"
}

url = 'https://online.sbis.ru/oauth/service/'
response = requests.post(url, json=json)
products = []
if response.status_code == 200:
    # Извлекаем данные из ответа
    data = response.json()

    # Извлекаем данные из словаря и сохраняем в переменные
    access_token = data.get('access_token', None)
    sid = data.get('sid', None)
    token = data.get('token', None)

    # Выводим переменные
    print(f"access_token: {access_token}")
    print(f"sid: {sid}")
    print(f"token: {token}")

    # получаем прайс лист
    parameters_65 = {
        'pointId': 123,
        'priceListId': 65,
        'withName': True,
        'page': 0
    }
    url_65 = 'https://api.sbis.ru/retail/nomenclature/list?'
    headers_65 = {
        "X-SBISAccessToken": access_token
    }
    has_more_65 = True
    while has_more_65:
        response_65 = requests.get(url_65, params=parameters_65, headers=headers_65)
        response_65.encoding = 'utf-8'

        if response_65.status_code == 200:
            data_65 = response_65.json()
            nomenclatures_65 = data_65.get('nomenclatures', [])
            for nomenclature in nomenclatures_65:
                name = nomenclature.get('name', '')
                cost = nomenclature.get('cost', None)
                unit = nomenclature.get('unit', '')
                category_name = name.split()[0]

                if not (cost is None):
                    # category, created = ProductCategory.objects.get_or_create(name=category_name)
                    # product = Product.objects.create(
                    #     name=name,
                    #     description='',
                    #     price=cost,
                    #     quantity=1,
                    #     category=category
                    # )
                    # product.save()
                    product_dict = {
                        'name': name,
                        'cost': cost,
                        'description': '',
                        'manufacturer': category_name,
                        'quantity' : random.randint(1,10)
                    }
                    products.append(product_dict)

            has_more_65 = data_65.get('outcome', {}).get('hasMore', False)
            parameters_65['page'] += 1

    # получаем прайс лист
    parameters_66 = {
        'pointId': 123,
        'priceListId': 66,
        'withName': True,
        'page': 0
    }
    url_66 = 'https://api.sbis.ru/retail/nomenclature/list?'
    headers_66 = {
        "X-SBISAccessToken": access_token
    }
    has_more_66 = True

    while has_more_66:
        response_66 = requests.get(url_66, params=parameters_66, headers=headers_66)
        response_66.encoding = 'utf-8'

        if response_66.status_code == 200:
            data_66 = response_66.json()
            nomenclatures_66 = data_66.get('nomenclatures', [])
            for nomenclature in nomenclatures_66:
                name = nomenclature.get('name', '')
                cost = nomenclature.get('cost', None)
                unit = nomenclature.get('unit', '')
                category_name = name.split()[0]

                if not(cost is None):
                    # category, created = ProductCategory.objects.get_or_create(name=category_name)
                    # product = Product.objects.create(
                    #     name=name,
                    #     description='',
                    #     price=cost,
                    #     quantity=1,
                    #     category=category
                    # )
                    # product.save()
                    product_dict = {
                        'name': name,
                        'cost': cost,
                        'description': '',
                        'manufacturer': category_name,
                        'quantity': random.randint(1, 10)
                    }
                    products.append(product_dict)
                    print(product_dict)
            has_more_66 = data_66.get('outcome', {}).get('hasMore', False)
            parameters_66['page'] += 1

else:
    print(f"Ошибка при выполнении запроса. Код статуса: {response.status_code}")

products = tuple(products)
print(products)
