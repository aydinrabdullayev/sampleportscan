# Scrypt to test ip reachability via port
import subprocess
import csv

with open("iplist.csv", "r") as csvfile:
    csvreader = csv.reader(csvfile)

    # This skips the first row of the CSV file.
    next(csvreader)
    #
    for row in csvreader:
        # do stuff with rows...

        # subprocess.call(["nc", "-zv", "142.251.36.78", "443", "-w", "5"])#, stdout=f)
        subprocess.call(["nc", "-zv", str(row[0]), str(row[1]), "-w", "5"])  # , stdout=f)
        #print(f)
        # print(row[0]+" port "+row[1])