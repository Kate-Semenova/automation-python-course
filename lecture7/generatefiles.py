import json
from concurrent.futures.thread import ThreadPoolExecutor
import time
from lecture7.company import Company
from lxml import html
import requests

# Текущая стоимость в рублях (конвертацию производить по текущему курсу, взятому с сайта центробанка РФ)
# def get_companies()
# Код компании (справа от названия компании на странице компании)
# P/E компании (информация находится справа от графика на странице компании)
# Годовой рост/падение компании в процентах (основная таблица)
# Высчитать какую прибыль принесли бы акции компании (в процентах), если бы они были куплены на уровне 52 Week Low и проданы на уровне 52 Week High (справа от графика на странице компании)

url_page = "https://markets.businessinsider.com/index/components/s&p_500?p="

list_of_pages = []


def get_attr(company: Company):
    company.gather_data()


for i in range(1, 11):
    list_of_pages.append(url_page + str(i))


async def fetch_response(url):
    async with requests.get(url) as response:
        return response


list_of_companies = []
company_name_xpath = "//tr/td[1]/a"


def get_companies() -> [Company]:
    if len(list_of_companies) == 0:
        list_of_page_sources = []
        with ThreadPoolExecutor(max_workers=6) as pool_:
            pool_.map(lambda x: list_of_page_sources.append(html.fromstring(requests.get(x).content)), list_of_pages)

        for tree in list_of_page_sources:
            start_2 = time.time()

            with ThreadPoolExecutor(max_workers=6) as pool:
                pool.map(lambda x, y: list_of_companies.append(Company(x.text, y.attrib["href"])),
                         tree.xpath(company_name_xpath),
                         tree.xpath(company_name_xpath))
            with ThreadPoolExecutor(max_workers=6) as pool:
                pool.map(get_attr, list_of_companies)
            end_2 = time.time()
            print(end_2 - start_2, " seconds")

    return list_of_companies


def top_10_by_price():
    return sorted(get_companies(), key=lambda x: x.get_price_in_rubles(), reverse=True)[:10:]


def top_10_by_low_pe():
    return sorted(get_companies(), key=lambda x: str(x.pe_ratio))[:10:]


def top_10_by_high_pe():
    filtered = list(filter(lambda x: x.pe_ratio is not None, get_companies()))
    return sorted(filtered, key=lambda x: str(x.pe_ratio))[len(filtered) - 10::]


def top_10_by_gain():
    filtered = list(filter(lambda x: x.get_gain() is not None, get_companies()))
    return sorted(filtered, key=lambda x: x.get_gain(), reverse=True)[:10:]


# Топ 10 компаний с самими дорогими акциями в рублях.
with open('top_10_by_price.json', 'w') as f:
    f.write('[')
    for company in top_10_by_price():
        jsonStr = json.dumps({
            'code': company.code,
            'name': company.name,
            'price': company.price})
        f.write(jsonStr)
        f.write(',')
    f.write(']')

# Топ 10 компаний с самым низким показателем P/E.
with open('top_10_by_low_pe.json', 'w') as f:
    f.write('[')
    for company in top_10_by_low_pe():
        jsonStr = json.dumps({
            'code': company.code,
            'name': company.name,
            'P/E': company.pe_ratio})
        f.write(jsonStr)
        f.write(',')
    f.write(']')

# Топ 10 компаний, которые показали самый высокий рост за последний год
with open('top_10_by_high_pe.json', 'w') as f:
    f.write('[')
    for company in top_10_by_high_pe():
        jsonStr = json.dumps({
            'code': company.code,
            'name': company.name,
            'P/E': company.pe_ratio})
        f.write(jsonStr)
        f.write(',')
    f.write(']')

# Топ 10 комппаний, которые принесли бы наибольшую прибыль, если бы были куплены на самом минимуме и проданы на самом
with open('top_10_by_gain.json', 'w') as f:
    f.write('[')
    for company in top_10_by_gain():
        jsonStr = json.dumps({
            'code': company.code,
            'name': company.name,
            'gain': str(company.gain) + '%'})
        f.write(jsonStr)
        f.write(',')
    f.write(']')
