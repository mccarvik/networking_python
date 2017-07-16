import sys, pdb, gzip, requests
from urllib.request import urlopen, Request, build_opener, HTTPCookieProcessor
import urllib.error
from urllib.parse import urlparse, urljoin, parse_qs, quote, urlencode, urlunparse
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
    
def url_encoding():
    print(quote('A duck?'))
    path = 'pypi'
    path_enc = quote(path)
    query_dict = {':action': 'searc', 'term': 'Are you qutie sure thi is a cheese show?'}
    query_enc = urlencode(query_dict)
    print(query_enc)
    
    netloc = 'pypi.python.org'
    print(urlunparse(('http', netloc, path_enc, '', query_enc, '')))
    
    path = '/images/users/+Zoot+/'
    print(quote(path))
    
    username = '+Zoot/Dingo+'
    path = 'images/users/{}'.format(username)
    print(quote(path))
    
    username = '+Zoot/Dingo+'
    user_encoded = quote(username, safe='')
    path = '/'.join(('', 'images', 'users', username))
    print(path)
    
def http_methods():
    req = Request('http://www.google.com', method='HEAD')
    response = urlopen(req)
    print(response.status)
    print(response.read())
    
    data_dict = {'P': 'Python'}
    data = urlencode(data_dict).encode('utf-8')
    req = Request('http://search.debian.org/cgi-bin/omega', data=data)
    req.add_header('Content-Type', 'application/x-www-form-urlencode: charset=UTF-8')
    response = urlopen(req)
    print(response)
    
def requests_module():
    response = requests.get('http://www.debian.org')
    print(response.status_code)
    print(response.reason)
    print(response.url)
    print(response.headers['content-type'])
    print(response.ok)
    print(response.is_redirect)
    print(response.request.headers)
    print(response.headers['content-encoding'])
    print(response.content[0:100])
    print(response.text[0:100])
    print(response.encoding)
    
    response = requests.get('http://www.github.com')
    print(response.cookies)
    
    s = requests.Session()
    s.get('http://www.google.com')
    response = s.get('http://www.google.com/preferences')
    print(response)
    
    response = requests.head('http://www.debian.org')
    print(response.status_code)
    print(response.text)
    
    headers = {'User-Agent': 'Mozilla/5.0 Firefox 24'}
    response = requests.get('http://www.debian.org', headers=headers)
    print(response)
    params = {':action': 'search', 'term': 'Are you quite sure this is a cheese sop?'}
    response = requests.get('http://pypi.python.org/pypi', params=params)
    print(response.url)
    
    data = {'P': 'Python'}
    response = requests.post('http://search.debian.org/cgi-bin/omega', data=data)
    print(response)
    
    response = requests.get('http://www.google.cm/notawebpage')
    print(response.status_code)
    # print(response.raise_for_status())
    r = requests.get('http://www.google.com')
    print(r.status_code)
    print(r.raise_for_status())
    
    r = requests.get('http://192.0.2.1')
    
    
    
    
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
    # query_strings()
    # url_encoding()
    # http_methods()
    requests_module()
    