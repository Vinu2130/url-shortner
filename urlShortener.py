import random,string

domain = "http://127.0.0.1:5000/"
url_map = {}

# Generating Random Key
def produce_random_val():
    random_digits = "".join( [random.choice(string.digits) for i in range(4)] )
    random_letters = "".join( [random.choice(string.ascii_letters) for i in range(4)] )
    random_val = "".join(random.sample(random_letters+random_digits,len(random_letters+random_digits)))
    return random_val

# Generating Short URL
def shorten_url(url, domain = domain):
    random_val = ''
    if url not in url_map.values():
        random_val = produce_random_val()
        url_map[random_val] = url
    else:
        for key in url_map.keys():
            if url_map[key] == url:
                random_val = key

    if domain[len(domain)-1]!= "/":
        domain += "/"
    return domain + random_val

# Retrieving actual url from short_url
def retrieve_url_from_short_url(short_url, domain = domain):
    if domain[len(domain)-1] != "/":
        domain+="/"
    url_key = short_url.replace(domain, '')
    return retrive_url_from_key(url_key)


# Retrieving actual url from key
def retrive_url_from_key(key):
    return (url_map[key])





