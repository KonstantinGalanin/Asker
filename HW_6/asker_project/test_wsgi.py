HELLO_WORLD = b"Hello world!\n"

def simple_app(environ, start_response):
    request_method = environ['REQUEST_METHOD']
    
    query_string = environ['QUERY_STRING']

    response_body = [
        f"Method: {request_method}\n",
    ]
    
    if request_method == 'POST':
        content_length = int(environ.get('CONTENT_LENGTH', 0))
        data = environ['wsgi.input'].read(content_length).decode("utf-8").split('&')
        response_body.append(f"POST data: {data}\n")
        print("POST: ", data)
    else:
        response_body.append(f"GET params: {query_string}\n",)


    response_text = ''.join(response_body)
    response_bytes = (''.join(response_body)).encode('utf-8')

    status = '200 OK'
    response_headers = [('Content-type', 'text/plain'), ('Content-Length', str(len(response_bytes)))]
    start_response(status, response_headers)



    return [response_text.encode('utf-8')]
        

application = simple_app
