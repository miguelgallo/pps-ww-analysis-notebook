from ProcessData import *

# lepton_type_ = "muon"
lepton_type_ = "electron"
label_ = "data-single-arm-{}".format( lepton_type_ )

base_path_ = "/eos/home-a/antoniov/SWAN_projects/pps-ww-analysis/output"
fileNames_data_ = []
if lepton_type_ == 'muon':
    fileNames_data_ = [
        'output-data-2017B.h5',
        'output-data-2017C.h5',
        'output-data-2017D.h5',
        'output-data-2017E.h5',
        'output-data-2017F.h5'
    ]
elif lepton_type_ == 'electron':
    fileNames_data_ = [
        'output-data-electron-2017B.h5',
        'output-data-electron-2017C.h5',
        'output-data-electron-2017D.h5',
        'output-data-electron-2017E.h5',
        'output-data-electron-2017F.h5'
    ]
fileNames_data_ = [ "{}/{}".format( base_path_, item_ ) for item_ in fileNames_data_ ]
print ( fileNames_data_ )

process_data_ = ProcessData( lepton_type=lepton_type_, labels=[ label_ ], fileNames={ label_: fileNames_data_ }, runOnMC=False )

process_data_( apply_fiducial=True, within_aperture=True, select_2protons=False )
