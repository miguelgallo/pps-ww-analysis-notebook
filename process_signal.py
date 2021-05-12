from ProcessData import *

# labels_signals = [ "GGToWW-AQGC-A0W1e-6" ]
labels_signals = [ "GGToWW-AQGC-A0W1e-6", "GGToWW-AQGC-A0W2e-6", "GGToWW-AQGC-A0W5e-6" ]

fileNames_signals = {
    "GGToWW-AQGC-A0W1e-6": [ "output-GGToWW-AQGC-A0W1e-6.h5" ],
    "GGToWW-AQGC-A0W2e-6": [ "output-GGToWW-AQGC-A0W2e-6.h5" ],
    "GGToWW-AQGC-A0W5e-6": [ "output-GGToWW-AQGC-A0W5e-6.h5" ]
    }

process_data_ = ProcessData( labels=labels_signals, fileNames=fileNames_signals, mix_protons=False, runOnMC=True )

# labels_signals_mix_protons = [ "GGToWW-AQGC-mix_protons-A0W1e-6" ]
labels_signals_mix_protons = [ "GGToWW-AQGC-mix_protons-A0W1e-6", "GGToWW-AQGC-mix_protons-A0W2e-6", "GGToWW-AQGC-mix_protons-A0W5e-6" ]

fileNames_signals_mix_protons = {
    "GGToWW-AQGC-mix_protons-A0W1e-6": [ "output-GGToWW-AQGC-mix_protons-A0W1e-6.h5" ],
    "GGToWW-AQGC-mix_protons-A0W2e-6": [ "output-GGToWW-AQGC-mix_protons-A0W2e-6.h5" ],
    "GGToWW-AQGC-mix_protons-A0W5e-6": [ "output-GGToWW-AQGC-mix_protons-A0W5e-6.h5" ]
    }

process_data_mix_protons_ = ProcessData( labels=labels_signals_mix_protons, fileNames=fileNames_signals_mix_protons, mix_protons=True, runOnMC=True )

process_data_( apply_fiducial=True, within_aperture=True, select_2protons=False )

process_data_mix_protons_( apply_fiducial=True, within_aperture=True, select_2protons=False )
