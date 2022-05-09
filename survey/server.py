from flask import Flask, render_template, request, redirect, session, url_for
app = Flask(__name__)
app.secret_key = "surfoften"


@app.route('/hello')
def hello_world():
    return 'Hello World!'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form_data', methods=['POST'])
def handle_form_data():
    print(request.form)
    return redirect('/')

@app.route('/set-background/<mode>')
def set_background(mode):
    session['mode']= mode
    return redirect(url_for('index'))


if __name__=="__main__":    
    app.run(debug=True)