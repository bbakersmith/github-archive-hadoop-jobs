#!/usr/bin/env python
import sys
import json


# tally event counts per repo
repos = {}


for line in sys.stdin:
  cleanline = line.strip()
  repo_id, repo_fullname, repo_language, event_type = cleanline.split('\t')

  if repo_id not in repos:
    repos[repo_id] = {
      'name': repo_fullname,
      'language': repo_language,
      'events': {event_type: 1}
    }

  else:
    if event_type not in repos[repo_id]['events']:
      repos[repo_id]['events'][event_type] = 1

    else:
      repos[repo_id]['events'][event_type] += 1


for id, event_counts in repos.iteritems():
  print json.dumps(repos)
