from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")   # "html.parser" represents Python’s built-in HTML parser.

print(soup.get_text())      # .get_text() is a method that extracts all the text from the document and automatically removes any HTML tags.
print(soup.find_all("img"))     # .find_all() returns a list of all instances of that particular tag

image1, image2 = soup.find_all("img")
print(image1["src"])    # returns the content of the attribute ("src" in this case) with a key-value-like relationship
print(image2["src"])
print(soup.title)   # cetain tags in html can be accessed directly. automatically ignores cases and spaces.

print(soup.title.string)    # .string helps retrieve just the strings between the title tags.

soup.find_all("img", src="/static/dionysus.jpg")    # search for specific kinds of tags whose attributes match certain values
                                                    # helps you extract particular parts of the page.