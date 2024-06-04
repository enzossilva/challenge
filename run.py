from flask import request
from app import create_app
from app.controller import start_scan_controller, list_scan_controller, index

app = create_app()
zap_url = "http://127.0.0.1:8090"


@app.route("/")
def index_route():
    return index()


@app.route("/start_scan", methods=["POST"])
def start_scan_route():
    return start_scan_controller()


@app.route("/list_scans/<url>", methods=["GET"])
def list_scan_route(url):
    return list_scan_controller(url)


if __name__ == "__main__":
    app.run(debug=True)
