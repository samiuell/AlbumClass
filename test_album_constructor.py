# test_album_constructor
#
# Author: Sam Gupta
# Email: s76gupta@uwaterloo.ca
# Student ID: 21070644
#
# these are the unit tests for Album


import unittest
from test import AlbumClassBaseTestCases
from album.Album import Album


class TestAlbumConstructor(AlbumClassBaseTestCases):
    """
    Tests constructor method for Album Class
    """

## TYPICAL ##

    # Tests a typical case
    def test_constructor_typical1(self):
        ab = self._typical1
        self.assertEqual("The Rise and Fall of Ziggy Stardust and the Spiders from Mars",ab.get_name())
        self.assertEqual("David Bowie", ab.get_artist())
        self.assertAlmostEqual(49.99, ab.get_price())
        self.assertEqual(["Five Years", "Soul Love", "Moonage Daydream", "Starman", 
                                "It Ain't Easy", "Lady Stardust", "Star", "Hang On to Yourself", 
                                "Ziggy Stardust", "Suffragette City", "Rock 'n' Roll Suicide"], ab.get_tracks())
        self.assertEqual(11, ab.get_num_tracks())
        self.assertAlmostEqual(38.65, ab.get_duration_minutes())
        self.assertFalse(ab.get_ep())

    # Tests a typical case
    def test_constructor_typical2(self):
        ab = self._typical2
        self.assertEqual("The Modern Age", ab.get_name())
        self.assertEqual("The Strokes", ab.get_artist())
        self.assertEqual(30.00, ab.get_price())
        self.assertEqual(["The Modern Age", "Last Nite", "Barely Legal"], ab.get_tracks())
        self.assertEqual(3, ab.get_num_tracks())
        self.assertEqual(11.15, ab.get_duration_minutes())
        self.assertTrue(ab.get_ep())


## ._NAME ##

    # Tests unusual case with int
    def test_constructor_intName(self):
        self.assertEqual("234", self._unusual_name2.get_name())

    # Tests ValueError for empty name
    def test_constructor_valueError_emptyName(self):
        with self.assertRaises(ValueError):
            ab = Album("", "Artist", 10, ["one", "two"], 10)


## _ARTIST ##

    # Tests an unusual case with float
    def test_constructor_floatArtist(self):
        self.assertEqual("2.3", self._unusual_artist2.get_artist())

    # Tests ValueError for empty artist
    def test_constructor_valueError_emptyArtist(self):
        with self.assertRaises(ValueError):
            ab = Album("Name", "", 10, ["one", "two"], 10)


## _COLOUR ##

    # Tests an unusual case with int
    def test_constructor_intColour(self):
        self.assertEqual("21", self._unusual_colour2.get_colour())

    # Tests ValueError as empty colour
    def test_contructor_valueError_emptyColour(self):
        with self.assertRaises(ValueError):
            ab = Album("Name", "Artist", 10, ["one", "two"], 10, "")


## _TRACKS ##

    # Tests unusual case for list of ints
    def test_constructor_unusual_tracks(self):
        ab = Album("Name", "Artist", 10, [1, 2], 10)
        self.assertEqual(["1", "2"], ab.get_tracks())

    # Tests ValueError for empty list    
    def test_constructor_valueError_emptyList(self):
        with self.assertRaises(ValueError):
            ab = Album("Name", "Artist", 10, [], 10)

    # Tests TypeError for string as tracklist
    def test_constructor_typeError_stringTracks(self):
        with self.assertRaises(TypeError):
            ab = Album("Name", "Artist", 10, "test", 10)


## _DURATION ##

    # Tests unusual case for string 
    def test_constructor_strDuration(self):
        self.assertEqual(10.0, self._unusual_duration3.get_duration_minutes())

    # Tests ValueError for value of 0
    def test_constructor_valueError_zeroDuration(self):
        with self.assertRaises(ValueError):
            ab = Album("Name", "Artist", 10, ["one", "two"], 0)

    # Tests ValueError for negative values
    def test_constructor_valueError_negativeDuration(self):
        with self.assertRaises(ValueError):
            ab = Album("Name", "Artist", 10, ["one", "two"], -10)
        with self.assertRaises(ValueError):
            ab = Album("Name", "Artist", 10, ["one", "two"], -42.10)
    
    # Tests ValueError for string as duration
    def test_constructor_typeError_stringDuration(self):
        with self.assertRaises(ValueError):
            ab = Album("Name", "Artist", 10, ["one", "two"], "ten")


## _PRICE ##

    # Tests unusual case for string
    def test_constructor_strPrice(self):
        self.assertEqual(10.0, self._unusual_price3.get_price())

    # Tests ValueError for negative values
    def test_constructor_valueError_negativePrice(self):
        with self.assertRaises(ValueError):
            ab = Album("Name", "Artist", -10, ["one", "two"], 10)
        with self.assertRaises(ValueError):
            ab = Album("Name", "Artist", -00.32, ["one", "two"], 10)
    
    # Tests ValueError for string as price
    def test_constructor_typeError_stringPrice(self):
        with self.assertRaises(ValueError):
            ab = Album("Name", "Artist", "ten", ["one", "two"], 10)