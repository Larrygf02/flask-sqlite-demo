from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return f"Hello world heroku enable"

if __name__ == "__main__":
    app.run()