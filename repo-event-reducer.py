#!/usr/bin/env python
import sys
import urllib2


# tally event counts per repo
repo_event_counts = {}

# lookup table for event keys
event_keys = {
    'CommitCommentEvent': 0,
    'CreateEvent': 1,
    'DeleteEvent': 2,
    'DeploymentEvent': 3,
    'DeploymentStatusEvent': 4,
    'DownloadEvent': 5,
    'FollowEvent': 6,
    'ForkEvent': 7,
    'ForkApplyEvent': 8,
    'GistEvent': 9,
    'GollumEvent': 10,
    'IssueCommentEvent': 11,
    'IssuesEvent': 12,
    'MemberEvent': 13,
    'PageBuildEvent': 14,
    'PublicEvent': 15,
    'PullRequestEvent': 16,
    'PullRequestReviewCommentEvent': 17,
    'PushEvent': 18,
    'ReleaseEvent': 19,
    'StatusEvent': 20,
    'TeamAddEvent': 21,
    'WatchEvent': 22
}

event_template = [0] * 23


for line in sys.stdin:

  cleanline = line.strip()
  repo_id, repo_name, event_type = cleanline.split('\t', 2)

  if repo_id not in repo_event_counts:
    repo_event_counts[repo_id] = list(event_template)

  repo_event_counts[repo_id][event_keys[event_type]] += 1


for id, event_counts in repo_event_counts.iteritems():

  all_counts = '\t'.join(str(c) for c in event_counts)

  print '\t'.join([id, repo_name, all_counts])
