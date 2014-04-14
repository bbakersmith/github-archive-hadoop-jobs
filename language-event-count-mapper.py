#!/usr/bin/env python
import sys
import json


for line in sys.stdin:
  cleanline = line.strip()

  try:
    repo = json.loads(line)
    language = repo['language']
    events = json.dumps(repo['events'])

  except:
    # ignore bad input
    continue

  print '\t'.join([
    language,
    events])
