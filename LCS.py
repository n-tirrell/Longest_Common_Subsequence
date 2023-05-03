# Nikki Tirrell 
# Longest Common Subsequence
# references:
# Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). Introduction to algorithms (3rd ed.). Cambridge, MA: MIT Press.  
# 

# -- import relevant libraries (not including numpy) --
import sys # allows for getting the input and reading it
import os # allows for interacting with the operating system
import re # used when examining input file
import time # allows for runtime statistic
import decimal # used in calculating and displaying run time

# first the functions are defined

# this function finds the length of the LCS and makes a row-major order table of matches
# this is modeled after the pseudocode LCS-LENGTH(X,Y)
def find_LCS(s1, s2, m, n):
    # initialize the b and c tables
    b = []
    c = []

    # make a b table with dimensions [1..m][1..n]
    for _ in range(0, m):
        b.append([0] * n)

    # make a c table with dimensions[0..m][0..n]
    for _ in range(0, m):
        c.append([0] * n)

    # populate the tables with the LCS analysis
    for i in range(0, m):
        for j in range(0, n):
            if s1[i] == s2[j]:
                c[i][j] = c[i-1][j-1] + 1
                b[i][j] = "^<" # represents diagonal arrow pointing to the top left corner
            elif c[i-1][j] >= c[i][j-1]:
                c[i][j] = c[i-1][j]
                b[i][j] = "^ " # represents the arrow pointing up
            else:
                c[i][j] = c[i][j-1]
                b[i][j] = "<-" # represents the arrow pointing to the left

    return b, c # return populated tables

# this function takes in the b table of arrows, one input string, indices of b, and the output file path
# this directly writes the LCS to the output file rather than compiling the LCS in a variable then writing it to output
# this reduces the storage cost of the program
# this is modeled after the PRINT-LCS pseudocode
def print_LCS(b, s1, i, j, LCS_length, comparison_count, output_file):
    if i == 0 or j == 0: # we have reached the end of the string, no more common bases
        return LCS_length, comparison_count # end the function

    # use the arrows to determine which base we print
    if b[i][j] == "^<":
        comparison_count += 1 # count comparison
        LCS_length, comparison_count = print_LCS(b, s1, i-1, j-1, LCS_length + 1, comparison_count, output_file)
        output_file.write("{0}" .format(s1[i]))
    elif b[i][j] == "^ ":
        comparison_count += 1
        LCS_length, comparison_count = print_LCS(b, s1, i-1, j, LCS_length, comparison_count, output_file)
    else:
        comparison_count += 1
        LCS_length, comparison_count = print_LCS(b, s1, i, j-1, LCS_length, comparison_count, output_file)
        

    return LCS_length, comparison_count # returns the length of the LCS and the count of comparisons

# this will print the two strands given an output file path
def print_comparison_info(i, j, s1, s2,output_file):
    
    output_file.write("\n --------------- \n")
    output_file.write("Strand {0}: \n{1}" .format(str(i + 1), s1)) # account for zero-indexing of strands
    output_file.write("\nStrand {0}: \n{1}" .format(str(j + 1), s2))
    output_file.write("\nLCS: \n")
    return 

# this will format the b and c matrices for writing to output
def print_matrix(matrix, m, n, output_file):

    for i in range(m):
        for j in range(n):
            output_file.write("\t {0}" .format(str(matrix[i][j])))
        output_file.write("\n")
    
    return


# this will print the data and statistics of the comparison
def print_comparison_data(i, j, b, c, m, n, runtime, LCS_length, comparison_count, output_file):
    output_file.write("\n-- Strand Comparison Statistics -- \n")
    output_file.write("Strand {0} length \t Strand {1} length \t LCS length \t Comparisons \t LCS Percent of Strand {0} \t LCS Percent of Strand {1} \t Runtime" .format(i+1, j+1))
    output_file.write("\n {0} bp \t\t {1} bp \t\t {2} bp \t\t {3} \t\t\t {4:.4}% \t\t\t\t {5:.4}% \t\t\t\t {6:.8} ms" .format(m, n, LCS_length, comparison_count, (LCS_length/m * 100), (LCS_length/n*100), str(runtime)))
    output_file.write("\n\n--Construction Tables -- \n" )
    output_file.write("\nb table: \n")
    print_matrix(b, m, n, output_file)
    output_file.write("\nc table: \n")
    print_matrix(c, m, n, output_file)
    return

# this is the master function to facilitate the program
def run_LCS(i, j, s1, s2, output_file):

    time_start = time.time() # start timing for runtime

    m = len(s1)
    n = len(s2)
    # initialize variables
    LCS_length = 0 # need a counter for the LCS length since LCS is not saved to a string that we can find the length of
    comparison_count = 0
    
    b, c = find_LCS(s1, s2, m, n) # get LCS data

    print_comparison_info(i, j, s1, s2, output_file) # write the first lines of the comparison to output
    LCS_length, comparison_count = print_LCS(b, s1, m-1, n-1, LCS_length, comparison_count, output_file) # write the LCS to output, get length data

    time_end = time.time()
    runtime = decimal.Decimal(time_end - time_start) * 1000

    print_comparison_data(i, j, b, c, m, n, runtime, LCS_length, comparison_count, output_file) # print comparison information

   

# now the functions have been defined

if __name__ == '__main__':

    # -- get input file and check error cases --

    # get input file from commandline
    args = sys.argv # this makes an array of two strings in the format ['file/path of this script' 'file/path of the input file'] so the input is args[1]

    # error checking: make sure that one input file and one output file has been entered
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
            
            # initialize variables to store strand info
            strandArray = []

            # get the input data
            # only want the lines with numbers in them
            for line in input_file:
                if len(line.strip()) < 1:
                    continue # skip empty line
                else: # the line contains strand information
                    # get strand information
                    strand_info = line.split("=") # splits strand between its label and the sequence
                    strand = strand_info[1].upper() # make strand uppercase for easier handling
                    strand = strand.strip()

                    # error check the strand to make sure it is acceptable
                    if re.search(r"[\d]+", strand): # if the sequence has numbers in it
                        print("Error: number in strand: \n" + strand)
                        continue
                    if re.search(r"[^ACGT]+", strand): # if the sequence has letters other than A, C, T, G
                        print("Error: unacceptable letter in strand: \n" + strand)
                        continue
                    strandArray.append(strand) # append strand to array of strands 
            
            print("the strands are" + strandArray)
            print("this should print")
            # count strands for output file
            strand_counter = len(strandArray) 

            # last error check: make sure there are enough strands for comparison
            if strand_counter < 2:
                print("Error: input file must contain two or more acceptable strands for comparison.")
                sys.exit(1)

            # now we know that the input is acceptable        
           
            # first save the input data to the output file
            output_file.write("---------------- \n")
            output_file.write("Input Data:")
            output_file.write("\nN = {0} strands" .format(str(strand_counter)))
            output_file.write("\nInput strands:\n")
            
            for i in range(strand_counter):
                output_file.write("Stand {0}: {1}\n" .format(str(i + 1), strandArray[i]))

            # now do the functionality
            # compare two strings at a time
            for i in range(0, strand_counter-1):
                for j in range(i+1, strand_counter): # don't want to repeat comparisons
                    run_LCS(i, j, strandArray[i], strandArray[j], output_file) # find LCS on each combination of strands
