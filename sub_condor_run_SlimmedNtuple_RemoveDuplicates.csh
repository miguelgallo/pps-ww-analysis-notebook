#!/bin/tcsh

### Replace the following lines according to your setup.
set EXEC=/afs/cern.ch/work/a/antoniov/Workspace/analysis/PPS/CMSSW_10_6_18/src/workspace
set OUTPUT=/eos/home-a/antoniov/Workspace/analysis/data/PPS/tmp
###

#set file=$1
#set label=$2
#set option1="$3"
#set option2="$4"
#set option3="$5"
#set option4="$6"
#set option5="$7"
#set option6="$8"
#echo "file: "$file
#echo "label: "$label
#echo "option: "$option1
#echo "option: "$option2
#echo "option: "$option3
#echo "option: "$option4
#echo "option: "$option5
#echo "option: "$option6

echo $EXEC
echo $OUTPUT

cp $EXEC/SlimmedNtuple_RemoveDuplicates.h .
cp $EXEC/SlimmedNtuple_RemoveDuplicates_C* .
cp $EXEC/run_SlimmedNtuple_RemoveDuplicates.C .

set currentdir=`pwd`
cd $EXEC
echo $EXEC
cmsenv
cd $currentdir
echo $currentdir
ls

echo 'Running...'
echo root -b run_SlimmedNtuple_RemoveDuplicates.C
root -b run_SlimmedNtuple_RemoveDuplicates.C
cp *.root $OUTPUT
