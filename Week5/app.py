from flask import Flask, request, render_template, session, redirect
import numpy as np
import pandas as pd
import os
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class data(db.Model):
    __tablename__ = 'database'
    CountryName = db.Column(db.String(120), primary_key=True)

    def __init__(self, CountryName):
        self.CountryName = CountryName

os.chdir('E:/OneDrive - sjtu.edu.cn/vscode_env/visualization/Week5')

df = pd.read_csv('countriesData.csv')

df = df.drop(columns=['CountryCode','SeriesCode'])

df.to_sql('db', db.engine)

dfs=df

for df in dfs.keys():
    cols = dfs[df].values
    cols = [str(col) for col in cols if 'id' in col.lower()]
    schema = pd.io.sql.get_schema(dfs[df],df, con=db.engine, keys=cols)
    db.engine.execute('DROP TABLE ' + df + ';')
    db.engine.execute(schema)
    dfs[df].to_sql(df,con=db.engine, index=False, if_exists='append')


@app.route('/', methods=("POST", "GET"))
def html_table():

    return render_template('upload.html',  tables=[df.to_html(classes='data')], titles=df.columns.values)


if __name__ == '__main__':
    app.run(debug=True)