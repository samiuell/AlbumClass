import unittest
from album.Album import Album


class AlbumClassBaseTestCases(unittest.TestCase):
    """
    Base class for Album Class test cases.
    Implements setUp() for every test case that inherits it.
    """

    def setUp(self):
        """ sets up typical and unusual cases"""


    ## TYPICAL ##
        # Using David Bowie's iconic album as the first sample test case- has all typical values and no specified value for colour
        self._typical1 = Album("The Rise and Fall of Ziggy Stardust and the Spiders from Mars", "David Bowie", 49.99, 
                               ["Five Years", "Soul Love", "Moonage Daydream", "Starman", 
                                "It Ain't Easy", "Lady Stardust", "Star", "Hang On to Yourself", 
                                "Ziggy Stardust", "Suffragette City", "Rock 'n' Roll Suicide"],
                                38.65)
        
        # Using The Strokes' debut EP to test a typical album that is an EP and has a specified colour
        self._typical2 = Album("The Modern Age", "The Strokes", 30.00, ["The Modern Age", "Last Nite", "Barely Legal"],
                               11.15, "Red")
        

    ## NAME ##
        
        # An album name without words
        self._unusual_name1 = Album("!!234", "artist", 10, ["one", "two"], 10)

        # An int value for album name
        self._unusual_name2 = Album(234, "artist", 10, ["one", "two"], 10)


    ## ARTIST ##

        # An arist name without words 
        self._unusual_artist1 = Album("Name", "29.aj3 &&", 10, ["one", "two"], 10)

        # A float value for artist name
        self._unusual_artist2 = Album("Name", 2.30, 10, ["one", "two"], 10)


    ## COLOUR ##

        # A weird colour name -> should be handled as normal because creative designs are common in vinyls
        self._unusual_colour1 = Album("Name", "Artist", 10, ["one", "two"], 10, "Brownish redish stripes with white polka dots")

        # An int value for colour
        self._unusual_colour2 = Album("Name", "Artist", 10, ["one", "two"], 10, 21)

        
    ### PRICE ###

        # A price of 0 -> should be handled as normal incase an Album is given away for free
        self._unusual_price1 = Album("Name", "Artist", 0, ["one", "two"], 10)

        # A very high price
        self._unusual_price2 = Album("Name", "Artist", 19990, ["one", "two"], 10)

        # A string value for price
        self._unusual_price3 = Album("Name", "Artist", "10", ["one", "two"], 10)


    ### DURATION ###

        # A very low duration
        self._unusual_duration1 = Album("Name", "Artist", 10, ["one", "two"], 0.010)

        # A very high duration
        self._unusual_duration2 = Album("Name", "Artist", 10, ["one", "two"], 100000)

        # A string value for duration
        self._unusual_duration3 = Album("Name", "Artist", 10, ["one", "two"], "10")


    ### TRACKS ####

        # A single track in the tracklist
        self._unusual_track1 = Album("Name", "Artist", 10, ["one"], 10)
        
        # int values for tracks
        self._unusual_track2 = Album("Name", "Artist", 10, [1, 2], 10)
