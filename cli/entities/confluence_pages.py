
from .confluence_page import ConfluencePage

class ConfluencePages():
    def __init__(self, array):
        self.pages = []
        
        for item in array:
            self.pages.append(ConfluencePage(item))
    
    def __iter__(self):
        return self.pages.__iter__()

    def single_or_default(self, sequence, default=None):
        last_item = default
        for s in sequence:
            last_item = s
        return last_item