#!/bin/tcsh

### Replace the following lines according to your setup.
set EXEC=/afs/cern.ch/work/m/malvesga/ProtonRecon/TEST/CMSSW_11_2_4/src/workspace/pps-ww-analysis-notebook
set OUTPUT=/eos/home-m/malvesga/SWAN_projects/Antonio_UL/output_05-07
###

#set file=$1
#set label=$2
set option1="$1"
set option2="$2"
#set option3="$5"
#set option4="$6"
#set option5="$7"
#set option6="$8"
#echo "file: "$file
#echo "label: "$label
echo "option: "$option1
echo "option: "$option2
#echo "option: "$option3
#echo "option: "$option4
#echo "option: "$option5
#echo "option: "$option6

echo $EXEC
echo $OUTPUT

#source /afs/cern.ch/user/a/antoniov/work/env/uproot-LCG_101/bin/activate.csh

set currentdir=`pwd`
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
echo python3 $EXEC/create_table_BkgMC_mix_protons_new.py $option1 $option2
python3 $EXEC/create_table_BkgMC_mix_protons_new.py $option1 $option2
cp *.h5 $OUTPUT
