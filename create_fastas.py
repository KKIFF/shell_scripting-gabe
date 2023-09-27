#! usr/bin/env python3

import os

#get each fasta file from the path then read the fasta files
path = 'ExampleAlignments/'
fasta_list = os.listdir(path)
created_fastas = 'individual_fastas/'
if not os.path.exists(created_fastas):
        os.mkdir(created_fasta)

sequence_list = []
for fasta in fasta_list:
    file_path = path + fasta
    print(file_path)
    new_fasta = open(file_path, "r")
    lines = fasta.readlines()
    i = 0
    while i < len(lines):
        if lines[i].startswith('>'):
            for sequence in sequence_list:
                if lines[i] != sequence:
                    file_name = lines[i].strip()[1:]
                    file_name = file_name.replace(" ","_")
                    with open(created_fastas + file_name + ".fasta", "w") as new_fasta_file
                        new_fasta_file.write(lines[i])
                        i += 1
                        if i < len(lines):
                            new_fasta_file.write(lines[i])
        i += 1
new_fasta.close()
