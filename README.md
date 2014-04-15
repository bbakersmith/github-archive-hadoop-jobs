# Github Archive Hadoop Jobs

Hadoop streaming API jobs written in Python to analyze Github Archive event data

## Data

I’m interested in open source software. I do most of my development with open source tools, and contribute to such projects as I am able. In the last few years GitHub has become one of the most active places to find and release open source projects, and in 2011 they began releasing their public event metadata via the GitHub Archive project: http://www.githubarchive.org/

I have downloaded 3 years of GitHub data, which has the following attributes:

- each file contains one hour of event data in json
- 26275 files totalling 45.5GB gzipped
- 18 event types: http://developer.github.com/v3/activity/events/types/

## Jobs

Run `rake -T` from the project root to display a list of commands. 

### 1. Repo Event Count

Tabulate counts and metadata for all repos.

### 2. Language Event Count

Using the results of job 1, tabulate event counts per language.
