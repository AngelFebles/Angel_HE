from bs4 import BeautifulSoup
import polars as pl
from selenium import webdriver
import xlsxwriter


def get_table(state):

    browser = webdriver.Firefox()
    browser.get(f"https://www.bls.gov/oes/current/{state}_counties.htm")
    browser.execute_script("window.stop();")
    html = browser.page_source
    browser.quit()

    soup = BeautifulSoup(html, "html.parser")
    table = soup.find_all("ul", {"class": ""})
    inner_texts = [element.get_text(strip=True) for element in table]
    # print("inner_texts")
    # print(inner_texts)

    split_data = [item.split('\xa0-') for item in inner_texts]

    # Create a Polars DataFrame
    df = pl.DataFrame({
        'County': [item[0] for item in split_data],
        'Area': [item[1] for item in split_data]
    })

    return df


state_abbreviations = [
    "al", "ak", "az", "ar", "ca", "co", "ct", "de", "dc", "fl",
    "ga", "hi", "id", "il", "in", "ia", "ks", "ky", "la", "me",
    "md", "ma", "mi", "mn", "ms", "mo", "mt", "ne", "nv", "nh",
    "nj", "nm", "ny", "nc", "nd", "oh", "ok", "or", "pa", "pr",
    "ri", "sc", "sd", "tn", "tx", "ut", "vt", "va", "wa", "wv",
    "wi", "wy"
]


abb2 = ["al", "ak"]

with xlsxwriter.Workbook("Equivalence_table.xlsx") as workbook:

    for state in state_abbreviations:
        df = get_table(state)
        df.write_excel(
            workbook=workbook,
            worksheet=state.upper())
