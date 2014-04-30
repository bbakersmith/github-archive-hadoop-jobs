#!/usr/bin/env python
import sys
import json


# tally event counts per language
languages = {}


for line in sys.stdin:
  cleanline = line.strip()
  repo, language, events_json = cleanline.split('\t')
  events = json.loads(events_json)

  if language not in languages:
    languages[language] = {
      'events': {},
      'repos': set([repo]),
      'actors': set([])
    }

  else:
    languages[language]['repos'].add(repo)

  for event, contents in events.iteritems():
    count = contents['count']
    actors_count = contents['actors_count']
    new_actors = languages[language]['actors'].union(contents['actors'])
    languages[language]['actors'] = new_actors

    if event not in languages[language]['events']:
      languages[language]['events'][event] = {
        'count': count,
        'actors_count': actors_count
      }

    else:
      new_c = languages[language]['events'][event]['count'] + count
      new_ac = languages[language]['events'][event]['actors_count'] + actors_count
      languages[language]['events'][event] = {
        'count': new_c,
        'actors_count': new_ac
      }


for language, details in languages.iteritems():
  repo_count = len(details['repos'])
  languages[language]['repos'] = repo_count

  actor_count = len(details['actors'])
  languages[language]['actors'] = actor_count


print json.dumps(languages)
