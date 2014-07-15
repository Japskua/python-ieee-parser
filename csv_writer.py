__author__ = 'Janne'

import csv

class CSVWriter:
    """
    Writes the Entry Data to an CSV file for faster browsing and safekeeping
    """

    def __init__(self):
        """
        The Constructor
        :return:
        """
        self._filename = ""

    def write_to_file(self, filename, contents):
        """
        Writes the given contents to a .csv file for further processing and evaluating
        :param filename: Name of the .csv file where to write to
        :param contents: A list containing all the entries to write
        :return:
        """
        with open(filename, 'w', newline='', encoding="utf8") as csvfile:
            spamwriter = csv.writer(csvfile, dialect="excel")
            #spamwriter = csv.writer(csvfile, delimiter=';', quotechar='\'', quoting=csv.QUOTE_MINIMAL)

            # Write the first row to contain the headings
            spamwriter.writerow(["Rank;Title;Authors"])

            # Loop through all the contents
            for entry in contents:
                print(entry.getEntryDataForCSV(';'))
                spamwriter.writerow([entry.getEntryDataForCSV(';')])


