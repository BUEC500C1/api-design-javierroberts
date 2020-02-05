import tweepy
import keys
from google.cloud import vision
import io


def getFeed():
    auth = tweepy.OAuthHandler(keys.key, keys.skey)
    auth.set_access_token(keys.token, keys.stoken)

    api = tweepy.API(auth)

    public_tweets = api.home_timeline()
    for tweet in public_tweets:
        print(tweet.text)


# def annotateImage():
#     client = vision.ImageAnnotatorClient()
#     path = "test_image.png"

#     with io.open(path, 'rb') as image_file:
#         content = image_file.read()

#     image = vision.types.Image(content=content)

#     response = client.label_detection(image=image)
#     labels = response.label_annotations
#     print('Labels:')

#     for label in labels:
#         print(label.description)

#     if response.error.message:
#         raise Exception(
#             '{}\nFor more info on error messages, check: '
#             'https://cloud.google.com/apis/design/errors'.format(
#                 response.error.message))


if __name__ == "__main__":
