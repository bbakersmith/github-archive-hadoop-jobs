HADOOP_ROOT = "/home/ben/projects/roosevelt/312/hadoop-1.2.1"
BASIC_HADOOP_TASK = "#{HADOOP_ROOT}/bin/hadoop jar #{HADOOP_ROOT}/contrib/streaming/hadoop-streaming-1.2.1.jar -jobconf mapred.reduce.tasks=1"

# run tasks with hadoop
namespace :run do

  task :event_count do
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

# run tasks with simple unix pipes
namespace :run_simple do

  task :language_event_count do
    print "Enter path to data file (defaults to 'data/2014-02-28-20.json'): "
    data_file = STDIN.gets.chomp

    if(data_file == '')
      data_file = 'data/2014-02-28-20.json'
    end

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
