from playwright.sync_api import sync_playwright
from selectolax.parser import HTMLParser


def show_me_the_money():
    url="https://www.usaspending.gov/agency/department-of-defense?fy=2023"
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=50)
        page = browser.new_page()
        page.goto(url)
        TIMEOUT=90000
        page.wait_for_load_state('networkidle',timeout=TIMEOUT)
        page.wait_for_selector("div.visualization-section__data")

        return page.inner_html("body")
    
        # print(page.title())
        # browser.close()

def extract_budget(html):
    tree= HTMLParser(html)
    budget_div = tree.css_first("div.visualization-section__data")
    return budget_div.text()


if __name__== "__main__":
    html=show_me_the_money()
    budget= extract_budget(html)
    print(budget)