# python -m pip install MechanicalSoup
import mechanicalsoup

# ========================
# Interact With HTML Forms
# ========================

# MechanicalSoup is a popular and relatively straightforward package
# to work with web pages interactively.

browser = mechanicalsoup.Browser()
# This creates a Browser object.
# It's a headless browser, which is a web browser with no graphical user interface.

url = "http://olympus.realpython.org/login"
page = browser.get(url) # Thsi returns a Response object.
print(page) # Output: <Response [200]>      <-- Represents Status Code. 200 if successful, 400 if not found.
print(page.soup)    # MechanicalSoup uses Beautiful Soup to parse the HTML from the request


# ==================================================
# Using MechanicalSoup to fill out and submit a form
# ==================================================

# 1
browser = mechanicalsoup.Browser()
url = "http://olympus.realpython.org/login"
login_page = browser.get(url)
login_html = login_page.soup

# 2 Needs much attention to detail of html structure.
form = login_html.select("form")[0]     # returns a list of all <form> elements on the page, then select 0th index.
form.select("input")[0]["value"] = "zeus"           # Username: <input name="user" type="text"/><br/>
form.select("input")[1]["value"] = "ThunderDude"    # Password: <input name="pwd" type="password"/><br/><br/>

# 3
profiles_page = browser.submit(form, login_page.url)    # Submit modified form (set with username and password)
print(profiles_page.url)            # ^ or just print(url)



# ===================================================================
# Programmatically obtain the URL for each link on the /profiles page
# ===================================================================

# print(profiles_page.soup)
links = profiles_page.soup.select("a")

# # Retrieves relative URLs e.g. "/profiles/aphrodite"
# for link in links:
#     address = link["href"]
#     text = link.text
#     print(f"{text}: {address}")

base_url = "http://olympus.realpython.org"
for link in links:
    address = base_url + link["href"]
    text = link.text
    print(f"{text}: {address}")
