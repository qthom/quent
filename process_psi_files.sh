 #process files from psi blast

INPUT_DIR=/home/thomas/Desktop/19-02-2016-DSSPhelix-project/output/fasta_files/psi_output/psi_files
OUTPUT_DIR=/home/thomas/Desktop/19-02-2016-DSSPhelix-project/output/fasta_files/conservation/conservation

for i in $INPUT_DIR/*.psi
do
filename=`basename $i .psi`
tail -n +4 $INPUT_DIR/$filename.psi | head -n -6 | awk '{ print $43 }'  >$OUTPUT_DIR/$filename.cons
done

