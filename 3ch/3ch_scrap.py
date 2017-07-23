import sys, pdb, json
sys.path.append("/usr/local/lib/python3.4/dist-packages")
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom
import requests
import requests_aws4auth
import boto
from lxml.etree import HTML



def element_tree():
    root = ET.Element('inventory')
    ET.dump(root)
    
    cheese = ET.Element('cheese')
    root.append(cheese)
    ET.dump(root)
    
    name = ET.SubElement(cheese, 'name')
    name.text = 'Caerphilly'
    ET.dump(root)
    
    temp = ET.SubElement(root, 'temp')
    ET.dump(root)
    root.remove(temp)
    ET.dump(root)
    xml_pprint(root)
    
    cheese.attrib['id'] = 'c01'
    xml_pprint(cheese)
    
    text = ET.tostring(name)
    print(text)
    
    text = ET.tostring(name, encoding='utf-8')
    
    
def xml_pprint(element):
    s = ET.tostring(element)
    print(minidom.parseString(s).toprettyxml())
    
    
def handling_errors():
    auth = requests_aws4auth.AWS4Auth('<ID>', '', 'eu-west-1', '')
    r = requests.get('http://s3.eu-west-1.amazonaws.com', auth=auth)
    root = ET.fromstring(r.text)
    for element in root:
        print('Tag: ' + element.tag)
        
    for element in root.findall('Message'):
        print(element.tag + ': ' + element.text)


def boto_demo():
    from boto.s3.connection import Location
    
    conn = boto.connect_s3('<ID>', '<access>')
    conn.create_bucket('mybucket.example.com')
    conn.create_bucket('mybucket.example.com', location=Location.EU)
    print([x for x in dir(Location) if x.isalnum()])
    buckets = conn.get_all_buckets()
    print([b.name for b in buckets])
    bucket = conn.get_bucket('mybucket.example.com')
    print([k.name for k in bucket.list()])
    
    from boto.s3.key import Key
    key = Key(bucket)
    key.key = 'lumberjack_song.txt'
    key.set_contents_from_filename('~/lumberjack_song.txt')
    
    key = bucket.get_key('parrot.txt')
    key.get_contents_to_filename('~/parrot.txt')
    key.set_acl('public-read')
    
    
def json_demo():
    l = ['a', 'b', 'c']
    print(json.dumps(l))
    
    s = json.dumps(l)
    print(type(s))
    print(s[0])
    s = '["a", "b", "c"]'
    l = json.loads(s)
    print(l)
    print(l[0])
    
    print(json.dumps({'A': 'Arthur', 'B':'Brian', 'C': 'Colonel'}))
    d = {
        'Chapman': ['King Arthur', 'Brian'],
        'Cleese': ['Sir Lancelot', 'The Black Knight']
    }
    print(json.dumps(d))
    print(json.dumps({1:10, 2:20, 3:30}))
    
    j = json.dumps({1:10, 2:20, 3:30})
    d_raw = json.loads(j)
    print(d_raw)
    
    print({int(key):val for key, val in d_raw.items()})
    
    j = json.dumps(('a', 'b', 'c'))
    print(j)
    print(json.loads(j))
    
    j = set(['a', 'b', 'c'])
    # print(json.dumps(j))
    print(json.dumps(list(j)))
    
    
def html_parsing():
    response = requests.get('https://www.debian.org/releases/stable')
    root = HTML(response.content)
    print([e.tag for e in root])
    print(root.find('head').find('title').text)
    print(root.find('body').findall('div')[1].find('p').text)
    
    print(root.xpath('body'))
    print(root.xpath('body/div'))
    print(root.xpath('//h1'))
    print(root.find('head').xpath('.//h1'))
    print(root.xpath('//div[@id="content"]'))
    print(root.xpath('//div[h1]'))
    print(root.xpath('body/div[2]'))


if __name__ == '__main__':
    # element_tree()
    # handling_errors()
    # boto_demo()
    # json_demo()
    html_parsing()