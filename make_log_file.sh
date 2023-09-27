#! usr/bin/env bash

wd=~/class2/shell_scripting-gabe
# The python scripts run to make individual fasta files that will be named
# after the sequence in that file, then the sequence gets put into that file
python3 create_fastas.py
base_pair_total=$(python3 num_fasta.py 2> /dev/null)
#python3 num_fasta.py
total_fasta_files=$( ls ${wd}/ExampleAlignments/ | grep -c "\.fasta" )
total_sequences=$( ls ${wd}/individual_fastas/ | grep -c "\.fasta" )
total_base_pairs=$( cat ${cd}/individual_fastas/Sample* | grep -v "^>" | wc -c )
#clear the log file and then add to it
echo "" > log.txt
echo $total_fasta_files >> log.txt
echo $total_sequences >> log.txt
echo $total_base_pairs >> log.txt

echo "Number of fasta files: $total_fasta_files"
echo "Number of sequences: $total_sequences"
echo "Number of base pairs: $total_base_pairs"
