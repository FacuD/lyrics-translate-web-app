import lyricsgenius
import translators as ts
from cfg import GENIUS_TOKEN


def get_lyrics(artist, song):
    genius = lyricsgenius.Genius(GENIUS_TOKEN)
    genius.response_format = "html"
    # Eliminate the "Song Title + Lyrics" string from the lyrics
    ignore_str_index = len(song) + len("Lyrics") + 1
    song = genius.search_song(song, artist)
    return song.lyrics[ignore_str_index:]


def translate_lyrics(lyrics):
    return ts.translate_text(lyrics, translator="google", to_language="es")
