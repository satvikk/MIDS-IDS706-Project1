from flask import Flask
from flask import jsonify

application = Flask(__name__)


@application.route("/")
def hello():
    """Return a friendly HTTP greeting."""
    print("Inside Root")
    return "<p> Append your birth month number to the url (with a slash) </p>"


@application.route("/echo/<m>")
def echo(m):
    print(f"This was placed in the url: {m}")
    if m not in record.keys:
        return {"error":"invalid"}
    record[m] += 1
    return {m:record[m]}


if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    record = {i:0 for i in range(1,13)}
    application.run(host="0.0.0.0", port=8080, debug=True)