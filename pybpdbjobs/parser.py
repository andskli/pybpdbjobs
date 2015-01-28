from pybpdbjobs.job import Job
from pybpdbjobs.jobtry import Jobtry

import csv

class Parser(object):
    def process_line(self, line):
        """
        Process single line and return as :class:`Job <Job>` object
        :param buf: Line to be processed
        :return: Returns Job object if successful, None if not
        """
        job = Job()
        i = 0

        for x in csv.reader([line], escapechar='\\'):
            buf = x

        # Well, this is an awkward solution to avoid null lists to be processed
        try:
            _ = buf[1]
        except IndexError:
            return None

        for label in ('id', 'type', 'state', 'status', 'policyname', 'schedname',
                      'client', 'server', 'start', 'elapsed', 'end', 'stunit',
                      'jobtry', 'operation', 'kbytes', 'files',
                      'path_last_written', 'percent', 'pid', 'owner', 'subtype',
                      'policytype', 'schedtype', 'priority', 'group',
                      'master_server', 'retention_units', 'retention_period',
                      'compression', 'kbyteslastwritten', 'fileslastwritten',
                      'filelistcount'):
            setattr(job, label, buf[i])
            i += 1

        if job.filelistcount > 0:
            for _ in range(i, i + job.filelistcount):
                job.filelist.append(buf[i])
                i += 1

        job.trycount = buf[i]
        i += 1

        for job_try in range(1, job.trycount + 1):
            jobtry = Jobtry()
            jobtry.id = job_try
            for trylabel_1 in ('pid', 'stunit', 'server', 'started', 'elapsed',
                               'ended', 'status', 'statusdescription',
                               'statuscount'):
                setattr(jobtry, trylabel_1, buf[i])
                i += 1

            if jobtry.statuscount > 0:
                for _ in range(i, i + jobtry.statuscount):
                    jobtry.statuslines.append(buf[i])
                    i += 1

            for trylabel_2 in ('byteswritten', 'fileswritten'):
                setattr(jobtry, trylabel_2, buf[i])
                i += 1

            # Append all Jobtry() objects to Job() object as dicts
            job.tries[jobtry.id] = self.json_serializer(jobtry)

        for label in ('parentjob', 'kbpersec', 'copy', 'robot', 'vault', 'profile',
                      'session', 'ejecttapes', 'srcstunit', 'srcserver',
                      'srcmedia', 'dstmedia', 'stream'):
            setattr(job, label, buf[i])
            i += 1

        for label in ('suspendable', 'resumable', 'restartable', 'datamovement',
                      'frozenimage', 'backupid', 'killable', 'controllinghost'):
            setattr(job, label, buf[i])
            i += 1

        return job


    def json_serializer(self, obj):
        """
        Serializer that removes leading underscore from key names in objects
        :param obj: Object to be jsonized and dicitfied
        :return dict:
        """
        res = obj.__dict__.copy()
        for key in res.keys():
            if key.startswith('_'):
                newkeyname = key.lstrip('_')
                res[newkeyname] = res[key]
                del res[key]
        return res