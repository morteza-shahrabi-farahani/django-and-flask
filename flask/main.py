from flask import Flask, render_template, request
from chart import draw_chart

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/data/', methods=['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        form_data = request.form
        plot = draw_chart(form_data['a1'], form_data['b1'], form_data['c1'], form_data['d1'], form_data['a2'], form_data['b2'], form_data['c2'], form_data['d2'])
        return render_template('data.html', plot = plot)


if __name__ == '__main__':
   app.debug = True
   app.run()
