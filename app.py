from flask import Flask,render_template

app = Flask(__name__,template_folder='templates',static_folder='static',static_url_path='/static')

@app.route('/movie_view',methods = ["GET","POST"])
def grade_cut():
    return render_template("grade_cut_view.html")

if __name__ == "__main__":
	app.run(debug=True, port=5000,host='0.0.0.0')