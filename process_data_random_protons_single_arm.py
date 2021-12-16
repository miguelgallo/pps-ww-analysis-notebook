from ProcessData import *

# lepton_type_ = "muon"
lepton_type_ = "electron"

base_path_ = "/eos/home-a/antoniov/SWAN_projects/pps-ww-analysis/output"
labels_ = []
fileNames_bkg_ = {}
if lepton_type_ == 'muon':
    labels_ = [
        "data-random-resample_50-single-arm-muon-2017B",
        "data-random-resample_50-single-arm-muon-2017C",
        "data-random-resample_50-single-arm-muon-2017D",
        "data-random-resample_50-single-arm-muon-2017E",
        "data-random-resample_50-single-arm-muon-2017F"
    ]
    fileNames_bkg_ = {
        "data-random-resample_50-single-arm-muon-2017B": [ "{}/output-data-random-resample_50-2017B.h5".format( base_path_ ) ],
        "data-random-resample_50-single-arm-muon-2017C": [ "{}/output-data-random-resample_50-2017C.h5".format( base_path_ ) ],
        "data-random-resample_50-single-arm-muon-2017D": [ "{}/output-data-random-resample_50-2017D.h5".format( base_path_ ) ],
        "data-random-resample_50-single-arm-muon-2017E": [ "{}/output-data-random-resample_50-2017E.h5".format( base_path_ ) ],
        "data-random-resample_50-single-arm-muon-2017F": [ "{}/output-data-random-resample_50-2017F.h5".format( base_path_ ) ]
    }
elif lepton_type_ == 'electron':
    labels_ = [
        "data-random-resample_50-single-arm-electron-2017B",
        "data-random-resample_50-single-arm-electron-2017C",
        "data-random-resample_50-single-arm-electron-2017D",
        "data-random-resample_50-single-arm-electron-2017E",
        "data-random-resample_50-single-arm-electron-2017F"
    ]
    fileNames_bkg_ = {
        "data-random-resample_50-single-arm-electron-2017B": [ "{}/output-data-random-resample_50-electron-2017B.h5".format( base_path_ ) ],
        "data-random-resample_50-single-arm-electron-2017C": [ "{}/output-data-random-resample_50-electron-2017C.h5".format( base_path_ ) ],
        "data-random-resample_50-single-arm-electron-2017D": [ "{}/output-data-random-resample_50-electron-2017D.h5".format( base_path_ ) ],
        "data-random-resample_50-single-arm-electron-2017E": [ "{}/output-data-random-resample_50-electron-2017E.h5".format( base_path_ ) ],
        "data-random-resample_50-single-arm-electron-2017F": [ "{}/output-data-random-resample_50-electron-2017F.h5".format( base_path_ ) ]
    }
print ( fileNames_bkg_ )

#process_data_random_protons_ = ProcessData( labels=[ label_ ], fileNames={ label_: fileNames_bkg_ }, random_protons=True, runOnMC=False )
process_data_random_protons_ = ProcessData( lepton_type=lepton_type_, labels=labels_, fileNames=fileNames_bkg_, random_protons=True, runOnMC=False )

process_data_random_protons_( apply_fiducial=True, within_aperture=True, select_2protons=False )
