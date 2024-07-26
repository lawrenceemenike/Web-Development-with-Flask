from flask import Flask, render_template, abort
import requests
from post import Post

app = Flask(__name__)

def get_blog_posts():
    url = "https://api.npoint.io/0c123a506f5632ad4530"
    response = requests.get(url)
    if response.status_code == 200:
        return [Post(post['id'], post['title'], post['subtitle'], post['body']) for post in response.json()]
    else:
        return []

@app.route('/')
def home():
    posts = get_blog_posts()
    return render_template("index.html", posts=posts)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    posts = get_blog_posts()
    requested_post = next((post for post in posts if post.id == post_id), None)
    if requested_post:
        return render_template("post.html", post=requested_post)
    else:
        abort(404)

if __name__ == "__main__":
    app.run(debug=True)