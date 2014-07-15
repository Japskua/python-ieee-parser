__author__ = 'Janne'


class Entry:
    def __init__(self, rank, authors, title):
        self.rank = rank,
        self.authors = authors,
        self.title = title

    def showEntry(self):
        print("Entry number: " + str(self.rank))
        print("Title: " + self.title)
        print("Authors: " + str(self.authors))

    def getEntryDataForCSV(self, delimiter):
        return str(self.rank).strip("()\',").replace("\"", "") + delimiter + self.title.replace(",", "").replace("\"", "") + delimiter + str(self.authors).strip("()\',").replace(".", "").replace(",", "").replace("\"", "")