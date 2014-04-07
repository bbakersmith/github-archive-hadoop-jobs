#!/usr/bin/env python
import sys
import json


for line in sys.stdin:

  cleanline = line.strip()

  try:
    event = json.loads(line)

    event_type = event['type']
    repo_id = event['repository']['id']
    repo_owner = event['repository']['owner']
    repo_name = event['repository']['name']

  except:
    # ignore bad input
    continue

  print '%s\t%s/%s\t%s' % (repo_id, repo_owner, repo_name, event_type)
