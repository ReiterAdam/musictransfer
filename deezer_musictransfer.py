from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session

import deezer
import properties

config_values = properties.read_yaml(file_path='./config/dev.yml')
secret_values = properties.read_yaml(file_path='./config/dev_secret.yml')        

class Deezer:
    def __init__(self):
        # Load Deezer API credentials from YAML file
        auth_url = 'https://connect.deezer.com/oauth/access_token.php'
        self.client_id = secret_values['DEEZER']['CLIENT_ID']
        self.client_secret = secret_values['DEEZER']['CLIENT_SECRET']
        self.redirect_uri = secret_values['DEEZER']['REDIRECT_URI']
        self.client = deezer.Client(app_id=self.client_id, app_secret=self.client_secret)
        self.state = None
        self.code = None
        self.access_token = None

    def complete_deezer_oauth2_authorization(self):
        # Create an OAuth2Session instance with a BackendApplicationClient
        client = BackendApplicationClient(client_id=self.client_id)
        oauth = OAuth2Session(client=client)

        # Generate a Deezer authorization URL and open it in the user's browser
        authorization_url, self.state = oauth.authorization_url("https://connect.deezer.com/oauth/auth.php", redirect_uri=self.redirect_uri)
        print(f"Please visit this URL to authorize your Deezer account: {authorization_url}")
        authorization_code = input("Enter the authorization code: ")

        # Exchange the authorization code for an access token
        token_url = "https://connect.deezer.com/oauth/access_token"
        data = {"grant_type": "authorization_code", "code": authorization_code, "redirect_uri": self.redirect_uri}
        headers = {"Authorization": f"Basic {self.client_id}:{self.client_secret}"}
        response = oauth.post(token_url, data=data, headers=headers)

        # If the request is successful, return the access_token
        if response.status_code == 200:
            print(response.json()['access_token'])
            self.access_token = response.json()['access_token']
            
        else:
            raise Exception("Unable to obtain access token.")
    

    def get_saved_songs(self):
        

        return self.client.get_user_tracks()
        # else:
            # self.logger.error('Failed to retrieve saved songs from Deezer API')
            # raise Exception('Failed to retrieve saved songs from Deezer API')
        
    def add_fav_songs(self, tracklist):
        pass
        # TODO
        # function which will take tracklist, find if it is available and return list of IDs in Deezer
        # also give list of songs that couldnt be find

        self.get_songs_ids(tracklist)

        # TODO
        # post to tracklist to reezer something

    def get_songs_ids(self):
        pass
