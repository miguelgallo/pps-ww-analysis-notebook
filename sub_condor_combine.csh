#!/bin/tcsh

### Replace the following lines according to your setup.
set CMSSWPATH=/eos/home-a/antoniov/SWAN_projects/pps-ww-analysis
set EXEC=/eos/home-a/antoniov/SWAN_projects/pps-ww-analysis/combine/version1
set OUTPUT=/eos/home-a/antoniov/SWAN_projects/pps-ww-analysis/combine/version1/output
###

set card=$1
set name=$2
set option1="$3"
set option2="$4"
set option3="$5"
set option4="$6"
set option5="$7"
set option6="$8"
set option7="$9"
set option8="$10"
set option9="$11"
set option10="$12"
echo "datacard: "$card
echo "name: "$name
echo "option: "$option1
echo "option: "$option2
echo "option: "$option3
echo "option: "$option4
echo "option: "$option5
echo "option: "$option6
echo "option: "$option7
echo "option: "$option8
echo "option: "$option9
echo "option: "$option10
echo $CMSSWPATH
echo $EXEC
echo $OUTPUT

set currentdir=`pwd`
echo $CMSSWPATH
cd $CMSSWPATH
source set_cmssw_combine.csh

echo $currentdir
cd $currentdir
cp $EXEC/$card .
ls

if ( ! $?PYTHONPATH ) then
    if ( ! $?PYTHON3PATH ) then
        setenv PYTHONPATH ${EXEC}
        echo "PYTHONPATH set to $PYTHONPATH"
    else
        setenv PYTHON3PATH ${PYTHON3PATH}:${EXEC}
        echo "PYTHON3PATH set to $PYTHON3PATH"
    endif 
else
    setenv PYTHONPATH ${PYTHONPATH}:${EXEC}
    echo "PYTHONPATH set to $PYTHONPATH"
endif
env

echo 'Running...'
echo combine -M HybridNew --LHCmode LHC-limits --saveToys -t -1 --bypassFrequentistFit $card --name=$name $option1 $option2 $option3 $option4 $option5 $option6 $option7 $option8 $option9 $option10
combine -M HybridNew --LHCmode LHC-limits --saveToys -t -1 --bypassFrequentistFit $card --name=$name $option1 $option2 $option3 $option4 $option5 $option6 $option7 $option8 $option9 $option10
cp *.root $OUTPUT
