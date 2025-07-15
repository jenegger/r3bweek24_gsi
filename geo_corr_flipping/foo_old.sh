#!/bin/bash

for xfile in x_corr_vals_carbon_target_*.txt; do
    # Build the corresponding y file
    base=${xfile#x_corr_vals_}
    yfile="y_corr_vals_$base"

    # Check if matching y file exists
    if [[ -f "$yfile" ]]; then
		if [ $(echo "$base" | awk -F'_' '{print $1}') = "carbon" ];then
			echo "corrrecccccctt"
		fi
        # Extract metadata from filename
        thickness=$(echo "$base" | awk -F'_' '{print $3}')
        energy=$(echo "$base" | awk -F'_' '{print $4}' | sed 's/amev//')
        runnumber=$(echo "$base" | awk -F'_' '{print $6"_"$7}' | sed 's/.txt//')

        # Output file name
        outfile="combined_column2_${base}"

        # Combine only column 2 of both files
        paste "$xfile" "$yfile" | awk -v t="$thickness" -v e="$energy" -v r="$runnumber" -F'\t' '
        BEGIN { OFS="," }
        {
            split($1, x, ",")
            split($2, y, ",")
            print t, e, r, x[2], y[2]
        }' > "$outfile"

        echo "Created $outfile"
    else
        echo "No matching y file for $xfile"
    fi
done

