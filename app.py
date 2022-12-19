from flask import Flask, request, render_template
from lyrics import get_lyrics, translate_lyrics

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/translate", methods=["GET"])
def translate():
    args = request.args
    artist = args.get("artist")
    song = args.get("song")

    lyrics = get_lyrics(artist, song)
    translated_lyrics = translate_lyrics(lyrics)

    return render_template(
        "translate.html", lyrics=lyrics, translated_lyrics=translated_lyrics
    )


if __name__ == "__main__":
    app.run()
