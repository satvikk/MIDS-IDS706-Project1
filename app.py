from flask import Flask
from flask import jsonify

app = Flask(__name__)


@app.route("/")
def front_page():
    """Providing Instructions"""
    print("On front_page")
    return "<p> To use this app, append your string to the url</p>"


@app.route("/<var>")
def echo(var):
    print(f"This was placed in the url: new-{var}")
    val = {var: var[::-1]}
    return jsonify(val)


if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    app.debug = True
    app.run()
