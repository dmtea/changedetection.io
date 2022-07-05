from bs4 import BeautifulSoup
import requests


def get_links_from_sitemap(url):

    headers = {}
    links = []

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "xml")

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

    return links


def recursive_search_from_sitemap(url, datastore):
    new_links = []
    links = get_links_from_sitemap(url)
    for link in links:
        print(f"SEARCH: ({link})")
        link = link.strip()
        if not datastore.url_exists(link):
            new_links.append(link)
            if link.split(".")[-1] == "xml":
                print("XML SITEMAP is Found!")
                link_links = recursive_search_from_sitemap(link, datastore=datastore)
                new_links.extend(link_links)
        # else:
        #     print(f"Link is already in watch, pass ({link})")
    return new_links


def not_recursive_search_from_sitemap(url, datastore):
    new_links = []
    links = get_links_from_sitemap(url)
    for link in links:
        print(f"SEARCH: ({link})")
        link = link.strip()
        if not datastore.url_exists(link):
            new_links.append(link)
            # if link.split(".")[-1] == "xml":
            #     print("XML SITEMAP is Found!")
            #     link_links = recursive_search_from_sitemap(link, datastore=datastore)
            #     new_links.extend(link_links)
        # else:
        #     print(f"Link is already in watch, pass ({link})")
    return new_links
