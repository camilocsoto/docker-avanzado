# This is an API 
import json
from flask import Flask
app = Flask(__name__)

@app.route('/getMyInfo')
def getMyInfo():
    value = {
        "name": "Juan Camilo",
        "lastname": "Suárez",
        "socialMedia":
        [
            {"reddirUser": "camilocsoto"},
            {"instagramUser": "na"},
            {"platziUser": "camilocsoto"},
            {"linkedin": "camilocsoto"},
            {"githubUser": "camilocsoto"}
        ],
        "blog": "https://camilocsoto.com",
        "author": "juan camilo suarez"
    }
    return json.dumps(value)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
