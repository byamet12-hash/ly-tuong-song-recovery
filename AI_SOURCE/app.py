from http.server import BaseHTTPRequestHandler, HTTPServer
import json

from core.architect import architect
from core.memory import memory
from core.permissions import permissions
from core.tools import tools


class Handler(BaseHTTPRequestHandler):

    def send_json(self, data, status=200):

        body = json.dumps(
            data,
            ensure_ascii=False,
            indent=2
        ).encode()

        self.send_response(status)
        self.send_header(
            "Content-Type",
            "application/json; charset=utf-8"
        )
        self.send_header(
            "Content-Length",
            str(len(body))
        )
        self.end_headers()

        self.wfile.write(body)


    def do_GET(self):

        if self.path == "/":
            return self.send_json({
                "name": "AI Architect Hub",
                "version": "0.1",
                "modules": [
                    "architect",
                    "agents",
                    "memory",
                    "tools",
                    "permissions"
                ]
            })

        if self.path == "/memory":
            return self.send_json(memory.all())

        if self.path == "/tools":
            return self.send_json(tools.list())

        if self.path == "/permissions":
            return self.send_json(permissions.list())

        return self.send_json(
            {"error": "Not found"},
            404
        )


    def do_POST(self):

        try:
            length = int(
                self.headers.get(
                    "Content-Length",
                    "0"
                )
            )

            data = json.loads(
                self.rfile.read(length) or b"{}"
            )

        except Exception:
            return self.send_json(
                {"error": "Invalid JSON"},
                400
            )


        if self.path == "/architect/plan":

            return self.send_json(
                architect.plan(
                    data.get("goal", "")
                )
            )


        if self.path == "/memory":

            return self.send_json(
                memory.remember(
                    data.get("key", ""),
                    data.get("value", "")
                ),
                201
            )


        if self.path == "/execute":

            result = architect.execute(
                data.get("agent", ""),
                data.get("tool", ""),
                data.get("input", {})
            )

            status = 200

            if "error" in result:
                status = 403

            return self.send_json(
                result,
                status
            )


        return self.send_json(
            {"error": "Not found"},
            404
        )


print("================================")
print("   AI ARCHITECT HUB")
print("================================")
print("Server: http://127.0.0.1:8000")
print("Đang khởi động...")


HTTPServer(
    ("127.0.0.1", 8000),
    Handler
).serve_forever()
