#!/usr/bin/env python
import sys
import json


# tally event counts per repo
repos = {}


for line in sys.stdin:
  cleanline = line.strip()
  actor, repo_id, repo_language, event_type = cleanline.split('\t')

  if repo_id not in repos:
    repos[repo_id] = {
      'id': repo_id,
      'language': repo_language,
      'events': {event_type: [actor]}
    }

  else:
    if event_type not in repos[repo_id]['events']:
      repos[repo_id]['events'][event_type] = [actor]

    else:
      repos[repo_id]['events'][event_type].append(actor)


for id, data in repos.iteritems():
  print json.dumps(data)
