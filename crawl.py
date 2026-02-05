from urllib.parse import urlparse
from bs4 import BeautifulSoup

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

    if len(html) == 0:
        return text

    text = doc.find('h1')
    print(f"wooo first text {text}")
    text = text.get_text()
    print(f"wooo second text {text}")

    return text