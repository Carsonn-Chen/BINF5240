import xml.etree.ElementTree as ET
import urllib.request

thefile = urllib.request.urlopen("http://www.uniprot.org/uniprot/Q9H400.xml")
tree = ET.parse(thefile)
root = tree.getroot()

ns = '{http://uniprot.org/uniprot}'

for entry in root.findall(ns+'entry'):
    print(entry.attrib)
    for reference in entry.findall(ns+'reference'):
        print(reference.tag, reference.attrib, reference.text)

        citation = reference.find(ns+'citation')
        authorList = citation.find(ns+'authorList')
        author = authorList.findall(ns+'person')
        title = citation.find(ns+'title')

        if citation:
            print("citation", citation.attrib)
        if title:
            print("Title:", title.text)
        if author:
            print("author:")
            for each in author:
                print(each.attrib)
        print()
