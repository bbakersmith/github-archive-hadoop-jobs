#!/usr/bin/env python
import sys
import json


for line in sys.stdin:
  cleanline = line.strip()

  try:
    event = json.loads(line)
    repo = event['repository']

    repo_id = str(repo['id'])
    repo_fullname = '%s/%s' % (repo['owner'], repo['name'])

    # sometimes repos don't have a language defined
    if 'language' not in repo:
      repo['language'] = 'unknown'

  except:
    # ignore bad input
    continue

  print '\t'.join([
    repo_id,
    repo_fullname,
    repo['language'], 
    event['type']])
