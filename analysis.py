from Spotify_Api import SpotifyApi
import csv


def analyse_playlist(playlist_id, output_file):
    """
    Fetches track features for every track in playlist. Saves csv file with tracks features in output_file
    :param playlist_id: playlist id with tracks to analyse
    :param output_file: output file
    """
    api = SpotifyApi()
    with open(output_file, "w", encoding="utf-8", newline='') as file:
        tracks = api.get_playlist_items(playlist_id)
        initialised = False
        writer = None
        for track in tracks:
            analysis = api.get_track_audio_features(track.split(":")[-1])
            if not initialised:
                fieldnames = analysis.keys()
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                initialised = True
            writer.writerow(analysis)
