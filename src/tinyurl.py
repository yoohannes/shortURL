import json
from flask import (
    Flask,
    redirect,
    url_for,
    jsonify,
    request,
    render_template,
    make_response,
)
from flask.scaffold import _matching_loader_thinks_module_is_package

from EncodeDecode import EncodeDecode


tinyurl = Flask(__name__)


@tinyurl.route("/")
def index():
    """routes to the homepage"""
    return render_template("index.html")


@tinyurl.route("/encode_url", methods=["POST"])
def create_link():
    """encode and returns short url response"""
    original_url = request.form["original_url"]
    encoded_url = link_object.encode(original_url)
    return jsonify(encoded_url)


@tinyurl.route("/<short_url>", methods=["GET"])
def url_redirect(short_url):
    """redirects the short url entered"""

    if short_url in link_object.decodemap.keys():
        redirect_link = link_object.decodemap.get(short_url)

        return redirect(redirect_link)
    else:

        return f"<h1>url doent exist</h1>"


"""dictionary stores unique key value store 
so we can use dict as a in memory storage """
if __name__ == "__main__":
    link_object = EncodeDecode()
    tinyurl.run(host="0.0.0.0", debug=True)
