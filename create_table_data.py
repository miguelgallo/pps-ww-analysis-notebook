# import sys
# sys.path.insert( 0, "/afs/cern.ch/work/a/antoniov/env/uproot/lib/python3.6/site-packages" )
# print ( sys.path )

from CreateTable import *

lepton_type = 'muon'
#lepton_type = 'electron'

# data_sample = '2017'
data_sample = '2018'

label = "data-{}-{}".format( data_sample, lepton_type )

tree_path = "SlimmedNtuple"
# tree_path = "demo/SlimmedNtuple"
step_size = 100000
debug = False

fileNames_data = {}
if data_sample == '2017':
    ranges_crossing_angles = [ 100., 130., 140., 150., 200. ]
    if lepton_type == 'muon':
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
    elif lepton_type == 'electron':
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
    if lepton_type == 'muon':
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
    elif lepton_type == 'electron':
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

create_table_ = CreateTable( label=label, lepton_type=lepton_type, data_sample=data_sample, fileNames=fileNames_data, tree_path=tree_path, output_dir="/eos/home-m/malvesga/SWAN_projects/Antonio_UL/output-final" )

create_table_( random_protons=False, step_size=step_size, firstEvent=None, entryStop=None, debug=debug, ranges_crossing_angles=ranges_crossing_angles ) 
