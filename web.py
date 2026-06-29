import os
from flask import Flask

web_app = Flask(__name__)

@web_app.route("/")
def home():
    return "Bot is running"

def run():
    web_app.run(host="0.0.0.0", port=int(os.getenv("PORT", "8080")))

if __name__ == "__main__":
    run()
