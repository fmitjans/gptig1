from http.server import BaseHTTPRequestHandler, HTTPServer
from time import sleep
import urllib.parse as urlparse
import json

from main import get_offers, get_details, generar_correo_openai

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse.urlparse(self.path)
        path = parsed_path.path
        query_components = urlparse.parse_qs(parsed_path.query)
        
        if path == "/offers":  # First kind of GET request
            keyword = query_components.get("keyword", ["software"])[0]
            results_json = get_offers(keyword)
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(results_json.encode('utf-8'))
        
        elif path == "/details":
            offer_id = query_components.get("offer_id", ["0"])[0]
            
            details_dict = get_details(offer_id)
            details_json = json.dumps(details_dict)
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(details_json.encode('utf-8'))

        elif path == "/mail":
            details_json = query_components.get("details_json", [0])[0]
            details = json.loads(details_json)
            generated_email = generar_correo_openai(details)

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps({"email": generated_email}).encode('utf-8'))     
        
        else:
            # Handle unknown paths
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Not Found')


def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Server running on port {port}")
    httpd.serve_forever()

if __name__ == '__main__':
    codigo = '2024-083180'
    # data = get_details(codigo)
    # correo = generar_correo_openai(data)
    # print(correo)
    run()
