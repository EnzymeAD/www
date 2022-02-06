#!/bin/python3

from flask import *
import requests

app = Flask(__name__)
import sys

from flask import request

@app.route('/<path:path>')
def proxy(path):
    try:
        import sys
        #print(request.headers, file=sys.stderr)
        resp = requests.get('http://wsmoses.github.io/'+path, headers=request.headers)
        excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
        headers = [(name, value) for (name, value) in resp.raw.headers.items() if name.lower() not in excluded_headers]
        #print(headers,file=sys.stderr)
        res = Response(resp.content, resp.status_code, headers)
        return res
    except Exception as e:
        return str(e)

@app.route('/julia', defaults={'path': ''})
@app.route('/julia/<path:path>')
def get_resource(path):  # pragma: no cover
    mimetypes = {
        ".css": "text/css",
        ".html": "text/html",
        ".js": "application/javascript",
    }
    complete_path = os.path.join(root_dir(), "julia", path)
    ext = os.path.splitext(path)[1]
    mimetype = mimetypes.get(ext, "text/html")
    content = get_file(complete_path)
    return Response(content, mimetype=mimetype)

@app.route('/doxygen', defaults={'path': ''})
@app.route('/doxygen/<path:path>')
def dox_get_resource(path):  # pragma: no cover
    mimetypes = {
        ".css": "text/css",
        ".html": "text/html",
        ".js": "application/javascript",
    }
    complete_path = os.path.join(root_dir(), "doxygen", path)
    ext = os.path.splitext(path)[1]
    mimetype = mimetypes.get(ext, "text/html")
    content = get_file(complete_path)
    return Response(content, mimetype=mimetype)

@app.route('/rust', defaults={'path': ''})
@app.route('/rust/<path:path>')
def dox_get_resource(path):  # pragma: no cover
    mimetypes = {
        ".css": "text/css",
        ".html": "text/html",
        ".js": "application/javascript",
    }
    complete_path = os.path.join(root_dir(), "rust", path)
    ext = os.path.splitext(path)[1]
    mimetype = mimetypes.get(ext, "text/html")
    content = get_file(complete_path)
    return Response(content, mimetype=mimetype)

@app.route('/')
def root():
    return proxy('/')

@app.route('/google03f38f66bacc8764.html')
def gsite():
    return "google-site-verification: google03f38f66bacc8764.html"
