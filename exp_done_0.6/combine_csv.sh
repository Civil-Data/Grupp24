#!/bin/bash

output_file="combined_output_0_6.csv"

for file in *.csv; do
    echo "Filename: $file" >> "$output_file"
    
    cat "$file" >> "$output_file"
    
    #Newline
    echo "" >> "$output_file"
done

echo "done"
