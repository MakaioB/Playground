from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello!"

@app.route('/play')
def make_boxes():
    return render_template('index.html', times = 3, color = 'blue')

@app.route('/play/<int:times>')
def make_many_boxes(times):
    times = times
    return render_template('index.html', times = times)

@app.route('/play/<int:times>/<string:color>')
def make_many_colored_boxes(times, color):
    times = times
    color = color
    return render_template('index.html', times = times, color = color)

if __name__ == '__main__':
    app.run(debug=True)