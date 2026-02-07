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
            try:
                #absolute
                if url.get('href').startswith('http') or url.get('href').startswith('https'):
                    urls.append(url.get('href'))
                #relative
                else:
                    urls.append(urljoin(base_url, url.get('href')))
            except Exception as e:
                print(f"error parsing URL {url.get('href')}: {e}")
                continue        
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
        print(f"fetched URL {url} with status code {req.status_code}")
        print(f"with headers {req.headers.get('content-type', 'no content-type header')}")

    except Exception as e:

        if req.status_code not in requests.codes.ok:
            raise Exception(f"error: {req.status_code} {req.reason}")

        content_type = req.headers.get("content-type", "")
        if "text/html" not in content_type:
            raise Exception(f"error: content-type is not text/html, it is {content_type}")

        raise Exception(f"timeout error occurred while fetching URL {url}: {e}")

    return req.text

def get_safe_html(url):
    try:
        html = get_html(url)
        return html

    except Exception as e:
        print(f"error fetching URL {url}: {e}")
        return None

def crawl_page(base_url, current_url=None, page_data=None):
    if current_url == None:
        current_url = base_url
    
    if page_data == None:
        page_data = {}

    base_parsed = urlparse(base_url)
    current_parsed = urlparse(current_url)

    if base_parsed.hostname != current_parsed.hostname and current_parsed != None:
        return page_data
    
    normalized = normalize_url(current_url)

    if page_data != {} and normalized in page_data.keys():
        return page_data
    
    if page_data != {}:
        print(f"collected keys: {page_data.keys()}")

    print(f"crawling {current_url}")
    
    html = get_safe_html(current_url)
    if html == None:
        print(f"skipping {current_url} because it could not be fetched")
        return page_data

    page_data[normalized] = extract_page_data(html, current_url)

    urls = get_urls_from_html(html, current_url)

    for url in urls:

        print (f"found {len(urls)} urls on {current_url}")
        
        print(f"checking {url} for crawling")

        if normalize_url(url) not in page_data.keys():
            page_data = crawl_page(base_url, url, page_data)
        else:
            print(f"skipping {url} because it has already been crawled")
    
    return page_data