from flask import app, render_template, Flask, jsonify, request
import yt_dlp

app = Flask(__name__)


def get_playable_url(url):
    ydl_opts = {
        # Path to the cookies.txt file we just created
        'cookiefile': '/home/admin/yt_player/ytplayer/cookies.txt',
        # 'bestaudio' is often more reliable for audio-only players
        'format': 'best',
        'skip_download': True,
        # Quiet mode prevents excessive logging to the terminal
        'quiet': True,
        'no_warnings': True,
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            # 'url' contains the direct playable link
            return info.get('url')
    except Exception as e:
        print(f"Error during extraction: {e}")
        return None




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