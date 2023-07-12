from ProcessData import *

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

use_hash_index_ = True

base_path_ = "/eos/home-m/malvesga/SWAN_projects/Antonio_UL/output_05-07"
labels_bkgs_mix_protons_ = []
fileNames_bkgs_mix_protons_ = {}
if data_sample == '2017':
    if lepton_type_ == 'muon':
        labels_bkgs_mix_protons_ = [ "GGToWW-AQGC-mix_protons-2017-muon-A0W1e-6", "GGToWW-AQGC-mix_protons-2017-muon-A0W2e-6", "GGToWW-AQGC-mix_protons-2017-muon-A0W5e-6" ]
        fileNames_bkgs_mix_protons_ = {
            "GGToWW-AQGC-mix_protons-2017-muon-A0W1e-6": [ "output-GGToWW-AQGC-mix_protons-2017-muon-A0W1e-6.h5" ],
            "GGToWW-AQGC-mix_protons-2017-muon-A0W2e-6": [ "output-GGToWW-AQGC-mix_protons-2017-muon-A0W2e-6.h5" ],
            "GGToWW-AQGC-mix_protons-2017-muon-A0W5e-6": [ "output-GGToWW-AQGC-mix_protons-2017-muon-A0W5e-6.h5" ]
            }
    elif lepton_type_ == 'electron':
        labels_bkgs_mix_protons_ = [ "GGToWW-AQGC-mix_protons-2017-electron-A0W1e-6", "GGToWW-AQGC-mix_protons-2017-electron-A0W2e-6", "GGToWW-AQGC-mix_protons-2017-electron-A0W5e-6" ]
        fileNames_bkgs_mix_protons_ = {
            "GGToWW-AQGC-mix_protons-2017-electron-A0W1e-6": [ "output-GGToWW-AQGC-mix_protons-2017-electron-A0W1e-6.h5" ],
            "GGToWW-AQGC-mix_protons-2017-electron-A0W2e-6": [ "output-GGToWW-AQGC-mix_protons-2017-electron-A0W2e-6.h5" ],
            "GGToWW-AQGC-mix_protons-2017-electron-A0W5e-6": [ "output-GGToWW-AQGC-mix_protons-2017-electron-A0W5e-6.h5" ]
            }
elif data_sample == '2018':
    if lepton_type_ == 'muon':
        labels_bkgs_mix_protons_ = [ "Bkg-mix_protons-2018-muon-TTJets", "Bkg-mix_protons-2018-muon-DYJetsToLL_0J", "Bkg-mix_protons-2018-muon-DYJetsToLL_1J", "Bkg-mix_protons-2018-muon-DYJetsToLL_2J", "Bkg-mix_protons-2018-muon-WJetsToLNu_0J", "Bkg-mix_protons-2018-muon-WJetsToLNu_1J", "Bkg-mix_protons-2018-muon-WJetsToLNu_2J", "Bkg-mix_protons-2018-muon-QCD_Pt_170to300", "Bkg-mix_protons-2018-muon-QCD_Pt_300to470", "Bkg-mix_protons-2018-muon-QCD_Pt_470to600", "Bkg-mix_protons-2018-muon-QCD_Pt_600to800", "Bkg-mix_protons-2018-muon-QCD_Pt_800to1000", "Bkg-mix_protons-2018-muon-QCD_Pt_1000to1400", "Bkg-mix_protons-2018-muon-QCD_Pt_1400to1800", "Bkg-mix_protons-2018-muon-QCD_Pt_1800to2400", "Bkg-mix_protons-2018-muon-QCD_Pt_2400to3200", "Bkg-mix_protons-2018-muon-QCD_Pt_3200toInf", "Bkg-mix_protons-2018-muon-ST_s-channel_4f_leptonDecays", "Bkg-mix_protons-2018-muon-ST_t-channel_antitop_4f_InclusiveDecays", "Bkg-mix_protons-2018-muon-ST_t-channel_top_4f_InclusiveDecays", "Bkg-mix_protons-2018-muon-ST_tW_antitop_5f_inclusiveDecays", "Bkg-mix_protons-2018-muon-ST_tW_top_5f_inclusiveDecays", "Bkg-mix_protons-2018-muon-WW", "Bkg-mix_protons-2018-muon-WZ", "Bkg-mix_protons-2018-muon-ZZ" ]
        fileNames_bkgs_mix_protons_= {
            "Bkg-mix_protons-2018-muon-TTJets": [ "output-Bkg-mix_protons-2018-muon-TTJets.h5" ],
            "Bkg-mix_protons-2018-muon-DYJetsToLL_0J": [ "output-Bkg-mix_protons-2018-muon-DYJetsToLL_0J.h5" ],
            "Bkg-mix_protons-2018-muon-DYJetsToLL_1J": [ "output-Bkg-mix_protons-2018-muon-DYJetsToLL_1J.h5" ],
            "Bkg-mix_protons-2018-muon-DYJetsToLL_2J": [ "output-Bkg-mix_protons-2018-muon-DYJetsToLL_2J.h5" ],
            "Bkg-mix_protons-2018-muon-WJetsToLNu_0J": [ "output-Bkg-mix_protons-2018-muon-WJetsToLNu_0J.h5" ],
            "Bkg-mix_protons-2018-muon-WJetsToLNu_1J": [ "output-Bkg-mix_protons-2018-muon-WJetsToLNu_1J.h5" ],
            "Bkg-mix_protons-2018-muon-WJetsToLNu_2J": [ "output-Bkg-mix_protons-2018-muon-WJetsToLNu_2J.h5" ],
            "Bkg-mix_protons-2018-muon-QCD_Pt_170to300": [ "output-Bkg-mix_protons-2018-muon-QCD_Pt_170to300.h5" ],
            "Bkg-mix_protons-2018-muon-QCD_Pt_300to470": [ "output-Bkg-mix_protons-2018-muon-QCD_Pt_300to470.h5" ],
            "Bkg-mix_protons-2018-muon-QCD_Pt_470to600": [ "output-Bkg-mix_protons-2018-muon-QCD_Pt_470to600.h5" ],
            "Bkg-mix_protons-2018-muon-QCD_Pt_600to800": [ "output-Bkg-mix_protons-2018-muon-QCD_Pt_600to800.h5" ],
            "Bkg-mix_protons-2018-muon-QCD_Pt_800to1000": [ "output-Bkg-mix_protons-2018-muon-QCD_Pt_800to1000.h5" ],
            "Bkg-mix_protons-2018-muon-QCD_Pt_1000to1400": [ "output-Bkg-mix_protons-2018-muon-QCD_Pt_1000to1400.h5" ],
            "Bkg-mix_protons-2018-muon-QCD_Pt_1400to1800": [ "output-Bkg-mix_protons-2018-muon-QCD_Pt_1400to1800.h5" ],
            "Bkg-mix_protons-2018-muon-QCD_Pt_1800to2400": [ "output-Bkg-mix_protons-2018-muon-QCD_Pt_1800to2400.h5" ],
            "Bkg-mix_protons-2018-muon-QCD_Pt_2400to3200": [ "output-Bkg-mix_protons-2018-muon-QCD_Pt_2400to3200.h5" ],
            "Bkg-mix_protons-2018-muon-QCD_Pt_3200toInf": [ "output-Bkg-mix_protons-2018-muon-QCD_Pt_3200toInf.h5" ],
            "Bkg-mix_protons-2018-muon-ST_s-channel_4f_leptonDecays": [ "output-Bkg-mix_protons-2018-muon-ST_s-channel_4f_leptonDecays.h5" ],
            "Bkg-mix_protons-2018-muon-ST_t-channel_antitop_4f_InclusiveDecays": [ "output-Bkg-mix_protons-2018-muon-ST_t-channel_antitop_4f_InclusiveDecays.h5" ],
            "Bkg-mix_protons-2018-muon-ST_t-channel_top_4f_InclusiveDecays": [ "output-Bkg-mix_protons-2018-muon-ST_t-channel_top_4f_InclusiveDecays.h5" ],
            "Bkg-mix_protons-2018-muon-ST_tW_antitop_5f_inclusiveDecays": [ "output-Bkg-mix_protons-2018-muon-ST_tW_antitop_5f_inclusiveDecays.h5" ],
            "Bkg-mix_protons-2018-muon-ST_tW_top_5f_inclusiveDecays": [ "output-Bkg-mix_protons-2018-muon-ST_tW_top_5f_inclusiveDecays.h5" ],
            "Bkg-mix_protons-2018-muon-WW": [ "output-Bkg-mix_protons-2018-muon-WW.h5" ],
            "Bkg-mix_protons-2018-muon-WZ": [ "output-Bkg-mix_protons-2018-muon-WZ.h5" ],
            "Bkg-mix_protons-2018-muon-ZZ": [ "output-Bkg-mix_protons-2018-muon-ZZ.h5" ]
            }
    elif lepton_type_ == 'electron':
        labels_bkgs_mix_protons_ = [ "Bkg-mix_protons-2018-electron-TTJets", "Bkg-mix_protons-2018-electron-DYJetsToLL_0J", "Bkg-mix_protons-2018-electron-DYJetsToLL_1J", "Bkg-mix_protons-2018-electron-DYJetsToLL_2J", "Bkg-mix_protons-2018-electron-WJetsToLNu_0J", "Bkg-mix_protons-2018-electron-WJetsToLNu_1J", "Bkg-mix_protons-2018-electron-WJetsToLNu_2J", "Bkg-mix_protons-2018-electron-QCD_Pt_170to300", "Bkg-mix_protons-2018-electron-QCD_Pt_300to470", "Bkg-mix_protons-2018-electron-QCD_Pt_470to600", "Bkg-mix_protons-2018-electron-QCD_Pt_600to800", "Bkg-mix_protons-2018-electron-QCD_Pt_800to1000", "Bkg-mix_protons-2018-electron-QCD_Pt_1000to1400", "Bkg-mix_protons-2018-electron-QCD_Pt_1400to1800", "Bkg-mix_protons-2018-electron-QCD_Pt_1800to2400", "Bkg-mix_protons-2018-electron-QCD_Pt_2400to3200", "Bkg-mix_protons-2018-electron-QCD_Pt_3200toInf", "Bkg-mix_protons-2018-electron-ST_s-channel_4f_leptonDecays", "Bkg-mix_protons-2018-electron-ST_t-channel_antitop_4f_InclusiveDecays", "Bkg-mix_protons-2018-electron-ST_t-channel_top_4f_InclusiveDecays", "Bkg-mix_protons-2018-electron-ST_tW_antitop_5f_inclusiveDecays", "Bkg-mix_protons-2018-electron-ST_tW_top_5f_inclusiveDecays", "Bkg-mix_protons-2018-electron-WW", "Bkg-mix_protons-2018-electron-WZ", "Bkg-mix_protons-2018-electron-ZZ" ]
        fileNames_bkgs_mix_protons_= {
            "Bkg-mix_protons-2018-electron-TTJets": [ "output-Bkg-mix_protons-2018-electron-TTJets.h5" ],
            "Bkg-mix_protons-2018-electron-DYJetsToLL_0J": [ "output-Bkg-mix_protons-2018-electron-DYJetsToLL_0J.h5" ],
            "Bkg-mix_protons-2018-electron-DYJetsToLL_1J": [ "output-Bkg-mix_protons-2018-electron-DYJetsToLL_1J.h5" ],
            "Bkg-mix_protons-2018-electron-DYJetsToLL_2J": [ "output-Bkg-mix_protons-2018-electron-DYJetsToLL_2J.h5" ],
            "Bkg-mix_protons-2018-electron-WJetsToLNu_0J": [ "output-Bkg-mix_protons-2018-electron-WJetsToLNu_0J.h5" ],
            "Bkg-mix_protons-2018-electron-WJetsToLNu_1J": [ "output-Bkg-mix_protons-2018-electron-WJetsToLNu_1J.h5" ],
            "Bkg-mix_protons-2018-electron-WJetsToLNu_2J": [ "output-Bkg-mix_protons-2018-electron-WJetsToLNu_2J.h5" ],
            "Bkg-mix_protons-2018-electron-QCD_Pt_170to300": [ "output-Bkg-mix_protons-2018-electron-QCD_Pt_170to300.h5" ],
            "Bkg-mix_protons-2018-electron-QCD_Pt_300to470": [ "output-Bkg-mix_protons-2018-electron-QCD_Pt_300to470.h5" ],
            "Bkg-mix_protons-2018-electron-QCD_Pt_470to600": [ "output-Bkg-mix_protons-2018-electron-QCD_Pt_470to600.h5" ],
            "Bkg-mix_protons-2018-electron-QCD_Pt_600to800": [ "output-Bkg-mix_protons-2018-electron-QCD_Pt_600to800.h5" ],
            "Bkg-mix_protons-2018-electron-QCD_Pt_800to1000": [ "output-Bkg-mix_protons-2018-electron-QCD_Pt_800to1000.h5" ],
            "Bkg-mix_protons-2018-electron-QCD_Pt_1000to1400": [ "output-Bkg-mix_protons-2018-electron-QCD_Pt_1000to1400.h5" ],
            "Bkg-mix_protons-2018-electron-QCD_Pt_1400to1800": [ "output-Bkg-mix_protons-2018-electron-QCD_Pt_1400to1800.h5" ],
            "Bkg-mix_protons-2018-electron-QCD_Pt_1800to2400": [ "output-Bkg-mix_protons-2018-electron-QCD_Pt_1800to2400.h5" ],
            "Bkg-mix_protons-2018-electron-QCD_Pt_2400to3200": [ "output-Bkg-mix_protons-2018-electron-QCD_Pt_2400to3200.h5" ],
            "Bkg-mix_protons-2018-electron-QCD_Pt_3200toInf": [ "output-Bkg-mix_protons-2018-electron-QCD_Pt_3200toInf.h5" ],
            "Bkg-mix_protons-2018-electron-ST_s-channel_4f_leptonDecays": [ "output-Bkg-mix_protons-2018-electron-ST_s-channel_4f_leptonDecays.h5" ],
            "Bkg-mix_protons-2018-electron-ST_t-channel_antitop_4f_InclusiveDecays": [ "output-Bkg-mix_protons-2018-electron-ST_t-channel_antitop_4f_InclusiveDecays.h5" ],
            "Bkg-mix_protons-2018-electron-ST_t-channel_top_4f_InclusiveDecays": [ "output-Bkg-mix_protons-2018-electron-ST_t-channel_top_4f_InclusiveDecays.h5" ],
            "Bkg-mix_protons-2018-electron-ST_tW_antitop_5f_inclusiveDecays": [ "output-Bkg-mix_protons-2018-electron-ST_tW_antitop_5f_inclusiveDecays.h5" ],
            "Bkg-mix_protons-2018-electron-ST_tW_top_5f_inclusiveDecays": [ "output-Bkg-mix_protons-2018-electron-ST_tW_top_5f_inclusiveDecays.h5" ],
            "Bkg-mix_protons-2018-electron-WW": [ "output-Bkg-mix_protons-2018-electron-WW.h5" ],
            "Bkg-mix_protons-2018-electron-WZ": [ "output-Bkg-mix_protons-2018-electron-WZ.h5" ],
            "Bkg-mix_protons-2018-electron-ZZ": [ "output-Bkg-mix_protons-2018-electron-ZZ.h5" ]
            }

for key_ in fileNames_bkgs_mix_protons_:
    fileNames_bkgs_mix_protons_[ key_ ] = [ "{}/{}".format( base_path_, item_ ) for item_ in fileNames_bkgs_mix_protons_[ key_ ] ]
print ( labels_bkgs_mix_protons_ )
print ( fileNames_bkgs_mix_protons_ )

# output_dir_=""
output_dir_="/eos/home-m/malvesga/SWAN_projects/Antonio_UL/output_05-07"
process_data_mix_protons_ = ProcessData( lepton_type=lepton_type_, data_sample=data_sample, labels=labels_bkgs_mix_protons_, fileNames=fileNames_bkgs_mix_protons_, mix_protons=True, runOnMC=True, output_dir=output_dir_, use_hash_index=use_hash_index_ )

process_data_mix_protons_( apply_fiducial=True, within_aperture=True, select_2protons=True )
