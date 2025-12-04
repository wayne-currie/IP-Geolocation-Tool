from flask import Flask, render_template, request
from validator import validate_ip
from geolocate import lookup_ip

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None

    if request.method == "POST":
        ip = request.form.get("ip", "").strip()

        if not validate_ip(ip):
            error = "Invalid IP address"
        else:
            result = lookup_ip(ip)
            if not result:
                error = "Could not retrieve geolocation data"

    return render_template("index.html", result=result, error=error)

if __name__ == "__main__":
    app.run(debug=True)
