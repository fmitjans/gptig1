from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse as urlparse
import json

from main import get_offers

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        query_components = urlparse.parse_qs(urlparse.urlparse(self.path).query)
        keyword = query_components.get("keyword", ["software"])[0]
        
        results_json = get_offers(keyword)
        # response_data = {"message": f"Hello, {name}!"}
        # response_json = json.dumps(response_data)
        
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')  # Allow requests from any origin
        self.end_headers()
        self.wfile.write(results_json.encode('utf-8'))

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Server running on port {port}")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
