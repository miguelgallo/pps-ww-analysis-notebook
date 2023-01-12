from ProcessData import *

#lepton_type = "muon"
lepton_type = "electron"

# data_sample = '2017'
data_sample = '2018'

use_hash_index_ = True

# labels_signals_mix_protons = [ "GGToWW-AQGC-mix_protons-A0W1e-6" ]
# labels_signals_mix_protons = [ "GGToWW-AQGC-mix_protons-A0W1e-6", "GGToWW-AQGC-mix_protons-A0W2e-6", "GGToWW-AQGC-mix_protons-A0W5e-6" ]

base_path_ = "/eos/home-m/malvesga/SWAN_projects/Antonio_UL/output"
labels_signals_mix_protons_ = []
fileNames_signals_mix_protons_ = {}
if data_sample == '2017':
    if lepton_type == 'muon':
        labels_signals_mix_protons_ = [ "GGToWW-AQGC-mix_protons-2017-muon-A0W1e-6", "GGToWW-AQGC-mix_protons-2017-muon-A0W2e-6", "GGToWW-AQGC-mix_protons-2017-muon-A0W5e-6" ]
        fileNames_signals_mix_protons_ = {
            "GGToWW-AQGC-mix_protons-2017-muon-A0W1e-6": [ "output-GGToWW-AQGC-mix_protons-2017-muon-A0W1e-6.h5" ],
            "GGToWW-AQGC-mix_protons-2017-muon-A0W2e-6": [ "output-GGToWW-AQGC-mix_protons-2017-muon-A0W2e-6.h5" ],
            "GGToWW-AQGC-mix_protons-2017-muon-A0W5e-6": [ "output-GGToWW-AQGC-mix_protons-2017-muon-A0W5e-6.h5" ]
            }
    elif lepton_type == 'electron':
        labels_signals_mix_protons_ = [ "GGToWW-AQGC-mix_protons-2017-electron-A0W1e-6", "GGToWW-AQGC-mix_protons-2017-electron-A0W2e-6", "GGToWW-AQGC-mix_protons-2017-electron-A0W5e-6" ]
        fileNames_signals_mix_protons_ = {
            "GGToWW-AQGC-mix_protons-2017-electron-A0W1e-6": [ "output-GGToWW-AQGC-mix_protons-2017-electron-A0W1e-6.h5" ],
            "GGToWW-AQGC-mix_protons-2017-electron-A0W2e-6": [ "output-GGToWW-AQGC-mix_protons-2017-electron-A0W2e-6.h5" ],
            "GGToWW-AQGC-mix_protons-2017-electron-A0W5e-6": [ "output-GGToWW-AQGC-mix_protons-2017-electron-A0W5e-6.h5" ]
            }
elif data_sample == '2018':
    if lepton_type == 'muon':
        # labels_signals_mix_protons_ = [ "GGToWW-AQGC-mix_protons-2018-muon-A0W5e-7", "GGToWW-AQGC-mix_protons-2018-muon-A0W1e-6", "GGToWW-AQGC-mix_protons-2018-muon-A0W2e-6", "GGToWW-AQGC-mix_protons-2018-muon-A0W5e-6" ]
        labels_signals_mix_protons_ = [ "GGToWW-AQGC-mix_protons-2018-muon-A0W1e-6", "GGToWW-AQGC-mix_protons-2018-muon-A0W2e-6", "GGToWW-AQGC-mix_protons-2018-muon-A0W5e-6" ]
        fileNames_signals_mix_protons_ = {
            # "GGToWW-AQGC-mix_protons-2018-muon-A0W5e-7": [ "output-GGToWW-AQGC-mix_protons-2018-muon-A0W5e-7.h5" ],
            "GGToWW-AQGC-mix_protons-2018-muon-A0W1e-6": [ "output-GGToWW-AQGC-mix_protons-2018-muon-A0W1e-6.h5" ],
            "GGToWW-AQGC-mix_protons-2018-muon-A0W2e-6": [ "output-GGToWW-AQGC-mix_protons-2018-muon-A0W2e-6.h5" ],
            "GGToWW-AQGC-mix_protons-2018-muon-A0W5e-6": [ "output-GGToWW-AQGC-mix_protons-2018-muon-A0W5e-6.h5" ]
            }
    elif lepton_type == 'electron':
        # labels_signals_mix_protons_ = [ "GGToWW-AQGC-mix_protons-2018-electron-A0W5e-7", "GGToWW-AQGC-mix_protons-2018-electron-A0W1e-6", "GGToWW-AQGC-mix_protons-2018-electron-A0W2e-6", "GGToWW-AQGC-mix_protons-2018-electron-A0W5e-6" ]
        labels_signals_mix_protons_ = [ "GGToWW-AQGC-mix_protons-2018-electron-A0W1e-6", "GGToWW-AQGC-mix_protons-2018-electron-A0W2e-6", "GGToWW-AQGC-mix_protons-2018-electron-A0W5e-6" ]
        fileNames_signals_mix_protons_ = {
            # "GGToWW-AQGC-mix_protons-2018-electron-A0W5e-7": [ "output-GGToWW-AQGC-mix_protons-2018-electron-A0W5e-7.h5" ],
            "GGToWW-AQGC-mix_protons-2018-electron-A0W1e-6": [ "output-GGToWW-AQGC-mix_protons-2018-electron-A0W1e-6.h5" ],
            "GGToWW-AQGC-mix_protons-2018-electron-A0W2e-6": [ "output-GGToWW-AQGC-mix_protons-2018-electron-A0W2e-6.h5" ],
            "GGToWW-AQGC-mix_protons-2018-electron-A0W5e-6": [ "output-GGToWW-AQGC-mix_protons-2018-electron-A0W5e-6.h5" ]
            }

for key_ in fileNames_signals_mix_protons_:
    fileNames_signals_mix_protons_[ key_ ] = [ "{}/{}".format( base_path_, item_ ) for item_ in fileNames_signals_mix_protons_[ key_ ] ]
print ( labels_signals_mix_protons_ )
print ( fileNames_signals_mix_protons_ )

# output_dir_=""
output_dir_="/eos/home-m/malvesga/SWAN_projects/Antonio_UL/output"
process_data_mix_protons_ = ProcessData( lepton_type=lepton_type, data_sample=data_sample, labels=labels_signals_mix_protons_, fileNames=fileNames_signals_mix_protons_, mix_protons=True, runOnMC=True, output_dir=output_dir_, use_hash_index=use_hash_index_ )

process_data_mix_protons_( apply_fiducial=True, within_aperture=True, select_2protons=False )
