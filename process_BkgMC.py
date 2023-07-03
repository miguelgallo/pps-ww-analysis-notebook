from ProcessData import *

#lepton_type = "muon"
lepton_type = "electron"

# data_sample = '2017'
data_sample = '2018'

use_hash_index_ = True

base_path_ = "/eos/home-m/malvesga/SWAN_projects/Antonio_UL/output"
labels_bkgs_ = []
fileNames_bkgs_ = {}
if data_sample == '2017':
    if lepton_type == 'muon':
        labels_bkgs_ = [ "GGToWW-AQGC-2017-muon-A0W1e-6", "GGToWW-AQGC-2017-muon-A0W2e-6", "GGToWW-AQGC-2017-muon-A0W5e-6" ]
        fileNames_bkgs_ = {
            "GGToWW-AQGC-2017-muon-A0W1e-6": [ "output-GGToWW-AQGC-2017-muon-A0W1e-6.h5" ],
            "GGToWW-AQGC-2017-muon-A0W2e-6": [ "output-GGToWW-AQGC-2017-muon-A0W2e-6.h5" ],
            "GGToWW-AQGC-2017-muon-A0W5e-6": [ "output-GGToWW-AQGC-2017-muon-A0W5e-6.h5" ]
            }
    elif lepton_type == 'electron':
        labels_bkgs_ = [ "GGToWW-AQGC-2017-electron-A0W1e-6", "GGToWW-AQGC-2017-electron-A0W2e-6", "GGToWW-AQGC-2017-electron-A0W5e-6" ]
        fileNames_bkgs_ = {
            "GGToWW-AQGC-2017-electron-A0W1e-6": [ "output-GGToWW-AQGC-2017-electron-A0W1e-6.h5" ],
            "GGToWW-AQGC-2017-electron-A0W2e-6": [ "output-GGToWW-AQGC-2017-electron-A0W2e-6.h5" ],
            "GGToWW-AQGC-2017-electron-A0W5e-6": [ "output-GGToWW-AQGC-2017-electron-A0W5e-6.h5" ]
            }
elif data_sample == '2018':
    if lepton_type == 'muon':
        labels_bkgs_ = [ "Bkg-2018-muon-WJetsToLNu_2J" ]#,"Bkg-2018-muon-QCD_Pt_600to800", "GGToWW-AQGC-2018-muon-A0W2e-6", "GGToWW-AQGC-2018-muon-A0W5e-6" ]
        fileNames_bkgs_ = {
            "Bkg-2018-muon-WJetsToLNu_2J": [ "output-Bkg-mix_protons-2018-muon-WJetsToLNu_2J.h5" ]#,
            }
    elif lepton_type == 'electron':
        labels_bkgs_ = [ "Bkg-2018-electron-WJetsToLNu_2J" ]#,"Bkg-2018-electron-QCD_Pt_600to800", "GGToWW-AQGC-2018-electron-A0W2e-6", "GGToWW-AQGC-2018-electron-A0W5e-6" ]
        fileNames_bkgs_ = {
            "Bkg-2018-electron-WJetsToLNu_2J": [ "output-Bkg-mix_protons-2018-electron-WJetsToLNu_2J.h5" ]#,
            }

for key_ in fileNames_bkgs_:
    fileNames_bkgs_[ key_ ] = [ "{}/{}".format( base_path_, item_ ) for item_ in fileNames_bkgs_[ key_ ] ]
print ( labels_bkgs_ )
print ( fileNames_bkgs_ )

# output_dir_=""
output_dir_="/eos/home-m/malvesga/SWAN_projects/Antonio_UL/output"
process_data_ = ProcessData( lepton_type=lepton_type, data_sample=data_sample, labels=labels_bkgs_, fileNames=fileNames_bkgs_, mix_protons=False, runOnMC=True, output_dir=output_dir_, use_hash_index=use_hash_index_ )

process_data_( apply_fiducial=True, within_aperture=True, select_2protons=False )
