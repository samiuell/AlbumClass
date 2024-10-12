# test_album_mutators
#
# Author: Sam Gupta
# Email: s76gupta@uwaterloo.ca
# Student ID: 21070644
#
# these are the unit tests for Album


import unittest
from test import AlbumClassBaseTestCases
from album.Album import Album


class TestAlbumMutators(AlbumClassBaseTestCases):
    """
    Tests all mutators for Album class
    """


#############
## SETTERS ##
#############

    #
    # set_name
    #

    # Tests typical case
    def test_setname_typical1(self):
        ab = self._typical1
        ab.set_name("test")
        self.assertEqual("test", ab.get_name())
    
    # Tests typical case
    def test_setname_typical2(self):
        ab = self._typical2
        ab.set_name("test")
        self.assertEqual("test", ab.get_name())

    # Tests unusual case of non-words for name
    def test_setname_unusual1(self):
        ab = self._typical1
        ab.set_name("12,53&")
        self.assertEqual("12,53&", ab.get_name())

    # Tests unusual case with int
        ab = self._typical1
        ab.set_name(12)
        self.assertEqual("12", ab.get_name())
    
    # Tests valueError of empty name
    def test_setname_valueError(self):
        ab = self._typical1
        with self.assertRaises(ValueError):
            ab.set_name("")


    #
    # set_artist
    #

    # Tests typical case
    def test_setartist_typical1(self):
        ab = self._typical1
        ab.set_artist("test")
        self.assertEqual("test", ab.get_artist())
    
    # Tests typical case
    def test_setartist_typical2(self):
        ab = self._typical2
        ab.set_artist("test")
        self.assertEqual("test", ab.get_artist())

    # Tests unusual case of non-words for artist
    def test_setartist_unusual1(self):
        ab = self._typical1
        ab.set_artist("!!!!")
        self.assertEqual("!!!!", ab.get_artist())

    # Tests unusual case with floats
    def test_setartist_unusual1(self):
        ab = self._typical1
        ab.set_artist(22.1)
        self.assertEqual("22.1", ab.get_artist())
    
    # Tests valueError of empty artist
    def test_setartist_valueError(self):
        ab = self._typical1
        with self.assertRaises(ValueError):
            ab.set_artist("")


    #
    # set_price
    #

    # Tests typical case
    def test_setprice_typical1(self):
        ab = self._typical1
        ab.set_price(20.0)
        self.assertEqual(20.0, ab.get_price())
    
    # Tests typical case
    def test_setprice_typical2(self):
        ab = self._typical2
        ab.set_price(33.2)
        self.assertEqual(33.2, ab.get_price())

    # Tests unusual case of 0 value
    def test_setprice_unusual1(self):
        ab = self._typical1
        ab.set_price(0.0)
        self.assertEqual(0.0, ab.get_price())

    # Tests unusual case of high value
    def test_setprice_unusual2(self):
        ab = self._typical1
        ab.set_price(9999.5)
        self.assertEqual(9999.5, ab.get_price())
    
    # Tests unusual case of string
    def test_setprice_unusual3(self):
        ab = self._typical1
        ab.set_price("10.0")
        self.assertEqual(10.0, ab.get_price())

    # Tests valueError of negative price
    def test_setprice_valueError(self):
        ab = self._typical1
        with self.assertRaises(ValueError):
            ab.set_price(-10.4)
        with self.assertRaises(ValueError):
            ab.set_price(-20)
    
    # Tests valueError for words
    def test_setprice_typeError(self):
        ab = self._typical1
        with self.assertRaises(ValueError):
            ab.set_price("ten")


    #
    # set_tracks
    #

    # Tests a typical case
    def test_settracks_typical1(self):
        ab = self._typical1
        ab.set_tracks(["one", "two"])
        self.assertEqual(["one", "two"], ab.get_tracks())

    # Tests a typical case 
    def test_settracks_typical2(self):
        ab = self._typical2
        ab.set_tracks(["one", "two"])
        self.assertEqual(["one", "two"], ab.get_tracks())

    # Tests unusual case of only one track
    def test_settracks_unusual1(self):
        ab = self._typical1
        ab.set_tracks(["one"])
        self.assertEqual(["one"], ab.get_tracks())

    # Tests unusual case of int values
    def test_settracks_unusual2(self):
        ab = self._typical1
        ab.set_tracks([1, 2])
        self.assertEqual(["1", "2"], ab.get_tracks())

    # Tests valueError for empty list
    def test_settracks_valueError(self):
        ab = self._typical1
        with self.assertRaises(ValueError):
            ab.set_tracks([])

    # Tests typeError for string
    def test_settracks_typeError(self):
        ab = self._typical1
        with self.assertRaises(TypeError):
            ab.set_tracks("Hi")


    #
    # set_duration
    #

    # Tests typical case
    def test_setduration_typical1(self):
        ab = self._typical1
        ab.set_duration(4.3)
        self.assertEqual(4.3, ab.get_duration_minutes())
    
    # Tests typical case
    def test_setduration_typical2(self):
        ab = self._typical2
        ab.set_duration(2.0)
        self.assertEqual(2.0, ab.get_duration_minutes())

    # Tests unusual case of low value
    def test_setduration_unusual1(self):
        ab = self._typical1
        ab.set_duration(0.001)
        self.assertEqual(0.001, ab.get_duration_minutes())

    # Tests unusual case of high value
    def test_setduration_unusual2(self):
        ab = self._typical1
        ab.set_duration(999.4)
        self.assertEqual(999.4, ab.get_duration_minutes())
    
    # Tests unusual case of string
    def test_setduration_unusual3(self):
        ab = self._typical1
        ab.set_duration("3.5")
        self.assertEqual(3.5, ab.get_duration_minutes())

    # Tests valueError for zero value
    def test_setduration_valueError_zero(self):
        ab = self._typical1
        with self.assertRaises(ValueError):
            ab.set_duration(0)

    # Tests valueError of negative value
    def test_setduration_valueError_negative(self):
        ab = self._typical1
        with self.assertRaises(ValueError):
            ab.set_duration(-2.4)
        with self.assertRaises(ValueError):
            ab.set_duration(-6)
    
    # Tests valueError for words
    def test_setduration_typeError(self):
        ab = self._typical1
        with self.assertRaises(ValueError):
            ab.set_duration("two")


    #
    # set_colour
    #

    # Tests typical case
    def test_setcolour_typical1(self):
        ab = self._typical1
        ab.set_colour("red")
        self.assertEqual("red", ab.get_colour())
    
    # Tests typical case
    def test_setcolour_typical2(self):
        ab = self._typical2
        ab.set_colour("white")
        self.assertEqual("white", ab.get_colour())

    # Tests unusual case of strange colour name
    def test_setcolour_unusual1(self):
        ab = self._typical1
        ab.set_colour("test")
        self.assertEqual("test", ab.get_colour())
    
    # Tests unusual case of int value
    def test_setcolour_unusual2(self):
        ab = self._typical1
        ab.set_colour(10)
        self.assertEqual("10", ab.get_colour())

    # Tests valueError of empty colour
    def test_setcolour_valueError(self):
        ab = self._typical1
        with self.assertRaises(ValueError):
            ab.set_colour("")


####################
## OTHER MUTATORS ##
####################


    #
    # add_track
    #

    # Tests a typical case 
    def test_addtrack_typical1(self):
        ab = self._typical1
        ab.add_track("Changes", 4, 3.62)
        self.assertEqual("Changes", ab._tracks[3])
        self.assertEqual(12, ab.get_num_tracks())
        self.assertAlmostEqual(42.27, ab.get_duration_minutes())

    # Tests a typical calse
    def test_addtrack_typical2(self):
        ab = self._typical2
        ab.add_track("test", 4, 30)
        self.assertEqual("test", ab._tracks[3])
        self.assertEqual(4, ab.get_num_tracks())
        self.assertAlmostEqual(41.15, ab.get_duration_minutes())
        self.assertEqual(False, ab.get_ep())

    # Tests an unusual case of low length value
    def test_addtrack_unusual1(self):
        ab = self._typical1
        ab.add_track("test", 4, 0.12)
        self.assertAlmostEqual(38.77, ab.get_duration_minutes())

    # Tests an unusual case of high length value
    def test_addtrack_unusual2(self):
        ab = self._typical1
        ab.add_track("test", 4, 999)
        self.assertAlmostEqual(1037.65, ab.get_duration_minutes())

    # Tests an unusual case for string track num
    def test_addtrack_unusual3(self):
        ab = self._typical1
        ab.add_track("test","4", 3.62)
        self.assertEqual("test", ab._tracks[3])

    # Tests an unusual case for a string track length
    def test_addtrack_unusual4(self):
        ab = self._typical1
        ab.add_track("test", 4, "3.62")
        self.assertAlmostEqual(42.27, ab.get_duration_minutes())

    # Tests valueError for empty name
    def test_addtrack_valueError_emptyName(self):
        ab = self._typical1
        with self.assertRaises(ValueError):
            ab.add_track("", 4, 2.0)

    # Tests valueError for 0 value for track num
    def test_addtrack_valueError_zeroNum(self):
        ab = self._typical1
        with self.assertRaises(ValueError):
            ab.add_track("test", 0, 2.0)

    # Tests valueError for 0 value for track length
    def test_addtrack_valueError_zeroLength(self):
        ab = self._typical1
        with self.assertRaises(ValueError):
            ab.add_track("test", 4, 0)

    # Tests valueError for negative track num
    def test_addtrack_valueError_negativeNum(self):
        ab = self._typical1
        with self.assertRaises(ValueError):
            ab.add_track("test", -4, 2.0)
        with self.assertRaises(ValueError):
            ab.add_track("test", -3.4, 2.0)

    # Tests valueError for negative track length
    def test_addtrack_valueError_negativeLength(self):
        ab = self._typical1
        with self.assertRaises(ValueError):
            ab.add_track("test", 4, -2.21)
        with self.assertRaises(ValueError):
            ab.add_track("test", 4, -5)

    # Tests valueError for words for track num
    def test_addtrack_typeError_wordNum(self):
        ab = self._typical1
        with self.assertRaises(ValueError):
            ab.add_track("test", "four", 2.0)

    # Tests ValueError for words for track length
    def test_addtrack_typeError_wordLength(self):
        ab = self._typical1
        with self.assertRaises(ValueError):
            ab.add_track("test", 4, "twenty")


    #
    # remove_track
    #

    # Tests a typical case
    def test_removetrack_typical1(self):
        ab = self._typical1
        ab.remove_track("Soul Love", 3.57)
        self.assertEqual("Moonage Daydream", ab._tracks[1])
        self.assertEqual(10, ab.get_num_tracks())
        self.assertAlmostEqual(35.08, ab.get_duration_minutes())

    # Tests a typical case
    def test_removetrack_typical2(self):
        ab = self._typical2
        ab.remove_track("Barely Legal", 4.62)
        self.assertEqual(2, ab.get_num_tracks())
        self.assertAlmostEqual(6.53, ab.get_duration_minutes())
    
    # Tests an unusual case for low track length
    def test_removetrack_unusual1(self):
        ab = self._typical1
        ab.remove_track("Soul Love", 0.01)
        self.assertAlmostEqual(38.64, ab.get_duration_minutes())

    # Tests an unusual case of string for track length
    def test_removetrack_unusual2(self):
        ab = self._typical1
        ab.remove_track("Soul Love", "3.57")
        self.assertAlmostEqual(35.08, ab.get_duration_minutes())
    
    # Tests valueError for 0 track length
    def test_removetrack_valueError_zerolength(self):
        ab = self._typical1
        with self.assertRaises(ValueError):
            ab.remove_track("test", 0)

    # Tests valueError for negative track length
    def test_removetrack_valueError_negativeLength(self):
        ab = self._typical1
        with self.assertRaises(ValueError):
            ab.remove_track("test", -3.40)
        with self.assertRaises(ValueError):
            ab.remove_track("test", -2)

    # Tests valueError for empty track name
    def test_removetrack_valueError_emptyName(self):
        ab = self._typical1
        with self.assertRaises(ValueError):
            ab.remove_track("", 0)

    # Tests valueError for words for track length
    def test_removetrack_typeError_wordLength(self):
        ab = self._typical1
        with self.assertRaises(ValueError):
            ab.remove_track("test", "thirty")

    # Tests valueError for track name not in tracklist
    def test_removetrack_valueError_dne(self):
        ab = self._typical1
        with self.assertRaises(ValueError):
            ab.remove_track("test", 3)
    

    #
    # change_track_name
    #

    # Tests a typical case
    def test_changetrackname_typical1(self):
        ab = self._typical1
        ab.change_track_name("Star", "Starlight")
        self.assertEqual("Starlight", ab._tracks[6])

    # Tests a typical case
    def test_changetrackname_typical2(self):
        ab = self._typical2
        ab.change_track_name("The Modern Age", "Is This It")
        self.assertEqual("Is This It", ab._tracks[0])
    
    # Tests valueError for empty old name
    def test_changetrackname_valueError_emptyOld(self):
        ab = self._typical1
        with self.assertRaises(ValueError):
            ab.change_track_name("", "test")

    # Tests valueError for empty new name
    def test_changetrackname_valueError_emptyNew(self):
        ab = self._typical1
        with self.assertRaises(ValueError):
            ab.change_track_name("Star", "")

    # Tests error for old name not found in list
    def test_changetrackname_valueError_dne(self):
        ab = self._typical1
        with self.assertRaises(ValueError):
            ab.change_track_name("test", "test2")
