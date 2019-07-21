from flask import *
from flask_paginate import Pagination
import pandas as pd


def read_csv_to_mysql(filename):
    value = pd.read_csv(filename)
    return value


app = Flask(__name__)
df = read_csv_to_mysql('data/countriesData.csv')
df.drop(range(df.shape[0] - 5, df.shape[0]), inplace=True)
df.drop(columns=['CountryCode','SeriesCode'], inplace=True)


def get_users(offset=0, per_page=5):
    return df[offset: offset + per_page]


@app.route('/', methods=['GET', 'POST'])
@app.route('/<int:page>/<int:perpage>', methods=['GET', 'POST'])
@app.route('/<int:page>', methods=['GET', 'POST'])
def index(page=1, per_page=5):
    global df
    total = df.shape[0]
    offset = (page - 1) * per_page
    pagination_users = get_users(offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='bootstrap4')
    return render_template('index2.html',
                           users=pagination_users,
                           page=page,
                           per_page=per_page,
                           pagination=pagination,
                           )


@app.route('/update', methods=['POST'])
def update():
    global df
    content = request.get_json()
    print(content)
    df = df.append(content, ignore_index=True)
    return ' insert succeed '


if __name__ == '__main__':
    app.run(debug=True)
