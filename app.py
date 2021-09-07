from flask import Flask


application = Flask(__name__)


@application.route("/")
def hello():
    #"""Return a friendly HTTP greeting."""
    print("Inside Root")
    return "Append /Number of month to url" 


@application.route("/<m>")
def echo(m):
    if m not in [str(i) for i in range(1,13)]:
        return {"error": "invalid input"}
    m = int(m)
    record = {
        1:"January", 2:"February", 3:"March", 4:"April", 5:"May", 6:"June", 7:"July", 8:"August", 9:"September", 10:"October", 
        11:"November", 12:"December"
    }
    return {m: record[m]}

if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    #record = {i:0 for i in range(1,13)}
    application.run(host="0.0.0.0", port=8080, debug=True)
