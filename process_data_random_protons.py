from ProcessData import *
import argparse

parser = argparse.ArgumentParser(description = 'Process data.')
parser.add_argument('--lepton_type', required=False, help = 'Lepton Type.' )
parser.add_argument('--period', required=False, help = 'Period.' )
parser.add_argument('--runMin', required=False, help = 'Run min.' )
parser.add_argument('--runMax', required=False, help = 'Run max.' )

args = parser.parse_args()
print ( args )

lepton_type_ = None
if hasattr( args, "lepton_type" ) and args.lepton_type is not None and args.lepton_type != "":
    lepton_type_ = args.lepton_type
    print ( "Lepton Type: " + lepton_type_ ) 

period_ = None
if hasattr( args, "period" ) and args.period is not None and args.period != "":
    period_ = args.period
    print ( "Period: " + period_ ) 

runMin_ = None
if hasattr( args, "runMin" ) and args.runMin is not None and int( args.runMin ) > 0:
    runMin_ = int( args.runMin )
    print ( "runMin: {}".format( runMin_ ) )

runMax_ = None
if hasattr( args, "runMax" ) and args.runMax is not None and int( args.runMax ) > 0:
    runMax_ = int( args.runMax )
    print ( "runMax: {}".format( runMax_ ) )

#lepton_type = "muon"
#lepton_type = "electron"

# data_sample = '2017'
data_sample = '2018'

# period = None
# period = "2018D"

label__ = "data-random-resample_50-{}-{}".format( data_sample, lepton_type_ )
if runMin_ is not None:
    label__ = label__ + "-runMin-{}".format( runMin_ )
if runMax_ is not None:
    label__ = label__ + "-runMax-{}".format( runMax_ )
print( label__ )

base_path_ = "/eos/home-m/malvesga/SWAN_projects/Antonio_UL/output-final"
labels_ = []
fileNames_bkg_ = {}
if data_sample == '2017':
    labels_ = [ label__ ]
    if lepton_type_ == 'muon':
        fileNames_bkg_[ label__ ] = [
            "output-data-random-resample_50-2017B.h5",
            "output-data-random-resample_50-2017C.h5",
            "output-data-random-resample_50-2017D.h5",
            "output-data-random-resample_50-2017E.h5",
            "output-data-random-resample_50-2017F.h5"
        ]
    elif lepton_type_ == 'electron':
        fileNames_bkg_[ label__ ] = [
            "output-data-random-resample_50-electron-2017B.h5",
            "output-data-random-resample_50-electron-2017C.h5",
            "output-data-random-resample_50-electron-2017D.h5",
            "output-data-random-resample_50-electron-2017E.h5",
            "output-data-random-resample_50-electron-2017F.h5"
        ]
elif data_sample == '2018':
    labels_ = []
    if lepton_type_ == 'muon':
        labels_.append( label__ + "-2018A" )
        fileNames_bkg_[ ( label__ + "-2018A" ) ] = [ 'output-data-random-resample_50-2018-muon-2018A.h5' ]
        labels_.append( label__ + "-2018B" )
        fileNames_bkg_[ ( label__ + "-2018B" ) ] = [ 'output-data-random-resample_50-2018-muon-2018B.h5' ]
        labels_.append( label__ + "-2018C" )
        fileNames_bkg_[ ( label__ + "-2018C" ) ] = [ 'output-data-random-resample_50-2018-muon-2018C.h5' ]
        # labels_.append( label__ + "-2018D" )
        # fileNames_bkg_[ ( label__ + "-2018D" ) ] = [ 'output-data-random-resample_50-2018-muon-2018D.h5' ]
        labels_.append( label__ + "-2018D-1" )
        fileNames_bkg_[ labels_[-1] ]  = [ 'output-data-random-resample_50-2018-muon-2018D-0-200000.h5' ]
        labels_.append( label__ + "-2018D-2" )
        fileNames_bkg_[ labels_[-1] ] = [ 'output-data-random-resample_50-2018-muon-2018D-200000-400000.h5' ]
        labels_.append( label__ + "-2018D-3" )
        fileNames_bkg_[ labels_[-1] ] = [ 'output-data-random-resample_50-2018-muon-2018D-400000-600000.h5' ]
        labels_.append( label__ + "-2018D-4" )
        fileNames_bkg_[ labels_[-1] ] = [ 'output-data-random-resample_50-2018-muon-2018D-600000-800000.h5' ]
        labels_.append( label__ + "-2018D-5" )
        fileNames_bkg_[ labels_[-1] ] = [ 'output-data-random-resample_50-2018-muon-2018D-800000-1000000.h5' ]
        labels_.append( label__ + "-2018D-6" )
        fileNames_bkg_[ labels_[-1] ] = [ 'output-data-random-resample_50-2018-muon-2018D-1000000.h5' ]
    elif lepton_type_ == 'electron':
        labels_.append( label__ + "-2018A" )
        fileNames_bkg_[ ( label__ + "-2018A" ) ] = [ 'output-data-random-resample_50-2018-electron-2018A.h5' ]
        labels_.append( label__ + "-2018B" )
        fileNames_bkg_[ ( label__ + "-2018B" ) ] = [ 'output-data-random-resample_50-2018-electron-2018B.h5' ]
        labels_.append( label__ + "-2018C" )
        fileNames_bkg_[ ( label__ + "-2018C" ) ] = [ 'output-data-random-resample_50-2018-electron-2018C.h5' ]
        # labels_.append( label__ + "-2018D" )
        # fileNames_bkg_[ ( label__ + "-2018D" ) ] = [ 'output-data-random-resample_50-2018-electron-2018D.h5' ]
        labels_.append( label__ + "-2018D-1" )
        fileNames_bkg_[ labels_[-1] ] = [ 'output-data-random-resample_50-2018-electron-2018D-0-200000.h5' ]
        labels_.append( label__ + "-2018D-2" )
        fileNames_bkg_[ labels_[-1] ] = [ 'output-data-random-resample_50-2018-electron-2018D-200000-400000.h5' ]
        labels_.append( label__ + "-2018D-3" )
        fileNames_bkg_[ labels_[-1] ] = [ 'output-data-random-resample_50-2018-electron-2018D-400000-600000.h5' ]
        labels_.append( label__ + "-2018D-4" )
        fileNames_bkg_[ labels_[-1] ] = [ 'output-data-random-resample_50-2018-electron-2018D-600000-800000.h5' ]
        labels_.append( label__ + "-2018D-5" )
        fileNames_bkg_[ labels_[-1] ] = [ 'output-data-random-resample_50-2018-electron-2018D-800000-1000000.h5' ]
        labels_.append( label__ + "-2018D-6" )
        fileNames_bkg_[ labels_[-1] ] = [ 'output-data-random-resample_50-2018-electron-2018D-1000000.h5' ]

if period_ is not None and period_ != "":
    labels_ = []
    labels_.append( "{}-{}".format( label__, period_ ) )
    path__ = fileNames_bkg_[ labels_[-1] ]
    fileNames_bkg_ = {}
    fileNames_bkg_[ labels_[-1] ] = path__

for key_ in fileNames_bkg_:
    fileNames_bkg_[ key_ ] = [ "{}/{}".format( base_path_, item_ ) for item_ in fileNames_bkg_[ key_ ] ]
print ( labels_ )
print ( fileNames_bkg_ )

output_dir_="/eos/home-m/malvesga/SWAN_projects/Antonio_UL/output-final"
# process_data_random_protons_ = ProcessData( lepton_type=lepton_type, labels=[ label_ ], fileNames={ label_: fileNames_bkg_ }, random_protons=True, runOnMC=False )
process_data_random_protons_ = ProcessData( lepton_type=lepton_type_, data_sample=data_sample, labels=labels_, fileNames=fileNames_bkg_, random_protons=True, runOnMC=False, output_dir=output_dir_ )

# process_data_random_protons_( apply_fiducial=True, within_aperture=True, select_2protons=True )
process_data_random_protons_( apply_fiducial=True, within_aperture=True, select_2protons=True, runMin=runMin_, runMax=runMax_ )
