from flask import Flask, redirect,url_for

app = Flask(__name__)

@app.route("/")
def index():
  return "<h1>Hello!Welcome</h1>"

if __name__ == '__main__':
   app.run()                            # This is important