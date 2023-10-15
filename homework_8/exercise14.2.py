import gzip
import xml.etree.ElementTree as ET

file_path = "Data1.mzXML.gz"
ms_count_1 = 0
ms_count_2 = 0
mz_count = 0
ns = "{http://sashimi.sourceforge.net/schema_revision/mzXML_2.0}"

with gzip.open(file_path) as f:
    for event, elem in ET.iterparse(f):
        # print(elem.tag)
        if elem.tag == (ns+"scan"):
            ms_level = int(elem.attrib.get("msLevel", 0))

            if ms_level == 1:
                ms_count_1 += 1
            elif ms_level == 2:
                ms_count_2 += 1

            precursorMz = elem.find(ns+"precursorMz")
            if precursorMz is not None:
                mz_value = float(precursorMz.text)
                if 750 <= mz_value <= 1000:
                    mz_count += 1


print(ms_count_1)
print(ms_count_2)
print(mz_count)