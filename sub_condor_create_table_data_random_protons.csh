#!/bin/tcsh

### Replace the following lines according to your setup.
set EXEC=/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_11_2_4/src/workspace/pps-ww-analysis-notebook
set OUTPUT=/eos/home-m/malvesga/SWAN_projects/Antonio_UL/output
###

set option1="$1"
set option2="$2"
set option3="$3"
echo "option: "$option1
echo "option: "$option2
echo "option: "$option3

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
echo python3 $EXEC/create_table_data_random_protons.py $option1 $option2 $option3
python3 $EXEC/create_table_data_random_protons.py $option1 $option2 $option3
cp *.h5 $OUTPUT
