#!/usr/bin/python3

# counter for vampire
count = 0

# open the file for reading
read_file = open("dracula.txt", "r")

# loop over the read_file
for line in read_file:

    # if the word 'vampire' appears in the line...
    if "vampire" in line.lower():
        count += 1 # increment count
        #print(count) # display count
        print(line) # display line

        # open the file for writing
        write_file = open("vampire.txt", "a")

        # write line to the write_file
        write_file.write(line)

read_file.close()
write_file.close()
