from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1> Flask DevOps Pipeline</h1><p>Deployed with Docker + GitHub Actions + AWS</p>"

@app.route("/health")
def health():
    return {"status": "ok"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)