from warnings import resetwarnings
from my_spotify import MySpotify
import logging

logger = logging.getLogger()

if __name__ == '__main__':

    scopes = [ "user-library-read", "playlist-read-private", "user-library-modify",\
            "user-follow-read", "playlist-modify-private", "playlist-modify-public",\
            "user-top-read", "user-read-recently-played"]

    sp = MySpotify(scope=scopes)
    sp.connect()
    sp.get_current_user_top_tracks()
    logger.info("Process Finished")
    