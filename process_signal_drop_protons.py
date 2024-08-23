from ProcessData import *

#lepton_type = "muon"
lepton_type = "electron"

# data_sample = '2017'
data_sample = '2018'

use_hash_index_ = True

# labels_signals = [ "GGToWW-AQGC-A0W1e-6" ]
# labels_signals = [ "GGToWW-AQGC-A0W1e-6", "GGToWW-AQGC-A0W2e-6", "GGToWW-AQGC-A0W5e-6" ]

base_path_ = "/eos/home-m/malvesga/SWAN_projects/Antonio_UL/output-final"
output_dir_ =  "/eos/home-m/malvesga/SWAN_projects/Antonio_UL/output-final"

labels_signals_ = []
fileNames_signals_ = {}
if data_sample == '2017':
    if lepton_type == 'muon':
        labels_signals_ = [
            "GGToWW-AQGC-2017-muon-A0W1e-6-Arm0", "GGToWW-AQGC-2017-muon-A0W2e-6-Arm0", "GGToWW-AQGC-2017-muon-A0W5e-6-Arm0",
            "GGToWW-AQGC-2017-muon-A0W1e-6-Arm1", "GGToWW-AQGC-2017-muon-A0W2e-6-Arm1", "GGToWW-AQGC-2017-muon-A0W5e-6-Arm1"
        ]
        fileNames_signals_ = {
            "GGToWW-AQGC-2017-muon-A0W1e-6-Arm0": [ "output-GGToWW-AQGC-2017-muon-A0W1e-6-Arm0.h5" ],
            "GGToWW-AQGC-2017-muon-A0W2e-6-Arm0": [ "output-GGToWW-AQGC-2017-muon-A0W2e-6-Arm0.h5" ],
            "GGToWW-AQGC-2017-muon-A0W5e-6-Arm0": [ "output-GGToWW-AQGC-2017-muon-A0W5e-6-Arm0.h5" ],
            "GGToWW-AQGC-2017-muon-A0W1e-6-Arm1": [ "output-GGToWW-AQGC-2017-muon-A0W1e-6-Arm1.h5" ],
            "GGToWW-AQGC-2017-muon-A0W2e-6-Arm1": [ "output-GGToWW-AQGC-2017-muon-A0W2e-6-Arm1.h5" ],
            "GGToWW-AQGC-2017-muon-A0W5e-6-Arm1": [ "output-GGToWW-AQGC-2017-muon-A0W5e-6-Arm1.h5" ]
            }
    elif lepton_type == 'electron':
        labels_signals_ = [
            "GGToWW-AQGC-2017-electron-A0W1e-6-Arm0", "GGToWW-AQGC-2017-electron-A0W2e-6-Arm0", "GGToWW-AQGC-2017-electron-A0W5e-6-Arm0",
            "GGToWW-AQGC-2017-electron-A0W1e-6-Arm1", "GGToWW-AQGC-2017-electron-A0W2e-6-Arm1", "GGToWW-AQGC-2017-electron-A0W5e-6-Arm1"
        ]
        fileNames_signals_ = {
            "GGToWW-AQGC-2017-electron-A0W1e-6-Arm0": [ "output-GGToWW-AQGC-2017-electron-A0W1e-6-Arm0.h5" ],
            "GGToWW-AQGC-2017-electron-A0W2e-6-Arm0": [ "output-GGToWW-AQGC-2017-electron-A0W2e-6-Arm0.h5" ],
            "GGToWW-AQGC-2017-electron-A0W5e-6-Arm0": [ "output-GGToWW-AQGC-2017-electron-A0W5e-6-Arm0.h5" ],
            "GGToWW-AQGC-2017-electron-A0W1e-6-Arm1": [ "output-GGToWW-AQGC-2017-electron-A0W1e-6-Arm1.h5" ],
            "GGToWW-AQGC-2017-electron-A0W2e-6-Arm1": [ "output-GGToWW-AQGC-2017-electron-A0W2e-6-Arm1.h5" ],
            "GGToWW-AQGC-2017-electron-A0W5e-6-Arm1": [ "output-GGToWW-AQGC-2017-electron-A0W5e-6-Arm1.h5" ]
            }
elif data_sample == '2018':
    if lepton_type == 'muon':
        # labels_signals_ = [ "GGToWW-AQGC-2018-muon-A0W5e-7", "GGToWW-AQGC-2018-muon-A0W1e-6", "GGToWW-AQGC-2018-muon-A0W2e-6", "GGToWW-AQGC-2018-muon-A0W5e-6" ]
        labels_signals_ = [
            "GGToWW-AQGC-2018-muon-A0W1e-7-Arm0", "GGToWW-AQGC-2018-muon-A0W2e-7-Arm0", "GGToWW-AQGC-2018-muon-A0W5e-7-Arm0",
            "GGToWW-AQGC-2018-muon-A0W1e-7-Arm1", "GGToWW-AQGC-2018-muon-A0W2e-7-Arm1", "GGToWW-AQGC-2018-muon-A0W5e-7-Arm1",
            "GGToWW-AQGC-2018-muon-A0W1e-6-Arm0", "GGToWW-AQGC-2018-muon-A0W2e-6-Arm0", "GGToWW-AQGC-2018-muon-A0W5e-6-Arm0",
            "GGToWW-AQGC-2018-muon-A0W1e-6-Arm1", "GGToWW-AQGC-2018-muon-A0W2e-6-Arm1", "GGToWW-AQGC-2018-muon-A0W5e-6-Arm1",
            "GGToWW-AQGC-2018-muon-ACW5e-7-Arm0", "GGToWW-AQGC-2018-muon-ACW1e-6-Arm0", "GGToWW-AQGC-2018-muon-ACW2e-6-Arm0", 
            "GGToWW-AQGC-2018-muon-ACW5e-7-Arm1", "GGToWW-AQGC-2018-muon-ACW1e-6-Arm1", "GGToWW-AQGC-2018-muon-ACW2e-6-Arm1", 
            "GGToWW-AQGC-2018-muon-ACW5e-6-Arm0", "GGToWW-AQGC-2018-muon-ACW1e-5-Arm0", "GGToWW-AQGC-2018-muon-ACW2e-5-Arm0",
            "GGToWW-AQGC-2018-muon-ACW5e-6-Arm1", "GGToWW-AQGC-2018-muon-ACW1e-5-Arm1", "GGToWW-AQGC-2018-muon-ACW2e-5-Arm1"
        ]
        fileNames_signals_ = {
            "GGToWW-AQGC-2018-muon-A0W1e-7-Arm0": [ "output-GGToWW-AQGC-2018-muon-A0W1e-7-Arm0.h5" ],
            "GGToWW-AQGC-2018-muon-A0W2e-7-Arm0": [ "output-GGToWW-AQGC-2018-muon-A0W2e-7-Arm0.h5" ],
            "GGToWW-AQGC-2018-muon-A0W5e-7-Arm0": [ "output-GGToWW-AQGC-2018-muon-A0W5e-7-Arm0.h5" ],
            "GGToWW-AQGC-2018-muon-A0W1e-6-Arm0": [ "output-GGToWW-AQGC-2018-muon-A0W1e-6-Arm0.h5" ],
            "GGToWW-AQGC-2018-muon-A0W2e-6-Arm0": [ "output-GGToWW-AQGC-2018-muon-A0W2e-6-Arm0.h5" ],
            "GGToWW-AQGC-2018-muon-A0W5e-6-Arm0": [ "output-GGToWW-AQGC-2018-muon-A0W5e-6-Arm0.h5" ],
            "GGToWW-AQGC-2018-muon-A0W1e-7-Arm1": [ "output-GGToWW-AQGC-2018-muon-A0W1e-7-Arm1.h5" ],
            "GGToWW-AQGC-2018-muon-A0W2e-7-Arm1": [ "output-GGToWW-AQGC-2018-muon-A0W2e-7-Arm1.h5" ],
            "GGToWW-AQGC-2018-muon-A0W5e-7-Arm1": [ "output-GGToWW-AQGC-2018-muon-A0W5e-7-Arm1.h5" ],
            "GGToWW-AQGC-2018-muon-A0W1e-6-Arm1": [ "output-GGToWW-AQGC-2018-muon-A0W1e-6-Arm1.h5" ],
            "GGToWW-AQGC-2018-muon-A0W2e-6-Arm1": [ "output-GGToWW-AQGC-2018-muon-A0W2e-6-Arm1.h5" ],
            "GGToWW-AQGC-2018-muon-A0W5e-6-Arm1": [ "output-GGToWW-AQGC-2018-muon-A0W5e-6-Arm1.h5" ],
            "GGToWW-AQGC-2018-muon-ACW5e-7-Arm0": [ "output-GGToWW-AQGC-2018-muon-ACW5e-7-Arm0.h5" ],
            "GGToWW-AQGC-2018-muon-ACW1e-6-Arm0": [ "output-GGToWW-AQGC-2018-muon-ACW1e-6-Arm0.h5" ],
            "GGToWW-AQGC-2018-muon-ACW2e-6-Arm0": [ "output-GGToWW-AQGC-2018-muon-ACW2e-6-Arm0.h5" ],
            "GGToWW-AQGC-2018-muon-ACW5e-6-Arm0": [ "output-GGToWW-AQGC-2018-muon-ACW5e-6-Arm0.h5" ],
            "GGToWW-AQGC-2018-muon-ACW1e-5-Arm0": [ "output-GGToWW-AQGC-2018-muon-ACW1e-5-Arm0.h5" ],
            "GGToWW-AQGC-2018-muon-ACW2e-5-Arm0": [ "output-GGToWW-AQGC-2018-muon-ACW2e-5-Arm0.h5" ],
            "GGToWW-AQGC-2018-muon-ACW5e-7-Arm1": [ "output-GGToWW-AQGC-2018-muon-ACW5e-7-Arm1.h5" ],
            "GGToWW-AQGC-2018-muon-ACW1e-6-Arm1": [ "output-GGToWW-AQGC-2018-muon-ACW1e-6-Arm1.h5" ],
            "GGToWW-AQGC-2018-muon-ACW2e-6-Arm1": [ "output-GGToWW-AQGC-2018-muon-ACW2e-6-Arm1.h5" ],
            "GGToWW-AQGC-2018-muon-ACW5e-6-Arm1": [ "output-GGToWW-AQGC-2018-muon-ACW5e-6-Arm1.h5" ],
            "GGToWW-AQGC-2018-muon-ACW1e-5-Arm1": [ "output-GGToWW-AQGC-2018-muon-ACW1e-5-Arm1.h5" ],
            "GGToWW-AQGC-2018-muon-ACW2e-5-Arm1": [ "output-GGToWW-AQGC-2018-muon-ACW2e-5-Arm1.h5" ]
            }
    elif lepton_type == 'electron':
        # labels_signals_ = [ "GGToWW-AQGC-2018-electron-A0W5e-7", "GGToWW-AQGC-2018-electron-A0W1e-6", "GGToWW-AQGC-2018-electron-A0W2e-6", "GGToWW-AQGC-2018-electron-A0W5e-6" ]
        labels_signals_ = [
            "GGToWW-AQGC-2018-electron-A0W1e-7-Arm0", "GGToWW-AQGC-2018-electron-A0W2e-7-Arm0", "GGToWW-AQGC-2018-electron-A0W5e-7-Arm0",
            "GGToWW-AQGC-2018-electron-A0W1e-7-Arm1", "GGToWW-AQGC-2018-electron-A0W2e-7-Arm1", "GGToWW-AQGC-2018-electron-A0W5e-7-Arm1",
            "GGToWW-AQGC-2018-electron-A0W1e-6-Arm0", "GGToWW-AQGC-2018-electron-A0W2e-6-Arm0", "GGToWW-AQGC-2018-electron-A0W5e-6-Arm0",
            "GGToWW-AQGC-2018-electron-A0W1e-6-Arm1", "GGToWW-AQGC-2018-electron-A0W2e-6-Arm1", "GGToWW-AQGC-2018-electron-A0W5e-6-Arm1",
            "GGToWW-AQGC-2018-electron-ACW5e-7-Arm0", "GGToWW-AQGC-2018-electron-ACW1e-6-Arm0", "GGToWW-AQGC-2018-electron-ACW2e-6-Arm0", 
            "GGToWW-AQGC-2018-electron-ACW5e-7-Arm1", "GGToWW-AQGC-2018-electron-ACW1e-6-Arm1", "GGToWW-AQGC-2018-electron-ACW2e-6-Arm1", 
            "GGToWW-AQGC-2018-electron-ACW5e-6-Arm0", "GGToWW-AQGC-2018-electron-ACW1e-5-Arm0", "GGToWW-AQGC-2018-electron-ACW2e-5-Arm0",
            "GGToWW-AQGC-2018-electron-ACW5e-6-Arm1", "GGToWW-AQGC-2018-electron-ACW1e-5-Arm1", "GGToWW-AQGC-2018-electron-ACW2e-5-Arm1"
        ]
        fileNames_signals_ = {
            "GGToWW-AQGC-2018-electron-A0W1e-7-Arm0": [ "output-GGToWW-AQGC-2018-electron-A0W1e-7-Arm0.h5" ],
            "GGToWW-AQGC-2018-electron-A0W2e-7-Arm0": [ "output-GGToWW-AQGC-2018-electron-A0W2e-7-Arm0.h5" ],
            "GGToWW-AQGC-2018-electron-A0W5e-7-Arm0": [ "output-GGToWW-AQGC-2018-electron-A0W5e-7-Arm0.h5" ],
            "GGToWW-AQGC-2018-electron-A0W1e-6-Arm0": [ "output-GGToWW-AQGC-2018-electron-A0W1e-6-Arm0.h5" ],
            "GGToWW-AQGC-2018-electron-A0W2e-6-Arm0": [ "output-GGToWW-AQGC-2018-electron-A0W2e-6-Arm0.h5" ],
            "GGToWW-AQGC-2018-electron-A0W5e-6-Arm0": [ "output-GGToWW-AQGC-2018-electron-A0W5e-6-Arm0.h5" ],
            "GGToWW-AQGC-2018-electron-A0W1e-7-Arm1": [ "output-GGToWW-AQGC-2018-electron-A0W1e-7-Arm1.h5" ],
            "GGToWW-AQGC-2018-electron-A0W2e-7-Arm1": [ "output-GGToWW-AQGC-2018-electron-A0W2e-7-Arm1.h5" ],
            "GGToWW-AQGC-2018-electron-A0W5e-7-Arm1": [ "output-GGToWW-AQGC-2018-electron-A0W5e-7-Arm1.h5" ],
            "GGToWW-AQGC-2018-electron-A0W1e-6-Arm1": [ "output-GGToWW-AQGC-2018-electron-A0W1e-6-Arm1.h5" ],
            "GGToWW-AQGC-2018-electron-A0W2e-6-Arm1": [ "output-GGToWW-AQGC-2018-electron-A0W2e-6-Arm1.h5" ],
            "GGToWW-AQGC-2018-electron-A0W5e-6-Arm1": [ "output-GGToWW-AQGC-2018-electron-A0W5e-6-Arm1.h5" ],
            "GGToWW-AQGC-2018-electron-ACW5e-7-Arm0": [ "output-GGToWW-AQGC-2018-electron-ACW5e-7-Arm0.h5" ],
            "GGToWW-AQGC-2018-electron-ACW1e-6-Arm0": [ "output-GGToWW-AQGC-2018-electron-ACW1e-6-Arm0.h5" ],
            "GGToWW-AQGC-2018-electron-ACW2e-6-Arm0": [ "output-GGToWW-AQGC-2018-electron-ACW2e-6-Arm0.h5" ],
            "GGToWW-AQGC-2018-electron-ACW5e-6-Arm0": [ "output-GGToWW-AQGC-2018-electron-ACW5e-6-Arm0.h5" ],
            "GGToWW-AQGC-2018-electron-ACW1e-5-Arm0": [ "output-GGToWW-AQGC-2018-electron-ACW1e-5-Arm0.h5" ],
            "GGToWW-AQGC-2018-electron-ACW2e-5-Arm0": [ "output-GGToWW-AQGC-2018-electron-ACW2e-5-Arm0.h5" ],
            "GGToWW-AQGC-2018-electron-ACW5e-7-Arm1": [ "output-GGToWW-AQGC-2018-electron-ACW5e-7-Arm1.h5" ],
            "GGToWW-AQGC-2018-electron-ACW1e-6-Arm1": [ "output-GGToWW-AQGC-2018-electron-ACW1e-6-Arm1.h5" ],
            "GGToWW-AQGC-2018-electron-ACW2e-6-Arm1": [ "output-GGToWW-AQGC-2018-electron-ACW2e-6-Arm1.h5" ],
            "GGToWW-AQGC-2018-electron-ACW5e-6-Arm1": [ "output-GGToWW-AQGC-2018-electron-ACW5e-6-Arm1.h5" ],
            "GGToWW-AQGC-2018-electron-ACW1e-5-Arm1": [ "output-GGToWW-AQGC-2018-electron-ACW1e-5-Arm1.h5" ],
            "GGToWW-AQGC-2018-electron-ACW2e-5-Arm1": [ "output-GGToWW-AQGC-2018-electron-ACW2e-5-Arm1.h5" ]
            }

for key_ in fileNames_signals_:
    fileNames_signals_[ key_ ] = [ "{}/{}".format( base_path_, item_ ) for item_ in fileNames_signals_[ key_ ] ]
print ( labels_signals_ )
print ( fileNames_signals_ )

process_data_ = ProcessData( lepton_type=lepton_type, data_sample=data_sample, labels=labels_signals_, fileNames=fileNames_signals_, mix_protons=False, runOnMC=True, output_dir=output_dir_, use_hash_index=use_hash_index_ )

process_data_( apply_fiducial=True, within_aperture=True, calculate_vars_pp=False, select_2protons=False )
