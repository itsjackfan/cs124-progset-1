#!/bin/bash

# Output file name
output_file="calculations.txt"

# Ensure the output file exists and is empty at the start, or clear it if it exists
> "$output_file"

# Graph types to iterate through (0 to 4)
for graph_type in {0..0}; do
  echo "Running for Graph Type: $graph_type" >> "$output_file"
  echo "-----------------------------------" >> "$output_file"

  # Numpoints values to iterate through (8, 16, 32, 64, 128, 256, 512)
  numpoints=8
  while [ "$numpoints" -le 256 ]; do
    echo "Running for numpoints: $numpoints" >> "$output_file"

    # Execute the mst_weights program and append output to the file
    ./mst_weights 0 "$numpoints" 1000 "$graph_type" >> "$output_file"

    # Double numpoints for the next iteration
    numpoints=$((numpoints * 2))
  done
  echo "" >> "$output_file" # Add an empty line for separation between graph types
done

echo "Script finished. Results written to $output_file"