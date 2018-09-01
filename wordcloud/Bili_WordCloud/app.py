from flask import Flask,render_template,request,g,abort,jsonify
from run import run


app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')

@app.route('/get_image', methods=['GET', 'POST'])
def get_img():
    if request.method == 'POST':
        name = request.form['project']
        ids = request.form['ids'].split(',')
        back_img = request.form['back_img']
        result_src = run(name, ids, back_img)
        return jsonify({'result_src': result_src})
    else:
        abort(404)
if __name__ == '__main__':
    app.run()