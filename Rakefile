HADOOP_ROOT = "/home/ben/projects/roosevelt/312/hadoop-1.2.1"
BASIC_HADOOP_TASK = "#{HADOOP_ROOT}/bin/hadoop jar #{HADOOP_ROOT}/contrib/streaming/hadoop-streaming-1.2.1.jar -jobconf mapred.reduce.tasks=1"

namespace :run do

  task :event_count do
    cmd = [
      BASIC_HADOOP_TASK,
      "-file ./event-count-mapper.py",
      "-file ./event-count-reducer.py",
      "-mapper event-count-mapper.py",
      "-reducer event-count-reducer.py",
      "-input ./2014-02-28-20.json",
      "-output event-count-output"
    ].join(' ')
    system cmd
  end

end
