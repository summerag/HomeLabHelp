from flask import render_template, redirect, url_for, request, flash
from app import app, DatabaseHelper
from app.forms import LoginForm



#Routes
#=====================================================================
database = DatabaseHelper()


@app.route('/Home')
@app.route('/')
def index():
    posts = database.get_all_posts()
    return render_template('index.html', title='Home', posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        
        return redirect(url_for('index'))
        
    return render_template('login.html', title='Sign In', form=form)


@app.route('/<int:post_id>')
def post(post_id):
    post = database.get_post(post_id)
    return render_template('post.html', post=post)

