
#!/bin/bash

# Setting IFS (input field separator) value as ","
IFS=','

# Reading the split string into task
read -ra tasks <<< "$TASKS"

# Print each value of the array by using the loop
for task in "${tasks[@]}";
do
  # Trim whitespaces from string
  task=$(tr -d ' ' <<< "$task")
  if [[ ("$task" =~ ^task_[1-9]?[0-9] && (-f "./src/$task/main.py")) ]]; then
  # Execute main file present
    python "./src/$task/main.py"
  fi
done
