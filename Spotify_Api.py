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
        """
        If the token is expired, get a new one
        :return: valid token
        """
        self.read_data()
        if self.token_expiration < time() or self.auth_code:
            self.get_token()
        else:
            self.valid_token = True
        return self.valid_token

    def get_token(self):
        """
        Grant new or renew old token
        :return: token
        """
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
        """
        Get user profile information
        """
        if not self.prepare_token():
            return None

        if len(self.user_id) > 0:
            return 0

        url = "https://api.spotify.com/v1/me"
        headers = {
            "Authorization": "Bearer " + self.token
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            print(response.text)
            response_j = response.json()
            self.user_id = response_j["id"]
            self.country = response_j["country"]
            self.configurator.config["user_info"]["user_id"] = self.user_id
            self.configurator.config["user_info"]["country"] = self.country
            self.configurator.write_config()
            return 0
        else:
            print("[SpotifyApi get_user_info] Error: " + response.text)
            return None

    def get_playlists_list(self):
        """
        Get list of user's playlists
        :return:
        """
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
        """
        Generate recommendations by seeds according to specified parameters
        """
        if not self.prepare_token():
            return

        if self.get_user_info() is None:
            print("[SpotifyApi get_recommendations] Error getting user info")
            return

        if len(seeds) > 5:
            print("[SpotifyApi get_recommendations] Error: Seeds limit (5) exceeded")
            return

        seed_artists = list()
        seed_tracks = list()
        seed_genres = list()

        for seed in seeds:
            sp_link = self.link_patterns_extract(seed)
            if not sp_link:
                print(f"[SpotifyApi get_recommendations] Spotify link not found at {seed}")
                continue
            if sp_link[1] == "artist":
                seed_artists += [sp_link[2]]
            elif sp_link[1] == "track":
                seed_tracks += [sp_link[2]]
            else:
                seed_genres += [sp_link[2]]

        if len(seed_artists)+len(seed_genres)+len(seed_tracks) == 0:
            print("[SpotifyApi get_recommendations] Error: seeds pool is empty")
            return

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
        """
        Returns list of track uris that are in the playlist
        :param playlist_id: id of a playlist
        :param offset: offset of returning tracks
        :return: list of track uris
        """
        if not self.prepare_token():
            return None

        tracks = list()

        limit = 100
        url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
        headers = {"Authorization": "Bearer " + self.token}
        params = {"offset": offset, "limit": limit, "fields": "total,items(track(uri))"}
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            content = response.json()
            for track in content["items"]:
                tracks += [track["track"]["uri"]]
            if limit+offset < content["total"]:
                tracks += self.get_playlist_items(playlist_id, offset+limit)
            return tracks
        else:
            print("[SpotifyApi get_playlist_items] Error:", response.json())
            return None

    def flush_playlist(self, playlist_id: str):
        """
        Deletes all items in specified playlist
        :param playlist_id: id of playlist
        """
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
            for i in range(len(playlist_items)):
                if i % 100 == 0 and i != 0:
                    response = requests.delete(url, headers=headers, json=data)
                    if response.status_code != 200:
                        errors += [response.text]
                    data["tracks"] = []
                data["tracks"] += [{"uri": playlist_items[i]}]
            response = requests.delete(url, headers=headers, json=data)
            if response.status_code != 200:
                errors += [response.text]
            if len(errors) != 0:
                print("[SpotifyApi flush_playlist] Error flushing:", "\n", errors)
                return None
            return 0

    def add_tracks_to_playlist(self, playlist_id: str, track_uris: list, add_duplicates=False):
        """
        Add tracks to a playlist
        :param playlist_id: id of target playlist
        :param track_uris: list of track uris to add
        :param add_duplicates: if duplicated tracks should be added
        """
        if not self.prepare_token():
            return None

        if not add_duplicates:
            current_tracks = self.get_playlist_items(playlist_id)
            new_tracks_filtered = []
            for new_track in track_uris:
                if new_track not in current_tracks:
                    new_tracks_filtered += [new_track]
        else:
            new_tracks_filtered = track_uris
        if len(new_tracks_filtered) == 0:
            print("[SpotifyApi add_tracks_to_playlist] Info: list of tracks was empty",
                  "(duplicates filtering was", ["ON)", "OFF)"][int(add_duplicates)])
            return 0
        url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
        headers = {"Authorization": "Bearer " + self.token}
        data = {"uris": new_tracks_filtered}
        response = requests.post(url, headers=headers, json=data)
        print(len(new_tracks_filtered))
        if response.status_code == 200 or response.status_code == 201:
            return response.json()
        else:
            print("[SpotifyApi add_tracks_to_playlist] Error: " + response.text)
            return None

    def overwrite_tracks_in_playlist(self, playlist_id: str, track_uris: list):
        """
        Flush playlist then add tracks to it
        :param playlist_id: target playlist
        :param track_uris: list of track uris to add
        """
        if not self.prepare_token():
            return None
        self.flush_playlist(playlist_id)
        return self.add_tracks_to_playlist(playlist_id, track_uris)

    def get_track_audio_features(self, track_id):
        """
        Get track's audio features
        """
        if not self.prepare_token():
            return None
        url = f"https://api.spotify.com/v1/audio-features/{track_id}"
        headers = {"Authorization": "Bearer " + self.token}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            content = response.json()
            track_info = self.get_track_info(track_id)
            content["name"] = track_info["name"]
            content["genres"] = track_info["genres"]
            content["popularity"] = track_info["popularity"]
            return content
        else:
            print("[SpotifyApi get_track_audio_features] Error:", response.text)

    def get_track_info(self, track_id):
        if not self.prepare_token():
            return None
        url = f"https://api.spotify.com/v1/tracks/{track_id}"
        headers = {"Authorization": "Bearer " + self.token}
        response = requests.get(url, headers=headers)
        genres = []
        if response.status_code == 200:
            content = response.json()
            for artist in content["artists"]:
                if "genres" in artist:
                    genres += artist["genres"]
            if "popularity" in content:
                popularity = content["popularity"]
            else:
                popularity = None

            return {"genres": list(set(genres)), "popularity": popularity, "name": content["name"]}
        else:
            print("[SpotifyApi get_possible_genres] Error:", response.text)
            return

    def get_users_top_items(self, type: int, limit=20, offset=0, time_range=1):
        """
        Get the current user's top artists or tracks based on calculated affinity.
        https://developer.spotify.com/documentation/web-api/reference/#/operations/get-users-top-artists-and-tracks
        :param type: the type of entity to return, 0 stands for artists, 1 stands for tracks
        :param limit: the maximum number of items to return
        :param offset: the index of the first item to return
        :param time_range: over what time frame the affinities are computed,
        0 stands for short_term (approximately last 4 weeks),
        1 stands for medium_term (approximately last 6 months),
        2 stands for long_term (calculated from several years)
        :return:
        """
        if not self.prepare_token():
            return None
        if type in (0, 1):
            type = ["artists", "tracks"][type]
        else:
            print("[SpotifyApi get_users_top_items] Items type not in range (0, 1)")
            return
        if time_range in (0, 1, 2):
            time_range = ["short_term", "medium_term", "long_term"][time_range]
        else:
            print("[SpotifyApi get_users_top_items] Items time_range not in range (0, 1, 2)")
            return
        url = f"https://api.spotify.com/v1/me/top/{type}"
        headers = {"Authorization": "Bearer " + self.token}
        response = requests.get(url, headers=headers,
                                params={"limit": limit, "offset": offset, "time_range": time_range})
        if response.status_code == 200:
            return response.text
            return response.json()
        else:
            print("[SpotifyApi get_users_top_items] Error:", response.status_code, response.text)
            return

    def link_patterns_extract(self, link):
        link_http = re.search(r"http[s]*://open.spotify.com/(track|artist|genre)/([\dA-Za-z]+)", link)
        link_uri = re.search(r"spotify:(track|artist|genre):([\dA-Za-z]+)", link)
        if link_uri:
            sp_link = link_uri
        else:
            sp_link = link_http
        return sp_link


if __name__ == "__main__":
    api = SpotifyApi()
