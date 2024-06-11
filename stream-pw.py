from playwright.sync_api import sync_playwright
from selectolax.parser import HTMLParser
url="https://store.steampowered.com/specials"
if __name__=="__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto(url)
        # page.wait_for_selector("div.someclass")
        page.wait_for_load_state('networkidle')
        page.evaluate("()=>window.scroll(0,document.body.scrollHeight)")
        page.wait_for_load_state('domcontentloaded')
        page.wait_for_selector('div[class*=ImpressionTrackedElement]')
        # page.screenshot(path="snapshot2.png",full_page=True)

        html=page.inner_html("body")
        tree = HTMLParser(html)

        divs =  tree.css('div[class*="ImpressionTrackedElement"]')

        for d in divs:
            print(d.text)
            title = d.css_first('div[class*="StoreSaleWidgetTitle"]')
            thumbnile = d.css_first('div[class*="CapsuleImageCtn"]').attributes.get('src')
            tags = [a.text() for a in d.css('div[class*="_3OSJsO_BdhSFujrHvCGLqV"]>a')[:5]]
            attr={
                "title":title,
                "tags":tags,
                "thumbnile":thumbnile
            }
            print(attr)