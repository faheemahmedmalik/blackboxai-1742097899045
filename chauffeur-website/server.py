from http.server import HTTPServer, SimpleHTTPRequestHandler
import os

class CustomHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        # Ensure we're serving from the frontend directory
        current_dir = os.path.dirname(os.path.abspath(__file__))
        frontend_dir = os.path.join(current_dir, "frontend")
        super().__init__(*args, directory=frontend_dir, **kwargs)
    
    def log_message(self, format, *args):
        # Enhanced logging that safely handles variable number of arguments
        message = format % args if args else format
        print(f"[Server] {message}")

def run(server_class=HTTPServer, handler_class=CustomHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    frontend_dir = os.path.join(current_dir, "frontend")
    print(f"Server running on port {port}...")
    print(f"Serving files from: {frontend_dir}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server...")
        httpd.server_close()

if __name__ == '__main__':
    run()
