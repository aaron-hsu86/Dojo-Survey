from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'secret_number'

@app.route('/')
def welcome():
    return render_template('index.html')


@app.route('/process', methods=['post'])
def process_data():
    session['name']=request.form['name']
    session['location']=request.form['location']
    session['fav_language']=request.form['fav_language']
    session['league'] = request.form.getlist('roles')
    if session['league'] == []:
        session['league'] = "Maybe doesn't play league?"
    session['comment']=request.form['comment']
    if session['comment'] is '':
        session['comment'] = 'No comment'
    
    return redirect('/result')


@app.route('/result')
def result_page():
    
    return render_template('result.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)