#!/usr/bin/env python
import sys
import json


for line in sys.stdin:

  cleanline = line.strip()

  try:
    event = json.loads(line)
  except:
    # ignore bad input
    continue

  event_type = event['type']
  repo_id = event['repository']['id']

  print '%s\t%s' % (repo_id, event_type)
