import codecs

import requests
from lxml import html, etree

base_url = "https://markets.businessinsider.com"

page_sources = {}


class Converter:
    cotirovki_url = "https://www.cbr.ru/scripts/XML_daily_eng.asp"
    usd_code = 'R01235'

    def convert_usd_to_rub(self, usd_value):
        response = requests.get(self.cotirovki_url)
        # ET.fromstring(response.content).find(self.usd_code).find('Value')
        with open('currency.xml', 'wb') as f:
            f.write(response.content)
        parser = etree.XMLParser(encoding='cp1251')
        tree = etree.parse('currency.xml', parser)
        return round(
            float(tree.xpath("//Valute[contains(@ID, 'R01235')]/Value")[0].text.replace(',', '.')) * float(usd_value),
            2)


class Company:
    pe_ratio_xpath = "//div[contains(text(), 'P/E Ratio')]/parent::div"
    week_low_52_xpath = "//div[contains(text(), '52 Week Low')]/parent::div"
    week_high_52_xpath = "//div[contains(text(), '52 Week High')]/parent::div"
    price_on_company_page_xpath = "//*[contains(@class, 'price-section__current-value')]"
    company_code_xpath = "//*[contains(@class,'price-section__category')]/span"

    def __init__(self, name, link, code=None, pe_ratio=None, gain=None, price=None):
        self.link = base_url + link
        self.name = name
        self.code = code
        self.pe_ratio = pe_ratio
        self.gain = gain
        self.price = price
        super().__init__()

    def get_page_source(self):
        if page_sources.get(self.link) is None:
            company_page = requests.get(self.link)
            tree = html.fromstring(company_page.content)
            page_sources.setdefault(self.link, tree)
            return tree
        else:
            return page_sources.get(self.link)

    def get_code(self):
        if self.code is None:
            self.code = self.get_page_source().xpath(self.company_code_xpath)[0].text[2::]
        return self.code

    def get_ratio(self):
        if self.pe_ratio is None:
            try:
                self.pe_ratio = float(self.get_page_source().xpath(self.pe_ratio_xpath)[0].text.strip())
            except:
                pass
        return self.pe_ratio

    def get_gain(self):
        if self.get_code() == "NVR":
            print()
        if self.gain is None:
            try:
                low = float(self.get_page_source().xpath(self.week_low_52_xpath)[0].text.replace(',', '').strip())
                high = float(self.get_page_source().xpath(self.week_high_52_xpath)[0].text.replace(',', '').strip())
                self.gain = round((high - low) * 100 / low, 2)
            except:
                pass
        return self.gain

    def get_price_in_rubles(self):
        if self.price is None:
            try:
                self.price = Converter().convert_usd_to_rub(
                    self.get_page_source().xpath(self.price_on_company_page_xpath)[0].text.replace(',', '').strip())
            except:
                pass
        return self.price

    def gather_data(self):
        self.get_price_in_rubles()
        self.get_gain()
        self.get_ratio()
        self.get_code()
        return self
