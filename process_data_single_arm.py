from ProcessData import *

label_ = "data-single-arm"

base_path_ = "/eos/home-a/antoniov/SWAN_projects/pps-ww-analysis/output"
fileNames_data = [
    'output-data-2017B.h5',
    'output-data-2017C.h5',
    'output-data-2017D.h5',
    'output-data-2017E.h5',
    'output-data-2017F.h5'
]
fileNames_data = [ "{}/{}".format( base_path_, item_ ) for item_ in fileNames_data ]
print ( fileNames_data )

process_data_ = ProcessData( labels=[ label_ ], fileNames={ label_: fileNames_data }, runOnMC=False )

process_data_( apply_fiducial=True, within_aperture=True, select_2protons=False )
