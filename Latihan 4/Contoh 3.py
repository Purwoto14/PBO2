class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist


class Playlist:
    def __init__(self):
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)
        print("Title", song.title)


class MediaPlayer:
    def __init__(self, playlist):
        self.playlist = playlist
        print("play music")


song1 = Song("Kenagan Terindah", " Hal")
song2 = Song("payung tuduh", "icon")
playlist = Playlist()
playlist.add_song(song1)
playlist.add_song(song2)
media_player = MediaPlayer(playlist)
media_player.playlist.songs  # output: [song1, song2]
