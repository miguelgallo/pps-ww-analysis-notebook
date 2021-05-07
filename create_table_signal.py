# import sys
# sys.path.insert( 0, "/afs/cern.ch/work/a/antoniov/env/uproot/lib/python3.6/site-packages" )
# print ( sys.path )

from CreateTable import *

fileNames_A0W_ACW = {}
fileNames_A0W_ACW[ "A0W1e-6" ] = [
    "/eos/user/a/antoniov/Workspace/analysis/data/PPS/GGToWW_bSM-A0W1e-6_13TeV-fpmc-herwig6-signal-proton-propagation-dilepton/200420_160422/0000/SlimmedNtuple_merged_0.root"
]
fileNames_A0W_ACW[ "A0W2e-6" ] = [
    "/eos/user/a/antoniov/Workspace/analysis/data/PPS/GGToWW_bSM-A0W2e-6_13TeV-fpmc-herwig6-signal-proton-propagation-dilepton/200420_160449/0000/SlimmedNtuple_merged_0.root"
]
fileNames_A0W_ACW[ "A0W5e-6" ] = [
    "/eos/user/a/antoniov/Workspace/analysis/data/PPS/GGToWW_bSM-A0W5e-6_13TeV-fpmc-herwig6-signal-proton-propagation-dilepton/200420_160355/0000/SlimmedNtuple_merged_0.root"
]
fileNames_A0W_ACW[ "ACW5e-6" ] = [
    "/eos/user/a/antoniov/Workspace/analysis/data/PPS/GGToWW_bSM-ACW5e-6_13TeV-fpmc-herwig6-signal-proton-propagation-dilepton/200424_185019/0000/SlimmedNtuple_1.root"
]
fileNames_A0W_ACW[ "ACW8e-6" ] = [
    "/eos/user/a/antoniov/Workspace/analysis/data/PPS/GGToWW_bSM-ACW8e-6_13TeV-fpmc-herwig6-signal-proton-propagation-dilepton/200424_185049/0000/SlimmedNtuple_merged_0.root"
]
fileNames_A0W_ACW[ "ACW2e-5" ] = [
    "/eos/user/a/antoniov/Workspace/analysis/data/PPS/GGToWW_bSM-ACW2e-5_13TeV-fpmc-herwig6-signal-proton-propagation-dilepton/200424_185121/0000/SlimmedNtuple_merged_0.root"
]

proton_files = [
    "/eos/home-a/antoniov/Workspace/analysis/data/PPS/SingleMuon-Run2017B-withDilepton/SlimmedNtuple_merged.root",
    "/eos/home-a/antoniov/Workspace/analysis/data/PPS/SingleMuon-Run2017C-withDilepton/SlimmedNtuple_merged.root",
    "/eos/home-a/antoniov/Workspace/analysis/data/PPS/SingleMuon-Run2017D-withDilepton/SlimmedNtuple_merged.root",
    "/eos/home-a/antoniov/Workspace/analysis/data/PPS/SingleMuon-Run2017E-withDilepton/SlimmedNtuple_merged.root",
    "/eos/home-a/antoniov/Workspace/analysis/data/PPS/SingleMuon-Run2017F-withDilepton/SlimmedNtuple_merged.root"
]

step_size = 100000
debug = False

create_table_ = CreateTable( label="GGToWW-AQGC", fileNames=fileNames_A0W_ACW )

create_table_mix_protons_ = CreateTable( label="GGToWW-AQGC-mix_protons", fileNames=fileNames_A0W_ACW )

create_table_( mix_protons=False, runOnMC=True, step_size=step_size, firstEvent=None, entryStop=None, debug=debug ) 

create_table_mix_protons_( mix_protons=True, proton_files=proton_files, runOnMC=True, step_size=step_size, firstEvent=None, entryStop=None, debug=debug)

