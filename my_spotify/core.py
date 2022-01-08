"""[summary]
"""

import logging
import json
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth

class MySpotify:
    def __init__(self, scope) -> None:
        self.scope = scope
        self.spotify = None
        self.auth = None
        self.username = None
        self.logger = logging.getLogger("My_Spotify")

    def __get_auth(self):
        if self.auth is None:
            self.auth = SpotifyOAuth(scope=self.scope)
        else:
            self.auth = SpotifyOAuth(scope=self.scope)
        return self.auth

    def connect(self):
        auth = self.__get_auth()
        self.spotify = Spotify(auth_manager=auth)
        
    def get_current_user_top_tracks(self):
        try:
            response = self.spotify.current_user_top_tracks()
            with open("top_tracks", 'w') as fh:
                json.dump(response, fh)
        except:
            self.logger.warning("Exception !!")
