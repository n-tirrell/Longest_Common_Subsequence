# Nikki Tirrell Programming Project 2
# references:
# Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). Introduction to algorithms (3rd ed.). Cambridge, MA: MIT Press.  

# -- import relevant libraries (not including numpy) --
import sys # allows for getting the input and reading it
import os # allows for interacting with the operating system
import re # used when examining input file
import math


# this function will be the collision strategies
# inputs are the key value, calculated slot, current hash table and collision strategy
# specify strategy- 1 for linear probing, 2 for quadratic probing, 3 for chaining
def handle_collision(key, slot, htable, strategy):
    tsize = len(htable)
    c1, c2 = 0.5, 0.5

    if strategy < 3:  # Linear & Quadratic Probing
        for i in range(0, tsize):
            idx = (key + i)%tsize if strategy == 1 else (key + (c1*i) + (c2*(i**2)))%tsize
            if htable[idx] is None:
                htable[idx] = key
    elif strategy == 3:  # Chaining
        if htable[slot] is None:
            htable[slot] = [key]
        else:
            htable[slot].append(key)
    
    return htable
    
    # continue looking at slots until we find an empty slot or determine that the table is full
    # while htable[j] != None:
    #     j = slot + 1 # the next index after the slot

    #     if strategy == 1: # linear probing
    #         # h'(k) = some method
    #         # i = index
    #         # m = size (12)
    #         j += 1 # keep looking at the next slot until we get an empty slot
        
    #     elif strategy == 2: # quadratic probing
    #         j = 0.5*j + 0.5*j**2
        
    #     #elif strategy == 3: # chaining
        
    #     else: # hash table is full ***************check this*************************
    #         print("Error: hash table is full")

    return j

def hash(size, keys, probe_strategy):

    print(keys)
    print(keys[1])

    slot = None
    htable = [slot] * size
    test_hash = []

    for i in range(0, len(keys)):
        slot = int(keys[i]) % size
        test_hash.append(slot)
    
        # print(test_hash)


        htable = handle_collision(keys[i], slot, htable, probe_strategy)

        # check if collision
        # if htable[slot] == None: # empty slot so add key
        #    htable[slot] = keys[i]
        # else: # slot is occupied so use collision techniques
        #    htable = handle_collision(keys[i], slot, htable, probe_strategy)

    return htable

# input = "1234"
# total = []

# for i in range(0, len(input)):
#     getnums = re.search(r"\d?", input[i])
#     total.append(getnums)


# print(getnums)

# match = getnums.group(2)
# print(match)

input = [12501, 84763, 22599, 55555, 2698, 72501, 99999, 33975, 62501, 42501]

size = int(120)

htable = hash(size, input, 2)  

print(htable)

if __name__ == '__main__':

    # -- get input and check error cases --

    # get input file from commandline
    args = sys.argv # this makes an array of two strings in the format ['file/path of this script' 'file/path of the input file'] so the input is args[1]

    # error checking: make sure that one input file and one output has been entered
    if len(args) < 3:   # this means that there is no input file entered
        print("Error: Please specify your input file name, then your output file name.")
        sys.exit(1) # exit(0) fully ends running the script but exit(1) allows for more command line arguments
    elif len(args) > 3: # this means that more than two files were entered, so there are either multiple input files or multiple output files 
        print("Error: Invalid number of arguments. Check your input file path and output file path for spaces, or try wrapping in quotes.")
        sys.exit(1)

    input_path = args[1] # the file of index 1 in args is the input file

    # error checking: make sure that the input file or input file path exists
    if not os.path.exists(input_path):
        print("Error: The input path specified does not exist.")
        sys.exit(1)

    # error checking: make sure that the input is a file not something else like an application
    if not os.path.isfile(input_path):
        print("Error: The path specified is not a file.")
        sys.exit(1)

    output_path = args[2] # the output file has an index of 2 in args

    # -- get data from input file --
    # input file has all of the keys to put into one hashing table

    # read the input per line into the lines variable
    with open(input_path, 'r') as input_file: # open the input file to be read
        with open(output_path, 'w') as output_file: # open the output file to be written to
            # get the input data
            for line in input_file:
                # the first three lines are not relevant
                if "." in line:
                    continue # skip this line
                elif re.search(r"[A-Za-z]?", line): # if there is a letter in the line
                    continue # skip this line
                elif len(line.strip()) == 0:
                    continue # skip empty line
                else: # the line either contains numbers or is an empty line
                    
                    numArray = []
                    nums = []
                    
                    # save the numbers to an array
                    nums = re.search(r"\d?", line)
                    # there is a line here that I think uses re groups but its taking me too long to determine exact syntax


                    # now the numbers are saved to array
                    numArray.append(nums)
                    # run the numbers through the hashing functions
                    for i in range(1,4):
                        
                        htable = hash(size, input, i) # go through each collision strategy
                        
                        # ---- write the data to the output file (which was already opened) -----

                        # maintain the format of the input file which is order, matrix A, matrix B, newline to separate them with the next set
                        # so the output file is order, matrix A, matrix B, matrix C, newline to separate them with the next set
                        
                        # separate each data set with a label
                        output_file.write("------Data Set:---------- \n")
                        output_file.write("Input Data:\n")
                        output_file.write("Input table size: ")
                        output_file.write("Input keys size: ")
                        write_matrix_to_output("Input Table", output_file, aMatrix)
                        
                        output_file.write("Hashing Schematics:")
                        output_file.write("Modulo: ")
                        output_file.write("Hash table size: ")
                        output_file.write("Bucket Size: ")

                        if i == 1:
                            method = "Linear Probing"
                        elif i == 2:
                            method = "Qudaratic Probing"
                        elif i == 3:
                            method = "Chaining"

                        output_file.write("Collision method:" + method)
                        write_matrix_to_output("Hash Table: ", output_file, aMatrix)
                        output_file.write("Hashing Statistics: ")
                        output_file.write("Number of collisions: ")
                        output_file.write("Number of comparisons: ")
                        output_file.write("Number of uninserted numbers: ")
                        output_file.write("Load factor: ")
                        output_file.write("Runtime: ")