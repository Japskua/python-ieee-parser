__author__ = 'Janne'

import xml.etree.ElementTree as ET
from ieeeprocessor import IEEEProcessor
from csv_writer import CSVWriter

# Construct the tree by parsing the XML file
tree = ET.parse('searchresult.xml')
# Then, get the root of the tree
root = tree.getroot()

# Then, parse it to Entry
processor = IEEEProcessor()
processor.ProcessSearchResults(root)

print("Found %i entries" % len(processor.entries))

# Okay, now we need to process all the entries into a .csv file
# Initialize the csv writer
csvWriter = CSVWriter()
csvWriter.write_to_file("test.csv", processor.entries)