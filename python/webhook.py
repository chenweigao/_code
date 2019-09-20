import os
import html
import urllib.parse
from wsgiref.simple_server import make_server

def app(env, resp):
    try:
        request_body_size = int(env.get('CONTENT_LENGTH', 0))
    except (ValueError):
        request_body_size = 0

    request_body = env.get('wsgi.input').read(request_body_size)
    parsed_request_body = urllib.parse.parse_qs(request_body)

    name = parsed_request_body.get('name', 'null')
    name = html.escape(name)
    
    resp('200 OK', [('Content-Type', 'text/html'), ('Content-Length', str(len(request_body))), ('name', name)])
    PATH_OF_BLOG = '/root/test_vueblog/vueblog'
    # os.chdir(PATH_OF_BLOG)
    os.chdir('C:\\Users\\nerche\Documents\\_code\\vueblog')
    res = str(os.listdir(os.getcwd()))
    os.system('git status')
    os.system('git pull')
    # os.system('yarn docs:build')
    return [request_body]

httpd = make_server('', 8899, app)
print('Serving on port 8899...')
httpd.serve_forever()