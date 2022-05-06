from flask import Flask, render_template, request, redirect, session, url_for
app = Flask(__name__)
app.secret_key = "surfoften"

@app.route('/')
def index():
    if "views" not in session:
        session['views'] = 0
    else:
        session['views'] = session['views'] + 1
    return render_template("index.html")


@app.route('/add_two')
def add_two():
    session['views'] += 1
    return redirect('/')

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/')

@app.route('/increase_views_by', methods=['POST'])
def increase_views_by():
    amt = int(request.form['views'])
    session['views'] += amt - 1
    return redirect('/')


@app.route('/set-background/<mode>')
def set_background(mode):
    session['mode']= mode
    return redirect(url_for('index'))
    
@app.errorhandler(404)
def pageNotFound(missing):
    return "Sorry! No response. Try again."

if __name__=="__main__":
    app.run(debug=True)