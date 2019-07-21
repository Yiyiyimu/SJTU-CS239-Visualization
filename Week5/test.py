from flask import Flask, request, render_template, session, redirect

import math
class Pagination(object):
    def __init__(self,row,per_row,iterable):
        self.row = row
        self.per_row = per_row
        self.iterable = iterable
        self.total = len(iterable)
    @property
    def total_row(self):
        return int(math.ceil(self.total/self.per_row))
    @property
    def has_prev(self):
        return self.row > 1
    @property
    def has_next(self):
        return self.row < self.total_row
    @property
    def row_list(self):
        return list(range(1,self.total_row+1))
    @property
    def items(self):
        index = self.row - 1
        start = index * self.per_row
        end = start + self.per_row
        return self.iterable[start:end]

app = Flask(__name__)

@app.route('/')#默认第一页路径为http://你的网站/posts
@app.route('/page/<int:page>/')#从第二页开始的路径
#def posts(row = 1):#page = 1是默认第一页的时候page为1
    #PER_ROW = 6
    #row_list = Pagination(row,PER_ROW,sorted_row)
    #return render_template('posts.html',pagination = row_list)