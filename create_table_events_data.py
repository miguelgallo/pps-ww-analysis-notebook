# import sys
# sys.path.insert( 0, "/afs/cern.ch/work/a/antoniov/env/uproot/lib/python3.6/site-packages" )
# print ( sys.path )

from CreateTableEvents import *

#lepton_type = 'muon'
lepton_type = 'electron'

#data_sample = '2017'
data_sample = '2018'

label = "data-{}-{}-events".format( data_sample, lepton_type )

tree_path = "SlimmedNtuple"
# tree_path = "demo/SlimmedNtuple"
step_size = 100000
debug = False

fileNames_data = {}
if data_sample == '2017':
    if lepton_type == 'muon':
        fileNames_data[ "2017B" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2017/Data/SingleMuon_UL2017B_MiniAODv2-v1_noduplicates.root"
        ]
        fileNames_data[ "2017C" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2017/Data/SingleMuon_UL2017C_MiniAODv2-v1_noduplicates.root"
        ]
        fileNames_data[ "2017D" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2017/Data/SingleMuon_UL2017D_MiniAODv2-v1_noduplicates.root"
        ]
        fileNames_data[ "2017E" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2017/Data/SingleMuon_UL2017E_MiniAODv2-v1_noduplicates.root"
        ]
        fileNames_data[ "2017F" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2017/Data/SingleMuon_UL2017F_MiniAODv2-v1_noduplicates.root"
        ]
    elif lepton_type == 'electron':
        fileNames_data[ "2017B" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2017/Data/SingleElectron_UL2017B_MiniAODv2-v1_noduplicates.root"
        ]
        fileNames_data[ "2017C" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2017/Data/SingleElectron_UL2017C_MiniAODv2-v1_noduplicates.root"
        ]
        fileNames_data[ "2017D" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2017/Data/SingleElectron_UL2017D_MiniAODv2-v1_noduplicates.root"
        ]
        fileNames_data[ "2017E" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2017/Data/SingleElectron_UL2017E_MiniAODv2-v1_noduplicates.root"
        ]
        fileNames_data[ "2017F" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2017/Data/SingleElectron_UL2017F_MiniAODv2-v1_noduplicates.root"
        ]
elif data_sample == '2018':
    if lepton_type == 'muon':
        fileNames_data[ "2018A" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/Data/SingleMuon_UL2018A_MiniAODv2-v3_noduplicates.root"
        ]
        fileNames_data[ "2018B" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/Data/SingleMuon_UL2018B_MiniAODv2-v2_noduplicates.root"
        ]
        fileNames_data[ "2018C" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/Data/SingleMuon_UL2018C_MiniAODv2-v2_noduplicates.root"
        ]
        fileNames_data[ "2018D" ] = [
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

create_table_ = CreateTableEvents( label=label, lepton_type=lepton_type, data_sample=data_sample, fileNames=fileNames_data, tree_path=tree_path, output_dir="/eos/home-m/malvesga/SWAN_projects/Antonio_UL/output_events" )

create_table_( step_size=step_size, firstEvent=None, entryStop=None, debug=debug )
