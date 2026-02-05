from urllib.parse import urlparse

def normalize_url(url: str): 
    #make logic here
    parsed = urlparse(url)
    print(f"parsed is here: {parsed.netloc}")

    if url.startswith("http://"):

        if url[len(url)-1] == "/":
            if "www." in parsed.netloc:
                
                normal = url.replace("www.", "")
                print(f"heyooo {normal}")
                return normal[len("http://"):len(normal)-1]
            
            return url[len("http://"):len(url)-1]
        
        return url[len("http://"):]

    elif url.startswith("https://"):
        if url[len(url)-1] == "/":
            return url[len("https://"):len(url)-1]
        
        return url[len("https://"):]

    else:
        return url