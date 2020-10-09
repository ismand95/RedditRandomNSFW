from cumrade import cumrade, db
from cumrade.forms import GenerateRandom
from cumrade.models import SubReddit

from sqlalchemy import func
from flask import render_template, flash
import numpy as np


@cumrade.route('/', methods=['GET', 'POST'])
def cumrade_welcome():
    form = GenerateRandom()

    sub = 'text'

    if form.validate_on_submit():
        index_length = SubReddit.query.count() - 1
        rand_index = np.random.randint(0, index_length)

        subreddit = SubReddit.query.filter_by(id=rand_index).first()
        flash('New NSFW subreddit link drawn ;)')

        sub = subreddit.subreddit

    return render_template('index.html', form=form, sub=sub)
