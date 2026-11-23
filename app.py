"""Dependency-free container API starter for SCAPE."""

import json
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer


def health_payload() -> dict[str, str]:
    return {"status": "ok"}


class Handler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        if self.path == "/health":
            body = json.dumps(health_payload()).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
        elif self.path == "/":
            body = json.dumps({"name": "scape-containerized-api", "status": "running"}).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
        else:
            body = json.dumps({"error": "not_found"}).encode("utf-8")
            self.send_response(404)
            self.send_header("Content-Type", "application/json; charset=utf-8")

        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format_string: str, *args: object) -> None:
        print(f"{self.address_string()} - {format_string % args}")


if __name__ == "__main__":
    port = int(os.getenv("PORT", "3000"))
    print(f"Containerized API listening on port {port}")
    ThreadingHTTPServer(("0.0.0.0", port), Handler).serve_forever()
