from wsgiref.simple_server import make_server

def application(env, start_response):
    print(env)
    start_response('200 ok', [('Content-type', 'text/html')])
    return [b'<h1>Hello World!</h1>']


httpd = make_server('', 80, application)

httpd.serve_forever()