from requests import get
from selectolax.parser import HTMLParser

def show_me_the_money():
    url="https://www.usaspending.gov/agency/department-of-defense?fy=2023"

    response = get(url)
    
    if( response.status_code==200):
        tree = HTMLParser(response.text)
        budget = tree.css_first("div.visualization-section__data")
        return budget.text()
    else:
        return "Failed to retrieve data"
    
if __name__== "__main__":
    show_me_the_money()