#!/usr/bin/env python3

import sys
import re

def do_file(fn):
    with open(fn, 'r') as fh:
        data = fh.read()
        lines =data.split("\n")
        for line in lines:
            m = re.search(r"<!--\s*include\s+'(?P<include_filename>[\w\-\.]+)'.*-->", line)
            m2 = re.search(r"<!--\s*include\s+\$(?P<include_number>\d+).*-->", line)
            m3 = re.search(r"<!--\s*\$(?P<variable>[a-zA-Z_]\w+).*-->", line)
            if m:
                include_filename = m.groupdict()['include_filename']
                do_file(include_filename)
            elif m2:
                include_number   = int(m2.groupdict()['include_number'])
                argv_idx = include_number+1 # $1 -> argv[2]
                if argv_idx > argc-1:
                    sys.stderr.write("error: tried to include $%d file but only provided %d parameters\n" % (include_number, argc-1))
                    exit(1)
                include_filename = sys.argv[argv_idx]
                do_file(include_filename)
            elif m3:
                variable = m3.groupdict()['variable']
                # TODO: print warning
                print(defines.get(variable, ""))
            else:
                print(line)

if __name__ == "__main__":

    argc = len(sys.argv)

    if (argc < 2):
        sys.stderr.write('usage: %s [FILE]\n' % sys.argv[0])
        exit()

    fn = sys.argv[1]

    defines = dict()

    for arg in sys.argv:
        m = re.match(r'-D(?P<key>[a-zA-Z_]\w+)=(?P<value>.*)', arg)
        if m:
            key = m.groupdict()['key']
            value = m.groupdict()['value']
            defines[key] = value

    do_file(fn)
