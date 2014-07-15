__author__ = 'Janne'


import cmd, sys
from parser_threaded import ThreadParser
from csv_writer import CSVWriter

class IEEEShell(cmd.Cmd):
    """

    """
    intro = "Welcome to IEEE Search Shell. Type help or ? to list commands."
    prompt = '(ieeeshell) '
    file = None
    searchTerms = ""
    tp = ThreadParser()
    results = []

    def do_keywords(self, arg):
        """
        Sets the search terms for the upcoming search and performs a test search
        Usage: keywords <keywords>
        """
        print("Using the following terms to do the search:" + self.searchTerms)
        self.searchTerms = arg
        self.tp.prepare_search(self.searchTerms)
        self.tp.show_preprocessing_info()

    def do_search(self, arg):
        """
        Does the search, according to the results gained in the preprocessing [keywords]
        Usage: search <amount_of_threads>
        """
        if self.searchTerms == "":
            print("You need to set keywords first with keywords <keywords> command")
            return
        print("Using the following terms to do the search:" + self.searchTerms)
        # Get the results
        results = self.tp.search_and_process(self.searchTerms, int(arg))
        # And parse them to proper listing
        self.results_to_listing(results)
        print("Searching done! You can write the results by calling write <filename>")

    def results_to_listing(self, results):
        """
        Converts the results to a proper listing for later processing
        :param result: The results gained by caclling search_and_process
        :return: Nothing
        """
        # Try to read through the whole results
        try:
            for i in range(results.qsize()):
                # Get one thread listing from the queue
                list = results.get()
                # Loop through the list
                for entry in list:
                    # And add each value to self.results
                    self.results.append(entry)
        except TypeError:
            print("Type Error")


    def do_write(self, filename):
        """
        Writes the results into the specified file
        usage: write <filename>
        """
        print("Writing the contents to " + filename)
        csvWriter = CSVWriter()
        print("Writing the results")
        print("Found %i results" % len(self.results))

        try:
            csvWriter.write_to_file(filename, self.results)
            print("All results written to file succesfully!")
        except PermissionError:
            print("\nNo permission to write to file. Might it be accidently left open?")

    def do_show_results(self, args):
        """
        Shows the results received from the search
        """
        if len(self.results) == 0:
            print("0 results founds or no search has been done")
            return

        # Okay, loop over the results and display all of them
        for entry in self.results:
            entry.showEntry()



    def do_exit(self, arg):
        """
        Exits the program
        """
        print("Thanks for using IEEE Search Shell! \nHave a nice day!")
        self.close()
        return True

    def close(self):
        """
        Close the file, if any was open
        """
        if self.file:
            self.file.close()
            self.file = None
