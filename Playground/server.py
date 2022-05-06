from flask import Flask, render_template


app = Flask(__name__)

@app.route('/play')
def play():
    return render_template('index.html',number=3,color="blue")

@app.route('/play/<int:number>')
def add_boxes(number):
    return render_template('index.html',number=number,color="blue")

@app.route('/play/<int:number>/<string:color>')
def add_boxes_and_color(number,color):
    return render_template('index.html',number=number,color=color)

if __name__=="__main__":
    app.run(debug=True)