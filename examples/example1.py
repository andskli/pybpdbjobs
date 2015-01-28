import subprocess
import json

from pprint import pprint

import pybpdbjobs

# BPDBJOBS_CMD = ['/usr/openv/netbackup/bin/admincmd/bpdbjobs',
#                 '-report', '-all_columns']

BPDBJOBS_CMD = ['cat', '../netbackup/example_output/bpdbjobsdump.out']


def run_process(cmd):
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    return p.stdout.read().decode('ascii', 'ignore')  # XXX


if __name__ == '__main__':
    parser = pybpdbjobs.Parser()
    for input_line in run_process(BPDBJOBS_CMD).split('\n'):
        jobobj = parser.process_line(input_line)
        if jobobj:  # Make sure we didn't get None back..
            print json.dumps(jobobj, sort_keys=True, indent=4,
                             default=parser.json_serializer)
