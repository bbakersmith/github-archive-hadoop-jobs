HADOOP_ROOT = "/home/ben/projects/roosevelt/312/hadoop-1.2.1"
BASIC_HADOOP_TASK = "#{HADOOP_ROOT}/bin/hadoop jar #{HADOOP_ROOT}/contrib/streaming/hadoop-streaming-1.2.1.jar -jobconf mapred.reduce.tasks=1"

# run tasks with hadoop
namespace :run_hadoop do

  desc "Run Repo Event Count job with Hadoop"
  task :repo_event_count do
    cmd = [
      BASIC_HADOOP_TASK,
      "-file ./repo-event-count-mapper.py",
      "-file ./repo-event-count-reducer.py",
      "-mapper repo-event-count-mapper.py",
      "-reducer repo-event-count-reducer.py",
      "-input ./2014-02-28-20.json",
      "-output repo-event-count-output"
    ].join(' ')
    system cmd
  end

end

namespace :run do

  desc "Run Language Event Count job with Unix pipes (no Hadoop)"
  task :language_event_count do

    data_file = 'data/2014-02-28-20.json'
    
    cmd = [
      "cat #{data_file}",
      "python repo-event-count-mapper.py",
      "python repo-event-count-reducer.py",
      "python language-event-count-mapper.py",
      "python language-event-count-reducer.py",
      "python -mjson.tool"
    ].join(' | ')
    system cmd
  end

end
