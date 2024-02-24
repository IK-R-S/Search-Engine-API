# DUCKGO SEARCH ENGINE - Beta

from bs4 import BeautifulSoup
import requests
import json


def duckgo(query):

    url = f'https://html.duckduckgo.com/html/?q={query}'

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"}

    req = requests.get(url, headers=headers)

    soup = BeautifulSoup(req.text, 'html.parser')

    # Finding elements
    titles_elements = soup.find_all("a", class_="result__a")
    urls_elements = soup.find_all("a", class_="result__url")

    # Store Titles
    response_titles = []

    for result in titles_elements:
        content = result.get_text().strip()
        response_titles.append(content)

    # Store URLs
    response_urls = []

    for result in urls_elements:
        content = 'https://' + result.get_text().strip()
        response_urls.append(content)

    response = {}
    if len(response_titles) == len(response_urls):
        results_num = len(response_urls)
        for i in range(0, results_num):
            response.update({response_titles[i]: response_urls[i]})

        return {"message": "search request sucessfuly", "search engine": "DuckGo", "query": query, "number of results": results_num, "results": response, "status": 200}, 200

