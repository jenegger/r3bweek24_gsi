#!/bin/bash

for file in y_corr_vals_*.txt; do
    if [[ "$file" == *"carbon_target"* ]]; then
        # Extract values for carbon target
        thickness=$(echo "$file" | awk -F'_' '{print $6}')
        energy=$(echo "$file" | awk -F'_' '{print $7}' | sed 's/amev//')
        runnumber=$(echo "$file" | awk -F'_' '{print $9"_"$10}' | sed 's/.txt//')

        # Prepend values as a new column to each row
        awk -v t="$thickness" -v e="$energy" -v r="$runnumber" -F',' \
            'BEGIN{OFS=","} {print t, e, r, $0}' "$file" > tmp && mv tmp "$file"

    elif [[ "$file" == *"empty_target"* ]]; then
        # Extract values for empty target
        thickness="empty"
        energy=$(echo "$file" | awk -F'_' '{print $6}' | sed 's/amev//')
        runnumber=$(echo "$file" | awk -F'_' '{print $8"_"$9}' | sed 's/.txt//')

        # Prepend values as a new column to each row
        awk -v t="$thickness" -v e="$energy" -v r="$runnumber" -F',' \
            'BEGIN{OFS=","} {print t, e, r, $0}' "$file" > tmp && mv tmp "$file"
    fi
done

