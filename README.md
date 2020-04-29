# Empirical Study on Music and its Popular Genres in the DHH Community
This Project focuses on finding the genres that are most popular in the DHH Community. We try to address accessibility in terms of music in context with the DHH Community.

## Methodology

To extract data from online platforms, we used Python APIs - tweepy and spotify on two different datasets to gather results based on DHH music related handles from twitter and playlists from Spotify. Then we combine the mined outputs to the output of the User Surveys on Google Forms and process the information on all three datasets in .csv format. 

We mine the popular genres, accessiblity services/technologies, composing of music and playing instruments from the datasets and analyze and visualize the findings to get some important inferences.  

## Running the Project

### Mining Twitter Handles

- clone the repository ```git clone```
- open with your favorite IDE (PyCharm preferable) or you can use IDLE
- ```pip install tweepy``` or add it in Project Interpreter from Settings in PyCharm
- run ```TopHashtags.py``` 
- input Twitter user account 
- input the number of latest tweets to process
- input number of top hashtags to retrieve
- get the top frequently used hashtags of the Twitter Account
- save it .csv or .xlxs or any maintainable format
- filter out genres in the Hashtags list

### Mining Spotify Playlists

- clone the repository ```git clone```
- open with your favorite IDE (PyCharm preferable) or you can use IDLE
- ```pip install spotipy``` or add it in Project Interpreter from Settings in PyCharm

#### Getting the Artists from DHH Playlists
- run ```SpotifyCrawler.py``` 
- input Playlist ID (from the URL) 
- get the list of Artists
- save it .csv or .xlxs or any maintainable format 

#### Getting the Artists from DHH Playlists
- run ```DHHGenres.py``` 
- input Artist ID from previous code 
- get the Genres 
- save it .csv or .xlxs or any maintainable format 

## Visualzing Results 
- Combine the outputs of all three datasets 
- Clean the data - eliminate redundancies and generalize some genres
- Generate Graphical Visualizations of following data:
  - popular genres among the DHH community
  - accessibility services/technologies availed by the DHH users for music
  - composition of music and instruments played by DHH indivduals  


