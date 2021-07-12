from flask import Flask,render_template
import sqlite3

app = Flask(__name__)


@app.route("/")
def hello():
      id=100
      return render_template('index.html',data=id)

@app.route("/admin")
def admin():
      text={"hi":'Hello admin','bye':'Good bye'}
      return render_template('admin.html',text=text)

if __name__ == "__main__":
  app.run(debug=True)
