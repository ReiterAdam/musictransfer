import logging
import requests
import properties


class Deezer:
    def __init__(self):
        
        self.access_token = self.get_access_token()

        if self.access_token is None:
            logging.error('Token is not available. Try to refresh by get_access_token() method')


    def get_access_token(self):
        
        # need to set an endpoint where code(codefromabove) will be sent 
        # https://connect.deezer.com/oauth/auth.php?app_id=YOUR_APP_ID&redirect_uri=YOUR_REDIRECT_URI&perms=basic_access,email
        # https://connect.deezer.com/oauth/access_token.php?app_id=YOU_APP_ID&secret=YOU_APP_SECRET&code=THE_CODE_FROM_ABOVE

        config_values = properties.read_yaml(file_path='./config/dev.yml')
        secret_values = properties.read_yaml(file_path='./config/dev_secret.yml')        
        auth_url = 'https://connect.deezer.com/oauth/access_token.php'
        auth_data = {
            'grant_type': 'client_credentials',
            'client_id': secret_values['DEEZER']['CLIENT_ID'],
            'client_secret': secret_values['DEEZER']['CLIENT_SECRET'],
        }

        
        response = requests.post(auth_url, data=auth_data)
        
        if response.status_code == 200:
            access_token = response.json()['access_token']
            logging.info('Successfully authenticated with Deezer API')
            return access_token
        else:
            logging.error('Failed to authenticate with Deezer API')
            raise Exception('Failed to authorize with Deezer API')
        

    def get_saved_songs(self):
        
        saved_songs_url = 'https://api.deezer.com/user/me/tracks'
        headers = { 'Authorization': f'Bearer {self.access_token}'}

        response = requests.get(saved_songs_url, headers=headers)

        if response.status_code == 200:
            song_data = response.json()['data']
            songs = []
            for song in song_data:
                songs.append({
                    'title': song['title'],
                    'artist': song['artist']['name'],
                    'album': song['album']['title'],
                    'duration': song['duration'],
                    'link': song['link'],
                })
            return songs
        else:
            self.logger.error('Failed to retrieve saved songs from Deezer API')
            raise Exception('Failed to retrieve saved songs from Deezer API')
        
    def add_fav_songs(self, tracklist):
        pass
        # TODO
        # function which will take tracklist, find if it is available and return list of IDs in Deezer
        # also give list of songs that couldnt be find

        get_songs_ids(tracklist)

        # TODO
        # post to tracklist to reezer something

    def get_songs_ids(self):
        pass
