import mechanicalsoup
import time

# Open the /dice page, scrape the result, and print:
browser = mechanicalsoup.Browser()
url = "http://olympus.realpython.org/dice"

for i in range(4):
    page = browser.get(url)
    html = page.soup
    tag = html.select("#result")[0]
    result = tag.text
    print(f"The result of your dice roll is: {result}")
    if i < 3:
        print("begin interval")
        time.sleep(10)
        print("end interval")
