INPUT_DIR=/home/thomas/Desktop/19-02-2016-DSSPhelix-project/output/cross_validation_svm/extracted_features_sets/basic/6_sets
OUTPUT_DIR=/home/thomas/Desktop/19-02-2016-DSSPhelix-project/output/cross_validation_svm/extracted_features_sets/psi_blast/topology_templates

for i in $INPUT_DIR/*.txt
do
filename=`basename $i .txt`
cat $INPUT_DIR/$filename.txt | awk '{ print  $1 }' | column -t >$OUTPUT_DIR/$filename.template
done

