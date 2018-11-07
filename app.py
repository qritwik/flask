from flask import Flask, redirect, url_for, request
from flask import Flask, render_template

app = Flask(__name__)



@app.route('/',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      username = request.form['username']
      password = request.form['password']

      if((username == "admin" and password == "admin") or (username == "admin" and password == "admin") or (username == "admin" and password == "admin") or (username == "admin" and password == "admin")):
      	return redirect(url_for('detail',name = username))
      else:
      	return "Incorrect login credentials"




   return render_template('index.html')



@app.route('/detail/<name>',methods = ['POST', 'GET'])
def detail(name):
    if request.method == 'POST':
        return redirect(url_for('detail',name = name))


    return render_template('detail.html',name = name)




if __name__ == '__main__':
   app.run(debug = True)
