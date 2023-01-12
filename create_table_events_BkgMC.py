# import sys
# sys.path.insert( 0, "/afs/cern.ch/work/a/antoniov/env/uproot/lib/python3.6/site-packages" )
# print ( sys.path )

from CreateTableEvents import *

lepton_type = 'muon'
# lepton_type = 'electron'

# data_sample = '2017'
data_sample = '2018'

label = "Bkg-{}-{}".format( data_sample, lepton_type )

tree_path = "demo/SlimmedNtuple"
step_size = 100000
debug = False
# debug = True

fileNames_ = {}
if data_sample == '2017':
	    fileNames_[ "TTJets" ] = [
    ]
elif data_sample == '2018':
    fileNames_[ "TTJets" ] = [
        "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Bkg/TTJets_TuneCP5_13TeV-amcatnloFXFX-pythia8.root"
    ]
    fileNames_[ "ST_s-channel_4f_leptonDecays" ] = [
        "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Bkg/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8.root"
    ]
    #fileNames_[ "ST_t-channel_top_4f_InclusiveDecays" ] = [
    #    "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Bkg/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8.root"
    #]
    fileNames_[ "ST_t-channel_antitop_4f_InclusiveDecays" ] = [
        "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Bkg/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8.root"
    ]
    fileNames_[ "ST_tW_top_5f_inclusiveDecays" ] = [
        "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Bkg/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8.root"
    ]
    fileNames_[ "ST_tW_antitop_5f_inclusiveDecays" ] = [
        "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Bkg/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8.root"
    ]
    fileNames_[ "WJetsToLNu_0J" ] = [
        "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Bkg/WJetsToLNu_0J_TuneCP5_13TeV-amcatnloFXFX-pythia8.root"
    ]
    fileNames_[ "WJetsToLNu_1J" ] = [
        "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Bkg/WJetsToLNu_1J_TuneCP5_13TeV-amcatnloFXFX-pythia8.root"
    ]
    fileNames_[ "WJetsToLNu_2J" ] = [
        "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Bkg/WJetsToLNu_2J_TuneCP5_13TeV-amcatnloFXFX-pythia8.root"
    ]
    fileNames_[ "WW" ] = [
        "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Bkg/WW_TuneCP5_13TeV-pythia8.root"
    ]
    fileNames_[ "WZ" ] = [
        "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Bkg/WZ_TuneCP5_13TeV-pythia8.root"
    ]
    fileNames_[ "ZZ" ] = [
        "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Bkg/ZZ_TuneCP5_13TeV-pythia8.root"
    ]
    fileNames_[ "DYJetsToLL_0J" ] = [
        "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Bkg/DYJetsToLL_0J_TuneCP5_13TeV-amcatnloFXFX-pythia8.root"
    ]
    fileNames_[ "DYJetsToLL_1J" ] = [
        "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Bkg/DYJetsToLL_1J_TuneCP5_13TeV-amcatnloFXFX-pythia8.root"
    ]
    fileNames_[ "DYJetsToLL_2J" ] = [
        "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Bkg/DYJetsToLL_2J_TuneCP5_13TeV-amcatnloFXFX-pythia8.root"
    ]
    fileNames_[ "QCD_Pt_170to300" ] = [
        "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Bkg/QCD_Pt_170to300_TuneCP5_13TeV_pythia8.root"
    ]
    fileNames_[ "QCD_Pt_300to470" ] = [
        "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Bkg/QCD_Pt_300to470_TuneCP5_13TeV_pythia8.root"
    ]
    fileNames_[ "QCD_Pt_470to600" ] = [
        "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Bkg/QCD_Pt_470to600_TuneCP5_13TeV_pythia8.root"
    ]
    #fileNames_[ "QCD_Pt_600to800" ] = [
    #    "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Bkg/QCD_Pt_600to800_TuneCP5_13TeV_pythia8.root"
    #]
    fileNames_[ "QCD_Pt_800to1000" ] = [
        "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Bkg/QCD_Pt_800to1000_TuneCP5_13TeV_pythia8.root"
    ]
    fileNames_[ "QCD_Pt_1000to1400" ] = [
        "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Bkg/QCD_Pt_1000to1400_TuneCP5_13TeV_pythia8.root"
    ]
    fileNames_[ "QCD_Pt_1400to1800" ] = [
        "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Bkg/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8.root"
    ]
    fileNames_[ "QCD_Pt_1800to2400" ] = [
        "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Bkg/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8.root"
    ]
    fileNames_[ "QCD_Pt_2400to3200" ] = [
        "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Bkg/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8.root"
    ]
    fileNames_[ "QCD_Pt_3200toInf" ] = [
        "/eos/cms/store/group/phys_pps/miguelgallo/WW_2018/MC_Bkg/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8.root"
    ]

# output_dir_=""
output_dir_="output"
create_table_events_ = CreateTableEvents( label=label, lepton_type=lepton_type, data_sample=data_sample, fileNames=fileNames_, tree_path=tree_path, output_dir=output_dir_ )

create_table_events_( runOnMC=True, step_size=step_size, firstEvent=None, entryStop=None, debug=debug ) 
