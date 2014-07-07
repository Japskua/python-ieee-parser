import xml.etree.ElementTree as ET
from ieeeprocessor import IEEEProcessor
import sys


def main():

    tree = ET.parse('searchresult.xml')
    root = tree.getroot()


    processor = IEEEProcessor()
    processor.ProcessSearchResults(root)


    print("Found %i entries", len(processor.entries))
    print(processor.entries[0].authors)

if __name__ == "__main__":
    sys.exit(main())


