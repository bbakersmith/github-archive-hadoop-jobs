#!/usr/bin/env python
import sys
import json


# tally event counts per language
languages = {}


for line in sys.stdin:
  cleanline = line.strip()
  language, events_json = cleanline.split('\t')
  events = json.loads(events_json)

  if language not in languages:
    languages[language] = {
      'events': events
    }

  else:
    for event, count in events.iteritems():
      if event not in languages[language]['events']:
        languages[language]['events'][event] = count

      else:
        languages[language]['events'][event] += count


print json.dumps(languages)
