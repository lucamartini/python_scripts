import os, sys
import xml.dom.minidom

impl = xml.dom.minidom.getDOMImplementation()

dom1 = xml.dom.minidom.parse("affinity_side.xml")

#ElementList
elements = dom1.getElementsByTagName("match")

#for node in dom1.getElementsByTagName('match'):  # visit every node <bar />
#    print node.toxml()

elements.sort(key=lambda elements:elements.attributes.item(0).value)

#for node in elements:
#    #print node.toxml()
#    print node.attributes.item(0).value

#print elements
#print dom1.toprettyxml()

dom2 = impl.createDocument(None, "matches", None)
top_element = dom2.documentElement

for element in elements:
#    print element.toxml()
    top_element.appendChild(element)

out_file = open("affinity_side_sorted.xml","w")
dom2.writexml(out_file)
out_file.close()

os.system("cp affinity_side.xml affinity_side.bkp")
os.system("cp affinity_side_sorted.xml affinity_side.xml")
os.system("rm affinity_side_sorted.xml")
