from ProcessData import *

# lepton_type = "muon"
lepton_type = "electron"

# data_sample = '2017'
data_sample = '2018'

# period = None
period = "2018D"

label__ = "data-random-resample_50-{}-{}".format( data_sample, lepton_type )

base_path_ = "/eos/home-a/antoniov/SWAN_projects/pps-ww-analysis/output"
labels_ = []
fileNames_bkg_ = {}
if data_sample == '2017':
    labels_ = [ label__ ]
    if lepton_type == 'muon':
        fileNames_bkg_[ label__ ] = [
            "output-data-random-resample_50-2017B.h5",
            "output-data-random-resample_50-2017C.h5",
            "output-data-random-resample_50-2017D.h5",
            "output-data-random-resample_50-2017E.h5",
            "output-data-random-resample_50-2017F.h5"
        ]
    elif lepton_type == 'electron':
        fileNames_bkg_[ label__ ] = [
            "output-data-random-resample_50-electron-2017B.h5",
            "output-data-random-resample_50-electron-2017C.h5",
            "output-data-random-resample_50-electron-2017D.h5",
            "output-data-random-resample_50-electron-2017E.h5",
            "output-data-random-resample_50-electron-2017F.h5"
        ]
elif data_sample == '2018':
    labels_ = []
    if lepton_type == 'muon':
        labels_.append( label__ + "-2018A" )
        fileNames_bkg_[ ( label__ + "-2018A" ) ] = [ 'output-data-random-resample_50-2018-muon-2018A.h5' ]
        labels_.append( label__ + "-2018B" )
        fileNames_bkg_[ ( label__ + "-2018B" ) ] = [ 'output-data-random-resample_50-2018-muon-2018B.h5' ]
        labels_.append( label__ + "-2018C" )
        fileNames_bkg_[ ( label__ + "-2018C" ) ] = [ 'output-data-random-resample_50-2018-muon-2018C.h5' ]
        labels_.append( label__ + "-2018D" )
        fileNames_bkg_[ ( label__ + "-2018D" ) ] = [ 'output-data-random-resample_50-2018-muon-2018D.h5' ]
    elif lepton_type == 'electron':
        labels_.append( label__ + "-2018A" )
        fileNames_bkg_[ ( label__ + "-2018A" ) ] = [ 'output-data-random-resample_50-2018-electron-2018A.h5' ]
        labels_.append( label__ + "-2018B" )
        fileNames_bkg_[ ( label__ + "-2018B" ) ] = [ 'output-data-random-resample_50-2018-electron-2018B.h5' ]
        labels_.append( label__ + "-2018C" )
        fileNames_bkg_[ ( label__ + "-2018C" ) ] = [ 'output-data-random-resample_50-2018-electron-2018C.h5' ]
        labels_.append( label__ + "-2018D" )
        fileNames_bkg_[ ( label__ + "-2018D" ) ] = [ 'output-data-random-resample_50-2018-electron-2018D.h5' ]

if period is not None:
    labels_ = []
    labels_.append( "{}-{}".format( label__, period ) )
    path__ = fileNames_bkg_[ labels_[-1] ]
    fileNames_bkg_ = {}
    fileNames_bkg_[ labels_[-1] ] = path__

for key_ in fileNames_bkg_:
    fileNames_bkg_[ key_ ] = [ "{}/{}".format( base_path_, item_ ) for item_ in fileNames_bkg_[ key_ ] ]
print ( labels_ )
print ( fileNames_bkg_ )

output_dir_=""
# process_data_random_protons_ = ProcessData( lepton_type=lepton_type, labels=[ label_ ], fileNames={ label_: fileNames_bkg_ }, random_protons=True, runOnMC=False )
process_data_random_protons_ = ProcessData( lepton_type=lepton_type, data_sample=data_sample, labels=labels_, fileNames=fileNames_bkg_, random_protons=True, runOnMC=False, output_dir=output_dir_ )

process_data_random_protons_( apply_fiducial=True, within_aperture=True, select_2protons=True )
