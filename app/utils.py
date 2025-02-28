import pyshorteners

def shorten_url(long_url):
    try: 
        return pyshorteners.Shortener().tinyurl.short(long_url)
    except Exception as e:
        print(f"Error shortening URL: {e}")
        return None

