import xml.etree.ElementTree as ET
import gzip

# Define the file name
file_name = "Data1.mzXML.gz"

# Function to count spectra
def count_spectra(file_name, ms_level=None, precursor_mz_range=None):
    ms_count = 0
    msms_count = 0
    msms_count_with_range = 0

    with gzip.open(file_name, 'rb') as gz_file:
        context = ET.iterparse(gz_file, events=("start", "end"))
        context = iter(context)
        event, root = next(context)

        for event, elem in context:
            if event == "end" and elem.tag == "scan":
                ms_level_attr = elem.attrib.get("msLevel")
                precursor_mz_attr = elem.attrib.get("precursorMz")

                if ms_level_attr == "1":
                    ms_count += 1
                elif ms_level_attr == "2":
                    msms_count += 1

                    if precursor_mz_range:
                        precursor_mz = float(precursor_mz_attr)
                        min_mz, max_mz = precursor_mz_range
                        if min_mz <= precursor_mz <= max_mz:
                            msms_count_with_range += 1

                root.clear()

    return ms_count, msms_count, msms_count_with_range

# Count MS and MS/MS spectra
ms_count, msms_count, msms_count_with_range = count_spectra(file_name)

print(f"Total MS spectra (msLevel=1): {ms_count}")
print(f"Total MS/MS spectra (msLevel=2): {msms_count}")

# Specify the precursor m/z range (e.g., 750 to 1000 Da)
precursor_mz_range = (750, 1000)
msms_count_with_range = count_spectra(file_name, ms_level=2, precursor_mz_range=precursor_mz_range)

print(f"MS/MS spectra with precursor m/z between {precursor_mz_range[0]} and {precursor_mz_range[1]} Da: {msms_count_with_range}")
