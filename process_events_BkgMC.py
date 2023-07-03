from ProcessDataEvents import *

#lepton_type = "muon"
lepton_type = "electron"

# data_sample = '2017'
data_sample = '2018'

# use_hash_index_ = True

base_path_ = "/eos/home-m/malvesga/SWAN_projects/Antonio_UL/output_events"
labels_ = []
fileNames_ = {}
if data_sample == '2017':
    if lepton_type == 'muon':
        labels_ = [ ]
        fileNames_ = {
            }
    elif lepton_type == 'electron':
        labels_ = [ ]
        fileNames_ = {
            }
elif data_sample == '2018':
    if lepton_type == 'muon':
        labels_ = [ "Bkg-2018-muon-TTJets", "Bkg-2018-muon-WJetsToLNu_0J", "Bkg-2018-muon-WJetsToLNu_1J", "Bkg-2018-muon-WJetsToLNu_2J", "Bkg-2018-muon-ST_s-channel_4f_leptonDecays", "Bkg-2018-muon-ST_t-channel_antitop_4f_InclusiveDecays", "Bkg-2018-muon-ST_tW_antitop_5f_inclusiveDecays", "Bkg-2018-muon-ST_tW_top_5f_inclusiveDecays", "Bkg-2018-muon-DYJetsToLL_0J", "Bkg-2018-muon-DYJetsToLL_1J", "Bkg-2018-muon-DYJetsToLL_2J", "Bkg-2018-muon-QCD_Pt_170to300", "Bkg-2018-muon-QCD_Pt_300to470", "Bkg-2018-muon-QCD_Pt_470to600", "Bkg-2018-muon-QCD_Pt_800to1000", "Bkg-2018-muon-QCD_Pt_1000to1400", "Bkg-2018-muon-QCD_Pt_1400to1800", "Bkg-2018-muon-QCD_Pt_1800to2400", "Bkg-2018-muon-QCD_Pt_2400to3200", "Bkg-2018-muon-QCD_Pt_3200toInf", "Bkg-2018-muon-QCD_Pt_600to800", "Bkg-2018-muon-ST_t-channel_top_4f_InclusiveDecays", "Bkg-2018-muon-WW", "Bkg-2018-muon-WZ", "Bkg-2018-muon-ZZ"]
        #labels_ = [ "Bkg-2018-muon-WJetsToLNu_0J", "Bkg-2018-muon-WJetsToLNu_1J", "Bkg-2018-muon-WJetsToLNu_2J" ]
        #labels_ = [ "Bkg-2018-muon-QCD_Pt_600to800", "Bkg-2018-muon-ST_t-channel_top_4f_InclusiveDecays", "Bkg-2018-muon-WW", "Bkg-2018-muon-WZ", "Bkg-2018-muon-ZZ" ]
        fileNames_ = {
            "Bkg-2018-muon-TTJets": [ "output-Bkg-2018-muon-TTJets.h5" ],
            "Bkg-2018-muon-WJetsToLNu_0J": [ "output-Bkg-2018-muon-WJetsToLNu_0J.h5" ],
            "Bkg-2018-muon-WJetsToLNu_1J": [ "output-Bkg-2018-muon-WJetsToLNu_1J.h5" ],
            "Bkg-2018-muon-WJetsToLNu_2J": [ "output-Bkg-2018-muon-WJetsToLNu_2J.h5" ],
            "Bkg-2018-muon-WW": [ "output-Bkg-2018-muon-WW.h5" ],
            "Bkg-2018-muon-WZ": [ "output-Bkg-2018-muon-WZ.h5" ],
            "Bkg-2018-muon-ZZ": [ "output-Bkg-2018-muon-ZZ.h5" ],
            "Bkg-2018-muon-ST_s-channel_4f_leptonDecays": [ "output-Bkg-2018-muon-ST_s-channel_4f_leptonDecays.h5" ],
            "Bkg-2018-muon-ST_t-channel_antitop_4f_InclusiveDecays": [ "output-Bkg-2018-muon-ST_t-channel_antitop_4f_InclusiveDecays.h5" ],
            "Bkg-2018-muon-ST_t-channel_top_4f_InclusiveDecays": [ "output-Bkg-2018-muon-ST_t-channel_top_4f_InclusiveDecays.h5" ],
            "Bkg-2018-muon-ST_tW_antitop_5f_inclusiveDecays": [ "output-Bkg-2018-muon-ST_tW_antitop_5f_inclusiveDecays.h5" ],
            "Bkg-2018-muon-ST_tW_top_5f_inclusiveDecays": [ "output-Bkg-2018-muon-ST_tW_top_5f_inclusiveDecays.h5" ],
            "Bkg-2018-muon-DYJetsToLL_0J": [ "output-Bkg-2018-muon-DYJetsToLL_0J.h5" ],
            "Bkg-2018-muon-DYJetsToLL_1J": [ "output-Bkg-2018-muon-DYJetsToLL_1J.h5" ],
            "Bkg-2018-muon-DYJetsToLL_2J": [ "output-Bkg-2018-muon-DYJetsToLL_2J.h5" ],
            "Bkg-2018-muon-QCD_Pt_170to300": [ "output-Bkg-2018-muon-QCD_Pt_170to300.h5" ],
            "Bkg-2018-muon-QCD_Pt_300to470": [ "output-Bkg-2018-muon-QCD_Pt_300to470.h5" ],
            "Bkg-2018-muon-QCD_Pt_470to600": [ "output-Bkg-2018-muon-QCD_Pt_470to600.h5" ],
            "Bkg-2018-muon-QCD_Pt_600to800": [ "output-Bkg-2018-muon-QCD_Pt_600to800.h5" ],
            "Bkg-2018-muon-QCD_Pt_800to1000": [ "output-Bkg-2018-muon-QCD_Pt_800to1000.h5" ],
            "Bkg-2018-muon-QCD_Pt_1000to1400": [ "output-Bkg-2018-muon-QCD_Pt_1000to1400.h5" ],
            "Bkg-2018-muon-QCD_Pt_1400to1800": [ "output-Bkg-2018-muon-QCD_Pt_1400to1800.h5" ],
            "Bkg-2018-muon-QCD_Pt_1800to2400": [ "output-Bkg-2018-muon-QCD_Pt_1800to2400.h5" ],
            "Bkg-2018-muon-QCD_Pt_2400to3200": [ "output-Bkg-2018-muon-QCD_Pt_2400to3200.h5" ],
            "Bkg-2018-muon-QCD_Pt_3200toInf": [ "output-Bkg-2018-muon-QCD_Pt_3200toInf.h5" ],
            }
    elif lepton_type == 'electron':
        labels_ = [ "Bkg-2018-electron-TTJets", "Bkg-2018-electron-WJetsToLNu_0J", "Bkg-2018-electron-WJetsToLNu_1J", "Bkg-2018-electron-WJetsToLNu_2J", "Bkg-2018-electron-ST_s-channel_4f_leptonDecays", "Bkg-2018-electron-ST_t-channel_antitop_4f_InclusiveDecays", "Bkg-2018-electron-ST_tW_antitop_5f_inclusiveDecays", "Bkg-2018-electron-ST_tW_top_5f_inclusiveDecays", "Bkg-2018-electron-DYJetsToLL_0J", "Bkg-2018-electron-DYJetsToLL_1J", "Bkg-2018-electron-DYJetsToLL_2J", "Bkg-2018-electron-QCD_Pt_170to300", "Bkg-2018-electron-QCD_Pt_300to470", "Bkg-2018-electron-QCD_Pt_470to600", "Bkg-2018-electron-QCD_Pt_800to1000", "Bkg-2018-electron-QCD_Pt_1000to1400", "Bkg-2018-electron-QCD_Pt_1400to1800", "Bkg-2018-electron-QCD_Pt_1800to2400", "Bkg-2018-electron-QCD_Pt_2400to3200", "Bkg-2018-electron-QCD_Pt_3200toInf","Bkg-2018-electron-QCD_Pt_600to800", "Bkg-2018-electron-ST_t-channel_top_4f_InclusiveDecays", "Bkg-2018-electron-WW", "Bkg-2018-electron-WZ", "Bkg-2018-electron-ZZ"]
        #labels_ = [ "Bkg-2018-electron-WJetsToLNu_0J", "Bkg-2018-electron-WJetsToLNu_1J", "Bkg-2018-electron-WJetsToLNu_2J" ]
        #labels_ = [ "Bkg-2018-electron-QCD_Pt_600to800", "Bkg-2018-electron-ST_t-channel_top_4f_InclusiveDecays", "Bkg-2018-electron-WW", "Bkg-2018-electron-WZ", "Bkg-2018-electron-ZZ" ]
        fileNames_ = {
            "Bkg-2018-electron-TTJets": [ "output-Bkg-2018-electron-TTJets.h5" ],
            "Bkg-2018-electron-WJetsToLNu_0J": [ "output-Bkg-2018-electron-WJetsToLNu_0J.h5" ],
            "Bkg-2018-electron-WJetsToLNu_1J": [ "output-Bkg-2018-electron-WJetsToLNu_1J.h5" ],
            "Bkg-2018-electron-WJetsToLNu_2J": [ "output-Bkg-2018-electron-WJetsToLNu_2J.h5" ],
            "Bkg-2018-electron-WW": [ "output-Bkg-2018-electron-WW.h5" ],
            "Bkg-2018-electron-WZ": [ "output-Bkg-2018-electron-WZ.h5" ],
            "Bkg-2018-electron-ZZ": [ "output-Bkg-2018-electron-ZZ.h5" ],
            "Bkg-2018-electron-ST_s-channel_4f_leptonDecays": [ "output-Bkg-2018-electron-ST_s-channel_4f_leptonDecays.h5" ],
            "Bkg-2018-electron-ST_t-channel_antitop_4f_InclusiveDecays": [ "output-Bkg-2018-electron-ST_t-channel_antitop_4f_InclusiveDecays.h5" ],
            "Bkg-2018-electron-ST_t-channel_top_4f_InclusiveDecays": [ "output-Bkg-2018-electron-ST_t-channel_top_4f_InclusiveDecays.h5" ],
            "Bkg-2018-electron-ST_tW_antitop_5f_inclusiveDecays": [ "output-Bkg-2018-electron-ST_tW_antitop_5f_inclusiveDecays.h5" ],
            "Bkg-2018-electron-ST_tW_top_5f_inclusiveDecays": [ "output-Bkg-2018-electron-ST_tW_top_5f_inclusiveDecays.h5" ],
            "Bkg-2018-electron-DYJetsToLL_0J": [ "output-Bkg-2018-electron-DYJetsToLL_0J.h5" ],
            "Bkg-2018-electron-DYJetsToLL_1J": [ "output-Bkg-2018-electron-DYJetsToLL_1J.h5" ],
            "Bkg-2018-electron-DYJetsToLL_2J": [ "output-Bkg-2018-electron-DYJetsToLL_2J.h5" ],
            "Bkg-2018-electron-QCD_Pt_170to300": [ "output-Bkg-2018-electron-QCD_Pt_170to300.h5" ],
            "Bkg-2018-electron-QCD_Pt_300to470": [ "output-Bkg-2018-electron-QCD_Pt_300to470.h5" ],
            "Bkg-2018-electron-QCD_Pt_470to600": [ "output-Bkg-2018-electron-QCD_Pt_470to600.h5" ],
            "Bkg-2018-electron-QCD_Pt_600to800": [ "output-Bkg-2018-electron-QCD_Pt_600to800.h5" ],
            "Bkg-2018-electron-QCD_Pt_800to1000": [ "output-Bkg-2018-electron-QCD_Pt_800to1000.h5" ],
            "Bkg-2018-electron-QCD_Pt_1000to1400": [ "output-Bkg-2018-electron-QCD_Pt_1000to1400.h5" ],
            "Bkg-2018-electron-QCD_Pt_1400to1800": [ "output-Bkg-2018-electron-QCD_Pt_1400to1800.h5" ],
            "Bkg-2018-electron-QCD_Pt_1800to2400": [ "output-Bkg-2018-electron-QCD_Pt_1800to2400.h5" ],
            "Bkg-2018-electron-QCD_Pt_2400to3200": [ "output-Bkg-2018-electron-QCD_Pt_2400to3200.h5" ],
            "Bkg-2018-electron-QCD_Pt_3200toInf": [ "output-Bkg-2018-electron-QCD_Pt_3200toInf.h5" ],
            }

for key_ in fileNames_:
    fileNames_[ key_ ] = [ "{}/{}".format( base_path_, item_ ) for item_ in fileNames_[ key_ ] ]
print ( labels_ )
print ( fileNames_ )

# output_dir_=""
output_dir_="/eos/home-m/malvesga/SWAN_projects/Antonio_UL/output_events"
process_data_events_ = ProcessDataEvents( lepton_type=lepton_type, data_sample=data_sample, labels=labels_, fileNames=fileNames_, runOnMC=True, output_dir=output_dir_ )

process_data_events_()
