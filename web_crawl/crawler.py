# This is the __init__.py file for the web_crawl package.

import queue
import requests
from bs4 import BeautifulSoup


def scan_directories(ip_address):
    wordlist = open('wordlist.txt', 'r')

    for i in wordlist:
        j = i.strip()

        try:
            response = requests.get(ip_address + j)
            if response:
                print(ip_address + j)
        except requests.exceptions.ConnectionError:
            pass


def crawl(base_url, start_anchor):
    search_anchor = queue.Queue()
    # print(search_anchor)
    urls = []

    while True:
        # if not start_anchor:
        #     start_anchor = "/"
        response = requests.get(base_url + start_anchor)
        soup = BeautifulSoup(response.text, "lxml")
        anchors = soup.find_all('a')
        for a in anchors:
            url =a['href']
            # print(url)
            if url not in urls:
                urls.append(url)
                # print(url)
        if not search_anchor.qsize():
            break
        start_anchor = search_anchor.get()
    for i in urls:
        if i:
            first_letter = i[0]
            if first_letter == "h":
                print(i)
            else:
                print(base_url + i)


    # for i in urls:
    #     first_letter = i[0]
    #     if first_letter == "h":
    #         print(i)
    #     else:
    #         print(base_url + i)
    #     count = count + 1
    # print("number of urls:",count)



# def find_local_anchors(soup, start_anchor):
#     print("start")
#     anchors = []
#     for link in soup.find_all('a'):
#         anchor = link['href']
#         if anchor.startswith(start_anchor):
#             anchors.append(anchor)
#     return anchors

# if __name__ == "__main__":
#     url = ""
#     start_anchor = "/"
#     urls = crawl(url, start_anchor)
#     print(len(urls), urls)


# print("option 1 for normal scan\noption 2 for Aggressive scan")
# w = int(input("enter the option:"))
#
# if w == 1:
#     ip_address = input("enter the url:")
#     print("[*] Starting directory scan...")
#     scan_directories(ip_address)
#
# elif w == 2:
#     url = input("Enter the base URL: ")
#     start_anchor = input("Enter the start anchor: ")
#     urls = crawl(url, start_anchor)

# else:
#     print("Invalid option. Please choose option 1 or 2.")



