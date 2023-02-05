#!/bin/python3

from flask import *
import requests
requests.packages.urllib3.util.connection.HAS_IPV6 = False

app = Flask(__name__)
import sys

from flask import request

@app.route('/<path:path>')
def proxy(path):
    try:
        import sys
        #print(request.headers, file=sys.stderr)
        resp = requests.get('https://enzymead.github.io/'+path, headers=request.headers)
        excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
        headers = [(name, value) for (name, value) in resp.raw.headers.items() if name.lower() not in excluded_headers]
        #print(headers,file=sys.stderr)
        res = Response(resp.content, resp.status_code, headers)
        return res
    except Exception as e:
        return str(e)

@app.route('/julia', defaults={'path': ''})
@app.route('/julia/', defaults={'path': ''})
@app.route('/julia/<path:path>')
def jl_get_resource(path):  # pragma: no cover
    try:
        import sys
        #print(request.headers, file=sys.stderr)
        resp = requests.get('https://enzymead.github.io/Enzyme.jl/'+path, allow_redirects=False) # , headers=request.headers)
        excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
        headers = [(name, value) for (name, value) in resp.raw.headers.items() if name.lower() not in excluded_headers]
        #print(headers,file=sys.stderr)
        res = Response(resp.content, resp.status_code, headers)
        return res
    except Exception as e:
        return str(e)

@app.route('/conference', defaults={'path': ''})
@app.route('/conference/<path:path>')
def conf_get_resource(path):  # pragma: no cover
    try:
        import sys
        #print(request.headers, file=sys.stderr)
        resp = requests.get('https://enzymead.github.io/enzyme-conf-website/'+path) # , headers=request.headers)
        excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
        headers = [(name, value) for (name, value) in resp.raw.headers.items() if name.lower() not in excluded_headers]
        #print(headers,file=sys.stderr)
        res = Response(resp.content, resp.status_code, headers)
        return res
    except Exception as e:
        return str(e)

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
def rust_get_resource(path):  # pragma: no cover
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
