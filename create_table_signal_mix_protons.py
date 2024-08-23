# import sys
# sys.path.insert( 0, "/afs/cern.ch/work/a/antoniov/env/uproot/lib/python3.6/site-packages" )
# print ( sys.path )

from CreateTable import *

lepton_type = 'muon'
#lepton_type = 'electron'

# data_sample = '2017'
data_sample = '2018'

# label = "GGToWW-AQGC-mix_protons-{}".format( lepton_type )
label = "GGToWW-AQGC-mix_protons-{}-{}".format( data_sample, lepton_type )

tree_path = "demo/SlimmedNtuple"
step_size = 100000
debug = False

fileNames_A0W_ACW = {}
proton_files = None
if data_sample == '2017':
    ranges_crossing_angles = [ 100., 130., 140., 150., 200. ]
    fileNames_A0W_ACW[ "A0W1e-6" ] = [
        "/eos/user/a/antoniov/Workspace/analysis/data/PPS/GGToWW_bSM-A0W1e-6_13TeV-fpmc-herwig6-signal-proton-propagation-dilepton/SlimmedNtuple_merged.root"
    ]
    fileNames_A0W_ACW[ "A0W2e-6" ] = [
        "/eos/user/a/antoniov/Workspace/analysis/data/PPS/GGToWW_bSM-A0W2e-6_13TeV-fpmc-herwig6-signal-proton-propagation-dilepton/SlimmedNtuple_merged.root"
    ]
    fileNames_A0W_ACW[ "A0W5e-6" ] = [
        "/eos/user/a/antoniov/Workspace/analysis/data/PPS/GGToWW_bSM-A0W5e-6_13TeV-fpmc-herwig6-signal-proton-propagation-dilepton/SlimmedNtuple_merged.root"
    ]
    fileNames_A0W_ACW[ "ACW5e-6" ] = [
        "/eos/user/a/antoniov/Workspace/analysis/data/PPS/GGToWW_bSM-ACW5e-6_13TeV-fpmc-herwig6-signal-proton-propagation-dilepton/SlimmedNtuple_merged.root"
    ]
    fileNames_A0W_ACW[ "ACW8e-6" ] = [
        "/eos/user/a/antoniov/Workspace/analysis/data/PPS/GGToWW_bSM-ACW8e-6_13TeV-fpmc-herwig6-signal-proton-propagation-dilepton/SlimmedNtuple_merged.root"
    ]
    fileNames_A0W_ACW[ "ACW2e-5" ] = [
        "/eos/user/a/antoniov/Workspace/analysis/data/PPS/GGToWW_bSM-ACW2e-5_13TeV-fpmc-herwig6-signal-proton-propagation-dilepton/SlimmedNtuple_merged.root"
    ]
    
    proton_files = [
        "/eos/home-a/antoniov/Workspace/analysis/data/PPS/SingleMuon-Run2017B-withDilepton/SlimmedNtuple_merged_noduplicates.root",
        "/eos/home-a/antoniov/Workspace/analysis/data/PPS/SingleMuon-Run2017C-withDilepton/SlimmedNtuple_merged_noduplicates.root",
        "/eos/home-a/antoniov/Workspace/analysis/data/PPS/SingleMuon-Run2017D-withDilepton/SlimmedNtuple_merged_noduplicates.root",
        "/eos/home-a/antoniov/Workspace/analysis/data/PPS/SingleMuon-Run2017E-withDilepton/SlimmedNtuple_merged_noduplicates.root",
        "/eos/home-a/antoniov/Workspace/analysis/data/PPS/SingleMuon-Run2017F-withDilepton/SlimmedNtuple_merged_noduplicates.root"
    ]
elif data_sample == '2018':
    #ranges_crossing_angles = [ 120., 140., 150., 170. ]
    ranges_crossing_angles = [ 120., 170. ]
    if lepton_type == 'muon':
        fileNames_A0W_ACW[ "A0W1e-7" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Signal/FPMC_WW_13TeV_a0w_1E-7_aCw_0E0_SemiDecay_pt0.root"
        ]
        fileNames_A0W_ACW[ "A0W2e-7" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Signal/FPMC_WW_13TeV_a0w_2E-7_aCw_0E0_SemiDecay_pt0.root"
        ]
        fileNames_A0W_ACW[ "A0W5e-7" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Signal/FPMC_WW_13TeV_a0w_5E-7_aCw_0E0_SemiDecay_pt0.root"
        ]
        fileNames_A0W_ACW[ "A0W1e-6" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Signal/FPMC_WW_13TeV_a0w_1E-6_aCw_0E0_SemiDecay_pt0.root"
        ]
        fileNames_A0W_ACW[ "A0W2e-6" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Signal/FPMC_WW_13TeV_a0w_2E-6_aCw_0E0_SemiDecay_pt0.root"
        ]
        fileNames_A0W_ACW[ "A0W5e-6" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Signal/FPMC_WW_13TeV_a0w_5E-6_aCw_0E0_SemiDecay_pt0.root"
        ]
        fileNames_A0W_ACW[ "ACW5e-7" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Signal/FPMC_WW_13TeV_a0w_0E0_aCw_5E-7_SemiDecay_pt0.root"
        ]
        fileNames_A0W_ACW[ "ACW1e-6" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Signal/FPMC_WW_13TeV_a0w_0E0_aCw_1E-6_SemiDecay_pt0.root"
        ]
        fileNames_A0W_ACW[ "ACW2e-6" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Signal/FPMC_WW_13TeV_a0w_0E0_aCw_2E-6_SemiDecay_pt0.root"
        ]
        fileNames_A0W_ACW[ "ACW5e-6" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Signal/FPMC_WW_13TeV_a0w_0E0_aCw_5E-6_SemiDecay_pt0.root"
        ]
        fileNames_A0W_ACW[ "ACW1e-5" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Signal/FPMC_WW_13TeV_a0w_0E0_aCw_1E-5_SemiDecay_pt0.root"
        ]
        fileNames_A0W_ACW[ "ACW2e-5" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Signal/FPMC_WW_13TeV_a0w_0E0_aCw_2E-5_SemiDecay_pt0.root"
        ]
    elif lepton_type == 'electron':
        fileNames_A0W_ACW[ "A0W1e-7" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Signal/FPMC_WW_13TeV_a0w_1E-7_aCw_0E0_SemiDecay_pt0.root"
        ]
        fileNames_A0W_ACW[ "A0W2e-7" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Signal/FPMC_WW_13TeV_a0w_2E-7_aCw_0E0_SemiDecay_pt0.root"
        ]
        fileNames_A0W_ACW[ "A0W5e-7" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Signal/FPMC_WW_13TeV_a0w_5E-7_aCw_0E0_SemiDecay_pt0.root"
        ]
        fileNames_A0W_ACW[ "A0W1e-6" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Signal/FPMC_WW_13TeV_a0w_1E-6_aCw_0E0_SemiDecay_pt0.root"
        ]
        fileNames_A0W_ACW[ "A0W2e-6" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Signal/FPMC_WW_13TeV_a0w_2E-6_aCw_0E0_SemiDecay_pt0.root"
        ]
        fileNames_A0W_ACW[ "A0W5e-6" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Signal/FPMC_WW_13TeV_a0w_5E-6_aCw_0E0_SemiDecay_pt0.root"
        ]
        fileNames_A0W_ACW[ "ACW5e-7" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Signal/FPMC_WW_13TeV_a0w_0E0_aCw_5E-7_SemiDecay_pt0.root"
        ]
        fileNames_A0W_ACW[ "ACW1e-6" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Signal/FPMC_WW_13TeV_a0w_0E0_aCw_1E-6_SemiDecay_pt0.root"
        ]
        fileNames_A0W_ACW[ "ACW2e-6" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Signal/FPMC_WW_13TeV_a0w_0E0_aCw_2E-6_SemiDecay_pt0.root"
        ]
        fileNames_A0W_ACW[ "ACW5e-6" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Signal/FPMC_WW_13TeV_a0w_0E0_aCw_5E-6_SemiDecay_pt0.root"
        ]
        fileNames_A0W_ACW[ "ACW1e-5" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Signal/FPMC_WW_13TeV_a0w_0E0_aCw_1E-5_SemiDecay_pt0.root"
        ]
        fileNames_A0W_ACW[ "ACW2e-5" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Signal/FPMC_WW_13TeV_a0w_0E0_aCw_2E-5_SemiDecay_pt0.root"
        ]

    proton_files = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/Data/SingleMuon_UL2018A_MiniAODv2-v3_noduplicates.root",
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/Data/SingleMuon_UL2018B_MiniAODv2-v2_noduplicates.root",
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/Data/SingleMuon_UL2018C_MiniAODv2-v2_noduplicates.root",
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/Data/SingleMuon_UL2018D_MiniAODv2-v3_noduplicates.root"
    ]

#output_dir_="output_test"
output_dir_="/eos/home-m/malvesga/SWAN_projects/Antonio_UL/output-final"
# create_table_mix_protons_ = CreateTable( label=label, data_sample=data_sample, lepton_type=lepton_type, fileNames=fileNames_A0W_ACW, tree_path=tree_path, output_dir="output" )
create_table_mix_protons_ = CreateTable( label=label, data_sample=data_sample, lepton_type=lepton_type, fileNames=fileNames_A0W_ACW, tree_path=tree_path, output_dir=output_dir_ )

create_table_mix_protons_( mix_protons=True, proton_files=proton_files, runOnMC=True, step_size=step_size, firstEvent=None, entryStop=None, debug=debug, ranges_crossing_angles=ranges_crossing_angles )
