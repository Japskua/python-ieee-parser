__author__ = 'Janne'

import urllib.request, urllib.parse


class SearchEngine:
    """
    The SearchEngine class is in charge of constructing and performing the queries
    at the IEEE Service.
    """
    def __init__(self):
        """
        The Constructor for the class
        :return:
        """
        # The constructor function
        self._contents = ""
        self._url = "http://ieeexplore.ieee.org/gateway/ipsSearch.jsp"
        self._response = ""
        self._queryText = ""
        self._fullQueryString = ""
        self._oa = 0
        self._pn = None
        self._pys = None
        self._pye = None
        self._pu = None
        self._ctype = None
        self._hc = 0
        self._rs = 0

    def perform_query(self):
        """
        Creates the query and runs it at the IEEE server
        :return:
        """
        # Construct the query
        self.__construct_query()

        self.__displayQuery()

        # Then, perform the query
        self._response = urllib.request.urlopen(self._fullQueryString)
        # And read the results
        byte_contents = self._response.read()
        # And finally, convert the bytes into utf-8
        self._contents = byte_contents.decode("utf8")

    def display_results(self):
        """
        Displays the results received
        :return:
        """
        print(self._contents)

    def set_query(self, text):
        """
        Sets the query text
        :param text:
        :return:
        """
        self._queryText = urllib.parse.quote(text)

    def set_paging(self, number_to_fetch, sequence_start):
        """
        Sets the paging settings for the query to be performed
        :param number_to_fetch: The number of items to fetch (1-100), maximum is 100 per query
        :param sequence_start: The sequence starting position (1 is the first, 50 means 50th results, etc...)
        :return: Returns nothing
        """
        if number_to_fetch != 0:
            self._hc = number_to_fetch
        if sequence_start != 0:
            self._rs = sequence_start

    # This is for debugging only!
    def __displayQuery(self):
        """
        Displays the constructed query
        :return:
        """
        print(self._fullQueryString)

    # Constructs the query
    def __construct_query(self):
        """
        Constructs the query to be run at IEEE server
        :return:
        """
        # Construct the query string
        # First, just take the url
        self._fullQueryString = self._url
        # Then, add the text query
        self._fullQueryString += "?querytext=" + self._queryText

        # Check if any of the filtering terms are defined
        if self._oa == 1:
            self._fullQueryString += "&oa=1"
        if self._pn is not None:
            self._fullQueryString += "&pn=" + str(self._pn)
        if self._pys is not None:
            self._fullQueryString += "&pys=" + str(self._pys)
        if self._pye is not None:
            self._fullQueryString += "&pye=" + str(self._pye)
        if self._pu is not None:
            self._fullQueryString += "&pu=" + str(self._pu)
        if self._ctype is not None:
            self._fullQueryString += "&ctype=" +str(self._ctype)

        # Construct the paging information
        if self._hc != 0:
            self._fullQueryString += "&hc=" + str(self._hc)
        if self._rs != 0:
            self._fullQueryString += "&rs=" + str(self._rs)

    def get_results(self):
        """
        Gets the contents returned from the query
        :return: an XML string containing the result information
        """
        return self._contents

    # Sets the filtering, if wanted
    def set_filtering(self, oa=0, pn=None, pys=None, pye=None, pu=None, ctype=None):
        """
        Sets the filtering parameters for the query data
        :param oa: Open Access Only (1 = true, blank otherwise)
        :param pn: Publication number
        :param pys: Start value of the publication year to restrict the results by
        :param pye: End value of the publication year to restrict the results by
        :param pu: Publisher, options are IEEE/AIP/IET/AVS/IBM
        :param ctype: Content type: Conferences/Journals/Books/Early Access/Standards/Educational Courses
        :return:
        """
        # Set the filtering terms
        if oa == 1:
            self._oa = 1
        if pn is not None:
            self._pn = pn
        if pys is not None:
            self._pys = pys
        if pye is not None:
            self._pye = pye
        if pu is not None:
            self._pu = pu
        if ctype is not None:
            self._ctype = ctype
