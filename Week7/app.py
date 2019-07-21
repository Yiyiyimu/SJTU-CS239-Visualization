from flask import *
from flask_paginate import Pagination
import pandas as pd
import numpy as np
import json


def read_csv_to_mysql(filename):
    value = pd.read_csv(filename)
    return value


app = Flask(__name__)
df = read_csv_to_mysql('data/countriesData.csv')
df.replace('..',0,inplace=True)
df.replace('.. ',0,inplace=True)
df.replace('...',0,inplace=True)
df.drop(range(df.shape[0] - 5, df.shape[0]), inplace=True)
df.rename(columns={"2010[YR2010]":"YR2010","2011[YR2011]":"YR2011","2012[YR2012]":"YR2012","2013[YR2013]":"YR2013","2014[YR2014]":"YR2014"}, inplace=True)

df1 = df.drop(columns=['CountryCode','SeriesCode'])
df2 = df.drop(columns=['CountryName','SeriesCode'])
df_map = df2.sort_values(by=['SeriesName'])[8*215:9*215][['CountryCode',"YR2010"]]

df_d3 = df1.drop(columns=['CountryName'])

cName = df1.CountryName.drop_duplicates()
cName = pd.DataFrame(np.array(cName))

cLabel = df1.SeriesName[:17]
cYear = np.array(df1.columns[2:7])

def get_users(offset=0, per_page=17):
    return df1[offset: offset + per_page]

def get_users_d3(offset=0, per_page=17):
    return df_d3[offset: offset + per_page]


@app.route('/', methods=['GET', 'POST'])
@app.route('/<int:page>/<int:perpage>', methods=['GET', 'POST'])
@app.route('/<int:page>', methods=['GET', 'POST'])
def index(page=1, per_page=17):
    if request.method == 'POST':
        a = request.get_data()
        print(a)
    total = df1.shape[0]
    offset = (page - 1) * per_page
    pagination_users = get_users(offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='bootstrap4')
    chart_data = get_users_d3(offset=offset, per_page=per_page).T.to_dict(orient='records')
    chart_data = json.dumps(chart_data, indent=2)
    d3_data = {'chart_data': chart_data}
    map_data = df_map.to_dict(orient='records')
    map_data = json.dumps(map_data, indent=2)
    d3_map_data = {'map_data': map_data}
    return render_template('index2.html',
                           users=pagination_users,
                           page=page,
                           per_page=per_page,
                           pagination=pagination,
                           countryName=cName,
                           label=cLabel,
                           year=cYear,
                           d3_data=d3_data,
                           d3_map=d3_map_data,
                           )



if __name__ == '__main__':
    app.run(debug=True)
