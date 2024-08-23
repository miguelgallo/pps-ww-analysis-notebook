# import sys
# sys.path.insert( 0, "/afs/cern.ch/work/a/antoniov/env/uproot/lib/python3.6/site-packages" )
# print ( sys.path )

from CreateTable import *

lepton_type = 'muon'
#lepton_type = 'electron'

# data_sample = '2017'
data_sample = '2018'

# label = "GGToWW-AQGC-{}".format( lepton_type )
label = "Bkg-{}-{}".format( data_sample, lepton_type )

tree_path = "demo/SlimmedNtuple"
step_size = 100000
debug = False
# debug = True

fileNames_A0W_ACW = {}
if data_sample == '2017':
    ranges_crossing_angles = [ 100., 130., 140., 150., 200. ]
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
    ranges_crossing_angles = [ 120., 170. ]
    if lepton_type == 'muon':
        fileNames_A0W_ACW[ "DYJetsToLL_0J" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Bkg/DYJetsToLL_0J_TuneCP5_13TeV-amcatnloFXFX-pythia8.root"
        ]
        fileNames_A0W_ACW[ "DYJetsToLL_1J" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Bkg/DYJetsToLL_1J_TuneCP5_13TeV-amcatnloFXFX-pythia8.root"
        ]
        fileNames_A0W_ACW[ "DYJetsToLL_2J" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Bkg/DYJetsToLL_2J_TuneCP5_13TeV-amcatnloFXFX-pythia8.root"
        ]
        fileNames_A0W_ACW[ "QCD_Pt_170to300" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Bkg/QCD_Pt_170to300_TuneCP5_13TeV_pythia8.root"
        ]
        fileNames_A0W_ACW[ "QCD_Pt_300to470" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Bkg/QCD_Pt_300to470_TuneCP5_13TeV_pythia8.root"
        ]
        fileNames_A0W_ACW[ "QCD_Pt_470to600" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Bkg/QCD_Pt_470to600_TuneCP5_13TeV_pythia8.root"
        ]
        fileNames_A0W_ACW[ "QCD_Pt_600to800" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Bkg/QCD_Pt_600to800_TuneCP5_13TeV_pythia8.root"
        ]
        fileNames_A0W_ACW[ "QCD_Pt_800to1000" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Bkg/QCD_Pt_800to1000_TuneCP5_13TeV_pythia8.root"
        ]
        fileNames_A0W_ACW[ "QCD_Pt_1000to1400" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Bkg/QCD_Pt_1000to1400_TuneCP5_13TeV_pythia8.root"
        ]
        fileNames_A0W_ACW[ "QCD_Pt_1400to1800" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Bkg/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8.root"
        ]
        fileNames_A0W_ACW[ "QCD_Pt_1800to2400" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Bkg/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8.root"
        ]
        fileNames_A0W_ACW[ "QCD_Pt_2400to3200" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Bkg/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8.root"
        ]
        fileNames_A0W_ACW[ "QCD_Pt_3200toInf" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Bkg/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8.root"
        ]
        fileNames_A0W_ACW[ "ST_s-channel_4f_leptonDecays" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Bkg/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8.root"
        ]
        fileNames_A0W_ACW[ "ST_t-channel_antitop_4f_InclusiveDecays" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Bkg/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8.root"
        ]
        fileNames_A0W_ACW[ "ST_t-channel_top_4f_InclusiveDecays" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Bkg/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8.root"
        ]
        fileNames_A0W_ACW[ "ST_tW_antitop_5f_inclusiveDecays" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Bkg/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8.root"
        ]
        fileNames_A0W_ACW[ "ST_tW_top_5f_inclusiveDecays" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Bkg/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8.root"
        ]
        fileNames_A0W_ACW[ "TTJets" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Bkg/TTJets_TuneCP5_13TeV-amcatnloFXFX-pythia8.root"
        ]
        fileNames_A0W_ACW[ "WJetsToLNu_0J" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Bkg/WJetsToLNu_0J_TuneCP5_13TeV-amcatnloFXFX-pythia8.root"
        ]
        fileNames_A0W_ACW[ "WJetsToLNu_1J" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Bkg/WJetsToLNu_1J_TuneCP5_13TeV-amcatnloFXFX-pythia8.root"
        ]
        fileNames_A0W_ACW[ "WJetsToLNu_2J" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Bkg/WJetsToLNu_2J_TuneCP5_13TeV-amcatnloFXFX-pythia8.root"
        ]
        fileNames_A0W_ACW[ "WW" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Bkg/WW_TuneCP5_13TeV-pythia8.root"
        ]
        fileNames_A0W_ACW[ "WZ" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Bkg/WZ_TuneCP5_13TeV-pythia8.root"
        ]
        fileNames_A0W_ACW[ "ZZ" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Bkg/ZZ_TuneCP5_13TeV-pythia8.root"
        ]
    elif lepton_type == 'electron':
        fileNames_A0W_ACW[ "DYJetsToLL_0J" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Bkg/DYJetsToLL_0J_TuneCP5_13TeV-amcatnloFXFX-pythia8.root"
        ]
        fileNames_A0W_ACW[ "DYJetsToLL_1J" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Bkg/DYJetsToLL_1J_TuneCP5_13TeV-amcatnloFXFX-pythia8.root"
        ]
        fileNames_A0W_ACW[ "DYJetsToLL_2J" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Bkg/DYJetsToLL_2J_TuneCP5_13TeV-amcatnloFXFX-pythia8.root"
        ]
        fileNames_A0W_ACW[ "QCD_Pt_170to300" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Bkg/QCD_Pt_170to300_TuneCP5_13TeV_pythia8.root"
        ]
        fileNames_A0W_ACW[ "QCD_Pt_300to470" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Bkg/QCD_Pt_300to470_TuneCP5_13TeV_pythia8.root"
        ]
        fileNames_A0W_ACW[ "QCD_Pt_470to600" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Bkg/QCD_Pt_470to600_TuneCP5_13TeV_pythia8.root"
        ]
        fileNames_A0W_ACW[ "QCD_Pt_600to800" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Bkg/QCD_Pt_600to800_TuneCP5_13TeV_pythia8.root"
        ]
        fileNames_A0W_ACW[ "QCD_Pt_800to1000" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Bkg/QCD_Pt_800to1000_TuneCP5_13TeV_pythia8.root"
        ]
        fileNames_A0W_ACW[ "QCD_Pt_1000to1400" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Bkg/QCD_Pt_1000to1400_TuneCP5_13TeV_pythia8.root"
        ]
        fileNames_A0W_ACW[ "QCD_Pt_1400to1800" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Bkg/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8.root"
        ]
        fileNames_A0W_ACW[ "QCD_Pt_1800to2400" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Bkg/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8.root"
        ]
        fileNames_A0W_ACW[ "QCD_Pt_2400to3200" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Bkg/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8.root"
        ]
        fileNames_A0W_ACW[ "QCD_Pt_3200toInf" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Bkg/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8.root"
        ]
        fileNames_A0W_ACW[ "ST_s-channel_4f_leptonDecays" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Bkg/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8.root"
        ]
        fileNames_A0W_ACW[ "ST_t-channel_antitop_4f_InclusiveDecays" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Bkg/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8.root"
        ]
        fileNames_A0W_ACW[ "ST_t-channel_top_4f_InclusiveDecays" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Bkg/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8.root"
        ]
        fileNames_A0W_ACW[ "ST_tW_antitop_5f_inclusiveDecays" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Bkg/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8.root"
        ]
        fileNames_A0W_ACW[ "ST_tW_top_5f_inclusiveDecays" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Bkg/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8.root"
        ]
        fileNames_A0W_ACW[ "TTJets" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Bkg/TTJets_TuneCP5_13TeV-amcatnloFXFX-pythia8.root"
        ]
        fileNames_A0W_ACW[ "WJetsToLNu_0J" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Bkg/WJetsToLNu_0J_TuneCP5_13TeV-amcatnloFXFX-pythia8.root"
        ]
        fileNames_A0W_ACW[ "WJetsToLNu_1J" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Bkg/WJetsToLNu_1J_TuneCP5_13TeV-amcatnloFXFX-pythia8.root"
        ]
        fileNames_A0W_ACW[ "WJetsToLNu_2J" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Bkg/WJetsToLNu_2J_TuneCP5_13TeV-amcatnloFXFX-pythia8.root"
        ]
        fileNames_A0W_ACW[ "WW" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Bkg/WW_TuneCP5_13TeV-pythia8.root"
        ]
        fileNames_A0W_ACW[ "WZ" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Bkg/WZ_TuneCP5_13TeV-pythia8.root"
        ]
        fileNames_A0W_ACW[ "ZZ" ] = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Bkg/ZZ_TuneCP5_13TeV-pythia8.root"
        ]

# output_dir_=""
output_dir_="/eos/home-m/malvesga/SWAN_projects/Antonio_UL/output-final"
create_table_ = CreateTable( label=label, lepton_type=lepton_type, data_sample=data_sample, fileNames=fileNames_A0W_ACW, tree_path=tree_path, output_dir=output_dir_ )

create_table_( mix_protons=False, runOnMC=True, step_size=step_size, firstEvent=None, entryStop=None, debug=debug, ranges_crossing_angles=ranges_crossing_angles ) 
