# Github Archive Hadoop Jobs

Hadoop streaming API jobs written in Python to analyze Github Archive event data

## Data

I’m interested in open source software. I do most of my development with open source tools, and contribute to such projects as I am able. In the last few years GitHub has become one of the most active places to find and release open source projects, and in 2011 they began releasing their public event metadata via the GitHub Archive project: http://www.githubarchive.org/

I have downloaded 3 years of GitHub data, which has the following attributes:

- each file contains one hour of event data in json
- 26275 files totalling 45.5GB gzipped
- 18 event types: http://developer.github.com/v3/activity/events/types/

## Jobs

Run `rake -T` from the project root to display a list of commands. Requires Ruby and Rake.

### 1. Repo Event Count

Tabulate counts and metadata for all repos.

### 2. Language Event Count

Using the results of job 1, tabulate event counts per language.

## License

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <http://unlicense.org/>
