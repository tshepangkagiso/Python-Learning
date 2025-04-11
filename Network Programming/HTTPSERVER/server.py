# Implement a simple HTTP server using the http.server module. Serve static files and handle basic GET and POST requests.
from http.server import HTTPServer
from Modules import RouteHandlerModule

RouteHandler = RouteHandlerModule.RouteHandler

def run(server_class = HTTPServer, handler_class = RouteHandler, port = 3000):
    try:
        server_address = ('', port)
        httpd = server_class(server_address, handler_class)
        print(f"server running on port: {port}")
        httpd.serve_forever()

    except Exception as ex:
        print(f"server running error: {ex}")

if __name__ == '__main__':
    run()