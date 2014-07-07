__author__ = 'Janne'

from entry import Entry

class IEEEProcessor:
    """
    A class for handling the IEEE XML documents received by doing the searches
    """
    def __init__(self):
        # Set the entries to be empty
        self.entries = []

    # Process the document to entry
    def ProcessDocumentToEntry(self, child):
        """
        Processes the documents in the child XML nodes into Entry classes
        :param child: The child node in the XML document
        :return: an Entry type object with content information
        """
        # Prepare to catch the values
        rank, authors, title = "", "", ""

        # Loop through the documents
        for document in child:
            if document.tag == "rank":
                rank = document.text
            elif document.tag == "authors":
                authors = document.text
            elif document.tag == "title":
                title = document.text
        # Create a new entry from the data and return it
        return Entry(rank, authors, title)

    def get_amount_entries_found(self, root):
        """
        Gets the amount of entries found with the query wrods
        :param root: The root node of the XML file received from the IEEE search server
        :return: integer telling the amount of found entries
        """
        # Loop through the set to get the total
        for child in root:
            if child.tag == "totalfound":
                return int(child.text)

    # Processes the search results
    def ProcessSearchResults(self, root):
        """
        Processes the search results
        :param root: The root node of the XML document
        :return:
        """
        # Loop through the whole root
        for child in root:
            if child.tag == "totalfound":
                print("total found: " + child.text)
            elif child.tag == "totalsearched":
                print("Total searched: " + child.text)
            elif child.tag == "document":
                # Process the document
                entry = self.ProcessDocumentToEntry(child)
                # Add the new entry to the list
                self.entries.append(entry)