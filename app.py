from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import crud

app = Flask(__name__)




@app.route('/add')
def add():
    return render_template('add.html')




@app.route('/insert',methods = ['GET','POST'])
def insert():
    if request.method == 'POST':
        nm = request.form['name']
        addr = request.form['add']
        city = request.form['city']
        pin = request.form['pin']
        data = [nm,addr,city,pin]
        mcg = crud.add_data(data)
        #return mcg
        data = crud.view_data()
        return render_template("index.html", mcg=mcg, rows=data)
    else:
        return 'Failed'




@app.route('/')
def view():
    data = crud.view_data()
    return render_template('index.html',rows=data)
    


@app.route('/delete/<id>')
def delete(id):
    mcg = crud.delete_data(id)
    #return mcg
    data = crud.view_data()
    return render_template("index.html", mcg=mcg, rows=data)
    



@app.route('/edit/<id>', methods = ['GET','POST'])
def edit(id):
    data = crud.edit_data(id)
    return render_template("edit.html",data=data)




@app.route('/update',methods = ['GET','POST'])
def update():
    #pass
    if request.method == 'POST':
        id = request.form['id']
        nm = request.form['name']
        addr = request.form['add']
        city = request.form['city']
        pin = request.form['pin']
        task= [nm,addr,city,pin,id]
        mcg = crud.update_data(task)
        #return mcg
        data = crud.view_data()
        return render_template("index.html", mcg=mcg, rows=data)
    else:
        return 'Failed'





app.run(debug=True)

if __name__ == '__main__':
    app.run()