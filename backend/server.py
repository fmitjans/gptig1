from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse as urlparse
import json
from main import get_offers, generar_correo_openai

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        query_components = urlparse.parse_qs(urlparse.urlparse(self.path).query)
        keyword = query_components.get("keyword", ["software"])[0]
        action = query_components.get("action", ["get_offers"])[0]

        if action == "get_offers":
            results_json = get_offers(keyword)
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(results_json.encode('utf-8'))

        elif action == "generate_email":
            index = int(query_components.get("index", [0])[0])  # Obtener el índice de la oferta
            results = json.loads(get_offers(keyword))  # Obtener las ofertas de trabajo
            selected_offer = results[index]  # Seleccionar la oferta según el índice
            generated_email = generar_correo_openai(selected_offer)  # Generar el correo usando OpenAI

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps({"email": generated_email}).encode('utf-8'))

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Server running on port {port}")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
