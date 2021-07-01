from ProcessData import *

# labels_signals_mix_protons = [ "GGToWW-AQGC-mix_protons-A0W1e-6" ]
labels_signals_mix_protons = [ "GGToWW-AQGC-mix_protons-A0W1e-6", "GGToWW-AQGC-mix_protons-A0W2e-6", "GGToWW-AQGC-mix_protons-A0W5e-6" ]

base_path_ = "/eos/home-a/antoniov/SWAN_projects/pps-ww-analysis/output"
fileNames_signals_mix_protons = {
    "GGToWW-AQGC-mix_protons-A0W1e-6": [ "{}/output-GGToWW-AQGC-mix_protons-A0W1e-6.h5".format( base_path_ ) ],
    "GGToWW-AQGC-mix_protons-A0W2e-6": [ "{}/output-GGToWW-AQGC-mix_protons-A0W2e-6.h5".format( base_path_ ) ],
    "GGToWW-AQGC-mix_protons-A0W5e-6": [ "{}/output-GGToWW-AQGC-mix_protons-A0W5e-6.h5".format( base_path_ ) ]
    }

process_data_mix_protons_ = ProcessData( labels=labels_signals_mix_protons, fileNames=fileNames_signals_mix_protons, mix_protons=True, runOnMC=True )

process_data_mix_protons_( apply_fiducial=True, within_aperture=True, select_2protons=False )
