#244p

import xml.etree.ElementTree as ET

f = open("order.xml",encoding="UTF-8")
string = f.read()
tree = ET.ElementTree(ET.fromstring(string))
root = tree.getroot()
# print(tree)
# print(root.tag)
# print(root.text) #실제 내용은 (아직) 없어용!!
for child in root :
     print("tag :",child.tag,"\t text: ",child.text)
f.close()
