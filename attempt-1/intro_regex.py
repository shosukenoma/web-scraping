from urllib.request import urlopen
import re

"""Scrape and Parse Texts from Websites"""

# ========================
# Extract HTML Source Code
# ========================

url = "http://olympus.realpython.org/profiles/aphrodite"
url2 = "http://olympus.realpython.org/profiles/poseidon"    # Edge Case
url3 = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url3)     # returns an HTTPResponse object.
# print(page)
html_bytes = page.read()    # use the HTTPResponse object’s .read() method, which returns a sequence of bytes
html = html_bytes.decode("utf-8")   # use .decode() to decode the bytes to a string using UTF-8

print(html)

# ================================
# Extract Text From HTML With String Methods
# ================================
# title_index = html.find("<title>") # .find() returns the index of the first occurrence of a substring
# start_index = title_index + len("<title>")  # Index of the title itself
# end_index = html.find("</title>")
# title = html[start_index:end_index]
# print(title)


# ================================
# Get To Know Regular Expressions
# ================================

# Regexes are patterns that you can use to search for text within a string.
# re.findall(regEx, inputString, re.IGNORECASE) returns a list of substrings that fulfill the regEx rule.
# . and # are special usages.

pattern = "<title.*?>.*?</title.*?>"    # Ignores any characters that come after "title" and "/title".
match_results = re.search(pattern, html, re.IGNORECASE) # re.search() returns a "MatchObject", returning every possible result.
title = match_results.group()   # return content of re.search()
title = re.sub("<.*?>", "", title)  # Remove HTML tags. In "title" replace "<.*?>" with "".
                                    # ".*" only replaces longest instance, so we also use "*?" which covers shortest instance.
