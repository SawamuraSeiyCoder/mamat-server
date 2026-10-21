import subprocess
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "🤖 M.A.M.A.T. Cloud Server Aktif!"

@app.route('/search')
def search_song():
    query = request.args.get('q')
    if not query:
        return jsonify({"error": "Query tidak boleh kosong"}), 400
    
    print(f"🔎 Mencari lagu: {query}")
    # Perintah untuk mencari 1 lagu teratas di YouTube dan mengambil link stream audionya
    cmd = f'yt-dlp "ytsearch1:{query}" --get-url --format bestaudio'
    
    try:
        url_stream = subprocess.check_output(cmd, shell=True).decode('utf-8').strip()
        if url_stream:
            return jsonify({"url": url_stream})
        else:
            return jsonify({"error": "Lagu tidak ditemukan"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)