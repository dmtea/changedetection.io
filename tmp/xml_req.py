import requests
from bs4 import BeautifulSoup


def get_links_from_sitemap(url):

    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    }
    links = []

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")

    maps_tags = soup.find_all("sitemap")
    if maps_tags and len(maps_tags) > 0:
        for loc_tag in maps_tags:
            __link = loc_tag.find("loc")
            links.append(__link.text)

    loc_tags = soup.find_all("url")
    if loc_tags and len(loc_tags) > 0:
        for loc_tag in loc_tags:
            __link = loc_tag.find("loc")
            links.append(__link.text)

    print("PARSED LNKS: ", links)

    return links


cookies = {
    # '_ga': 'GA1.1.699464716.1656709993',
    # '_ga_34YLV9HW4T': 'GS1.1.1656709993.1.0.1656709999.0',
}

headers = {
    # 'authority': 'lotteryngo.com',
    # 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    # 'accept-language': 'en-US,en;q=0.9,ru;q=0.8,uk;q=0.7',
    # 'cache-control': 'no-cache',
    # # Requests sorts cookies= alphabetically
    # # 'cookie': '_ga=GA1.1.699464716.1656709993; _ga_34YLV9HW4T=GS1.1.1656709993.1.0.1656709999.0',
    # 'pragma': 'no-cache',
    # 'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    # 'sec-ch-ua-mobile': '?0',
    # 'sec-ch-ua-platform': '"Linux"',
    # 'sec-fetch-dest': 'document',
    # 'sec-fetch-mode': 'navigate',
    # 'sec-fetch-site': 'none',
    # 'sec-fetch-user': '?1',
    # 'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
}

# response = requests.get('https://lotteryngo.com/sitemap_index.xml', cookies=cookies, headers=headers)
# response = requests.get('https://toponlinecasino.com.ph/sitemap_index.xml', cookies=cookies, headers=headers)
# response = requests.get('https://onlinegambling.com.ph/sitemap_index.xml', cookies=cookies, headers=headers)

linksfrom = get_links_from_sitemap('https://onlinegambling.com.ph/sitemap_index.xml')
print(linksfrom)

# print(response.text)

# with open('tmp/sitemap_test.xml', 'w') as f:
#     f.write(response.text)
