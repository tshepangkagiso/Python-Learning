from http.server import BaseHTTPRequestHandler
import json

items = []

class RouteHandler(BaseHTTPRequestHandler):
    def _set_Headers(self, status = 200):
        try:
            self.send_response(status)
            self.send_header("Content-Type", "application/json")
            self.end_headers()

        except Exception as ex:
            print(f"set headers error: {ex}")

    
    def do_GET(self):
        try:
            self._set_Headers()
            self.wfile.write(json.dumps(items).encode())

        except Exception as ex:
            print(f"get request error: {ex}")


    def do_POST(self):
        try:
            content_length = int(self.headers['Content-Length'])
            body = self.rfile.read(content_length)
            data = json.loads(body)

            items.append(data)
            self._set_Headers(201)
            self.wfile.write(json.dumps({"message":"Item added"}).encode())

        except Exception as ex:
            print(f"post request error: {ex}")


    def do_PUT(self):
        try:
            content_length = int(self.headers['Content-Length'])
            body = self.rfile.read(content_length)
            data = json.loads(body)

            if 'id' not in data or data['id'] >= len(items):
                self._set_Headers(404)
                self.wfile.write(json.dumps({"error":"Item not found"}).encode())
                return
            
            items[data['id']] = data['item']
            self._set_Headers()
            self.wfile.write(json.dumps({"message":"Item updated successfully"}).encode())

        except Exception as ex:
            print(f"put request error: {ex}")


    def do_DELETE(self):
        try:
            content_length = int(self.headers['Content-Length'])
            body = self.rfile.read(content_length)
            data = json.loads(body)

            if 'id' not in data or data['id'] >= len(items):
                self._set_Headers(404)
                self.wfile.write(json.dumps({"error":"Item not found"}).encode())
                return
            deleted = items.pop(data['id'])
            self._set_Headers()
            self.wfile.write(json.dumps({"message":"Item deleted successfully"}).encode())

        except Exception as ex:
            print(f"delete request error: {ex}")
