from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Ye dummy data hai, baad mein aap Spotify API se connect kar sakte hain
    songs = [
        {"title": "Kesariya", "artist": "Arijit Singh"},
        {"title": "Pasoori", "artist": "Ali Sethi"},
        {"title": "Excuses", "artist": "AP Dhillon"}
    ]
    return render_template('index.html', songs=songs)

if __name__ == '__main__':
    app.run(debug=True)
