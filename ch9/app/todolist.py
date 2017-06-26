#!/usr/bin/env python
# -*- coding: utf-8 -*-
import StringIO
import matplotlib
matplotlib.use('Agg')
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from flask.ext.wtf import Form
from wtforms import    StringField, SubmitField,  ValidationError,DateField,IntegerField
from  wtforms.validators import  DataRequired
from  flask.ext.script  import  Manager
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bootstrap import Bootstrap
from  flask import request, render_template, url_for, redirect, flash,make_response
from datetime  import datetime
import sys
import os
import numpy as np
reload(sys)
sys.setdefaultencoding('gb18030')
basedir =os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI']="postgresql://postgres:postgres@localhost/test" #'sqlite:///c:/todo.sqlite'
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///c:/todo.sqlite'
app.config['DEBUG']=True
app.config['SECRET_KEY'] = 'super secret key'
db = SQLAlchemy(app)
db.init_app(app)
manager = Manager(app)
bootstrap = Bootstrap(app)
@manager.command
def createall():

    db.create_all()
class TodoForm(Form):
    '''表单'''
    title = StringField(u"内容",validators=[DataRequired()])
    DateDue=DateField(u"截止日期")
    level=IntegerField(u'优先级 ',default=1 )
    validate_on_submit = SubmitField(u'提交')

from matplotlib.pyplot import *
from random import *
@app.route('/fig/<level>')
def fig(level):
    level =int(level)
    if level>4:
        level =4
    fig = Figure((8,8), dpi=50)
    axis = fig.add_subplot(1, 1, 1)
    x = np.random.rand(level)#位置随机
    y = np.random.rand(level)
    colors = ['blue', 'green', 'yellow', 'red']
    axis.scatter(x,y,s=10000, color=colors[level-1], marker=(5,1))
    canvas = FigureCanvas(fig)
    output = StringIO.StringIO()
    canvas.print_png(output)
    response = make_response(output.getvalue())
    response.mimetype = 'image/png'
    return response
@app.route("/",methods=['GET','POST'])
def  index():
    todo=Todo.query.all()
    todoform=TodoForm()
    if request.method == 'POST' and todoform.validate_on_submit():
        t=Todo(title=todoform.title.data,DateDue=todoform.DateDue.data,level=todoform.level.data)
        try :
            db.session.add(t)
            db.session.commit()
            return redirect (url_for("index"))
        except:
            flash(u"错误")
    return render_template('index.html',form=todoform,todo=todo )


@app.route('/del/<int:id>')
def delitem(id):
    todo = Todo.query.filter_by(id=id).first()
    if todo:
        db.session.delete(todo)
        db.session.commit()
    flash(u"记录删除成功")
    return redirect(url_for("index"))
@app.route('/done/<int:id>')
def done(id):
    todo = Todo.query.filter_by(id=id).first()
    if todo:
        Todo.query.filter_by(id=id).update({Todo.status:True})
        db.session.commit()
        flash(u"任务完成")
    return redirect("/")


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_404.html'), 404
class Todo(db.Model):
    '''数据模型'''
    __tablename__='todo'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    posted_on = db.Column(db.Date, default=datetime.utcnow)
    status = db.Column(db.Boolean(), default=False)
    DateDue=db.Column(db.Date, default=datetime.utcnow)
    level= db.Column(db.Integer )
    def __init__(self, *args, **kwargs):
        super(Todo, self).__init__(*args, **kwargs)
    def __repr__(self):
        return "<Todo '%s' :'%s':'%s':'%s':'%s'>" %( self.title,self.status,self.DateDue,self.posted_on,self.id)
    def validate_title(form, field):
        if field.data == 0:
            raise ValidationError, u'内容不能为空'
if __name__=="__main__":
    manager.run()
