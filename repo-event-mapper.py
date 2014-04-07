#!/usr/bin/env python
import sys
import json


# every event response contains the full repo metadata
# which seems very ineficient. probably best to have a separate
# job compile the unique repo list with metadata, then use this as
# a reference for the event counting reducer


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
