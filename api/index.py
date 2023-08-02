from flask import Flask, render_template, request, redirect, url_for, jsonify
import json

def get_friend_names(data):
    friend_names = [friend['name'] for friend in data['friends_v2']]
    return friend_names

import json

def find_unfollowers(following_data, followers_data):
    following_list = [entry["string_list_data"][0]["value"] for entry in following_data["relationships_following"]]
    following_set = set(following_list)
    
    followers_list = [entry["string_list_data"][0]["value"] for entry in followers_data]
    followers_set = set(followers_list)

    unfollowers = following_set - followers_set
    return list(unfollowers)


app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if len(request.files) == 0:
            return redirect(request.url)

        if 'fb-file' in request.files:
            friend_names = get_friend_names(json.load(request.files['fb-file']))
            return render_template('fb.html',friend_names=friend_names)
        elif 'following-file' in request.files and 'followers-file' in request.files:
            following_data = json.load(request.files['following-file'])
            followers_data = json.load(request.files['followers-file'])
            unfollowers = find_unfollowers(following_data, followers_data)
            return render_template('ig.html',unfollowers=unfollowers)
        else:
            return redirect(request.url)

            
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)