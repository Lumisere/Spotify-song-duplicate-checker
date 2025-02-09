import spotipy
from spotipy.oauth2 import SpotifyOAuth
from collections import defaultdict

clientid = 'ENTER CLIENTID'
secret = 'ENTER SECRET'
redirect = 'http://localhost:8888/callback'

try:
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=clientid,
                                                   client_secret=secret,
                                                   redirect_uri=redirect,
                                                   scope="playlist-modify-public playlist-modify-private"))
    print("Authentication successful!")
except Exception as e:
    print(f"Authentication failed: {e}")
    exit()

def getplaylist():
    try:
        playlists = sp.currentplaylist()['items']
        print(f"Found {len(playlists)} playlists.")
        return playlists
    except spotipy.exceptions.SpotifyException as e:
        print(f"Spotify API Error: {e}")
        print("make sure you set yourself in the dev dashboard")
        return []
    except Exception as e:
        print(f"Error fetching playlists: {e}")
        return []

def listplaylist(playlists):
    for i, playlist in enumerate(playlists):
        print(f"{i + 1}. {playlist['name']} (ID: {playlist['id']})")

def gettracks(playlist_id):
    try:
        results = sp.playlist_tracks(playlist_id)
        tracks = results['items']
        while results['next']:
            results = sp.next(results)
            tracks.extend(results['items'])
        print(f"Found {len(tracks)} tracks in the playlist.")
        return tracks
    except Exception as e:
        print(f"Error fetching tracks: {e}")
        return []

def finddupes(tracks):
    count = defaultdict(list)
    for i, item in enumerate(tracks):
        track = item['track']
        trackname = track['name']
        artistname = track['artists'][0]['name']
        count[(trackname, artistname)].append(i)
    return {k: v for k, v in count.items() if len(v) > 1}

def deletedupes(playlist_id, tracks, duplicates):
    for indices in duplicates.values():
        for index in reversed(indices[1:]):
            sp.removeallbutfirst(playlist_id, [tracks[index]['track']['id']])

def main():
    playlists = getplaylist()
    if not playlists:
        print("No playlists found. Please ensure you have playlists in your Spotify account.")
        return

    print("Your playlists:")
    listplaylist(playlists)

    try:
        choice = int(input("Enter the number of the playlist you want to check for duplicates: ")) - 1
        if choice < 0 or choice >= len(playlists):
            print("Invalid selection.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    selectedplaylist = playlists[choice]
    print(f"Selected playlist: {selectedplaylist['name']} (ID: {selectedplaylist['id']})")

    tracks = gettracks(selectedplaylist['id'])
    if not tracks:
        print("No tracks found in the playlist.")
        return

    duplicates = finddupes(tracks)
    if not duplicates:
        print("No duplicates found.")
        return

    print("Duplicates found:")
    for (trackname, artistname), indices in duplicates.items():
        print(f"{trackname} by {artistname} at positions {[i + 1 for i in indices]}")

    if input("Do you want to delete duplicates? (yes/no): ").lower() == 'yes':
        if input("Are you sure? This action cannot be undone. (yes/no): ").lower() == 'yes':
            deletedupes(selectedplaylist['id'], tracks, duplicates)
            print("Duplicates have been deleted.")
        else:
            print("Operation cancelled.")
    else:
        print("Operation cancelled.")

if __name__ == "__main__":
    main()
