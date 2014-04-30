#!/usr/bin/env python
import sys
import json


for line in sys.stdin:
  cleanline = line.strip()

  # try:
  repo = json.loads(line)
  repo_id = repo['id']
  language = repo['language']
  events = repo['events']
  event_stats = {}

  for event, contents in events.iteritems():
    event_count = len(events[event])
    unique_actors = list(set(events[event]))
    actors_count = len(unique_actors)

    event_stats[event] = {
      'count': event_count,
      'actors_count': actors_count,
      'actors': unique_actors
    }

  event_stats = json.dumps(event_stats)

  # except:
  #   # ignore bad input
  #   continue

  print '\t'.join([
    repo_id,
    language,
    event_stats])
