#! usr/bin/env python3

import os

def count_fastas(path):
    #when given the path to a fasta file, this function will read the file, read each sequence in the file, and return a    total for all of the base pairs in those fasta files.
    directories = os.listdir(path)
    fastas = []
    for directory in directories:
        if ".fasta" in directory:
            fastas.append(directory)

    total = 0
    #read the genetic sequence in each fasta file
    for fasta in fastas:
        fasta_path = path + fasta
        with open(fasta_path, "r") as cur_fasta:
            num_lines = cur_fasta.readlines()
            # lines[0] is sample lines[1] is the sequence
            if len(num_lines) > 1:
                total += len(lines[1])
    return total
path = "individual_fastas/"
print(count_fastas(path))
