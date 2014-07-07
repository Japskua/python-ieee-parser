import xml.etree.ElementTree as ET
tree = ET.parse('searchresult.xml')
root = tree.getroot()


class Entry:
    def __init__(self, rank, authors, title):
        self.rank = rank,
        self.authors = authors,
        self.title = title


class IEEEProcessor:
    def __init__(self):
        # Set the entries to be empty
        self.entries = []

    # Process the document to entry
    def ProcessDocumentToEntry(self, child):
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
        

    # Processes the search results
    def ProcessSearchResults(self, root):
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


processor = IEEEProcessor()
processor.ProcessSearchResults(root)
                       

print("Found %i entries", len(processor.entries))
print(processor.entries[0].authors)
