# SWEN712_FinalProject
This Project focuses on finding the genres that are most popular in the DHH Community. We try to address accessibility in terms of music in context with the DHH Community.

To extract data from online platforms, we used Pyhton APIs to gather results based off of music pages from twitter and playlists from Spotify.

How to Run the files

TopHastags.py: This is a Python file to extract top Hashtags for a specified twitter account. To use this file enter credentials such as API access token and secret key, also the consumer secret and key. After running the file, console will prompt to provide with a twitter account without '@' annotation and number of tweets to process. Entering the account will generate the top most frequently used hasgtags from that account for the spicified number of tweets.

SpotifyCrawler.py: To pull the artist names from a given playlist. It uses Spotipy API and to enable it, provide spotify developer client ID and secret key. After running the file, the console will display the output in json format. To results obtained will have artists ids that will be used in map corresponding genres in DHHGenres.py

DHHGenres.py:  This is map the artists to their genres using the artist ids obtained from running SpotifyCrawler.py, this will also make use of spotipy api so client ID and secret key will be required here again and output relevent results of genres.
