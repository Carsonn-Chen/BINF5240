import xml.etree.ElementTree as ET
import urllib.request

thefile = urllib.request.urlopen("http://www.uniprot.org/uniprot/Q9H400.xml")
tree = ET.parse(thefile)
root = tree.getroot()

ns = '{http://uniprot.org/uniprot}'

for entry in root.findall(ns+'entry'):
    print(entry.tag, entry.attrib, entry.text)
    for reference in entry.findall(ns+'reference'):
        print(reference.tag, reference.attrib, reference.text)
        for citation in reference.findall(ns+'citation'):
            print(citation.tag, citation.attrib, citation.text)
