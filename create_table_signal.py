# import sys
# sys.path.insert( 0, "/afs/cern.ch/work/a/antoniov/env/uproot/lib/python3.6/site-packages" )
# print ( sys.path )

from CreateTable import *

#lepton_type = 'muon'
lepton_type = 'electron'

# data_sample = '2017'
data_sample = '2018'

# label = "GGToWW-AQGC-{}".format( lepton_type )
label = "GGToWW-AQGC-{}-{}".format( data_sample, lepton_type )

tree_path = "demo/SlimmedNtuple"
step_size = 100000
debug = False
# debug = True

fileNames_A0W_ACW = {}
if data_sample == '2017':
    fileNames_A0W_ACW[ "A0W1e-6" ] = [
        # "/eos/user/a/antoniov/Workspace/analysis/data/PPS/GGToWW_bSM-A0W1e-6_13TeV-fpmc-herwig6-signal-proton-propagation-dilepton/200420_160422/0000/SlimmedNtuple_merged_0.root"
        "/eos/user/a/antoniov/Workspace/analysis/data/PPS/GGToWW_bSM-A0W1e-6_13TeV-fpmc-herwig6-signal-proton-propagation-dilepton/SlimmedNtuple_merged.root"
    ]
    fileNames_A0W_ACW[ "A0W2e-6" ] = [
        # "/eos/user/a/antoniov/Workspace/analysis/data/PPS/GGToWW_bSM-A0W2e-6_13TeV-fpmc-herwig6-signal-proton-propagation-dilepton/200420_160449/0000/SlimmedNtuple_merged_0.root"
        "/eos/user/a/antoniov/Workspace/analysis/data/PPS/GGToWW_bSM-A0W2e-6_13TeV-fpmc-herwig6-signal-proton-propagation-dilepton/SlimmedNtuple_merged.root"
    ]
    fileNames_A0W_ACW[ "A0W5e-6" ] = [
        # "/eos/user/a/antoniov/Workspace/analysis/data/PPS/GGToWW_bSM-A0W5e-6_13TeV-fpmc-herwig6-signal-proton-propagation-dilepton/200420_160355/0000/SlimmedNtuple_merged_0.root"
        "/eos/user/a/antoniov/Workspace/analysis/data/PPS/GGToWW_bSM-A0W5e-6_13TeV-fpmc-herwig6-signal-proton-propagation-dilepton/SlimmedNtuple_merged.root"
    ]
    fileNames_A0W_ACW[ "ACW5e-6" ] = [
        # "/eos/user/a/antoniov/Workspace/analysis/data/PPS/GGToWW_bSM-ACW5e-6_13TeV-fpmc-herwig6-signal-proton-propagation-dilepton/200424_185019/0000/SlimmedNtuple_1.root"
        "/eos/user/a/antoniov/Workspace/analysis/data/PPS/GGToWW_bSM-ACW5e-6_13TeV-fpmc-herwig6-signal-proton-propagation-dilepton/SlimmedNtuple_merged.root"
    ]
    fileNames_A0W_ACW[ "ACW8e-6" ] = [
        # "/eos/user/a/antoniov/Workspace/analysis/data/PPS/GGToWW_bSM-ACW8e-6_13TeV-fpmc-herwig6-signal-proton-propagation-dilepton/200424_185049/0000/SlimmedNtuple_merged_0.root"
        "/eos/user/a/antoniov/Workspace/analysis/data/PPS/GGToWW_bSM-ACW8e-6_13TeV-fpmc-herwig6-signal-proton-propagation-dilepton/SlimmedNtuple_merged.root"
    ]
    fileNames_A0W_ACW[ "ACW2e-5" ] = [
        # "/eos/user/a/antoniov/Workspace/analysis/data/PPS/GGToWW_bSM-ACW2e-5_13TeV-fpmc-herwig6-signal-proton-propagation-dilepton/200424_185121/0000/SlimmedNtuple_merged_0.root"
        "/eos/user/a/antoniov/Workspace/analysis/data/PPS/GGToWW_bSM-ACW2e-5_13TeV-fpmc-herwig6-signal-proton-propagation-dilepton/SlimmedNtuple_merged.root"
    ]
elif data_sample == '2018':
    if lepton_type == 'muon':
        fileNames_A0W_ACW[ "A0W1e-6" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Signal/FPMC_WW_bSM_13tev_a0w_1e-6_aCw_0_semi_pt0.root"
        ]
        fileNames_A0W_ACW[ "A0W2e-6" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Signal/FPMC_WW_bSM_13tev_a0w_2e-6_aCw_0_semi_pt0.root"
        ]
        fileNames_A0W_ACW[ "A0W5e-6" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Signal/FPMC_WW_bSM_13tev_a0w_5e-6_aCw_0_semi_pt0.root"
        ]
        fileNames_A0W_ACW[ "ACW5e-6" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Signal/FPMC_WW_bSM_13tev_a0w_0_aCw_5e-6_semi_pt0.root"
        ]
        fileNames_A0W_ACW[ "ACW8e-6" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Signal/FPMC_WW_bSM_13tev_a0w_0_aCw_8e-6_semi_pt0.root"
        ]
        fileNames_A0W_ACW[ "ACW2e-5" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Signal/FPMC_WW_bSM_13tev_a0w_0_aCw_2e-5_semi_pt0.root"
        ]
    elif lepton_type == 'electron':
        fileNames_A0W_ACW[ "A0W1e-6" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Signal/FPMC_WW_bSM_13tev_a0w_1e-6_aCw_0_semi_pt0.root"
        ]
        fileNames_A0W_ACW[ "A0W2e-6" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Signal/FPMC_WW_bSM_13tev_a0w_2e-6_aCw_0_semi_pt0.root"
        ]
        fileNames_A0W_ACW[ "A0W5e-6" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Signal/FPMC_WW_bSM_13tev_a0w_5e-6_aCw_0_semi_pt0.root"
        ]
        fileNames_A0W_ACW[ "ACW5e-6" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Signal/FPMC_WW_bSM_13tev_a0w_0_aCw_5e-6_semi_pt0.root"
        ]
        fileNames_A0W_ACW[ "ACW8e-6" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Signal/FPMC_WW_bSM_13tev_a0w_0_aCw_8e-6_semi_pt0.root"
        ]
        fileNames_A0W_ACW[ "ACW2e-5" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Signal/FPMC_WW_bSM_13tev_a0w_0_aCw_2e-5_semi_pt0.root"
        ]

# output_dir_=""
output_dir_="/eos/home-m/malvesga/SWAN_projects/Antonio_UL/output"
create_table_ = CreateTable( label=label, lepton_type=lepton_type, data_sample=data_sample, fileNames=fileNames_A0W_ACW, tree_path=tree_path, output_dir=output_dir_ )

create_table_( mix_protons=False, runOnMC=True, step_size=step_size, firstEvent=None, entryStop=None, debug=debug ) 
