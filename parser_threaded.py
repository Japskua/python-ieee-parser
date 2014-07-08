__author__ = 'Janne'

from threading import Thread
from queue import Queue
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

    def search_and_process(self, query_text):
        """
        Searches and Processes the IEEE database according to the query
        :return A Qeueue containing the result entries
        """

        # First, make the search
        search_results = self.search_multithreaded(query_text)
        # Second, process the results
        process_results = self.process_multi_threaded(search_results)
        # And finally, we have it ALL

        print("Whole job done")
        # Return the results
        return process_results

    def process_multi_threaded(self, process_queue):
        """
        Starts the multithreaded process of retrieving search data from the system
        """

        # First, make a list of threads to keep count
        threads = []
        # Make a results queue
        result_queue = Queue()

        # First, we need to loop over the result queue
        for i in range(process_queue.qsize()):
            # Make a new thread
            t = Thread(target=perform_search, args=(process_queue.get(), result_queue, ))
            threads.append(t)
            t.start()

        # Then, loop through the threads list and wait for all to end
        for i in range(len(threads)):
            # Join the threads
            threads[i].join()

        print("All processing threads finished")
        print(result_queue.qsize())

        # Then, return the queue
        return result_queue

    def search_multithreaded(self, query_text):
        """
        Performs the search in multithreaded manner
        Searching for 1-100, then 101-200, 201-300, etc...
        """

        # list to keep track of all the threads
        threads = []
        # Make the results queue
        result_queue = Queue()

        # First, initialize all the threads
        for i in range(3):
            t = Thread(target=create_and_perform_query, args=(query_text, result_queue, (i*100 + 1),))
            threads.append(t)
            t.start()

        # Then, loop through all the results, ordering to wait until all are done
        for i in range(len(threads)):
            threads[i].join()

        print("All search threads finished")
        print(result_queue.qsize())

        # Then, return the queue
        return result_queue


def perform_search(xml_string, results):
    # Initialize the processor
    processor = IEEEProcessor()

    # Then, read the XML string into a ETree
    root = ET.fromstring(xml_string)
    # Next, send it for processing
    processor.ProcessSearchResults(root)

    # And finally, get the results and save them to the results Queue
    results.put(processor.get_entries())


def create_and_perform_query(queryText, results, start_point):
    # Perform the query

    # First, create the search engine client
    se = SearchEngine()
    # Second, set the query
    se.set_query(queryText)
    # Third, set the paging (get full 100, start with the given point)
    se.set_paging(100, start_point)
    # Fourth, set filtering
    # TODO: Missing filtering
    # Five, perform the query
    se.perform_query()
    # Six, get the results
    res = se.get_results()
    # Put it to the queue
    results.put(res)

    # Give some info on what has happened so far
    end_point = start_point+100
    print(str(start_point) + " - " + str(end_point) + " results parsed")




"""
def myfunc(i):
    print("Sleeping 5 sec from thread %i" % i)
    time.sleep(5)
    print("Finished sleeping from thread %i" % i)

for i in range(10):
    t = Thread(target=myfunc, args=(i,))
    t.start()
    """