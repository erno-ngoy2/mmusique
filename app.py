import os
from pathlib import Path
from flask import Flask, jsonify, send_file

app = Flask(__name__)

# Fichiers et chemins
BASE_DIR = Path(__file__).resolve().parent
APK_PATH = BASE_DIR / "app-release.apk"


# Simulation de la version actuelle
def version_actuelle():
    return "1.0.0"


# HTML avec design bleu ciel sans compteur
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MMUSIQUE - Téléchargement APK</title>
    <style>
        body {
            background-color: #000000;
            color: #00bfff;
            font-family: monospace;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            margin: 0;
        }
        .container {
            border: 2px dashed #00bfff;
            padding: 40px;
            text-align: center;
            background: #050505;
            box-shadow: 0 0 15px rgba(0, 191, 255, 0.2);
        }
        h1 { 
            font-size: 1.8rem; 
            margin-bottom: 20px; 
            text-transform: uppercase; 
            letter-spacing: 2px;
        }
        p {
            color: #87cefa;
            margin-bottom: 30px;
        }
        .btn {
            display: inline-block;
            background: #00bfff;
            color: #000000;
            padding: 15px 30px;
            text-decoration: none;
            font-weight: bold;
            font-size: 1.2rem;
            border: none;
            cursor: pointer;
            text-transform: uppercase;
            transition: all 0.2s ease;
        }
        .btn:hover {
            background: #ffffff;
            color: #000000;
            box-shadow: 0 0 10px #ffffff;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Munkoyo Musique</h1>
        <p>Téléchargez l'application officielle directement pour Android.</p>
        <a href="/api/download" class="btn">Télécharger l'APK</a>
    </div>
</body>
</html>
"""


@app.route("/")
def home():
    return HTML_TEMPLATE


@app.route("/api/download")
def download_apk():
    if not APK_PATH.exists():
        return jsonify({"error": "APK introuvable sur le serveur."}), 404

    version = version_actuelle()
    nom = f"munkoyo_musique_v{version}.apk" if version else "munkoyo_musique.apk"

    return send_file(
        str(APK_PATH),
        mimetype="application/vnd.android.package-archive",
        as_attachment=True,
        download_name=nom
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))