from cumrade import db


class SubReddit(db.Model):
    __tablename__ = 'subreddit'

    id = db.Column(db.Integer, primary_key=True)
    subreddit = db.Column(db.String(128))
