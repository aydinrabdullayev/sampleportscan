# Scrypt to test ip reachability via port
import subprocess
import csv

with open("iplist.csv", "r") as csvfile:
    csvreader = csv.reader(csvfile)

    # This skips the first row of the CSV file.
    next(csvreader)
    #
    for row in csvreader:

        # subprocess.call(["nc", "-zv", "142.251.36.78", "443", "-w", "5"])#, stdout=f)
        # it will do nc -zv ip port -w 5 (wait for 5 second) if network is high latency please put 15 seconds
        subprocess.call(["nc", "-zv", str(row[0]), str(row[1]), "-w", "5"])  # , stdout=f)

#will filter output in future for now it will spit into the concole