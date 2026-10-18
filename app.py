

from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import os


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        response = {
            "app": "devops-lab",
            "version": os.getenv("APP_VERSION", "1.0"),
            "status": "running",
        }

        body = json.dumps(response).encode("utf-8")

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


def create_server(host="0.0.0.0", port=8000):
    return HTTPServer((host, port), Handler)


if __name__ == "__main__":
    server = create_server()
    print("Server running on port 8000")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
