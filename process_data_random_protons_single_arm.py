from ProcessData import *

# label_ = "data-random-resample_20-single-arm"
# label_ = "data-random-resample_50-single-arm"

base_path_ = "/eos/home-a/antoniov/SWAN_projects/pps-ww-analysis/output"
# fileNames_bkg = [
#     "output-data-random-resample_20-2017B.h5",
#     "output-data-random-resample_20-2017C.h5",
#     "output-data-random-resample_20-2017D.h5",
#     "output-data-random-resample_20-2017E.h5",
#     "output-data-random-resample_20-2017F.h5"
# ]
# fileNames_bkg = [
#     "output-data-random-resample_50-2017B.h5",
#     "output-data-random-resample_50-2017C.h5",
#     "output-data-random-resample_50-2017D.h5",
#     "output-data-random-resample_50-2017E.h5",
#     "output-data-random-resample_50-2017F.h5"
# ]
# fileNames_bkg = [ "{}/{}".format( base_path_, item_ ) for item_ in fileNames_bkg ]
labels = [
    "data-random-resample_50-single-arm-2017B",
    "data-random-resample_50-single-arm-2017C",
    "data-random-resample_50-single-arm-2017D",
    "data-random-resample_50-single-arm-2017E",
    "data-random-resample_50-single-arm-2017F"
]
fileNames_bkg = {
    "data-random-resample_50-single-arm-2017B": [ "{}/output-data-random-resample_50-2017B.h5".format( base_path_ ) ],
    "data-random-resample_50-single-arm-2017C": [ "{}/output-data-random-resample_50-2017C.h5".format( base_path_ ) ],
    "data-random-resample_50-single-arm-2017D": [ "{}/output-data-random-resample_50-2017D.h5".format( base_path_ ) ],
    "data-random-resample_50-single-arm-2017E": [ "{}/output-data-random-resample_50-2017E.h5".format( base_path_ ) ],
    "data-random-resample_50-single-arm-2017F": [ "{}/output-data-random-resample_50-2017F.h5".format( base_path_ ) ]
}
print ( fileNames_bkg )

#process_data_random_protons_ = ProcessData( labels=[ label_ ], fileNames={ label_: fileNames_bkg }, random_protons=True, runOnMC=False )
process_data_random_protons_ = ProcessData( labels=labels, fileNames=fileNames_bkg, random_protons=True, runOnMC=False )

process_data_random_protons_( apply_fiducial=True, within_aperture=True, select_2protons=False )
