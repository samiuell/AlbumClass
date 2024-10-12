# test_album_accessors
#
# Author: Sam Gupta
# Email: s76gupta@uwaterloo.ca
# Student ID: 21070644
#
# these are the unit tests for Album


import unittest
from test import AlbumClassBaseTestCases
from album.Album import Album


class TestAlbumAccessors(AlbumClassBaseTestCases):
    """ Tests all the accessors for the Album Class
    
        Accessors: 
        get_name()
        get_artist()
        get_price()
        get_colour()
        get_tracks()
        get_num_tracks()
        get_duration__minutes()
        get_duration_seconds()
    """


    # 
    # get_name
    # 

    # Tests a typical case
    def test_getname_typical1(self):
        self.assertEqual("The Rise and Fall of Ziggy Stardust and the Spiders from Mars", self._typical1.get_name())

    # Tests a typical case
    def test_getname_typical2(self):
        self.assertEqual("The Modern Age", self._typical2.get_name())

    # Tests an unusal case with non-words
    def test_getname_unusual1(self):
        self.assertEqual("!!234", self._unusual_name1.get_name())

    
    #
    # get_artist
    #

    # Tests a typical case
    def test_getartist_typical1(self):
        self.assertEqual("David Bowie", self._typical1.get_artist())

    # Tests a typical case
    def test_getartist_typical2(self):
        self.assertEqual("The Strokes", self._typical2.get_artist())

    # Tests an unusual case with non-words
    def test_getartist_unusual1(self):
        self.assertEqual("29.aj3 &&", self._unusual_artist1.get_artist())




    #
    # get_price
    #

    # Tests a typical case
    def test_getprice_typical1(self):
        self.assertEqual(49.99, self._typical1.get_price())

    # Tests a typical case
    def test_getprice_typical2(self):
        self.assertEqual(30.00, self._typical2.get_price())

    # Tests an unusual case with a price of 0
    def test_getprice_unusual1(self):
        self.assertEqual(0, self._unusual_price1.get_price())

    # Tests an unusual case with a high value
    def test_getprice_unusual2(self):
        self.assertEqual(19990, self._unusual_price2.get_price())


    #
    # get_colour
    #

    # Tests a typical case 
    def test_getcolour_typical1(self):
        self.assertEqual("Black", self._typical1.get_colour())

    # Tests a typical case
    def test_getcolour_typical2(self):
        self.assertEqual("Red", self._typical2.get_colour())

    # Tests an unusual case with a non-colour
    def test_getcolour_unusual1(self):
        self.assertEqual("Brownish redish stripes with white polka dots", self._unusual_colour1.get_colour())
    

    #
    # get_tracks
    #

    # Tests a typical case 
    def test_gettracks_typical1(self):
        self.assertEqual(["Five Years", "Soul Love", "Moonage Daydream", "Starman", 
                                "It Ain't Easy", "Lady Stardust", "Star", "Hang On to Yourself", 
                                "Ziggy Stardust", "Suffragette City", "Rock 'n' Roll Suicide"], self._typical1.get_tracks())

    # Tests a typical case
    def test_gettracks_typical2(self):
        self.assertEqual(["The Modern Age", "Last Nite", "Barely Legal"], self._typical2.get_tracks())

    # Tests an unusual case with a single track
    def test_gettracks_unusual1(self):
        self.assertEqual(["one"], self._unusual_track1.get_tracks())


    #
    # get_num_tracks
    #

    # Tests a typical case 
    def test_getnumtracks_typical1(self):
        self.assertEqual(11, self._typical1.get_num_tracks())

    # Tests a typical case
    def test_getnumtracks_typical2(self):
        self.assertEqual(3, self._typical2.get_num_tracks())

    # Tests an unusual case with a single track
    def test_getnumtracks_unusual(self):
        self.assertEqual(1, self._unusual_track1.get_num_tracks())


    #
    # get_duration_minutes
    #

    # Tests a typical case
    def test_durationmin_typical1(self):
        self.assertAlmostEqual(38.65, self._typical1.get_duration_minutes())

    # Tests a typical case
    def test_durationmin_typical2(self):
        self.assertAlmostEqual(11.15, self._typical2.get_duration_minutes())

    # Tests an unusual case with a low value
    def test_durationmin_unusual1(self):
        self.assertAlmostEqual(0.01, self._unusual_duration1.get_duration_minutes())

    # Tests an unusual case with a high value
    def test_durationmin_unusual2(self):
        self.assertAlmostEqual(100000, self._unusual_duration2.get_duration_minutes())


    #
    # get_duration_seconds
    #

    # Tests a typical case
    def test_durationsec_typical1(self):
        self.assertAlmostEqual(2319, self._typical1.get_duration_seconds())

    # Tests a typical case
    def test_durationsec_typical2(self):
        self.assertAlmostEqual(669, self._typical2.get_duration_seconds())

    # Tests an unusual case with a low value
    def test_durationsec_unusual1(self):
        self.assertAlmostEqual(0.6, self._unusual_duration1.get_duration_seconds())

    # Tests an unusual case with a high value
    def test_durationsec_unusual2(self):
        self.assertAlmostEqual(6000000, self._unusual_duration2.get_duration_seconds())

    
    #
    # get_ep
    #

    # Tests a typical case
    def test_getep_typical1(self):
        self.assertFalse(self._typical1.get_ep())

    # Tests a typical case
    def test_getep_typical2(self):
        self.assertTrue(self._typical2.get_ep())
