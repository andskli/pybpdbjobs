from .translations import *

class Jobtry(object):
    def __init__(self):
        self.pid = None
        self.stunit = None
        self.server = None
        self.started = None
        self.elapsed = None
        self.ended = None
        self.status = None
        self.statusdescription = None
        self.statuslines = []
        self.byteswritten = None
        self.fileswritten = None

    @property
    def statuscount(self):
        return self._statuscount

    @statuscount.setter
    def statuscount(self, val):
        self._statuscount = int(val)
