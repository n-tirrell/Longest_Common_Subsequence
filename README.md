# Longest_Common_Subsequence

This python file compares combination of two DNA strand sequences from an input file. It then prints the comparison and program data to an output file.

## Requirements

Python >= 3.0.0

## Input File

The python file reads an input file that is provided by the user. This file contains the input DNA strand sequences that will be compared. Each strand is on a separate line. The strands do not have to be the same length. The strand sequence must only contain the letters 'A', 'C', 'G', and/or 'T'. Any line containing a number or letter other than those will not be read in as an input strand. 

The strand is specified as "strand label" = "strand sequence."
An example of the input file is shown below:
S1 = AACGGTCTCTCG
S2 = GGGTAGCTCTCTCGGC
S3 = TCTCTCTAGACGACGATAC

Which would give input strands AACGGTCTCTCG, AACGGTCTCTCG, and TCTCTCTAGACGACGATAC.

Every strand in the input file will be read into one array of strands and then combinations of each pair of strands will be compared for their LCS. For a different set of strands, create a different input file. 

## Output File

The python file writes to an output file that you also specify in the commandline. It contains several sections of information. First, it shows the input information, which is the number of strands and the list of strands determined from the input file. Then, the output file shows each strand comparison. Each strand comparison starts with the two strands being compared and their sequences. 

Then, the LCS is printed. After that, the strand comparison statistics are printed. This data is the length of each strand, the length of the LCS, the percent of each strand that the LCS consists of, and the runtime of each comparison. 

Finally, the construction tables b and c that were used to make the LCS are printed. They are printed last since I was unsure if they were significant enough to print, and take up a lot of space in the file. I wanted all of the information about the LCS to be together so the statistics are printed above the tables even though chronologically the tables are made first. The tables are printed according to the dimensions of the tables, so there are m columns and n rows where m is the length of strand A and n is the length of strand B.

The format of the output file for one comparisonof two strands is shown in the example below:
---------------- 
Input Data:
N = 4 strands
Input strands:
Stand 1: ACCGGTCGACTGCGCGGAAGCCGGCCGAA
Stand 2: GTCGTTCGGAATGCCGTTGCTCTGTAAA
Stand 3: ATTGCATTGCATGGGCGCGATGCATTTGGTTAATTCCTCG
Stand 4: CTTGCTTAAATGTGCA

 --------------- 
Strand 1: 
ACCGGTCGACTGCGCGGAAGCCGGCCGAA
Strand 2: 
GTCGTTCGGAATGCCGTTGCTCTGTAAA
LCS: 
CGCGGAAGCCGGCCGAA
-- Strand Comparison Statistics -- 
Strand 1 length 	 Strand 2 length 	 LCS length 	 Comparisons 	 LCS Percent of Strand 1 	 LCS Percent of Strand 2 	 Runtime
 29 bp 		 28 bp 		 17 bp 		 27 			 58.62% 				 60.71% 				 0.998020 ms

--Construction Tables -- 

b table: 
	 ^ 	 ^ 	 ^ 	 ^ 	 ^ 	 ^ 	 ^ 	 ^ 	 ^ 	 ^<	 ^<	 <-	 <-	 <-	 <-	 <-	 <-	 <-	 <-	 <-	 <-	 <-	 <-	 <-	 <-	 ^<	 ^<	 ^<
	 ^ 	 ^ 	 ^<	 <-	 <-	 <-	 ^<	 <-	 <-	 ^ 	 ^ 	 ^ 	 ^ 	 ^<	 ^<	 <-	 <-	 <-	 <-	 ^<	 <-	 ^<	 <-	 <-	 <-	 <-	 <-	 <-
	 ^ 	 ^ 	 ^<	 ^ 	 ^ 	 ^ 	 ^<	 <-	 <-	 <-	 <-	 <-	 <-	 ^<	 ^<	 <-	 <-	 <-	 <-	 ^<	 <-	 ^<	 <-	 <-	 <-	 <-	 <-	 <-
	 ^<	 <-	 <-	 ^<	 <-	 <-	 ^ 	 ^<	 ^<	 <-	 <-	 <-	 ^<	 <-	 ^ 	 ^<	 <-	 <-	 ^<	 <-	 <-	 <-	 <-	 ^<	 <-	 <-	 <-	 <-
	 ^<	 <-	 <-	 ^<	 <-	 <-	 <-	 ^<	 ^<	 <-	 <-	 <-	 ^<	 <-	 <-	 ^<	 ^ 	 ^ 	 ^<	 <-	 <-	 <-	 <-	 ^<	 <-	 <-	 <-	 <-
	 ^ 	 ^<	 <-	 <-	 ^<	 ^<	 <-	 <-	 <-	 <-	 <-	 ^<	 <-	 <-	 <-	 <-	 ^<	 ^<	 ^ 	 ^ 	 ^<	 <-	 ^<	 <-	 ^<	 <-	 <-	 <-
	 ^ 	 ^ 	 ^<	 <-	 <-	 <-	 ^<	 <-	 <-	 <-	 <-	 <-	 <-	 ^<	 ^<	 <-	 <-	 <-	 <-	 ^<	 ^ 	 ^<	 <-	 <-	 <-	 <-	 <-	 <-
	 ^<	 <-	 <-	 ^<	 <-	 <-	 <-	 ^<	 ^<	 <-	 <-	 <-	 ^<	 <-	 <-	 ^<	 <-	 <-	 ^<	 <-	 <-	 ^ 	 ^ 	 ^<	 <-	 <-	 <-	 <-
	 ^ 	 ^ 	 ^ 	 ^ 	 ^ 	 ^ 	 ^ 	 ^ 	 ^ 	 ^<	 ^<	 <-	 <-	 <-	 <-	 <-	 <-	 <-	 <-	 <-	 <-	 <-	 <-	 <-	 <-	 ^<	 ^<	 ^<
	 ^ 	 ^ 	 ^<	 <-	 <-	 <-	 ^<	 <-	 <-	 ^ 	 ^ 	 ^ 	 ^ 	 ^<	 ^<	 <-	 <-	 <-	 <-	 ^<	 <-	 ^<	 <-	 <-	 <-	 <-	 <-	 <-
	 ^ 	 ^<	 ^ 	 ^ 	 ^<	 ^<	 <-	 <-	 <-	 <-	 <-	 ^<	 <-	 ^ 	 ^ 	 ^ 	 ^<	 ^<	 <-	 <-	 ^<	 <-	 ^<	 <-	 ^<	 <-	 <-	 <-
	 ^<	 <-	 <-	 ^<	 ^ 	 ^ 	 ^ 	 ^<	 ^<	 <-	 <-	 <-	 ^<	 <-	 <-	 ^<	 ^ 	 ^ 	 ^<	 <-	 <-	 <-	 <-	 ^<	 <-	 <-	 <-	 <-
	 ^ 	 ^ 	 ^<	 <-	 <-	 <-	 ^<	 ^ 	 ^ 	 ^ 	 ^ 	 ^ 	 ^ 	 ^<	 ^<	 <-	 <-	 <-	 ^ 	 ^<	 <-	 ^<	 <-	 <-	 <-	 <-	 <-	 <-
	 ^<	 <-	 <-	 ^<	 <-	 <-	 <-	 ^<	 ^<	 <-	 <-	 <-	 ^<	 ^ 	 ^ 	 ^<	 <-	 <-	 ^<	 ^ 	 ^ 	 ^ 	 ^ 	 ^<	 <-	 <-	 <-	 <-
	 ^ 	 ^ 	 ^<	 <-	 <-	 <-	 ^<	 <-	 <-	 <-	 <-	 <-	 <-	 ^<	 ^<	 ^ 	 ^ 	 ^ 	 ^ 	 ^<	 <-	 ^<	 <-	 ^ 	 ^ 	 ^ 	 ^ 	 ^ 
	 ^<	 <-	 ^ 	 ^<	 <-	 <-	 <-	 ^<	 ^<	 <-	 <-	 <-	 ^<	 <-	 <-	 ^<	 <-	 <-	 ^<	 ^ 	 ^ 	 ^ 	 ^ 	 ^<	 <-	 <-	 <-	 <-
	 ^<	 <-	 <-	 ^<	 ^ 	 ^ 	 ^ 	 ^<	 ^<	 <-	 <-	 <-	 ^<	 <-	 <-	 ^<	 <-	 <-	 ^<	 <-	 <-	 <-	 <-	 ^<	 ^ 	 ^ 	 ^ 	 ^ 
	 ^ 	 ^ 	 ^ 	 ^ 	 ^ 	 ^ 	 ^ 	 ^ 	 ^ 	 ^<	 ^<	 <-	 <-	 <-	 <-	 <-	 <-	 <-	 <-	 <-	 <-	 <-	 <-	 <-	 <-	 ^<	 ^<	 ^<
	 ^ 	 ^ 	 ^ 	 ^ 	 ^ 	 ^ 	 ^ 	 ^ 	 ^ 	 ^<	 ^<	 <-	 <-	 <-	 <-	 <-	 <-	 <-	 <-	 <-	 <-	 <-	 <-	 <-	 <-	 ^<	 ^<	 ^<
	 ^<	 <-	 <-	 ^<	 <-	 <-	 <-	 ^<	 ^<	 ^ 	 ^ 	 ^ 	 ^<	 <-	 <-	 ^<	 <-	 <-	 ^<	 <-	 <-	 <-	 <-	 ^<	 <-	 <-	 <-	 <-
	 ^ 	 ^ 	 ^<	 <-	 <-	 <-	 ^<	 <-	 ^ 	 ^ 	 ^ 	 ^ 	 ^ 	 ^<	 ^<	 <-	 <-	 <-	 <-	 ^<	 <-	 ^<	 <-	 <-	 <-	 <-	 <-	 <-
	 ^ 	 ^ 	 ^<	 ^ 	 ^ 	 ^ 	 ^<	 <-	 <-	 <-	 <-	 <-	 ^ 	 ^<	 ^<	 <-	 <-	 <-	 <-	 ^<	 <-	 ^<	 <-	 <-	 <-	 <-	 <-	 <-
	 ^<	 <-	 <-	 ^<	 <-	 <-	 ^ 	 ^<	 ^<	 <-	 <-	 <-	 ^<	 ^ 	 ^ 	 ^<	 <-	 <-	 ^<	 <-	 <-	 <-	 <-	 ^<	 <-	 <-	 <-	 <-
	 ^<	 <-	 <-	 ^<	 <-	 <-	 <-	 ^<	 ^<	 <-	 <-	 <-	 ^<	 <-	 ^ 	 ^<	 ^ 	 ^ 	 ^<	 <-	 <-	 <-	 <-	 ^<	 <-	 <-	 <-	 <-
	 ^ 	 ^ 	 ^<	 <-	 <-	 <-	 ^<	 <-	 <-	 <-	 <-	 <-	 <-	 ^<	 ^<	 ^ 	 ^ 	 ^ 	 ^ 	 ^<	 <-	 ^<	 <-	 <-	 <-	 <-	 <-	 <-
	 ^ 	 ^ 	 ^<	 ^ 	 ^ 	 ^ 	 ^<	 <-	 <-	 <-	 <-	 <-	 <-	 ^<	 ^<	 <-	 <-	 <-	 ^ 	 ^<	 ^ 	 ^<	 <-	 <-	 <-	 <-	 <-	 <-
	 ^<	 <-	 <-	 ^<	 <-	 <-	 ^ 	 ^<	 ^<	 <-	 <-	 <-	 ^<	 <-	 <-	 ^<	 <-	 <-	 ^<	 ^ 	 ^ 	 ^ 	 ^ 	 ^<	 <-	 <-	 <-	 <-
	 ^ 	 ^ 	 ^ 	 <-	 <-	 <-	 <-	 ^ 	 ^ 	 ^<	 ^<	 <-	 <-	 <-	 <-	 <-	 <-	 <-	 <-	 <-	 <-	 <-	 <-	 <-	 <-	 ^<	 ^<	 ^<
	 ^ 	 ^ 	 ^ 	 ^ 	 ^ 	 ^ 	 ^ 	 ^ 	 ^ 	 ^<	 ^<	 <-	 <-	 <-	 <-	 <-	 <-	 <-	 <-	 <-	 <-	 <-	 <-	 <-	 <-	 ^<	 ^<	 ^<

c table: 
	 0	 0	 0	 0	 0	 0	 0	 0	 0	 1	 1	 1	 1	 1	 1	 1	 1	 1	 1	 1	 1	 1	 1	 1	 1	 1	 1	 1
	 0	 0	 1	 1	 1	 1	 1	 1	 1	 1	 1	 1	 1	 2	 2	 2	 2	 2	 2	 2	 2	 2	 2	 2	 2	 2	 2	 2
	 0	 0	 1	 1	 1	 1	 2	 2	 2	 2	 2	 2	 2	 2	 3	 3	 3	 3	 3	 3	 3	 3	 3	 3	 3	 3	 3	 3
	 4	 4	 4	 2	 2	 2	 2	 3	 3	 3	 3	 3	 3	 3	 3	 4	 4	 4	 4	 4	 4	 4	 4	 4	 4	 4	 4	 4
	 5	 5	 5	 5	 5	 5	 5	 3	 4	 4	 4	 4	 4	 4	 4	 4	 4	 4	 5	 5	 5	 5	 5	 5	 5	 5	 5	 5
	 5	 6	 6	 6	 6	 6	 6	 6	 6	 6	 6	 5	 5	 5	 5	 5	 5	 5	 5	 5	 6	 6	 6	 6	 6	 6	 6	 6
	 5	 6	 7	 7	 7	 7	 7	 7	 7	 7	 7	 7	 7	 6	 6	 6	 6	 6	 6	 6	 6	 7	 7	 7	 7	 7	 7	 7
	 8	 8	 8	 8	 8	 8	 8	 8	 8	 8	 8	 8	 8	 8	 8	 7	 7	 7	 7	 7	 7	 7	 7	 8	 8	 8	 8	 8
	 8	 8	 8	 8	 8	 8	 8	 8	 8	 9	 9	 9	 9	 9	 9	 9	 9	 9	 9	 9	 9	 9	 9	 9	 9	 9	 9	 9
	 8	 8	 9	 9	 9	 9	 9	 9	 9	 9	 9	 9	 9	 10	 10	 10	 10	 10	 10	 10	 10	 10	 10	 10	 10	 10	 10	 10
	 8	 9	 9	 9	 10	 10	 10	 10	 10	 10	 10	 10	 10	 10	 10	 10	 11	 11	 11	 11	 11	 11	 11	 11	 11	 11	 11	 11
	 12	 12	 12	 10	 10	 10	 10	 11	 11	 11	 11	 11	 11	 11	 11	 11	 11	 11	 12	 12	 12	 12	 12	 12	 12	 12	 12	 12
	 12	 12	 13	 13	 13	 13	 11	 11	 11	 11	 11	 11	 11	 12	 12	 12	 12	 12	 12	 13	 13	 13	 13	 13	 13	 13	 13	 13
	 14	 14	 14	 14	 14	 14	 14	 12	 12	 12	 12	 12	 12	 12	 12	 13	 13	 13	 13	 13	 13	 13	 13	 14	 14	 14	 14	 14
	 14	 14	 15	 15	 15	 15	 15	 15	 15	 15	 15	 15	 15	 13	 13	 13	 13	 13	 13	 14	 14	 14	 14	 14	 14	 14	 14	 14
	 15	 15	 15	 16	 16	 16	 16	 16	 16	 16	 16	 16	 16	 16	 16	 14	 14	 14	 14	 14	 14	 14	 14	 15	 15	 15	 15	 15
	 16	 16	 16	 16	 16	 16	 16	 17	 17	 17	 17	 17	 17	 17	 17	 17	 17	 17	 15	 15	 15	 15	 15	 15	 15	 15	 15	 15
	 16	 16	 16	 16	 16	 16	 16	 17	 17	 18	 18	 18	 18	 18	 18	 18	 18	 18	 18	 18	 18	 18	 18	 18	 18	 16	 16	 16
	 16	 16	 16	 16	 16	 16	 16	 17	 17	 18	 19	 19	 19	 19	 19	 19	 19	 19	 19	 19	 19	 19	 19	 19	 19	 19	 17	 17
	 18	 18	 18	 17	 17	 17	 17	 17	 18	 18	 19	 19	 20	 20	 20	 20	 20	 20	 20	 20	 20	 20	 20	 20	 20	 20	 20	 20
	 18	 18	 19	 19	 19	 19	 18	 18	 18	 18	 19	 19	 20	 21	 21	 21	 21	 21	 21	 21	 21	 21	 21	 21	 21	 21	 21	 21
	 18	 18	 19	 19	 19	 19	 20	 20	 20	 20	 20	 20	 20	 21	 22	 22	 22	 22	 22	 22	 22	 22	 22	 22	 22	 22	 22	 22
	 23	 23	 23	 20	 20	 20	 20	 21	 21	 21	 21	 21	 21	 21	 22	 23	 23	 23	 23	 23	 23	 23	 23	 23	 23	 23	 23	 23
	 24	 24	 24	 24	 24	 24	 24	 21	 22	 22	 22	 22	 22	 22	 22	 23	 23	 23	 24	 24	 24	 24	 24	 24	 24	 24	 24	 24
	 24	 24	 25	 25	 25	 25	 25	 25	 25	 25	 25	 25	 25	 23	 23	 23	 23	 23	 24	 25	 25	 25	 25	 25	 25	 25	 25	 25
	 24	 24	 25	 25	 25	 25	 26	 26	 26	 26	 26	 26	 26	 26	 24	 24	 24	 24	 24	 25	 25	 26	 26	 26	 26	 26	 26	 26
	 27	 27	 27	 26	 26	 26	 26	 27	 27	 27	 27	 27	 27	 27	 27	 25	 25	 25	 25	 25	 25	 26	 26	 27	 27	 27	 27	 27
	 27	 27	 27	 27	 27	 27	 27	 27	 27	 28	 28	 28	 28	 28	 28	 28	 28	 28	 28	 28	 28	 28	 28	 28	 28	 28	 28	 28
	 27	 27	 27	 27	 27	 27	 27	 27	 27	 28	 29	 29	 29	 29	 29	 29	 29	 29	 29	 29	 29	 29	 29	 29	 29	 29	 29	 29

## Executing

Depending on your operating system you may need to use python3 as the command to execute this script using a Python 3.0.0 or higher version. You can check by running "python --version". If you have a version > 3.0.0 then you can use the command "python". If not, then you should try "python3". If neither commands are available, i.e. they're not installed, or "python" gives you a version < 3.0.0 you should refer to the Python download page (https://www.python.org/downloads/) for how to get >= 3.0.0 installed to your machine and activated. Alternatively, you may wish to setup to use a virtual environment (https://docs.python.org/3/library/venv.html).

An input file path and output file path are required to execute the python script.

python .\LabLCS.py .\path\to\input.txt .\path\to\output.txt

Input and output file paths may be relative or absolute. If the output file exists it will be overwritten, or if it does not exist then it will be created.

## Contributing

As a standlone python script that uses only built-in python modules, any IDE or text-editor may be used to modify/contribute to this script. The only requirement is that you have a Python version >= 3.0.0 installed on your machine and accessible, or have a Python virtual environment installed elsewhere that is activated and uses a version >= 3.0.0.
