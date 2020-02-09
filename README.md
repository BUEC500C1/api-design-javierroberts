# api-design-javierroberts

GENERAL

This is an API for retrieving the twitter feed of a user (in the current implementation, that is myself). The data is presented in key-value pairs, where one key is "text", meaning the actual text of the tweet, and the other key is "image description", which is the Google Vision description of any image associated with the tweet.

TESTING

Testing was done locally because keys cannot be uploaded to GitHub. Testing was comprised of checking that the getFeed() function returned accurate text and image description values of my current twitter feed. I also tested the annotateImage() function by making sure that it consitently returned the same description for the same image URL.

TO RUN API

It is a flask-based API. To start hosting, simply run the api.py file.
