#!/usr/bin/python3
import sys
from collections import defaultdict

total_size = 0
status_counts = defaultdict(int)
line_count = 0

try:
    for line in sys.stdin:
        # parse line
        parts = line.split()
        status_code = parts[3]
        file_size = int(parts[4])

        # update metrics
        total_size += file_size
        status_counts[status_code] += 1
        line_count += 1

        # print metrics every 10 lines
        if line_count % 10 == 0:
            print(f"Total file size: {total_size}")
            for status_code in sorted(status_counts.keys()):
                print(f"{status_code}: {status_counts[status_code]}")

except KeyboardInterrupt:
    # print final metrics on keyboard interruption
    print(f"Total file size: {total_size}")
    for status_code in sorted(status_counts.keys()):
        print(f"{status_code}: {status_counts[status_code]}")

