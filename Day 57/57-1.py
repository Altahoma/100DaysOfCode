from flask import Flask, render_template
import datetime
import requests


app = Flask(__name__)
url = 'https://api.npoint.io/c790b4d5cab58020d391'
all_posts = requests.get(url).json()


@app.route('/')
def blogs():
    return render_template('index.html', posts=all_posts)


@app.route('/post/<int:num>')
def post(num):
    post_title = str
    post_body = str
    for post in all_posts:
        if post['id'] == num:
            post_title = post['title']
            post_body = post['body']
    return render_template('post.html', title=post_title, body=post_body)


@app.route("/<user_name>")
def guess(user_name):
    age_api = f'https://api.agify.io/?name={user_name}'
    gender_api = f'https://api.genderize.io/?name={user_name}'
    guessed_gender = requests.get(gender_api).json()['gender']
    guessed_age = requests.get(age_api).json()['age']
    current_year = datetime.datetime.now().year
    return render_template('guess.html', name=user_name, gender=guessed_gender, age=guessed_age, year=current_year)


if __name__ == '__main__':
    app.run(debug=True)
