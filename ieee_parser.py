import xml.etree.ElementTree as ET
from ieeeprocessor import IEEEProcessor
from ieeesearch import SearchEngine
from parser_threaded import ThreadParser
import sys


def main():

    # Initialize the search engine
    tp = ThreadParser()
    tp.prepare_search("games AND interoperability")

    tp.show_preprocessing_info()
    tp.search_multithreaded("games AND interoperability")

    """
    # Define the query terms
    se.set_query("games AND interoperability")

    # Set the paging
    se.set_paging(10, 1)
    # Perform the query
    se.perform_query()
    #se.display_results()
    # Get the results
    res = se.get_results()"""

    """ <<--- Okay, now we continue with parsing the results into wanted format --->> """
"""
    # Construct the tree by parsin the XML file
    #tree = ET.parse(res)
    # Then, get the root of the tree
    root = ET.fromstring(res)
    #tree = ET.parse('searchresult.xml')

    # Then, start processing the information
    processor = IEEEProcessor()
    processor.ProcessSearchResults(root)

    print("Found %i entries", len(processor.entries))"""

if __name__ == "__main__":
    sys.exit(main())


