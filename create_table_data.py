# import sys
# sys.path.insert( 0, "/afs/cern.ch/work/a/antoniov/env/uproot/lib/python3.6/site-packages" )
# print ( sys.path )

from CreateTable import *

fileNames_data = {}
fileNames_data[ "2017B" ] = [
#     "/eos/user/a/antoniov/Workspace/analysis/data/PPS/SingleMuon-Run2017B-Dilepton/190621_214052/0000/SlimmedNtuple_merged_0.root"
#     "/eos/user/a/antoniov/Workspace/analysis/data/PPS/SingleMuon-Run2017B-withDilepton/0000/SlimmedNtuple_merged_0.root"
    # "/eos/home-a/antoniov/Workspace/analysis/data/PPS/SingleMuon-Run2017B-withDilepton/SlimmedNtuple_merged.root"
    "/eos/home-a/antoniov/Workspace/analysis/data/PPS/SingleMuon-Run2017B-withDilepton/SlimmedNtuple_merged_noduplicates.root"
]
fileNames_data[ "2017C" ] = [
#     "/eos/user/a/antoniov/Workspace/analysis/data/PPS/SingleMuon-Run2017C-Dilepton/190621_214124/0000/SlimmedNtuple_merged_0.root",
#     "/eos/user/a/antoniov/Workspace/analysis/data/PPS/SingleMuon-Run2017C-Dilepton/190621_214124/0000/SlimmedNtuple_merged_1.root"
#     "/eos/user/a/antoniov/Workspace/analysis/data/PPS/SingleMuon-Run2017C-withDilepton/0000/SlimmedNtuple_merged_0.root",
#     "/eos/user/a/antoniov/Workspace/analysis/data/PPS/SingleMuon-Run2017C-withDilepton/0000/SlimmedNtuple_merged_1.root",
#     "/eos/user/a/antoniov/Workspace/analysis/data/PPS/SingleMuon-Run2017C-withDilepton/0001/SlimmedNtuple_merged_0.root"
    # "/eos/home-a/antoniov/Workspace/analysis/data/PPS/SingleMuon-Run2017C-withDilepton/SlimmedNtuple_merged.root"
    "/eos/home-a/antoniov/Workspace/analysis/data/PPS/SingleMuon-Run2017C-withDilepton/SlimmedNtuple_merged_noduplicates.root"
]
fileNames_data[ "2017D" ] = [
#     "/eos/user/a/antoniov/Workspace/analysis/data/PPS/SingleMuon-Run2017D-Dilepton/190621_214154/SlimmedNtuple_merged_0.root"
#     "/eos/user/a/antoniov/Workspace/analysis/data/PPS/SingleMuon-Run2017D-withDilepton/0000/SlimmedNtuple_merged_0.root",
#     "/eos/user/a/antoniov/Workspace/analysis/data/PPS/SingleMuon-Run2017D-withDilepton/0000/SlimmedNtuple_merged_1.root"
    # "/eos/home-a/antoniov/Workspace/analysis/data/PPS/SingleMuon-Run2017D-withDilepton/SlimmedNtuple_merged.root"
    "/eos/home-a/antoniov/Workspace/analysis/data/PPS/SingleMuon-Run2017D-withDilepton/SlimmedNtuple_merged_noduplicates.root"
]
fileNames_data[ "2017E" ] = [
#     "/eos/user/a/antoniov/Workspace/analysis/data/PPS/SingleMuon-Run2017E-Dilepton/190621_214224/0000/SlimmedNtuple_merged_0.root",
#     "/eos/user/a/antoniov/Workspace/analysis/data/PPS/SingleMuon-Run2017E-Dilepton/190621_214224/0000/SlimmedNtuple_merged_1.root"
#     "/eos/user/a/antoniov/Workspace/analysis/data/PPS/SingleMuon-Run2017E-withDilepton/0000/SlimmedNtuple_merged_0.root",
#     "/eos/user/a/antoniov/Workspace/analysis/data/PPS/SingleMuon-Run2017E-withDilepton/0000/SlimmedNtuple_merged_1.root",
#     "/eos/user/a/antoniov/Workspace/analysis/data/PPS/SingleMuon-Run2017E-withDilepton/0001/SlimmedNtuple_merged_0.root"
    # "/eos/home-a/antoniov/Workspace/analysis/data/PPS/SingleMuon-Run2017E-withDilepton/SlimmedNtuple_merged.root"
    "/eos/home-a/antoniov/Workspace/analysis/data/PPS/SingleMuon-Run2017E-withDilepton/SlimmedNtuple_merged_noduplicates.root"
]
fileNames_data[ "2017F" ] = [
#     "/eos/user/a/antoniov/Workspace/analysis/data/PPS/SingleMuon-Run2017F-Dilepton/190621_214253/0000/SlimmedNtuple_merged_0.root",
#     "/eos/user/a/antoniov/Workspace/analysis/data/PPS/SingleMuon-Run2017F-Dilepton/190621_214253/0000/SlimmedNtuple_merged_1.root"
#     "/eos/user/a/antoniov/Workspace/analysis/data/PPS/SingleMuon-Run2017F-Dilepton/190621_214253/0001/SlimmedNtuple_merged_0.root"
#     "/eos/user/a/antoniov/Workspace/analysis/data/PPS/SingleMuon-Run2017F-withDilepton/0000/SlimmedNtuple_merged_0.root",
#     "/eos/user/a/antoniov/Workspace/analysis/data/PPS/SingleMuon-Run2017F-withDilepton/0000/SlimmedNtuple_merged_1.root",
#     "/eos/user/a/antoniov/Workspace/analysis/data/PPS/SingleMuon-Run2017F-withDilepton/0001/SlimmedNtuple_merged_0.root",
#     "/eos/user/a/antoniov/Workspace/analysis/data/PPS/SingleMuon-Run2017F-withDilepton/0001/SlimmedNtuple_merged_1.root",
#     "/eos/user/a/antoniov/Workspace/analysis/data/PPS/SingleMuon-Run2017F-withDilepton/0002/SlimmedNtuple_merged_0.root",
#     "/eos/user/a/antoniov/Workspace/analysis/data/PPS/SingleMuon-Run2017F-withDilepton/0003/SlimmedNtuple_merged_0.root"
    # "/eos/home-a/antoniov/Workspace/analysis/data/PPS/SingleMuon-Run2017F-withDilepton/SlimmedNtuple_merged.root"
    "/eos/home-a/antoniov/Workspace/analysis/data/PPS/SingleMuon-Run2017F-withDilepton/SlimmedNtuple_merged_noduplicates.root"
]

tree_path = "SlimmedNtuple"
step_size = 100000
debug = False

create_table_ = CreateTable( label="data", fileNames=fileNames_data, tree_path=tree_path )

create_table_( random_protons=False, step_size=step_size, firstEvent=None, entryStop=None, debug=debug ) 
