import requests
from time import time
from base64 import b64encode
from Configurator import Configurator
import re


class SpotifyApi:
    def __init__(self):
        self.configurator = Configurator()
        self.valid_token = False

    def read_data(self):
        self.configurator.read_config()
        self.redirect_uri = self.configurator.config["general"]["redirect_uri"]
        self.client_id = self.configurator.config["general"]["client_id"]
        self.client_secret = self.configurator.config["general"]["client_secret"]
        self.auth_code = self.configurator.config["protected"]["auth_code"]
        self.token = self.configurator.config["protected"]["token"]
        try:
            self.token_expiration = int(self.configurator.config["protected"]["token_expiration"])
        except ValueError:
            self.token_expiration = 0
        self.refresh_token = self.configurator.config["protected"]["refresh_token"]
        self.user_id = self.configurator.config["user_info"]["user_id"]
        self.country = self.configurator.config["user_info"]["country"]

    def save_protected(self):
        self.configurator.config["protected"]["auth_code"] = self.auth_code
        self.configurator.config["protected"]["token"] = self.token
        self.configurator.config["protected"]["token_expiration"] = str(self.token_expiration)
        self.configurator.config["protected"]["refresh_token"] = self.refresh_token
        self.configurator.config["user_info"]["user_id"] = self.user_id
        self.configurator.write_config()

    def prepare_token(self):
        self.read_data()
        if self.token_expiration < time():
            self.get_token()
        else:
            self.valid_token = True
        return self.valid_token

    def get_token(self):
        if len(self.refresh_token) + len(self.auth_code) == 0:
            print("No saved refresh token or authorization code")
            self.valid_token = False
            return
        url = 'https://accounts.spotify.com/api/token'
        if len(self.refresh_token) > 0:
            params = {
                "grant_type": "refresh_token",
                "refresh_token": self.refresh_token,
            }
        else:
            params = {
                "grant_type": "authorization_code",
                "code": self.auth_code,
                "redirect_uri": self.redirect_uri
            }
        auth = str(b64encode(bytes(self.client_id + ":" + self.client_secret, encoding="utf-8")))[2:][:-1]
        headers = {
            "Authorization": "Basic " + auth,
            "Content-Type": "application/x-www-form-urlencoded"
        }
        response = requests.post(url, data=params, headers=headers)
        response_j = response.json()
        if "error" in response_j:
            print("[SpotifyApi get_token] Error: " + response.text)
        self.token = response_j["access_token"]
        self.token_expiration = int(time() + int(response_j["expires_in"]))
        print(response_j)
        if "refresh_token" in response_j:
            print(response_j["refresh_token"])
            self.refresh_token = response_j["refresh_token"]
        self.auth_code = ""
        self.save_protected()
        self.valid_token = True

    def get_user_info(self):
        if len(self.user_id) > 0:
            return 0

        if not self.prepare_token():
            return None

        url = "https://api.spotify.com/v1/me"
        headers = {
            "Authorization": "Bearer " + self.token
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            response_j = response.json()
            self.user_id = response_j["id"]
            self.configurator.config["user_info"]["user_id"] = self.user_id
            self.configurator.config["user_info"]["country"] = self.country
            self.configurator.write_config()
            return 0
        else:
            print("[SpotifyApi get_user_info] Error: " + response.text)
            return None

    def get_playlists_list(self):
        if not self.prepare_token():
            return None

        if self.get_user_info() is None:
            print("[SpotifyApi get_playlists_list] Error getting user info")

        playlists = []
        url = f"https://api.spotify.com/v1/users/{self.user_id}/playlists"
        params = {"limit": 50}
        headers = {"Authorization": "Bearer " + self.token}
        response = requests.get(url, params=params, headers=headers)
        if response.status_code == 200:
            response_j = response.json()
            playlists += response_j["items"]
            if response_j["total"] > 50:
                for offset in range(50, response_j["total"]//50*50+1, 50):
                    params["offset"] = offset
                    response_f = requests.get(url, params=params, headers=headers)
                    if response.status_code == 200:
                        response_f_j = response_f.json()
                        playlists += response_f_j["items"]
                    else:
                        print("[SpotifyApi get_playlists_list] Error: " + response.text)
            return playlists
        else:
            print("[SpotifyApi get_playlists_list] Error: " + response.text)
            return None

    def get_recommendations(self, seeds, limit=20, acousticness=None, danceability=None, duration_ms=None, energy=None,
                            instrumentalness=None, key=None, liveness=None, loudness=None, mode=None, popularity=None,
                            speechiness=None, tempo=None, time_signature=None, valence=None):
        if not self.prepare_token():
            return None

        if self.get_user_info() is None:
            print("[SpotifyApi get_recommendations] Error getting user info")
            return None

        if len(seeds) > 5:
            print("[SpotifyApi get_recommendations] Seeds limit (5) exceeded")
            return None

        seed_artists = list()
        seed_tracks = list()
        seed_genres = list()

        for seed in seeds:
            sp_link = re.search(r"http[s]*://open.spotify.com/(track|artist|genre)/[\dA-Za-z]+", seed)
            if sp_link is None:
                print(f"[SpotifyApi get_recommendations] Spotify link not found at {seed}")
            else:
                if "artist" in sp_link[0]:
                    seed_artists += [sp_link[0].split("/")[-1]]
                elif "track" in sp_link[0]:
                    seed_tracks += [sp_link[0].split("/")[-1]]
                else:
                    seed_genres += [sp_link[0].split("/")[-1]]

        url = "https://api.spotify.com/v1/recommendations"
        params = {
            "seed_artists": ",".join(seed_artists),
            "seed_tracks": ",".join(seed_tracks),
            "seed_genres": ",".join(seed_genres),
            "limit": limit,
            "market": self.country
        }

        if acousticness is not None:
            if acousticness[0] is not None:
                params["min_acousticness"] = acousticness[0]
            if acousticness[1] is not None:
                params["target_acousticness"] = acousticness[1]
            if acousticness[2] is not None:
                params["max_acousticness"] = acousticness[2]
        if danceability is not None:
            if danceability[0] is not None:
                params["min_danceability"] = danceability[0]
            if danceability[1] is not None:
                params["target_danceability"] = danceability[1]
            if danceability[2] is not None:
                params["max_danceability"] = danceability[2]
        if duration_ms is not None:
            if duration_ms[0] is not None:
                params["min_duration_ms"] = duration_ms[0]
            if duration_ms[1] is not None:
                params["target_duration_ms"] = duration_ms[1]
            if duration_ms[2] is not None:
                params["max_duration_ms"] = duration_ms[2]
        if energy is not None:
            if energy[0] is not None:
                params["min_energy"] = energy[0]
            if energy[1] is not None:
                params["target_energy"] = energy[1]
            if energy[2] is not None:
                params["max_energy"] = energy[2]
        if instrumentalness is not None:
            if instrumentalness[0] is not None:
                params["min_instrumentalness"] = instrumentalness[0]
            if instrumentalness[1] is not None:
                params["target_instrumentalness"] = instrumentalness[1]
            if instrumentalness[2] is not None:
                params["max_instrumentalness"] = instrumentalness[2]
        if key is not None:
            if key[0] is not None:
                params["min_key"] = key[0]
            if key[1] is not None:
                params["target_key"] = key[1]
            if key[2] is not None:
                params["max_key"] = key[2]
        if liveness is not None:
            if liveness[0] is not None:
                params["min_liveness"] = liveness[0]
            if liveness[1] is not None:
                params["target_liveness"] = liveness[1]
            if liveness[2] is not None:
                params["max_liveness"] = liveness[2]
        if loudness is not None:
            if loudness[0] is not None:
                params["min_loudness"] = loudness[0]
            if loudness[1] is not None:
                params["target_loudness"] = loudness[1]
            if loudness[2] is not None:
                params["max_loudness"] = loudness[2]
        if mode is not None:
            if mode[0] is not None:
                params["min_mode"] = mode[0]
            if mode[1] is not None:
                params["target_mode"] = mode[1]
            if mode[2] is not None:
                params["max_mode"] = mode[2]
        if popularity is not None:
            if popularity[0] is not None:
                params["min_popularity"] = popularity[0]
            if popularity[1] is not None:
                params["target_popularity"] = popularity[1]
            if popularity[2] is not None:
                params["max_popularity"] = popularity[2]
        if speechiness is not None:
            if speechiness[0] is not None:
                params["min_speechiness"] = speechiness[0]
            if speechiness[1] is not None:
                params["target_speechiness"] = speechiness[1]
            if speechiness[2] is not None:
                params["max_speechiness"] = speechiness[2]
        if tempo is not None:
            if tempo[0] is not None:
                params["min_tempo"] = tempo[0]
            if tempo[1] is not None:
                params["target_tempo"] = tempo[1]
            if tempo[2] is not None:
                params["max_tempo"] = tempo[2]
        if time_signature is not None:
            if time_signature[0] is not None:
                params["min_time_signature"] = time_signature[0]
            if time_signature[1] is not None:
                params["target_time_signature"] = time_signature[1]
            if time_signature[2] is not None:
                params["max_time_signature"] = time_signature[2]
        if valence is not None:
            if valence[0] is not None:
                params["min_valence"] = valence[0]
            if valence[1] is not None:
                params["target_valence"] = valence[1]
            if valence[2] is not None:
                params["max_valence"] = valence[2]

        headers = {"Authorization": "Bearer " + self.token}
        response = requests.get(url, params=params, headers=headers)
        print(response.request.url)
        if response.status_code == 200:
            return response.json()
        print("[SpotifyApi get_recommendations] Error:", response.json())
        return None

    def get_playlist_items(self, playlist_id: str, offset=0):
        if not self.prepare_token():
            return None

        url = f"https://api.spotify.com/v1/playlists/{playlist_id}"
        headers = {"Authorization": "Bearer " + self.token}
        params = {"offset": offset}
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            print("[SpotifyApi get_playlist_items] Error:", response.json())
            return None

    def flush_playlist(self, playlist_id: str):
        if not self.prepare_token():
            return None
        playlist_items = self.get_playlist_items(playlist_id)
        if playlist_items is None:
            print("[SpotifyApi flush_playlist] Error getting playlist items")
            return None
        else:
            url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
            headers = {"Authorization": "Bearer " + self.token}
            data = {"tracks": []}
            errors = []
            if playlist_items["tracks"]["limit"] == 100:
                for track in playlist_items["tracks"]["items"]:
                    data["tracks"] += [{"uri": track["track"]["uri"]}]
            response = requests.delete(url, headers=headers, json=data)
            if response.status_code != 200:
                errors += [response.text]
            response = requests.delete(url, headers=headers, json=data)
            if playlist_items["tracks"]["total"] > len(playlist_items["tracks"]["items"]):
                recursive = self.flush_playlist(playlist_id)
                if recursive != 0:
                    return recursive
            if response.status_code != 200:
                print("[SpotifyApi flush_playlist] Error flushing:", response.text)
                return None
            return 0

    def append_tracks_to_playlist(self, playlist_id: str, track_uris: list, add_duplicates=False):
        if not self.prepare_token():
            return None

        if not add_duplicates:
            offset = 0
            content = self.get_playlist_items(playlist_id)
            while offset+content["tracks"]["total"] > content["tracks"]["limit"]:
                offset += content["tracks"]["total"]
                content["tracks"] += self.get_playlist_items(playlist_id, offset)
            for content_item in content["tracks"]["items"]:
                if content_item["track"]["uri"] in track_uris:
                    track_uris.remove(content_item["track"]["uri"])
        url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
        headers = {"Authorization": "Bearer " + self.token}
        data = {"uris": track_uris}
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200 or response.status_code == 201:
            return response.json()
        else:
            print("[SpotifyApi append_tracks_to_playlist] Error: " + response.text)
            return None

    def overwrite_tracks_in_playlist(self, playlist_id: str, track_uris: list):
        if not self.prepare_token():
            return None
        self.flush_playlist(playlist_id)
        return self.append_tracks_to_playlist(playlist_id, track_uris)


if __name__ == "__main__":
    config = Configurator()
    api = SpotifyApi()
    print(api.get_playlist_items("6hiGB76fT5SQlztmAeV5pY"))
