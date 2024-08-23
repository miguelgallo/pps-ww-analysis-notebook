#!/bin/tcsh

### Replace the following lines according to your setup.
set EXEC=/afs/cern.ch/work/m/malvesga/ProtonRecon/TEST/CMSSW_11_2_4/src/workspace/pps-ww-analysis-notebook
set OUTPUT=/eos/home-m/malvesga/SWAN_projects/Antonio_UL/output-final
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
echo python3 $EXEC/process_BkgMC_mix_protons2.py $option1
python3 $EXEC/process_BkgMC_mix_protons2.py $option1
cp *.h5 $OUTPUT
