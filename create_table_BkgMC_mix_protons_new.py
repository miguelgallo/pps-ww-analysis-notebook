# import sys
# sys.path.insert( 0, "/afs/cern.ch/work/a/antoniov/env/uproot/lib/python3.6/site-packages" )
# print ( sys.path )

from CreateTable import *
import argparse

parser = argparse.ArgumentParser(description = 'Process BkgMC with mix protons.')
parser.add_argument('--lepton_type', required=False, help = 'Lepton Type.' )
parser.add_argument('--sample', required=False, help = 'Sample.' )

args = parser.parse_args()
print ( args )

lepton_type_ = None
if hasattr( args, "lepton_type" ) and args.lepton_type is not None and args.lepton_type != "":
    lepton_type_ = args.lepton_type
    print ( "Lepton Type: " + lepton_type_ ) 

sample_ = None
if hasattr( args, "sample" ) and args.sample is not None and args.sample != "":
    sample_ = args.sample
    print ( "Sample: " + sample_ ) 

#lepton_type = 'muon'
#lepton_type = 'electron'

# data_sample = '2017'
data_sample = '2018'

# label = "GGToWW-AQGC-mix_protons-{}".format( lepton_type )
label = "Bkg-mix_protons-{}-{}".format( data_sample, lepton_type_ )

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
    ranges_crossing_angles = [ 120., 170. ]
    if lepton_type_ == 'muon':
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
        
    elif lepton_type_ == 'electron':
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

    proton_files = [
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/Data/EGamma_UL2018A_MiniAODv2-v1_noduplicates.root",
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/Data/EGamma_UL2018B_MiniAODv2-v1_noduplicates.root",
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/Data/EGamma_UL2018C_MiniAODv2-v1_noduplicates.root",
            "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/Data/EGamma_UL2018D_MiniAODv2-v2_noduplicates.root"
    ]

if sample_ is not None and sample_ != "":
    path__ = fileNames_A0W_ACW[ sample_ ]
    fileNames_A0W_ACW = {}
    fileNames_A0W_ACW[ sample_ ] = path__

output_dir_="/eos/home-m/malvesga/SWAN_projects/Antonio_UL/output-final"
# create_table_mix_protons_ = CreateTable( label=label, data_sample=data_sample, lepton_type=lepton_type, fileNames=fileNames_A0W_ACW, tree_path=tree_path, output_dir="output" )
create_table_mix_protons_ = CreateTable( label=label, data_sample=data_sample, lepton_type=lepton_type_, fileNames=fileNames_A0W_ACW, tree_path=tree_path, output_dir=output_dir_ )

create_table_mix_protons_( mix_protons=True, proton_files=proton_files, runOnMC=True, step_size=step_size, firstEvent=None, entryStop=None, debug=debug, ranges_crossing_angles=ranges_crossing_angles )
