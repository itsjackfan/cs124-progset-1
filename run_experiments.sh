#!/bin/bash

# Compile the C++ code (assuming you have a Makefile)
make clean
make

# Number of trials per n value
num_trials="$1"

# Output file
output_file="results.txt"

# Clear output file
> "$output_file"

# Graph types to run
graph_types=("complete" "hypercube" "complete2d" "complete3d" "complete4d")

# Common n values
n_values_complete=(128 256 512 1024 2048 4096 8192 16384 32768)
n_values_hypercube=(128 256 512 1024 2048 4096 8192 16384 32768 65536 131072 262144)

# Run experiments for each graph type
for graph_type in "${graph_types[@]}"; do
  if [ "$graph_type" == "complete" ]; then
      n_values=("${n_values_complete[@]}")
      dimension=0
  elif [ "$graph_type" == "hypercube" ]; then
      n_values=("${n_values_hypercube[@]}")
      dimension=1
  elif [ "$graph_type" == "complete2d" ]; then
      n_values=("${n_values_complete[@]}")
      dimension=2
  elif [ "$graph_type" == "complete3d" ]; then
      n_values=("${n_values_complete[@]}")
      dimension=3
  elif [ "$graph_type" == "complete4d" ]; then
      n_values=("${n_values_complete[@]}")
      dimension=4
  else
      echo "Invalid graph type: $graph_type"
      continue  # Skip to the next graph type
  fi

  echo "Running experiments for graph type: $graph_type"

  for n in "${n_values[@]}"; do
    echo "  - Running n = $n"
    ./randmst "$graph_type" "$n" "$num_trials" "$dimension" >> "$output_file"
  done
done

echo "All experiments completed. Results in $output_file"