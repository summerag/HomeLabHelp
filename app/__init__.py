from flask import Flask
from config import Config
import sqlite3
from werkzeug.exceptions import abort


app = Flask(__name__)
app.config.from_object(Config)



    


class DatabaseHelper():
    def __init__(self):
        pass
        
        
    def get_db_connection(self):
        self.conn = sqlite3.connect('database.db')
        self.conn.row_factory = sqlite3.Row

    def get_post(self, post_id):
        self.get_db_connection()
        post = self.conn.execute('SELECT * FROM posts WHERE id = ?',
                            (post_id,)).fetchone()
        self.conn.close()
        if post is None:
            abort(404)
        return post
    def get_all_posts(self):
        self.get_db_connection()
        posts = self.conn.execute('SELECT * FROM posts').fetchall()
        self.conn.close()
        return posts

from app import routes



