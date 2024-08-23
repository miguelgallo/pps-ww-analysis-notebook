# import sys
# sys.path.insert( 0, "/afs/cern.ch/work/a/antoniov/env/uproot/lib/python3.6/site-packages" )
# print ( sys.path )

from CreateTable import *
import argparse

parser = argparse.ArgumentParser(description = 'Process data.')
parser.add_argument('--lepton_type', required=False, help = 'Lepton Type.' )
parser.add_argument('--period', required=False, help = 'Period.' )
parser.add_argument('--start', required=False, help = 'Start event.' )
parser.add_argument('--stop', required=False, help = 'Stop event.' )

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

if period_ is None and hasattr( args, "start" ) and args.start is not None and int( args.start ) >= 0:
    raise RuntimeError( "Invalid 'start' argument: set 'period.'" )
if period_ is None and hasattr( args, "stop" ) and args.stop is not None and int( args.stop ) >= 0:
    raise RuntimeError( "Invalid 'stop' argument: set 'period.'" )

start_ = None
if period_ is not None and hasattr( args, "start" ) and args.start is not None and int( args.start ) >= 0:
    start_ = int( args.start )
    print ( "Event start: {}".format( start_ ) ) 
stop_ = None
if period_ is not None and hasattr( args, "stop" ) and args.stop is not None and int( args.stop ) >= 0:
    stop_ = int( args.stop )
    print ( "Event stop: {}".format( stop_ ) ) 

#lepton_type = 'muon'
#lepton_type = 'electron'

#data_sample = '2017'
data_sample = '2018'

# resample_factor = 20
resample_factor = 50
# label = "data-random-resample_20"
# label = "data-random-resample_50"
# label = "data-random-resample_50-{}".format( lepton_type )
label = "data-random-resample_50-{}-{}".format( data_sample, lepton_type_ )

tree_path = "SlimmedNtuple"
# step_size = 50000
#step_size = 20000
step_size = 1000
debug = False

fileNames_data = {}
if data_sample == '2017':
    ranges_crossing_angles = [ 100., 130., 140., 150., 200. ]
    #if lepton_type == 'muon':
    if lepton_type_ == 'muon':
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
    #elif lepton_type == 'electron':
    elif lepton_type_ == 'electron':
        fileNames_data[ "2017B" ] = [
            "/eos/home-a/antoniov/Workspace/analysis/data/PPS/SingleElectron-Run2017B/SingleElectron-Run2017B_merged.root"
        ]
        fileNames_data[ "2017C" ] = [
            "/eos/home-a/antoniov/Workspace/analysis/data/PPS/SingleElectron-Run2017C/SingleElectron-Run2017C_merged.root"
        ]
        fileNames_data[ "2017D" ] = [
            "/eos/home-a/antoniov/Workspace/analysis/data/PPS/SingleElectron-Run2017D/SingleElectron-Run2017D_merged.root"
        ]
        fileNames_data[ "2017E" ] = [
            "/eos/home-a/antoniov/Workspace/analysis/data/PPS/SingleElectron-Run2017E/SingleElectron-Run2017E_merged.root"
        ]
        fileNames_data[ "2017F" ] = [
            "/eos/home-a/antoniov/Workspace/analysis/data/PPS/SingleElectron-Run2017F/SingleElectron-Run2017F_merged.root"
        ]
elif data_sample == '2018':
    ranges_crossing_angles = [ 120., 140., 150., 170. ]
    #if lepton_type == 'muon':
    if lepton_type_ == 'muon':
        fileNames_data[ "2018A" ] = [
            # "/eos/home-a/antoniov/Workspace/analysis/data/PPS/SingleMuon-Run2018A/SingleMuon-Run2018A_merged.root"
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/Data/SingleMuon_UL2018A_MiniAODv2-v3_noduplicates.root"
        ]
        fileNames_data[ "2018B" ] = [
            # "/eos/home-a/antoniov/Workspace/analysis/data/PPS/SingleMuon-Run2018B/SingleMuon-Run2018B_merged.root"
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/Data/SingleMuon_UL2018B_MiniAODv2-v2_noduplicates.root"
        ]
        fileNames_data[ "2018C" ] = [
            # "/eos/home-a/antoniov/Workspace/analysis/data/PPS/SingleMuon-Run2018C/SingleMuon-Run2018C_merged.root"
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/Data/SingleMuon_UL2018C_MiniAODv2-v2_noduplicates.root"
        ]
        fileNames_data[ "2018D" ] = [
            # "/eos/home-a/antoniov/Workspace/analysis/data/PPS/SingleMuon-Run2018D/SingleMuon-Run2018D_merged.root"
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/Data/SingleMuon_UL2018D_MiniAODv2-v3_noduplicates.root"
        ]
    #elif lepton_type == 'electron':
    elif lepton_type_ == 'electron':
        fileNames_data[ "2018A" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/Data/EGamma_UL2018A_MiniAODv2-v1_noduplicates.root"
        ]
        fileNames_data[ "2018B" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/Data/EGamma_UL2018B_MiniAODv2-v1_noduplicates.root"
        ]
        fileNames_data[ "2018C" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/Data/EGamma_UL2018C_MiniAODv2-v1_noduplicates.root"
        ]
        fileNames_data[ "2018D" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/Data/EGamma_UL2018D_MiniAODv2-v2_noduplicates.root"
        ]

if period_ is not None and period_ != "":
    path__ = fileNames_data[ period_ ]
    fileNames_data = {}
    fileNames_data[ period_ ] = path__

output_dir_="/eos/home-m/malvesga/SWAN_projects/Antonio_UL/output-final"
#output_dir_="/eos/home-m/malvesga/SWAN_projects/Antonio_UL/output_new"
# create_table_ = CreateTable( label=label, lepton_type=lepton_type, data_sample=data_sample, fileNames=fileNames_data, tree_path=tree_path, output_dir="output" )
#create_table_ = CreateTable( label=label, lepton_type=lepton_type, data_sample=data_sample, fileNames=fileNames_data, tree_path=tree_path, output_dir=output_dir_ )
create_table_ = CreateTable( label=label, lepton_type=lepton_type_, data_sample=data_sample, fileNames=fileNames_data, tree_path=tree_path, output_dir=output_dir_ )

# create_table_( random_protons=True, resample_factor=resample_factor, step_size=step_size, firstEvent=None, entryStop=None, debug=debug ) 
create_table_( random_protons=True, resample_factor=resample_factor, step_size=step_size, firstEvent=start_, entryStop=stop_, debug=debug, ranges_crossing_angles=ranges_crossing_angles ) 
