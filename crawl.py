from urllib.parse import urlparse

def normalize_url(url: str): 
    #make logic here
    parsed = urlparse(url)

    print(f"parsed is here: {parsed}")

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