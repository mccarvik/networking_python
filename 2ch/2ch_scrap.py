import sys, pdb, gzip
from urllib.request import urlopen, Request, build_opener, HTTPCookieProcessor
import urllib.error
from urllib.parse import urlparse, urljoin, parse_qs
from http.cookiejar import CookieJar
import datetime

def resp1():
    response = urlopen('http://www.debian.org')
    
    print(response)
    print(response.readline())
    print(response.url)
    print(response.read(50))
    # print(response.read())
    
    print(response.status)

def resp_err():
    pdb.set_trace()
    try:
        urlopen('http://www.ietf.org/rfc/rfc0.txt')
    except urllib.error.HTTPError as e:
        print('status', e.code)
        print('reason', e.reason)
        print('url', e.url)
      
    print(urlopen('http://192.0.2.1/index.html'))

def headers():
    pdb.set_trace()
    response = urlopen('http://www.debian.org')
    print(response.getheaders())

def cust_request():
    req = Request('http://www.debian.org')
    req.add_header('Accept-Language', 'sv')
    print(req.header_items())
    response = urlopen(req)
    print(response.readlines()[:5])
    print(req.header_items())
    
    # Another way
    headers = {'Accetp-Language': 'sv'}
    req = Request('http://www.debian.org', headers=headers)
    print(req.header_items())
    
def content_compression():
    req = Request('http://www.debian.org')
    req.add_header('Accept-Encoding', 'gzip')
    response = urlopen(req)
    print(response.getheader('Content-Encoding'))
    content = gzip.decompress(response.read())
    print(content.splitlines()[:5])
    
    req = Request('http://www.debian.org')
    req.add_header('Accept-Encoding', 'gzip')
    response = urlopen(req)
    print(response.getheader('Content-Encoding'))
    
    req = Request('http://www.debian.org')
    encodings = 'deflate, gzip, identity'
    req.add_header('Accept-Encoding', encodings)
    response = urlopen(req)
    print(response.getheader('Content-Encoding'))
    
    encodings = 'gzip, deflate;q=0.8, identity;q=0.0'
    
def content_negotiation():
    response = urlopen('http://www.debian.org')
    print(response.getheader('Content-Type'))
    
    response = urlopen('http://www.python.org')
    form, params = response.getheader('Content-Type').split(';')
    print(params)
    charset = params.split('=')[1]
    print(charset)
    content = response.read().decode(charset)
    # print(content)

def user_agents():
    req = Request('http://www.python.org')
    urlopen(req)
    print(req.get_header('User-agent'))
    
    req = Request('http://www.debian.org')
    req.add_header('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64; rv24.0)')
    response = urlopen(req)

def cookies():
    cookie_jar = CookieJar()
    opener = build_opener(HTTPCookieProcessor(cookie_jar))
    opener.open('http://www.github.com')
    print(len(cookie_jar))
    
    cookies = list(cookie_jar)
    print(cookies)
    print(cookies[0].name)
    print(cookies[0].value)
    print(cookies[0].domain)
    print(cookies[0].path)
    print(cookies[0].expires)
    print(datetime.datetime.fromtimestamp(cookies[0].expires))
    print(cookies[0].get_nonstandard_attr('HttpOnly'))
    print(cookies[0].secure)
    
def redirects():
    req = Request('http://www.gmail.com')
    response = urlopen(req)
    print(response.url)
    print (req.redirect_dict)

def urls():
    result = urlparse('http://www.python.org/dev/peps')
    print(result)
    print(result.netloc)
    print(result.path)
    
    print(urlparse('http://www.python.org:8080/'))
    
    print(urlparse('http://www.python.org/'))
    print(urlparse('../images/tux.png'))
    
    print(urljoin('http://www.debian.org', 'intro/about'))
    print(urljoin('http://www.debian.org/intro/', 'about'))
    print(urljoin('http://www.debian.org/intro', 'about'))
    print(urljoin('http://www.debian.org/intro/about/', '/News'))
    print(urljoin('http://www.debian.org/intro/about/', '../News'))
    print(urljoin('http://www.debian.org/intro/about', '../News'))
    print(urljoin('http://www.debian.org/about', 'http://www.python.org'))

def query_strings():
    print(urlparse('http://docs.python.prg/3/search.html?q=urlparse&area=default'))
    result = urlparse('http://docs.python.prg/3/search.html?q=urlparse&area=default')
    print(parse_qs(result.query))
    
    result = urlparse('http://docs.python.prg/3/search.html?q=urlparse&q=urljoin')
    print(parse_qs(result.query))
    
if __name__ == '__main__':
    # resp1()
    # resp_err()
    # headers()
    # cust_request()
    # content_compression()
    # content_negotiation()
    # user_agents()
    # cookies()
    # redirects()
    # urls()
    query_strings()