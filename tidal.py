import tidalapi


class Tidal:
    def __init__(self) -> None:

        self.session = tidalapi.Session()
        # another login will be used probably
        self.session.login_oauth_simple()
        self.user_id = self.session.user.id

    def get_saved_songs(self):
        favorites = tidalapi.user.Favorites(self.session, self.user_id)
        tracks = favorites.tracks()
        tracks_readable = []

        for track in tracks:
            tracks_readable.append({
                'title': track.name,
                'artist': track.artist.name
            })
        return tracks_readable
    
    def get_saved_playlists(self):
        user_playlists = self.session.user.playlists()
        # TODO
        # return list of dicts, every dict
        # {playlist name, number of tracks, list of tracks}

        return user_playlists



# ----------------------------


# session = tidalapi.Session()
# session.login_oauth_simple()

# user_id = session.user.id
# user_playlists = session.user.playlists()

# user = tidalapi.user.User(session, user_id)

# favorites = tidalapi.user.Favorites(session, user_id)

# tracks = favorites.tracks()
# for track in tracks:
#     print(track.name, track.artist.name)
