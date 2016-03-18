#!/bin/bash
#INPUT_DIR2=/home/thomas/Desktop/19-02-2016-DSSPhelix-project/output/fasta_files/topology_files/
INPUT_DIR2=/home/thomas/Desktop/19-02-2016-DSSPhelix-project/output/fasta_files/conservation/conservation/features
INPUT_DIR=/home/thomas/Desktop/19-02-2016-DSSPhelix-project/input/psi_matrix_target_value_svm
OUTPUT_DIR=/home/thomas/Desktop/19-02-2016-DSSPhelix-project/output/fasta_files/conservation/matrice/
SCRIPT_DIR=/home/thomas/Desktop/19-02-2016-DSSPhelix-project/script

for i in $INPUT_DIR/*.svm
do
filename=`basename $i .svm`
python $SCRIPT_DIR/conservation.py $i $INPUT_DIR2/$filename.cons.feat  $OUTPUT_DIR/$filename.cons
done


