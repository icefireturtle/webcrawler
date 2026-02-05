from urllib.parse import urlparse

def normalize_url(url: str): 
    #make logic here
    parsed = urlparse(url)
    print(f"parsed is here: {parsed}")

    if url.startswith("http://"):
        normalized = url[len("http://"):]
    elif url.startswith("https://"):
        normalized = url[len("https://"):]
    else:
        normalized = url

    return normalized