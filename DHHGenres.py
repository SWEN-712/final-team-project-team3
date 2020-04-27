'''
SWEN 712 - Engineering Accessible Software- Final Project Deliverable

@developed by: Sai Gowtham Kapa, Vaibhavi Raut, Manish Hemkant Waghdhare, Pratyush Karna

@Interpreter- 3.6.0

This is a python script to mine a list of artist IDs retrieved from SpotifyCrawler.py and get the corresponding genre(s) to the artist.
'''
from spotipy.oauth2 import SpotifyClientCredentials #spotify library to process spotify data points
import spotipy

class DHHGenres():
    '''
    Override Function on_data() to print a data stream
    '''
    def on_data(self, data):
        print(data)
        return True

    '''
    Override Function on_error() to return error in reading a stream if any
    '''
    def on_error(self, status):
        print(status)


'''
    Driver Function
    '''
def main():

    #spotify developer client ID and secret key to enable the API
    cid = '1802dfa46438454595c5627b670339f3'
    secret = 'fc3771e4140f4caf87e43c01b8bdecdd'

    '''
          try-except block to handle the authentication provided by the SpotifyClientCredentials interface of spotipy
          @:exception - Checked Exception for failed Authentication 
          '''
    try:
        client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
        sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    except:
        print("Authentication Failed...")

    #take user input a list of artists IDs
    id_list = [] #initialize an empty list[] to store the IDs
    ar_id = input("Enter artists ID: ") #take list input from the user
    n = len(ar_id) #set the length of the list
    for i in range(0,n): #iterate over all elements input by the user
        id_list.append(ar_id) #keep appending them to the empty list

    #store the mined spotify artist information in the variable output
    #mine the genre as the primary attribute

    output = sp.artist(artist_id=ar_id) #set the parameter to user input of artist ID
    print(output) #print the output stream

# Calling main function
if __name__ == "__main__":
      while True:
       main()

#--------------------------------------------------END------------------------------------------------------------------