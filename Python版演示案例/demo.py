from http.server import HTTPServer, BaseHTTPRequestHandler
import json


class Resquest(BaseHTTPRequestHandler):
    def do_POST(self):
        # 获取数据
        json_str = self.rfile.read(int(self.headers["content-length"]))
        json_str = json_str.decode()
        result = json.loads(json_str)
        print(result)

        # 收到文本消息
        if result["msg_type"] == 1:
            print("收到文本消息：{}".format(result["data"]["content"]))

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps({"result": "ok"}).encode())


if __name__ == '__main__':
    host = ("127.0.0.1", 9000)
    server = HTTPServer(host, Resquest)
    print("Starting server, listen at: %s:%s" % host)
    server.serve_forever()



