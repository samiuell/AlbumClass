# Album.py
#
# Author: Sam Gupta
# Email: s76gupta@uwaterloo.ca
# Student ID: 21070644
#
# Source code for the Album class.


import sys 

class Album:
    """ Album

        Creates an individual vinyl to be sold on an online store
    """

    def __init__(self, name : str, artist : str, price : float, tracks : list[str], duration : float, colour = "Black"):
        """Album constructor

        name: the album name
        artist: the artist name
        price: the price of the album in CAD
        tracks: the tracks of the album in chronological order
        duration: the total duration of the album in minutes
        colour: the colour of the vinyl, defaults to black

        Calculated Fields: 
        num_tracks (int) = the number of tracks in the album
        ep (boolean) = whether or not the album is an EP
        """
        
    # _.NAME

        # Checking for empty string
        if name == "":
            raise ValueError
        
        # Checking for non-string value
        name = str(name)

        self._name = name
    
    # ._ARTIST

        # Checking for empty string
        if artist == "":
            raise ValueError
        
        # Checking for non-string value
        artist = str(artist)

        self._artist = artist
    
    #._PRICE

        # Checking for non-float values
        price = float(price)

        # Checking for negative values
        if price < 0:
            raise ValueError
        
        self._price = price

    #._TRACKS (and ._num_tracks)

        # Checking for string values in list
        for i in range(len(tracks)):
            tracks[i] = str(tracks[i])

        # Checking for empty list
        if len(tracks) == 0:
            raise ValueError
        
        self._tracks = tracks
        self._num_tracks = len(tracks)

    #._DURATION

        # Checking for float value
        duration = float(duration)

        # Checking for 0 or negative duration
        if duration <= 0:
            raise ValueError

        self._duration = duration

    #._COLOUR

        # Checking for empty string
        if colour == "":
            raise ValueError
        
        # Checking for non-string value
        colour = str(colour)

        self._colour = colour

    #._EP

        # True if total duration is less than or equal to 30 minutes
        if duration <= 30:
            self._ep = True
        else:
            self._ep = False


    ###############
    ## ACCESSORS ##
    ###############


    def get_name(self) -> str:
        """get_name()

        Returns the Albums's name
        """

        return self._name
    

    def get_artist(self) -> str:
        """get_artist()
        
        Returns the artist's name 
        """
        
        return self._artist


    def get_price(self) -> float:
        """get_price()

        Returns the Album's price in CAD
        """
        
        return self._price


    def get_tracks(self) -> list:
        """get_tracks()

        Returns the Album's tracklist
        """

        return self._tracks
    

    def get_num_tracks(self) -> int:
        """get_num_tracks()
        
        Returns the number of tracks in the Album
        """
        tracks = self.get_tracks()
        num_tracks = len(tracks)
        return num_tracks
    

    def get_duration_minutes(self) -> float:
        """get_duration_minutes()
        
        Returns the total duration of the album in minutes
        """
        
        return self._duration
    
    def get_duration_seconds(self) -> float:
        """get_duration_seconds()
        
        Returns the total duration of the album in seconds
        """
        
        # Multiplies the duration in minutes by 60
        minutes = self.get_duration_minutes()
        seconds = minutes * 60
        return seconds
    

    def get_colour(self) -> str:
        """get_colour()
        
        Returns the colour of the vinyl
        """
        
        return self._colour
    

    def get_ep(self) -> bool:
        """get_ep()
        
        Returns whether or not the Album is an EP
        """
        
        duration = self.get_duration_minutes()
        
        # Checks if duration is less than or equal to 30
        if duration <= 30:
            return True
        
        return False


    #############
    ## SETTERS ##
    #############
    

    def set_name(self, name : str):
        """set_name()

        name: the new name of the Album
        """

        # Checking for empty string
        if name == "":
            raise ValueError
        
        # Checking for non-string value
        name = str(name)

        self._name = name
    

    def set_artist(self, artist : str) -> str:
        """set_artist()
        
        artist: the new artist's name
        """
        
        # Checking for empty string
        if artist == "":
            raise ValueError
        
        # Checking for non-string value
        artist = str(artist)

        self._artist = artist
    

    def set_price(self, price : float):
        """set_price()

        price: the new price for the Album
        """
        
        # Checking for non-float values
        price = float(price)

        # Checking for negative values
        if price < 0:
            raise ValueError
        
        self._price = price


    def set_tracks(self, tracks : list[str]):
        """set_tracks()

        tracks: the Album's new tracklist
        """
        
        # Checking for string values in list
        for i in range(len(tracks)):
            tracks[i] = str(tracks[i])

        # Checking for empty list
        if len(tracks) == 0:
            raise ValueError
        
        self._tracks = tracks

    
    def set_duration(self, duration : float):
        """set_duration()
        
        duration: the new duration of the Album
        """
        
        # Checking for float value
        duration = float(duration)

        # Checking for 0 or negative duration
        if duration <= 0:
            raise ValueError

        self._duration = duration


    def set_colour(self, colour : str):
        """set_colour()
        
        colour: the new colour of the vinyl
        """

        # Checking for empty string
        if colour == "":
            raise ValueError
        
        # Checking for non-string value
        colour = str(colour)

        self._colour = colour


    ####################
    ## OTHER MUTATORS ##
    ####################


    def add_track(self, track_name : str, track_num : int, track_length : float):
        """add_track()
        
        adds a track to the Album tracklist
        also updates Album's duration

        track_name: name of track to add
        track_num: chronological position of track (4th track -> track_num = 4)
        track_length: duration of track in minutes 
        """
        
        ## ERRORS ##

        # Checking for correct types
        track_name = str(track_name)
        track_num = int(track_num)
        track_length = float(track_length)
        
        # Checking for empty name
        if track_name == "":
            raise ValueError
        
        # Checking for 0 or negative values for track num and track length
        elif track_num <= 0:
            raise ValueError
        elif track_length <= 0:
            raise ValueError
        
        # Checking if track num is more than num tracks + 1
        num_tracks = self.get_num_tracks()
        if track_num > (num_tracks + 1):
            raise ValueError
        

        ## ADDING TRACK ##

        tracklist = self.get_tracks()
        
        # Adding song to the end of the album
        if track_num == (num_tracks + 1):
            tracklist.append(track_name)
        
        # Adding song to desired index -> 1st track would be index = 0
        else:
            tracklist.insert(track_num - 1, track_name)
        

        ## UPDATING VALUES ##

        # Setting new tracklist
        self.set_tracks(tracklist)

        # Setting new duration
        duration = self.get_duration_minutes()
        self.set_duration(duration + track_length)



    def remove_track(self, track_name : str, track_length : float):
        """remove_track()
        
        removes a track from the Album tracklist
        also updates Album's duration
        
        track_name: name of track to remove
        track_length: duration of track in minutes
        """
        
        ## ERRORS ##

        # Checking for correct types
        track_name = str(track_name)
        track_length = float(track_length)

        # Checking for empty name
        if track_name == "":
            raise ValueError
        
        # Checking for 0 or negative track length
        elif track_length <= 0:
            raise ValueError
        
        # Checking if track length would make duration 0 or negative
        duration = self.get_duration_minutes()
        if (duration - track_length) <= 0:
            raise ValueError
        
        # Checking if track name exists in tracklist
        tracklist = self.get_tracks()
        tracklist.index(track_name)
        

        ## REMOVING TRACK AND UPDATING VALUES ##

        tracklist.remove(track_name)
        self.set_tracks(tracklist)
        self.set_duration(duration - track_length)



    def change_track_name(self, old_name : str, new_name : str):
        """change_track_name()
        
        changes a specific track's name
        
        old_name: current name of track to change
        new_name: desired name of track
        """
        
        ## ERRORS ##

        # Checking for correct types
        old_name = str(old_name)
        new_name = str(new_name)

        # Checking for empty strings
        if old_name == "":
            raise ValueError
        elif new_name == "":
            raise ValueError
        
        # Checking if old_name is in tracklist
        tracklist = self.get_tracks()
        index = tracklist.index(old_name)

        # CHANGING NAME
        tracklist[index] = new_name


    #####################
    ## MEMORY ANALYSIS ##
    #####################


    def __sizeof__(self) -> float:
        """ __sizeof__()
        Sums the memory of each individual field of an instance of the Album Class
        """

        return (sys.getsizeof(self._name) + sys.getsizeof(self._artist) + sys.getsizeof(self._price) 
                + sys.getsizeof(self._tracks) + sys.getsizeof(self._duration) + sys.getsizeof(self._colour)
                + sys.getsizeof(self._num_tracks) + sys.getsizeof(self._ep))


if __name__ ==  '__main__':
   """ 
   Prints the size of albums with 1-100 songs
   """
   basicAlbum = Album("name", "artist", 10, ["one"], 10)
   
   for i in range(1, 101):
       basicAlbum.add_track("name", 1, 1)   
       size = basicAlbum.__sizeof__()
       print("Size of Album with", i, "tracks:", size)
