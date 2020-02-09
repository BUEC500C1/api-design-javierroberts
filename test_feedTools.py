import pytest
import feedTools


# Testing that the annotateImage() function is correctly annotating images with Googles Vision API.
def test_imageVision():
    assert feedTools.annotateImage(
        "https://pbs.twimg.com/media/EQTfQDoUwAIMsRY?format=jpg&name=4096x4096") == "Basketball player, Basketball, Basketball moves, Player, Sports, Team sport, Basketball court, Ball game, Tournament, Muscle"
