from ProcessDataEvents import *

#lepton_type_ = "muon"
lepton_type_ = "electron"

# data_sample = '2017'
data_sample = '2018'

label__ = "data-{}-{}".format( data_sample, lepton_type_ )

base_path_ = "/eos/home-m/malvesga/SWAN_projects/Antonio_UL/output_events/"
labels_ = []
fileNames_data_ = {}
if data_sample == '2017':
    labels_ = [ label__ ]
    if lepton_type_ == 'muon':
        fileNames_data_[ label__ ] = [
            'output-data-muon-2017B.h5',
            'output-data-muon-2017C.h5',
            'output-data-muon-2017D.h5',
            'output-data-muon-2017E.h5',
            'output-data-muon-2017F.h5'
        ]
    elif lepton_type_ == 'electron':
        fileNames_data_[ label__ ] = [
            'output-data-electron-2017B.h5',
            'output-data-electron-2017C.h5',
            'output-data-electron-2017D.h5',
            'output-data-electron-2017E.h5',
            'output-data-electron-2017F.h5'
        ]
elif data_sample == '2018':
    labels_ = []
    if lepton_type_ == 'muon':
        labels_.append( label__ + "-2018A" )
        fileNames_data_[ ( label__ + "-2018A" ) ] = [ 'output-data-2018-muon-events-2018A.h5' ]
        labels_.append( label__ + "-2018B" )
        fileNames_data_[ ( label__ + "-2018B" ) ] = [ 'output-data-2018-muon-events-2018B.h5' ]
        labels_.append( label__ + "-2018C" )
        fileNames_data_[ ( label__ + "-2018C" ) ] = [ 'output-data-2018-muon-events-2018C.h5' ]
        labels_.append( label__ + "-2018D" )
        fileNames_data_[ ( label__ + "-2018D" ) ] = [ 'output-data-2018-muon-events-2018D.h5' ]
    elif lepton_type_ == 'electron':
        labels_.append( label__ + "-2018A" )
        fileNames_data_[ ( label__ + "-2018A" ) ] = [ 'output-data-2018-electron-events-2018A.h5' ]
        labels_.append( label__ + "-2018B" )
        fileNames_data_[ ( label__ + "-2018B" ) ] = [ 'output-data-2018-electron-events-2018B.h5' ]
        labels_.append( label__ + "-2018C" )
        fileNames_data_[ ( label__ + "-2018C" ) ] = [ 'output-data-2018-electron-events-2018C.h5' ]
        labels_.append( label__ + "-2018D" )
        fileNames_data_[ ( label__ + "-2018D" ) ] = [ 'output-data-2018-electron-events-2018D.h5' ]

for key_ in fileNames_data_:
    fileNames_data_[ key_ ] = [ "{}/{}".format( base_path_, item_ ) for item_ in fileNames_data_[ key_ ] ]
print ( labels_ )
print ( fileNames_data_ )

# output_dir_=""
output_dir_="/eos/home-m/malvesga/SWAN_projects/Antonio_UL/output_events/"
process_data_events_ = ProcessDataEvents( lepton_type=lepton_type_, data_sample=data_sample, labels=labels_, fileNames=fileNames_data_, runOnMC=False, output_dir=output_dir_ )

process_data_events_()
