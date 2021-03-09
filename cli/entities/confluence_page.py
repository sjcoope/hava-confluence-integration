from typing import List
from cli.entities.hava_link import HavaLink
from cli.utils import hava

class ConfluencePage:
    def __init__(self, content):
        self.id = content["id"]
        self.title = content["title"]
        self.body = ""
        self.children = []
        self.hava_link = HavaLink()

    def set_body(self, body):
        self.body = body

        if body:
            self.hava_link.id = hava.get_hava_data("HAVA-ID", body)
            self.hava_link.last_sync = hava.get_hava_data("HAVA-LAST-SYNC", body)
