# import sys
# sys.path.insert( 0, "/afs/cern.ch/work/a/antoniov/env/uproot/lib/python3.6/site-packages" )
# print ( sys.path )

from CreateTable import *

fileNames_data = {}
fileNames_data[ "2017B" ] = [
    "/eos/home-a/antoniov/Workspace/analysis/data/PPS/SingleMuon-Run2017B-withDilepton/SlimmedNtuple_merged_noduplicates.root"
]
fileNames_data[ "2017C" ] = [
    "/eos/home-a/antoniov/Workspace/analysis/data/PPS/SingleMuon-Run2017C-withDilepton/SlimmedNtuple_merged_noduplicates.root"
]
fileNames_data[ "2017D" ] = [
    "/eos/home-a/antoniov/Workspace/analysis/data/PPS/SingleMuon-Run2017D-withDilepton/SlimmedNtuple_merged_noduplicates.root"
]
fileNames_data[ "2017E" ] = [
    "/eos/home-a/antoniov/Workspace/analysis/data/PPS/SingleMuon-Run2017E-withDilepton/SlimmedNtuple_merged_noduplicates.root"
]
fileNames_data[ "2017F" ] = [
    "/eos/home-a/antoniov/Workspace/analysis/data/PPS/SingleMuon-Run2017F-withDilepton/SlimmedNtuple_merged_noduplicates.root"
]

tree_path = "SlimmedNtuple"
# resample_factor = 20
resample_factor = 50
# label = "data-random-resample_20"
label = "data-random-resample_50"
# step_size = 50000
step_size = 20000
debug = False

create_table_ = CreateTable( label=label, fileNames=fileNames_data, tree_path=tree_path )

create_table_( random_protons=True, resample_factor=resample_factor, step_size=step_size, firstEvent=None, entryStop=None, debug=debug ) 
