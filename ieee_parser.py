from parser_threaded import ThreadParser
from ieee_shell import IEEEShell


def main(searchTerms):

    # Initialize the search engine
    tp = ThreadParser()
    tp.prepare_search(searchTerms)

    tp.show_preprocessing_info()
    #tp.search_and_process("games AND interoperability")
    #tp.search_multithreaded("games AND interoperability")

    # Okay, now we need to process all the entries into a .csv file
    # Initialize the csv writer
    #csvWriter = CSVWriter()
    #csvWriter.write_to_file("test.csv", processor.entries)





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
    IEEEShell().cmdloop()


