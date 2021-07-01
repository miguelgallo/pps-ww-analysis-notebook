from ProcessData import *

# labels_signals = [ "GGToWW-AQGC-A0W1e-6" ]
labels_signals = [ "GGToWW-AQGC-A0W1e-6", "GGToWW-AQGC-A0W2e-6", "GGToWW-AQGC-A0W5e-6" ]

base_path_ = "/eos/home-a/antoniov/SWAN_projects/pps-ww-analysis/output"
fileNames_signals = {
    "GGToWW-AQGC-A0W1e-6": [ "{}/output-GGToWW-AQGC-A0W1e-6.h5".format( base_path_ ) ],
    "GGToWW-AQGC-A0W2e-6": [ "{}/output-GGToWW-AQGC-A0W2e-6.h5".format( base_path_ ) ],
    "GGToWW-AQGC-A0W5e-6": [ "{}/output-GGToWW-AQGC-A0W5e-6.h5".format( base_path_ ) ]
    }

process_data_ = ProcessData( labels=labels_signals, fileNames=fileNames_signals, mix_protons=False, runOnMC=True )

process_data_( apply_fiducial=True, within_aperture=True, select_2protons=False )
