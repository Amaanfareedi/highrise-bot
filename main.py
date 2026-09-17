import os, threading, http.server, socketserver
def run_dummy():
    port = int(os.environ.get("PORT", 10000))
    handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", port), handler) as httpd:
        httpd.serve_forever()
threading.Thread(target=run_dummy, daemon=True).start()

from highrise import BaseBot
import asyncio

EMOTE_LIST = [
"kiss","laugh","sit","fairytwirl","fairyfloat","launch","cutesalute","atattention","tiktok","smooch",
"pushit","foryou","touch","kawaii","repose","sleigh","hyped","jingle","gottago","timejump",
"scritchy","bitnervous","iceskating","partytime","arabesque","bashful","revelations
