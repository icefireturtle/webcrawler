from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
import requests

def normalize_url(url: str): 
    #make logic here
    parsed = urlparse(url)

    #print(f"parsed is here: {parsed}")

    if parsed.scheme == "http":
        normal = url[len("http://"):]

        if url[len(url)-1] == "/":
            normal = normal[:-1]
        
        if "www." in parsed.netloc:
            normal = normal.replace("www.", "")
            
        return normal

    elif parsed.scheme == "https":
        normal = url[len("https://"):]

        if url[len(url)-1] == "/":
            normal = normal[:-1]
        
        if "www." in parsed.netloc:
            normal = normal.replace("www.", "")
            
        return normal

    else:
        return url

def get_h1_from_html(html):
    doc = BeautifulSoup(html, 'html.parser')
    text = ""

    if len(html) == 0 or doc.find('h1') == None:
        return text

    text = doc.find('h1')
    #print(f"wooo first text {text}")
    text = text.get_text()
    #print(f"wooo second text {text}")

    return text

def get_first_paragraph_from_html(html):
    doc = BeautifulSoup(html, 'html.parser')
    main = doc.find('main')
    text = ""

    if len(html) == 0 or doc.find('p') == None:
        return text

    if main == None:
        text = doc.find('p')
        text = text.get_text()
    else:
        text = main.find('p')
        text = text.get_text()

    return text

def get_urls_from_html(html, base_url):
    doc = BeautifulSoup(html, 'html.parser')
    urls = []

    if len(html) == 0 or doc.find('a') == None:
        return urls

    for url in doc.find_all('a'):
        if url.get('href') != None:
            #absolute
            if url.get('href').startswith('http') or url.get('href').startswith('https'):
                urls.append(url.get('href'))
            #relative
            else:
                urls.append(urljoin(base_url, url.get('href')))
                
    return urls

def get_images_from_html(html, base_url):
    doc = BeautifulSoup(html, 'html.parser')
    images = []

    if len(html) == 0 or doc.find('img') == None:
        return images
    
    for image in doc.find_all('img'):
        if image.get('src') != None:
            images.append(urljoin(base_url, image.get('src')))

    return images

def extract_page_data(html, page_url):

   return {
        "url": page_url,
        "h1": get_h1_from_html(html),
        "first_paragraph": get_first_paragraph_from_html(html),
        "outgoing_links": get_urls_from_html(html, page_url),
        "image_urls": get_images_from_html(html, page_url)
    }

def get_html(url):

    try:
        req = requests.get(url, headers={"User-Agent": "BootCrawler/1.0"})

    except Exception as e:

        if req.status_code != requests.codes.ok:
            raise Exception(f"error: {req.status_code}")

        elif req.headers['Content-Type'] != "text/html":
            raise Exception(f"error: Content-Type is not text/html, it is {req.headers['Content-Type']}")

        else:
            raise Exception("timeout error occurred while fetching URL")

    return req.content

def crawl_page(base_url, current_url=None, page_data=None):
    if current_url == None:
        current_url = base_url
    
    if page_data == None:
        page_data = {}

    base_parsed = urlparse(base_url)
    current_parsed = urlparse(current_url)

    if base_parsed.hostname != current_parsed.hostname and current_parsed != None:
        return
    
    if page_data != {} and current_url in page_data.keys():
        return
    
    if page_data != {}:
        print(f"collected keys: {page_data.keys()}")

    print(f"crawling {current_url}")
    
    html = get_html(current_url)

    page_data[normalize_url(current_url)] = extract_page_data(html, current_url)

    urls = get_urls_from_html(html, current_url)

    for url in urls:
        crawl_page(base_url, url, page_data)