#!/bin/tcsh

### Replace the following lines according to your setup.
set EXEC=/eos/home-a/antoniov/SWAN_projects/pps-ww-analysis
set OUTPUT=/eos/home-a/antoniov/SWAN_projects/pps-ww-analysis/output
###

set option1="$1"
# set option1="$2"
echo "option: "$option1
# echo "option: "$option2

echo $EXEC
echo $OUTPUT

set currentdir=`pwd`
cd $EXEC
echo $EXEC
source set_cmssw.csh
cd $currentdir
echo $currentdir
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
echo python3 $EXEC/process_data_random_protons.py $option1
python3 $EXEC/process_data_random_protons.py $option1
cp *.h5 $OUTPUT
