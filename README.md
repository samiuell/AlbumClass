Name: Sam Gupta 

Email: s76gupta@uwaterloo.ca

This program tests and creates an Album class. An object of this class represents a musical album to be purchased as a vinyl on an online shop. The fields of this class include a name, artist, price, colour, tracklist, number of tracks, total duration and whether or not it is an EP. Methods within the class allow the user to display the track list, alter the tracks, change the price, get the total duration in either minutes or seconds, and more. 

# Purpose
This program was created for assignment 1 of MSE 240. Its purpose was to practice and develop skills in object oriented design as well as unit testing.

# Class Description

## Fields Overview
**Constructor:**    
Album(name, artist, price, tracks, duration, colour)

**Parameters:**    
name (str): the album nme     
artist (str): the artist name   
price (float): the price of the album in CAD    
tracks (list[str]): the tracks of the album in      chronological order    
duration (float): the total duration of the album in minutes   
colour (str): the colour of the vinyl- defaults to black

**Calculated Fields:**  
num_tracks (int): the number of tracks in the tracklist    
ep (bool): whether or not it is an ep

## Methods
**Getters:**      
get_name(): return's the album's name     
get_artist(): return's the album's artist     
get_price(): return's the price of the album    
get_colour(): return's the colour of the vinyl    
get_tracks(): return's the tracklist of the album    
get_num_tracks(): returns the number of tracks in the album    
get_duration_in_minutes(): returns the total duration in minutes     
get_duration_seconds(): returns the total duration in seconds    
get_ep(): returns whether or not the album is an ep   

**Setters**       
set_name(name -> str): sets the album's name    
set_artist(artist -> str): sets the album's artist   
set_price(price -> float): sets the price   
set_tracks(tracks -> list[str]): sets the album's tracklist    
set_duration(duration -> float): sets the duration    
set_colour(colour -> str): sets the vinyl's colour   

**Other Mutators**    
add_track(track_name -> str, track_num -> int, track_length -> float): Adds a track to the tracklist and updates total duration      
remove_track(track_name -> str, track_length -> float): Removes a track from the tracklist and updates total duration     
change_track_name(old_name -> str, new_name -> str): changes a specific track's name

# Acknowledgements

I attended the professor's office hours for clarification of accessor test cases and format details.     
I also used the following website as a quick refresher of the .index() function for lists: https://www.w3schools.com/python/ref_list_index.asp 
