from http.server import HTTPServer, BaseHTTPRequestHandler
import subprocess

# AGENT = subprocess.Popen(['pythonw', 'agent.py'])


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        with open("./output/out.txt", "r") as f:
            self.wfile.write(f.read().encode())


httpd = HTTPServer(("0.0.0.0", 3050), SimpleHTTPRequestHandler)
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    # AGENT.kill()
    exit()
