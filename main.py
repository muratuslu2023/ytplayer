from flask import app, render_template, Flask, jsonify, request
import yt_dlp

app = Flask(__name__)


def get_playable_url(url):
    ydl_opts = {
        'format': 'best',       # Selects the best quality combined audio+video
        'skip_download': True,  # Prevents actual download
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        # 'url' contains the direct playable link
        return info.get('url')

@app.route("/")
def index_page():
    return render_template("index.html")




@app.route("/process-music", methods=["POST"])
def process_music():
    data = request.get_json()
    url = data.get('music_url')
    # Use your get_playable_url function here
    playable_url = get_playable_url(url)
    return jsonify({"playable_url": playable_url})