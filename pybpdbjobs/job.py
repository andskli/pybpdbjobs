from .translations import *

class Job(object):
    def __init__(self):
        self._id = None
        self.filelist = []
        self.status = None
        self.client = None
        self.server = None
        self.start = None
        self.elapsed = None
        self.end = None
        self.stunit = None
        self.jobtry = None
        self.operation = None
        self.kbytes = None
        self.files = None
        self.path_last_written = None
        self.percent = None
        self.pid = None
        self.owner = None
        self.priority = None
        self.group = None
        self.master_server = None
        self.retention_period = None
        self.compression = None
        self.kbyteslastwritten = None
        self.fileslastwritten = None
        self.tries = {}

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, val):
        self._id = int(val)

    @property
    def filelistcount(self):
        return self._filelistcount

    @filelistcount.setter
    def filelistcount(self, val):
        self._filelistcount = int(val)

    @property
    def trycount(self):
        return self._trycount

    @trycount.setter
    def trycount(self, val):
        self._trycount = int(val)

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, val):
        try:
            self._type = JOB_TYPE[int(val)]
        except KeyError:
            self._type = val

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, val):
        try:
            self._state = JOB_STATE[int(val)]
        except KeyError:
            self._state = val

    @property
    def schedtype(self):
        return self._schedtype

    @schedtype.setter
    def schedtype(self, val):
        try:
            self._schedtype = SCHEDULE_TYPE[int(val)]
        except:
            self._schedtype = val

    @property
    def subtype(self):
        return self._subtype

    @subtype.setter
    def subtype(self, val):
        try:
            self._subtype = SUB_TYPE[int(val)]
        except:
            self._subtype = val

    @property
    def policytype(self):
        return self._policytype

    @policytype.setter
    def policytype(self, val):
        try:
            self._policytype = POLICY_TYPE[int(val)]
        except:
            self._policytype = val
