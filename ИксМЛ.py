from xml.etree import ElementTree

tree = ElementTree.parse("cd_catalog.xml")
root = tree.getroot()

print(root.tag)

cd = root[0]
data = next(cd.iter("Y1985"))
data.text = str(int(data.text) + 1000000)
print(data.text)

tree.write("cd_catalog_copy.xml")