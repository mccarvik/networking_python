import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom


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

if __name__ == '__main__':
    element_tree()