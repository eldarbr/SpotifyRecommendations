import http.server
import socketserver
from Configurator import Configurator
from urllib.parse import urlparse, parse_qs
from random import randint
import webbrowser


outer_instance = None


class SpotifyOAuth:
    def __init__(self, notify=None):
        self.configurator = Configurator()
        self.app_state = randint(0, 100000)
        self.auth_code = None
        self.notify = notify
        self.my_server = socketserver
        self.serving = True
        self.received_app_state = None

    def init_authorization(self):
        params = {
            "client_id": self.configurator.config["general"]["client_id"],
            "response_type": "code",
            "redirect_uri": self.configurator.config["general"]["redirect_uri"],
            "scope": "playlist-read-private playlist-read-collaborative playlist-modify-private "
                     "playlist-modify-public user-read-private",
            "state": str(self.app_state)
        }
        link = "https://accounts.spotify.com/authorize?"
        for key in params.keys():
            link += "=".join((key, params[key])) + "&"
        link = link[:-1]
        print(params["scope"])
        webbrowser.open(link)
        self.receive_auth_code()
        if self.auth_code is None:
            raise Exception("OAuth session failed")
        self.configurator.config["protected"]["auth_code"] = self.auth_code
        self.configurator.write_config()
        if self.notify is not None:
            self.notify()

    def receive_auth_code(self):
        global outer_instance
        outer_instance = self
        handler_object = self.MyHttpRequestHandler
        self.my_server = socketserver.TCPServer(("", 8888), handler_object)
        while self.serving:
            self.my_server.handle_request()

    def parse_auth_code(self, path):
        if "?" in path and "code" in path:
            if "error" in path:
                raise Exception("OAuth error " + path)
            else:
                arguments = parse_qs(urlparse(path).query)
                self.auth_code = arguments["code"][0]
                self.received_app_state = arguments["state"][0]
                self.serving = False

    class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
        def do_GET(self):
            global outer_instance
            outer_instance.parse_auth_code(self.path)
            self.path = "html/redirect.html"
            return http.server.SimpleHTTPRequestHandler.do_GET(self)


if __name__ == "__main__":
    sp = SpotifyOAuth()
    sp.init_authorization()
