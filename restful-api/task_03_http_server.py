# task_03_http_server.py

from http.server import BaseHTTPRequestHandler, HTTPServer
import json

HOST = "0.0.0.0"
PORT = 8000

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    """معالجة الطلبات HTTP"""

    def _set_headers(self, status_code=200, content_type="text/plain"):
        """إعداد الهيدر للرد"""
        self.send_response(status_code)
        self.send_header("Content-type", content_type)
        self.end_headers()

    def do_GET(self):
        """معالجة طلبات GET"""

        # الصفحة الرئيسية
        if self.path == "/":
            self._set_headers(200, "text/plain")
            self.wfile.write(b"Hello, this is a simple API!")

        # بيانات JSON
        elif self.path == "/data":
            self._set_headers(200, "application/json")
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode("utf-8"))

        # حالة API
        elif self.path == "/status":
            self._set_headers(200, "application/json")
            status = {"status": "OK"}
            self.wfile.write(json.dumps(status).encode("utf-8"))

        # مثال endpoint إضافي
        elif self.path == "/info":
            self._set_headers(200, "application/json")
            info = {"version": "1.0", "description": "A simple API built with http.server"}
            self.wfile.write(json.dumps(info).encode("utf-8"))

        # أي endpoint غير معرف
        else:
            self._set_headers(404, "text/plain")
            self.wfile.write(b"Endpoint not found")

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
    """تشغيل السيرفر"""
    server_address = (HOST, PORT)
    httpd = server_class(server_address, handler_class)
    print(f"Server running on http://{HOST}:{PORT}")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
