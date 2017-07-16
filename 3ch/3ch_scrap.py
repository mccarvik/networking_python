import xml.etree.ElementTree as ET


def element_tree():
    root = ET.Element('inventory')
    print(ET.dump(root))


if __name__ == '__main__':
    element_tree()