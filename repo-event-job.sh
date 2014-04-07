#!/bin/env/bash

hadoop jar $HADOOP_ROOT/contrib/streaming/hadoop-streaming-1.2.1.jar -jobconf mapred.reduce.tasks=1 -file ./repo-event-mapper.py -file ./repo-event-reducer.py -mapper repo-event-mapper.py -reducer repo-event-reducer.py -input ./2014-02-28-20.json -output repo-event-output
