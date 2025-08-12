from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>🚀 Hello from Azure!</h1><p>This Flask app is running on Azure App Service.</p>"

if __name__ == "__main__":
    app.run(debug=True)