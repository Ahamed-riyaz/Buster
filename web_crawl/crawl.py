# This is the crawl.py file.

from web_crawl import crawler
from crawler import crawl,scan_directories


url = input("enter the url:")
if not url.startswith("https://") and not url.startswith("http://"):
    url = "https://" + url
start_anchor = "/"
choice = int(input("1 or 2"))
if choice == 1:
    crawl(url, start_anchor)
elif choice == 2:
    scan_directories(url)
else:
    print("Invalid choice. Please choose either 1 or 2.")
# print("The Urls Are\n")
# print(urls)
# print("the length of urls:",len(urls))

