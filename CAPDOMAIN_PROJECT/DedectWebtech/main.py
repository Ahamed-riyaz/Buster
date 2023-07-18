import urllib.parse
import re

URL = input("Paste the URl : ")

regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,9}\.\d{1,9}\.\d{1,9}\.\d{1,9})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)


if (re.match(regex, URL) is not None):
    parsed_url = urllib.parse.urlparse(URL)
    URL = parsed_url.netloc
else:
    URL=URL
