__author__ = 'Janne'

from threading import Thread
from ieeesearch import SearchEngine
from ieeeprocessor import IEEEProcessor
import xml.etree.ElementTree as ET


class ThreadParser():
    """
    A Parses class for multithreaded parsing of IEEE results from the search engine
    """
    def __init__(self):
        self._threads = 0
        self._finished = 0

    def prepare_search(self, query_string):
        """
        Prepares the threaded search system for running efficiently in multiple threads
        """
        # Initialize the Search Engine and the IEEE Processor
        se = SearchEngine()
        processor = IEEEProcessor()

        # First, run the test query at the server
        query_results = se.make_test_query(query_string)
        # Second, read the results into XML parser root element
        root = ET.fromstring(query_results)
        # Third, get the amount of found results
        self._total_found = processor.get_amount_entries_found(root)
        self._calculate_amount_threads(self._total_found)

    def _calculate_amount_threads(self, count):
        """
        Calculates the amount of threads that is needed for the process
        """
        # The amount of threads required is the maximum of entries
        # that can be searched at once (100)
        self._threads = count/100
        # +1 if the count is not EXACT 100
        if count%100 != 0:
            self._threads += 1


    def show_preprocessing_info(self):
        """
        Displays the preprocessing information to help user understand
        what is going to happen next
        """
        print("Found %i entries" % self._total_found)
        print("Processing this requires %i threads" % self._threads)

    def process_multi_threaded(self):
        """
        Starts the multithreaded process of retrieving search data from the system
        """
        

"""
def myfunc(i):
    print("Sleeping 5 sec from thread %i" % i)
    time.sleep(5)
    print("Finished sleeping from thread %i" % i)

for i in range(10):
    t = Thread(target=myfunc, args=(i,))
    t.start()
    """