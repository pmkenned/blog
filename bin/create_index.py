#!/usr/bin/env python3

import sys
import re
import os
import subprocess

def to_date_str(seconds):
    return subprocess.run(["date", "-d", "@%s" % seconds, '+%e %b %Y'], capture_output=True, text=True).stdout.rstrip()

def get_posts(md_files):

    posts = list()
    for f in md_files:
        h1 = subprocess.run(["grep", "-m1", "^# ", f], capture_output=True, text=True).stdout
        title = re.sub(r'(^# *|\n)', '', h1)
        href = re.sub(r'\.md$', '.html', f)
        href = re.sub(r'.*/', '', href)
        timestamp = subprocess.run(["grep", "-oP", "(?<=TIMESTAMP:) *\d+", f], capture_output=True, text=True).stdout
        assert timestamp != ""
        posts.append({'href': href, 'title': title, 'timestamp': timestamp})

    posts = sorted(posts, key=lambda x: x['timestamp'], reverse=True)

    return posts

if __name__ == "__main__":

    #md_files = [f for f in os.listdir() if f.endswith(".md")]
    md_files = sys.argv[2:]
    posts = get_posts(md_files)

    #with open('index_template.html', 'r') as fh:
    with open(sys.argv[1], 'r') as fh:
        lines = fh.readlines()

    #with open('index.html', 'w') as fh:
    fh = sys.stdout
    for line in lines:
        if re.match(r'^ *<!-- *POSTS *--> *$', line):
            fh.write('        <ul class="no_bullet">\n')
            for post in posts:
                date_str = to_date_str(post['timestamp'])
                fh.write('            <li>%s: <a href="%s">%s</a></li>\n' % (date_str, post['href'], post['title']))
            fh.write('        </ul>\n')
        else:
            fh.write(line)
