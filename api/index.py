from flask import Flask, render_template, request, redirect, url_for
import json

global friend_names

def get_friend_names(data):
    friend_names = [friend['name'] for friend in data['friends_v2']]
    return friend_names

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)

        if file:
            friend_names = get_friend_names(json.load(file))
            return render_template('fb.html',friend_names=friend_names)
    return render_template('index.html')

@app.route("/ig")
def ig():
  return render_template('ig.html')

if __name__ == '__main__':
    app.run(debug=True)