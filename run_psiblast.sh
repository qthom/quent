OUTPUT_DIR=/home/thomas/Desktop/19-02-2016-DSSPhelix-project/output/fasta_files/psi_output/blastpgp_files
OUTPUT2_DIR=/home/thomas/Desktop/19-02-2016-DSSPhelix-project/output/fasta_files/psi_output/psi_files
INPUT_DIR=/home/thomas/Desktop/19-02-2016-DSSPhelix-project/output/fasta_files
DB=/home/thomas/blast/

for i in $INPUT_DIR/*.fasta
do
filename=`basename $i .fasta`
blastpgp -j 3 -d $DB/uniref90.fasta -i $INPUT_DIR/$filename.fasta -o $OUTPUT_DIR/$filename.blastpgp -Q $OUTPUT2_DIR/$filename.psi
done

