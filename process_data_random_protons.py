from ProcessData import *

label_ = "data-random-resample_20"

base_path_ = "/eos/home-a/antoniov/SWAN_projects/pps-ww-analysis/output"
fileNames_bkg = [
    "output-data-random-resample_20-2017B.h5",
    "output-data-random-resample_20-2017C.h5",
    "output-data-random-resample_20-2017D.h5",
    "output-data-random-resample_20-2017E.h5",
    "output-data-random-resample_20-2017F.h5"
]
fileNames_bkg = [ "{}/{}".format( base_path_, item_ ) for item_ in fileNames_bkg ]
print ( fileNames_bkg )

process_data_random_protons_ = ProcessData( labels=[ label_ ], fileNames={ label_: fileNames_bkg }, random_protons=True, runOnMC=False )

process_data_random_protons_( apply_fiducial=True, within_aperture=True, select_2protons=True )
