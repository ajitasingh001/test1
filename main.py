from flask import Flask,render_template,request,flash,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
app =Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='mysql://root:''@localhost/person_detail'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =True
app.config['SECRET_KEY'] = "random string"
db = SQLAlchemy(app)
class Person(db.Model):
    id = db.Column(db.Integer,primary_key= True)
    name = db.Column(db.String(100))
    city = db.Column(db.String(100))
    addr= db.Column(db.String(100))
    def __init__(self,name,city,addr):
        self.name =name
        self.city =city
        self.addr = addr
@app.route('/')
def index():
   return render_template("index.html",person=Person.query.all())
@app.route('/login/<id>',methods =['GET','POST'])
def login(id):
    print(type(id))
    data =None
    if request.method =='POST' and id=='0':
        result=Person(request.form['name'],request.form['city'],request.form['addr'])
        db.session.add(result)
        db.session.commit()
        flash("data has been added succusfully")
        return redirect(url_for("index"))
    elif request.method =='POST' and id!='0':
        data = Person.query.filter_by(id=id).first()
        data.name=request.form['name']
        data.city = request.form['city']
        data.addr = request.form['addr']
        db.session.commit()
        flash("data has been modified succusfully")
        return redirect(url_for("index"))
        print(data)
    else:
        data = Person.query.filter_by(id=id).first()
    return render_template('login.html',data=data)
@app.route('/delete/<id>')
def delete(id):
    result1 = Person.query.filter_by(id=id).first()
    db.session.delete(result1)
    db.session.commit()
    flash("data has been deleted succusfully")
    return redirect(url_for("index"))
@app.route('/search',methods=['GET','POST'])
def search():
    if request.method=='POST':



if __name__ == '__main__':
    app.run(debug=True)

    db.create_all()





