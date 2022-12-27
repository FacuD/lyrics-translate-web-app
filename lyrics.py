import lyricsgenius
import translators as ts
from cfg import GENIUS_TOKEN


def clean_lyrics(song):
    # Genius adds a header to the lyrics that we don't want
    target = song.title + " Lyrics"
    start_ignore_index = song.lyrics.find(target) + len(target)
    return song.lyrics[start_ignore_index:]


def get_lyrics(artist, song):
    genius = lyricsgenius.Genius(GENIUS_TOKEN)
    genius.response_format = "html"
    song = genius.search_song(song, artist)
    return clean_lyrics(song)


def translate_lyrics(lyrics):
    return ts.translate_text(lyrics, translator="google", to_language="es")
