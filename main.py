from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np



# #
# # website = 'https://coinmarketcap.com/'
# #
# # response = requests.get(website)
# #
# # response.status_code
# #
# #
# #
# # soup = BeautifulSoup(response.content, 'html.parser')
# #
# #
# # results = soup.find('table', {'class':'h7vnx2-2 czTsgW cmc-table'}).find('tbody').find_all('tr')
# #
# #
# #
# #
# # #name
# # results[0].find('p', {'class':'sc-1eb5slv-0 iworPT'}).get_text().strip()
# # #price
# # results[0].find('div', {'class': 'sc-131di3y-0 cLgOOr'}).get_text().strip()
# # #24h
# # results[0].find('span', {'class': 'sc-15yy2pl-0 hzgCfk'}).get_text().strip()
# # #7d
# # results[0].find('span', {'class': 'sc-15yy2pl-0 hzgCfk'}).get_text().strip()
# # #market cap
# # results[0].find('p', {'class': 'sc-1eb5slv-0 hykWbK'}).get_text().strip()
# # #volume
# # results[0].find('div', {'class': 'sc-16r8icm-0 j3nwcd-0 cRcnjD'}).get_text().strip()
# #
# #
# # #
# # #creating empty lists
# # name = []
# # price = []
# # change_24h = []
# # change_7d = []
# # market_cap = []
# # volume_24h = []
# #
# #
# # for result in results :
# #
# #     try:
# #         name.append(result.find('p', {'class':'sc-1eb5slv-0 iworPT'}).get_text().strip())
# #
# #     except:    name.append('n/a')
# #     try:
# #         price.append(result.find('div', {'class': 'sc-131di3y-0 cLgOOr'}).get_text().strip())
# #     except:
# #         price.append('n/a')
# #
# #
# #     try:
# #         change_24h.append(result.find('span', {'class': 'sc-15yy2pl-0 hzgCfk'}).get_text().strip())
# #     except:
# #         change_24h.append('n/a')
# #
# #     try:
# #         change_7d.append(result.find('span', {'class': 'sc-15yy2pl-0 hzgCfk'}).get_text().strip())
# #     except:
# #         change_7d.append('n/a')
# #
# #     try:
# #         market_cap.append(result.find('p', {'class': 'sc-1eb5slv-0 hykWbK'}).get_text().strip())
# #     except:
# #         market_cap.append('n/a')
# #
# #     try:
# #         volume_24h.append(result.find('div', {'class': 'sc-16r8icm-0 j3nwcd-0 cRcnjD'}).get_text().strip())
# #     except:
# #         volume_24h.append('n/a')
# #
# #
# #
# #
# #
# # crypto_df = pd.DataFrame({'coin':name , 'price': price,'change_24h': change_24h, 'change_7d': change_7d,
# #                           'market_cap': market_cap, 'volume_24h': volume_24h, })
# #
# #
# # crypto_df.to_csv('single_page_crypto.csv', index=False)
# #
# #
# #
#
#
#
#
#
#
# #
#
#
#
#
#
# #creating empty lists
# name = []
# price = []
# change_24h =[]
# change_7d = []
# market_cap = []
# volume_24h =[]
#
#
#
# for i in range(1,3):
#
#
#    websitee = 'https://coinmarketcap.com/?page=' + str(i)
#
#
#    response = requests.get(websitee)
#
#    response.status_code
#
#
#    soup = BeautifulSoup(response.content, 'html.parser')
#
#
#
#    results = soup.find('table', {'class':'h7vnx2-2 czTsgW cmc-table'}).find('tbody').find_all('tr')
#
#
#
#    for result in results :
#         try:
#             name.append(result.find.all('p', {'class': 'sc-1eb5slv-0 iworPT'}).get_text().strip())
#         except:
#             name.append('n/a')
#
#         try:
#             price.append(result.find('div', {'class': 'sc-131di3y-0 cLgOOr'}).get_text()).strip()
#         except:
#             price.append('n/a')
#
#         try:
#             change_24h.append(result.find.all('span', {'class': 'sc-15yy2pl-0 hzgCfk'}).get_text().strip())
#         except:
#             change_24h.append('n/a')
#
#         try:
#             change_7d.append(result.find.all('span', {'class': 'sc-15yy2pl-0 hzgCfk'}).get_text().strip())
#         except:
#             change_7d.append('n/a')
#
#         try:
#             market_cap.append(result.find.all('p', {'class': 'sc-1eb5slv-0 hykWbK'}).get_text().strip())
#         except:
#             market_cap.append('n/a')
#
#         try:
#             volume_24h.append(result.find.all('P', {'class': 'sc-1eb5slv-0 hykWbK font_weight_500'}).get_text().strip())
#         except:
#             volume_24h.append('n/a')
#
#
# print(volume_24h)
#
#
#


from urllib.parse import urlencode

import requests
from tabulate import tabulate


query_string = [
    ('start', '1'),
    ('limit', '100'),
    ('sortBy', 'market_cap'),
    ('sortType', 'desc'),
    ('convert', 'USD'),
    ('cryptoType', 'all'),
    ('tagType', 'all'),
]

base = "https://api.coinmarketcap.com/data-api/v3/cryptocurrency/listing?"
response = requests.get(f"{base}{urlencode(query_string)}").json()

results = [
    [
        currency["name"],
        round(currency["quotes"][0]["price"], 4),
        currency["Market Cap"],
        round(currency["Market Cap"],),


    ]
    for currency in response["data"]["cryptoCurrencyList"]
]

print(tabulate(results, headers=["Currency", "Price", "Market Cap"], tablefmt="pretty"))


from urllib.parse import urlencode
from tabulate import tabulate
import requests

query_string = [
    ('start', '1'),
    ('limit', '100'),
    ('sortBy', 'market_cap'),
    ('sortType', 'desc'),
    ('convert', 'USD'),
    ('cryptoType', 'all'),
    ('tagType', 'all'),
]

base = "https://api.coinmarketcap.com/data-api/v3/cryptocurrency/listing?"
response = requests.get(f"{base}{urlencode(query_string)}").json()
last_page = (int(response["data"]["totalCount"]) // 100) + 1
all_pages = [1 if i == 1 else (i * 100) + 1 for i in range(1, last_page)]

for page in all_pages[:10]:
    query_string = [
        ('start', str(page)),
        ('limit', '100'),
        ('sortBy', 'market_cap'),
        ('sortType', 'desc'),
        ('convert', 'USD'),
        ('cryptoType', 'all'),
        ('tagType', 'all'),
    ]
    response = requests.get(f"{base}{urlencode(query_string)}").json()
    results = [
        [
            currency["name"],
            round(currency["quotes"][0]["price"], 4),


        ]
        for currency in response["data"]["cryptoCurrencyList"]
    ]

    print(tabulate(results, headers=["currency", "Price" , ], tablefmt="pretty"))

    #creating empty lists
    name = []
    price = []
    change_24h =[]
    change_7d = []
    market_cap = []
    volume_24h =[]


df = pd.DataFrame({'coin':results,})

df.to_csv('crypto.csv', index=False)


# crypto_df = pd.DataFrame({'coin':name , 'price': price,'change_24h': change_24h, 'change_7d': change_7d,
#                           'market_cap': market_cap, 'volume_24h': volume_24h, })
#
#
# crypto_df.to_csv('single_page_crypto.csv', index=False)
#


#
#
#
# # currency = [name]
# price = []
# #
# crypto_df = pd.DataFrame({results})
#
# # crypto_
# df.to_csv('original.csv', index=False)
