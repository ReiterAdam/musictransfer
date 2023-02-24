import requests
import json
import properties
import base64
import logging

# similar for tiral, deezer etc

""" class which gets user id and other needed stuff for request and then can access to playlists like

get_saved_songs(): -> list of saved songs"""


class Spotify:
    def __init__(self):
        # pass
        if self.get_bearer_token_for_users():
            
            # go on
            self.get_user_data()

        else:
            logging.error("error during initialization")


    # not needed
    def get_bearer_token_for_users(self):


        config_values = properties.read_yaml(file_path=".\config\dev.yml")
        # read secret properties
        secret_values = properties.read_yaml(file_path=".\config\dev_secret.yml")

        l_client_id = secret_values['SPOTIFY']['CLIENT_ID']
        l_client_secret = secret_values['SPOTIFY']['CLIENT_SECRET']

        l_method = config_values['SPOTIFY']['API']['METHOD']
        l_url = config_values['SPOTIFY']['API']['URL']
        l_payload = 'grant_type=' + config_values['SPOTIFY']['API']['GRANT_TYPE']
        l_content_type = config_values['SPOTIFY']['API']['CONTENT_TYPE']

        #TODO find lib for this
        l_base64_decode = l_client_id + ':' + l_client_secret
        l_base64_decode_bytes = l_base64_decode.encode("ascii")
        l_base64_encode_bytes = base64.b64encode(l_base64_decode_bytes)
        l_base64_encode = l_base64_encode_bytes.decode("ascii")

        l_headers = {
            'Authorization': 'Basic ' + l_base64_encode,
            'Content-Type': l_content_type
        }
        try:
            rest_response = requests.request(
                method=l_method,
                url=l_url,
                data=l_payload,
                headers=l_headers
                )
            
            reponse_json = json.loads(rest_response.content)
        
            bearer_token = reponse_json['access_token']

            self.bearer_token = bearer_token

            logging.info("Spotify bearer token successfully fetched")
            return True

        except:
            logging.error("Error occured during Spotify bearer token fetching")
            return False

    # the important one
    def get_private_token(self):

        #TODO
        # 4 REST calls: 
        #   - GET     https://accounts.spotify.com/authorize
        #   - GET     https://accounts.spotify.com/pl/login
        #   - GET     https://accounts.spotify.com/authorize
        #   - POST    https://accounts.spotify.com/api/token
        # here window pops up for login
        # during research

        return True

    def get_user_data(self):

        l_url = 'https://api.spotify.com/v1/users/czeskyy'
        l_payload={}
        l_headers = {
            'Authorization': 'Bearer ' + self.bearer_token
        }
        l_method = 'GET'

        response = requests.request(method=l_method, 
                                    url=l_url, 
                                    headers=l_headers, 
                                    data=l_payload
                                    )

        print(response.text)


    def get_saved_songs(self):
        
        #TODO method for the 'private' one token
        l_private_token = self.get_private_token()

        url = "https://api.spotify.com/v1/me/tracks"
        payload = ""
        headers = {
        'Authorization': 'Bearer ' + l_private_token
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        resp = json.loads(response.content)

        for x in list(resp['items']):
            out = ''
            for a in x['track']['artists']:
                out = out + a['name'] + ' '
            out = out + x['track']['name']
            print(out)


        return "here goes the list..."
