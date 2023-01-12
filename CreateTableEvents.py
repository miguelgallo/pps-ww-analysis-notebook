import uproot
import awkward as ak
import numpy as np
import pandas as pd
import h5py

from processing import df_run_ranges_2017, df_run_ranges_2018, df_run_ranges_mixing_2017, df_run_ranges_mixing_2018, lumi_periods_2017, lumi_periods_2018

class CreateTableEvents:
    def __init__( self, label, lepton_type, data_sample, fileNames, tree_path, output_dir="" ):

        if lepton_type not in ( 'muon', 'electron' ):
            raise RuntimeError( "Invalid lepton_type argument." )
    
        if data_sample not in ( '2017', '2018' ):
            raise RuntimeError( "Invalid data_sample argument." )

        self.label_ = label
        self.data_sample_ = data_sample
        self.lepton_type_ = lepton_type
        self.fileNames_ = fileNames
        self.tree_path_ = tree_path
        self.output_dir_ = None
        if output_dir is not None and output_dir != "": self.output_dir_ = output_dir

    def __call__( self, runOnMC=False, data_periods=None, step_size=100000, firstEvent=None, entryStop=None, debug=False ):

        for key_ in self.fileNames_:
            import time
            print( time.strftime("%Y/%m/%d %H:%M:%S", time.localtime() ) )
            time_s_ = time.time()

            print ( key_, self.fileNames_[ key_ ] )
            label__ = "{}-{}".format( self.label_, key_ )
            self.create_table(
                self.fileNames_[ key_ ],
                label=label__,
                runOnMC=runOnMC,
                data_periods=data_periods,
                step_size=step_size,
                firstEvent=firstEvent,
                entryStop=entryStop,
                debug=debug
                )
            
            time_e_ = time.time()
            print ( "Total time elapsed: {:.0f}".format( time_e_ - time_s_ ) )

    def create_table( self, fileNames, label, runOnMC=False, data_periods=None, step_size=100000, firstEvent=None, entryStop=None, debug=False ):

        fileNames__ = fileNames
        label__ = label
        lepton_type__ = self.lepton_type_
        data_sample__ = self.data_sample_
        tree_path__ = self.tree_path_
        output_dir__ = self.output_dir_
    
        df_run_ranges_ = None
        df_run_ranges_mixing_ = None
        if data_sample__ == '2017':
            df_run_ranges_ = df_run_ranges_2017
            df_run_ranges_mixing_ = df_run_ranges_mixing_2017
        elif data_sample__ == '2018':
            df_run_ranges_ = df_run_ranges_2018
            df_run_ranges_mixing_ = df_run_ranges_mixing_2018
        print ( df_run_ranges_ )
        print ( df_run_ranges_mixing_ )
    
        runOnMC_ = runOnMC
        data_periods_ = data_periods if ( runOnMC_ and data_periods is not None and len(data_periods) > 0 ) else None
        if runOnMC_ and not data_periods_:
            data_periods_ = list( df_run_ranges_.index )
    
     
        step_size_ = step_size
        firstEvent_ = firstEvent
        entryStop_ = entryStop
    
        how_ = None
        #how_ = "zip"
        
        print ( "Run on MC: {}".format( runOnMC_ ) )
    
        lumi_periods_ = None
        if data_sample__ == '2017':
            if lepton_type__ == 'muon':
                lumi_periods_ = lumi_periods_2017[ 'muon' ]
            elif lepton_type__ == 'electron':
                lumi_periods_ = lumi_periods_2017[ 'electron' ]
        elif data_sample__ == '2018':
            if lepton_type__ == 'muon':
                lumi_periods_ = lumi_periods_2018[ 'muon' ]
            elif lepton_type__ == 'electron':
                lumi_periods_ = lumi_periods_2018[ 'electron' ]
    
        lumi_weights_ = None
        probs_lumi_ = None
        if runOnMC_:
            print ( "Data periods: ", data_periods_ )
            lumi_weights_ = pd.Series( lumi_periods_ )
            lumi_weights_ = lumi_weights_.loc[ data_periods_ ]
            probs_lumi_ = lumi_weights_ / lumi_weights_.sum()
            print ( "Data periods: ", data_periods_ )
            print ( "Lumi values: ", lumi_weights_)
            probs_lumi_ = lumi_weights_ / np.sum( lumi_weights_ )
            print ( "Prob. lumi: ", probs_lumi_ ) 
    
        np.random.seed( 42 )

        dset_chunk_size = 100000
    
        columns_events = [
            "run", "lumiblock", "event", "crossingAngle", "betaStar", "instLumi", 
            "jet0_pt", "jet0_eta", "jet0_phi", "jet0_energy", "jet0_mass", "jet0_corrmass", "jet0_tau1", "jet0_tau2", "jet0_vertexz",
            "jet0_px", "jet0_py", "jet0_pz",
            "calo_met", "met", "met_x", "met_y", "met_phi",
            "nVertices",
            "num_bjets_ak8", "num_bjets_ak4", "num_jets_ak4",
            "pfcand_nextracks", "pfcand_nextracks_noDRl",
            "recoMWhad", "recoMWlep", "recoMWW", "recoRapidityWW", "dphiWW", "WLeptonicPt", "WLeptonicEta", "WLeptonicPhi" ]
        if lepton_type__ == 'muon':
            columns_events.extend( [ "muon0_pt", "muon0_eta", "muon0_phi", "muon0_energy", "muon0_charge", "muon0_iso", "muon0_dxy", "muon0_dz", "muon0_trackerLayersWithMeasurement" ] )
        elif lepton_type__ == 'electron':
            columns_events.extend( [ "electron0_pt", "electron0_eta", "electron0_phi", "electron0_energy", "electron0_charge", "electron0_dxy", "electron0_dz", 'electron0_corr', 'electron0_ecalTrkEnPostCorr', 'electron0_ecalTrkEnErrPostCorr', 'electron0_ecalTrkEnPreCorr', 'electron0_energyScaleUp', 'electron0_energyScaleDown' ] )
    
        if runOnMC_:
            columns_runOnMC_  = []
    
            columns_runOnMC_.extend( [ "run_mc" ] )
    
            columns_runOnMC_.extend( [ "pileupWeight", "mc_pu_trueinteractions", "mcWeight", 'prefiring_weight', 'prefiring_weight_up', 'prefiring_weight_down', 'prefiring_weight_ECAL', 'prefiring_weight_ECAL_up', 'prefiring_weight_ECAL_down', 'prefiring_weight_Muon', 'prefiring_weight_Muon_up', 'prefiring_weight_Muon_down' ] )
    
            columns_runOnMC_.extend( [ "jet0_jer_res", "jet0_jer_sf", "jet0_jer_sfup", "jet0_jer_sfdown", 'jet0_cjer', 'jet0_cjer_up', 'jet0_cjer_down' ] )
    
            if lepton_type__ == 'electron':
                columns_runOnMC_.extend( [ 'electron0_energySigmaUp', 'electron0_energySigmaDown' ] )
    
            columns_runOnMC_.extend( [ 'met_ptJER_Up', 'met_ptJER_Down', 'met_phiJER_Up', 'met_phiJER_Down', 'met_ptJES_Up', 'met_ptJES_Down', 'met_phiJES_Up', 'met_phiJES_Down' ] )
            columns_runOnMC_.extend( [ "gen_jet0_pt", "gen_jet0_eta", "gen_jet0_phi", "gen_jet0_energy" ] )
            if lepton_type__ == 'muon':
                columns_runOnMC_.extend( [ "gen_muon0_pt", "gen_muon0_eta", "gen_muon0_phi", "gen_muon0_energy", "gen_muon0_charge", "gen_muon0_mass" ] )
            elif lepton_type__ == 'electron':
                columns_runOnMC_.extend( [ "gen_electron0_pt", "gen_electron0_eta", "gen_electron0_phi", "gen_electron0_energy", "gen_electron0_charge", "gen_electron0_mass" ] )
    
            columns_events.extend( columns_runOnMC_ )
    
        events_keys = {}
        for col_ in columns_events:
            events_keys[ col_ ] = col_
        events_keys[ 'prefiring_weight' ] = 'prefiring_weight_0'
        events_keys[ 'prefiring_weight_up' ] = 'prefiring_weight_up_0'
        events_keys[ 'prefiring_weight_down' ] = 'prefiring_weight_down_0'
        events_keys[ 'prefiring_weight_ECAL' ] = 'prefiring_weight_ECAL_0'
        events_keys[ 'prefiring_weight_ECAL_up' ] = 'prefiring_weight_ECAL_up_0'
        events_keys[ 'prefiring_weight_ECAL_down' ] = 'prefiring_weight_ECAL_down_0'
        events_keys[ 'prefiring_weight_Muon' ] = 'prefiring_weight_Muon_0'
        events_keys[ 'prefiring_weight_Muon_up' ] = 'prefiring_weight_Muon_up_0'
        events_keys[ 'prefiring_weight_Muon_down' ] = 'prefiring_weight_Muon_down_0'

        file_name_label_ = 'output-{}.h5'.format( label__ )
        if output_dir__ is not None and output_dir__ != "":
            output_file_path_ = '{}/{}'.format( output_dir__ , file_name_label_ )
        else:
            output_file_path_ = file_name_label_
        print ( output_file_path_ )
        with h5py.File( output_file_path_, 'w') as f:
    
            dset_events = f.create_dataset( 'events', ( dset_chunk_size, len( columns_events ) ), compression="gzip", chunks=True, maxshape=( None , len( columns_events ) ) )
            print ( "Initial dataset shape: {}".format( dset_events.shape ) )
    
            events_list = {}
            for col_ in columns_events:
                events_list[ col_ ] = []           
    
            selections = None
            counts = None
    
            dset_events_slice = 0
            dset_events_idx = 0
            dset_events_entries = 0

            for file_ in fileNames__:
                print ( file_ ) 
                root_ = uproot.open( file_ )
    
                print ( "Number of events in tree: {}".format( np.array( root_[ tree_path__ + "/event" ] ).size ) )
    
                tree_ = root_[ tree_path__ ]
    
                keys_ = [
                    "run", "event", "lumiblock", "crossingAngle", "betaStar", "instLumi", "nVertices",
                    "num_bjets_ak8", "num_bjets_ak4", "num_jets_ak4",
                    "pfcand_nextracks", "pfcand_nextracks_noDRl",
                    "recoMWhad", "recoMWlep", "recoMWW", "recoRapidityWW", "dphiWW", "WLeptonicPt", "WLeptonicEta", "WLeptonicPhi",
                    "pileupWeight", "mc_pu_trueinteractions", "mcWeight" ]
                keys_jet = tree_.keys( filter_name="jet*")
                keys_.extend( keys_jet )
                keys_genjet = tree_.keys( filter_name="gen_jet*")
                keys_genmuon = tree_.keys( filter_name="gen_muon*")
                keys_genelectron = tree_.keys( filter_name="gen_electron*")
                keys_.extend( keys_genjet )
                keys_.extend( keys_genmuon )
                keys_.extend( keys_genelectron )
                if lepton_type__ == 'muon':
                    keys_muon_ = tree_.keys( filter_name="muon*")
                    keys_.extend( keys_muon_ )
                elif lepton_type__ == 'electron':
                    keys_electron_ = tree_.keys( filter_name="electron*")
                    keys_.extend( keys_electron_ )
                keys_met = tree_.keys( filter_name="met*")
                keys_calomet = tree_.keys( filter_name="calo_met*")
                keys_.extend( keys_met )
                keys_.extend( keys_calomet )
                keys_prefiring = tree_.keys( filter_name="prefiring*")
                keys_.extend( keys_prefiring )
    
                print ( keys_ )
    
                for events_ in tree_.iterate( keys_ , library="ak", how=how_, step_size=step_size_, entry_start=firstEvent_, entry_stop=entryStop_ ):
                    print ( len(events_), events_ )
    
                    print ( "Num jets: {}".format( ak.num( events_["jet_pt"] ) ) )
                    if lepton_type__ == 'muon':
                        print ( "Num muons: {}".format( ak.num( events_["muon_pt"] ) ) )
                    elif lepton_type__ == 'electron':
                        print ( "Num electrons: {}".format( ak.num( events_["electron_pt"] ) ) )
    
                    selections_ = []
                    counts_ = []
    
                    selections_.append( "All" )
                    counts_.append( len( events_ ) )
    
                    # Event selections
                    msk_1jet = ( ak.num( events_["jet_pt"] ) >= 1 )
                    selections_.append( "Jet" )
                    counts_.append( np.sum( np.array( msk_1jet ).astype("int32") ) )
    
                    lepton_var_ = ''
                    lepton_sel_name_ = ''
                    # lepton_var_gen_ = ''
                    # lepton_sel_gen_name_ = ''
                    if lepton_type__ == 'muon':
                        lepton_var_ = "muon_pt"
                        lepton_sel_name_ = 'Muon'
                        # if runOnMC_:
                        #     lepton_var_gen_ = "gen_muon_pt"
                        #     lepton_sel_gen_name_ = 'GenMuon'
                    elif lepton_type__ == 'electron':
                        lepton_var_ = "electron_pt"
                        lepton_sel_name_ = 'Electron'
                        # if runOnMC_:
                        #     lepton_var_gen_ = "gen_electron_pt"
                        #     lepton_sel_gen_name_ = 'GenElectron'
    
                    msk_1lep = msk_1jet & ( ak.num( events_[ lepton_var_ ] ) >= 1 )
                    selections_.append( lepton_sel_name_ )
                    counts_.append( np.sum( np.array( msk_1lep ).astype("int32") ) )
    
                    # if runOnMC_:
                    #     msk_1genlep = msk_1lep & ( ak.num( events_[ lepton_var_gen_ ] ) >= 1 )
                    #     selections_.append( lepton_sel_gen_name_ )
                    #     counts_.append( np.sum( np.array( msk_1genlep ).astype("int32") ) )
                    # if runOnMC_:
                    #     events_ = events_[ msk_1genlep ]
                    # else:
                    #     events_ = events_[ msk_1lep ]

                    events_ = events_[ msk_1lep ]

                    # selections_.append( "check_none" )
                    # counts_.append( 0 )
                    
                    selections_ = np.array( selections_ )
                    counts_ = np.array( counts_ )
    
                    if selections is None:
                        selections = selections_
                        counts = counts_
                    else:
                        msk_selections = np.full_like( selections, False, dtype='bool' )
                        for key in selections_:
                            msk_selections |= ( selections == key )
                        counts[ msk_selections ] += counts_
    
                    if runOnMC_:
                        sample_idx_arr_ = np.random.choice( np.arange( probs_lumi_.index.size ), len( events_ ), p=probs_lumi_ )
                        print ( "Sampled index: ", sample_idx_arr_ )
                        run_arr_ = np.apply_along_axis( lambda idx_: df_run_ranges_.loc[ probs_lumi_.index[ idx_ ] ][ "min" ], 0, sample_idx_arr_ )
                        print ( "Run numbers: ", run_arr_ )
                        events_[ "run_mc" ] = run_arr_
    
                    print ( "Run: {}".format( events_[ "run" ] ) ) 
                    print ( "Lumi: {}".format( events_[ "lumiblock" ] ) ) 
                    print ( "Event: {}".format( events_[ "event" ] ) ) 
                    print ( "Crossing angle: {}".format( events_[ "crossingAngle" ] ) ) 
                    print ( "Num jets: {}".format( ak.num( events_["jet_pt"] ) ) )
                    if lepton_type__ == 'muon':
                        print ( "Num muons: {}".format( ak.num( events_["muon_pt"] ) ) )
                    elif lepton_type__ == 'electron':
                        print ( "Num electrons: {}".format( ak.num( events_["electron_pt"] ) ) )
    
                    if runOnMC_:
                        print ( "Run MC: {}".format( events_[ "run_mc" ] ) )
    
                    if debug:
                        print ( ak.to_list( events_ ) )

                    genjets_sel_ = None
                    genmuons_sel_ = None
                    genelectrons_sel_ = None
                    if runOnMC_:
                        if how_ == "zip":
                            genjets_ = events[ "gen_jet" ]
                            genmuons_ = events[ "gen_muon" ]
                            genelectrons_ = events[ "gen_electrons" ]
                        elif how_ is None:
                            arrays_genjet_ = {}
                            for key_ in keys_genjet: arrays_genjet_[ key_[ len("gen_jet_") : ] ] = events_[ key_ ]
                            genjets_ = ak.zip( arrays_genjet_ )
                            genjets_["dR"] = np.sqrt( ( genjets_["eta"] - events_["jet_eta"][:,0] ) ** 2 + ( genjets_["phi"] - events_["jet_phi"][:,0] ) ** 2  )
                            print ( genjets_ )
                            print ( ak.to_list( genjets_[:10] ) )
                            min_dR_ = ak.min( genjets_["dR"], axis=1 )
                            print ( min_dR_ )
                            genjets_sel_ = genjets_[ genjets_["dR"] <= min_dR_ ]
                            print ( genjets_sel_ )
                            print ( ak.to_list( genjets_sel_[:10] ) )
    
                            if lepton_type__ == 'muon':
                                arrays_genmuon_ = {}
                                for key_ in keys_genmuon: arrays_genmuon_[ key_[ len("gen_muon_") : ] ] = events_[ key_ ]
                                genmuons_ = ak.zip( arrays_genmuon_ )
                                genmuons_["dR"] = np.sqrt( ( genmuons_["eta"] - events_["muon_eta"][:,0] ) ** 2 + ( genmuons_["phi"] - events_["muon_phi"][:,0] ) ** 2  )
                                print ( genmuons_ )
                                print ( ak.to_list( genmuons_[:10] ) )
                                min_dR_ = ak.min( genmuons_["dR"], axis=1 )
                                print ( min_dR_ )
                                genmuons_sel_ = genmuons_[ genmuons_["dR"] <= min_dR_ ]
                                print ( genmuons_sel_ )
                                print ( ak.to_list( genmuons_sel_[:10] ) )
                            elif lepton_type__ == 'electron':
                                arrays_genelectron_ = {}
                                for key_ in keys_genelectron: arrays_genelectron_[ key_[ len("gen_electron_") : ] ] = events_[ key_ ]
                                genelectrons_ = ak.zip( arrays_genelectron_ )
                                genelectrons_["dR"] = np.sqrt( ( genelectrons_["eta"] - events_["electron_eta"][:,0] ) ** 2 + ( genelectrons_["phi"] - events_["electron_phi"][:,0] ) ** 2  )
                                print ( genelectrons_ )
                                print ( ak.to_list( genelectrons_[:10] ) )
                                min_dR_ = ak.min( genelectrons_["dR"], axis=1 )
                                print ( min_dR_ )
                                genelectrons_sel_ = genelectrons_[ genelectrons_["dR"] <= min_dR_ ]
                                print ( genelectrons_sel_ )
                                print ( ak.to_list( genelectrons_sel_[:10] ) )
    
                    # check_none_ = ak.is_none( events_ )
                    # arr_check_none_ = np.array( check_none_ ).astype("int32")
                    # print( "check_none", np.sum( arr_check_none_ ), check_none_ )
                    # msk_check_none_ = np.invert( check_none_ )
                    # events_ = events_[ msk_check_none_ ]
                    # msk_selections_ = ( selections == "check_none" )
                    # counts[ msk_selections_ ] += np.sum( msk_check_none_ )

                    events_["jet0_pt"]                = events_[ "jet_pt" ][:,0]
                    events_["jet0_eta"]               = events_[ "jet_eta" ][:,0]
                    events_["jet0_phi"]               = events_[ "jet_phi" ][:,0]
                    events_["jet0_energy"]            = events_[ "jet_energy" ][:,0]
                    events_["jet0_mass"]              = events_[ "jet_mass" ][:,0]
                    events_["jet0_corrmass"]          = events_[ "jet_corrmass" ][:,0]
                    events_["jet0_tau1"]              = events_[ "jet_tau1" ][:,0]
                    events_["jet0_tau2"]              = events_[ "jet_tau2" ][:,0]
                    events_["jet0_vertexz"]           = events_[ "jet_vertexz" ][:,0]
                    events_["jet0_px"]                = events_[ "jet_px" ][:,0]
                    events_["jet0_py"]                = events_[ "jet_py" ][:,0]
                    events_["jet0_pz"]                = events_[ "jet_pz" ][:,0]
                    if runOnMC_:
                        events_["jet0_jer_res"]       = events_[ "jet_jer_res" ][:,0]
                        events_["jet0_jer_sf"]        = events_[ "jet_jer_sf" ][:,0]
                        events_["jet0_jer_sfup"]      = events_[ "jet_jer_sfup" ][:,0]
                        events_["jet0_jer_sfdown"]    = events_[ "jet_jer_sfdown" ][:,0]
                        events_["jet0_cjer"]           = events_[ "jet_cjer" ][:,0]
                        events_["jet0_cjer_up"]        = events_[ "jet_cjer_up" ][:,0]
                        events_["jet0_cjer_down"]      = events_[ "jet_cjer_down" ][:,0]
                        # events_["gen_jet0_pt"]                = events_[ "gen_jet_pt" ][:,0]
                        # events_["gen_jet0_eta"]               = events_[ "gen_jet_eta" ][:,0]
                        # events_["gen_jet0_phi"]               = events_[ "gen_jet_phi" ][:,0]
                        # events_["gen_jet0_energy"]            = events_[ "gen_jet_energy" ][:,0]
                        events_["gen_jet0_pt"]        = genjets_sel_[ "pt" ][:,0]
                        events_["gen_jet0_eta"]       = genjets_sel_[ "eta" ][:,0]
                        events_["gen_jet0_phi"]       = genjets_sel_[ "phi" ][:,0]
                        events_["gen_jet0_energy"]    = genjets_sel_[ "energy" ][:,0]
    
                    if lepton_type__ == 'muon':
                        events_["muon0_pt"]                           = events_[ "muon_pt" ][:,0]
                        events_["muon0_eta"]                          = events_[ "muon_eta" ][:,0]
                        events_["muon0_phi"]                          = events_[ "muon_phi" ][:,0]
                        events_["muon0_energy"]                       = events_[ "muon_e" ][:,0]
                        events_["muon0_charge"]                       = events_[ "muon_charge" ][:,0]
                        events_["muon0_iso"]                          = events_[ "muon_iso" ][:,0]
                        events_["muon0_dxy"]                          = events_[ "muon_dxy" ][:,0]
                        events_["muon0_dz"]                           = events_[ "muon_dz" ][:,0]
                        events_["muon0_trackerLayersWithMeasurement"] = events_[ "muon_trackerLayersWithMeasurement" ][:,0]
                        if runOnMC_:
                            # msk__ = ( ak.num( genmuons_sel_ ) >= 1 )
                            # print ( ak.to_list( ak.num( genmuons_sel_ ) ) )
                            # print ( msk__ )
                            events_["gen_muon0_pt"]        = genmuons_sel_[ "pt" ][:,0]
                            events_["gen_muon0_eta"]       = genmuons_sel_[ "eta" ][:,0]
                            events_["gen_muon0_phi"]       = genmuons_sel_[ "phi" ][:,0]
                            events_["gen_muon0_energy"]    = genmuons_sel_[ "energy" ][:,0]
                            events_["gen_muon0_charge"]    = genmuons_sel_[ "charge" ][:,0]
                            events_["gen_muon0_mass"]      = genmuons_sel_[ "mass" ][:,0]
                            msk__ = ak.is_none( events_["gen_muon0_pt"] )
                            print ( msk__ )
                            print ( np.sum( msk__ ) )
                            events_["gen_muon0_pt"]        = ak.fill_none( events_["gen_muon0_pt"], -999. )
                            events_["gen_muon0_eta"]       = ak.fill_none( events_["gen_muon0_eta"], -999. )
                            events_["gen_muon0_phi"]       = ak.fill_none( events_["gen_muon0_phi"], -999. )
                            events_["gen_muon0_energy"]    = ak.fill_none( events_["gen_muon0_energy"], -999. )
                            events_["gen_muon0_charge"]    = ak.fill_none( events_["gen_muon0_charge"], -999. )
                            events_["gen_muon0_mass"]      = ak.fill_none( events_["gen_muon0_mass"], -999. )
                            msk__ = ak.is_none( events_["gen_muon0_pt"] )
                            print ( msk__ )
                            print ( np.sum( msk__ ) )
                            # print ( ak.to_list( events_["gen_muon0_pt"] ) )

                    elif lepton_type__ == 'electron':
                        events_["electron0_pt"]                   = events_[ "electron_pt" ][:,0]
                        events_["electron0_eta"]                  = events_[ "electron_eta" ][:,0]
                        events_["electron0_phi"]                  = events_[ "electron_phi" ][:,0]
                        events_["electron0_energy"]               = events_[ "electron_e" ][:,0]
                        events_["electron0_charge"]               = events_[ "electron_charge" ][:,0]
                        events_["electron0_dxy"]                  = events_[ "electron_dxy" ][:,0]
                        events_["electron0_dz"]                   = events_[ "electron_dz" ][:,0]
                        events_["electron0_corr"]                 = events_[ "electron_corr" ][:,0]
                        events_["electron0_ecalTrkEnPostCorr"]    = events_[ "electron_ecalTrkEnPostCorr" ][:,0]
                        events_["electron0_ecalTrkEnErrPostCorr"] = events_[ "electron_ecalTrkEnErrPostCorr" ][:,0]
                        events_["electron0_ecalTrkEnPreCorr"]     = events_[ "electron_ecalTrkEnPreCorr" ][:,0]
                        events_["electron0_energyScaleUp"]        = events_[ "electron_energyScaleUp" ][:,0]
                        events_["electron0_energyScaleDown"]      = events_[ "electron_energyScaleDown" ][:,0]
                        if runOnMC_:
                            events_["electron0_energySigmaUp"]    = events_[ "electron_energySigmaUp" ][:,0]
                            events_["electron0_energySigmaDown"]  = events_[ "electron_energySigmaDown" ][:,0]
                            events_["gen_electron0_pt"]        = genelectrons_sel_[ "pt" ][:,0]
                            events_["gen_electron0_eta"]       = genelectrons_sel_[ "eta" ][:,0]
                            events_["gen_electron0_phi"]       = genelectrons_sel_[ "phi" ][:,0]
                            events_["gen_electron0_energy"]    = genelectrons_sel_[ "energy" ][:,0]
                            events_["gen_electron0_charge"]    = genelectrons_sel_[ "charge" ][:,0]
                            events_["gen_electron0_mass"]      = genelectrons_sel_[ "mass" ][:,0]
                            msk__ = ak.is_none( events_["gen_electron0_pt"] )
                            print ( msk__ )
                            print ( np.sum( msk__ ) )
                            events_["gen_electron0_pt"]        = ak.fill_none( events_["gen_electron0_pt"], -999. )
                            events_["gen_electron0_eta"]       = ak.fill_none( events_["gen_electron0_eta"], -999. )
                            events_["gen_electron0_phi"]       = ak.fill_none( events_["gen_electron0_phi"], -999. )
                            events_["gen_electron0_energy"]    = ak.fill_none( events_["gen_electron0_energy"], -999. )
                            events_["gen_electron0_charge"]    = ak.fill_none( events_["gen_electron0_charge"], -999. )
                            events_["gen_electron0_mass"]      = ak.fill_none( events_["gen_electron0_mass"], -999. )
                            msk__ = ak.is_none( events_["gen_electron0_pt"] )
                            print ( msk__ )
                            print ( np.sum( msk__ ) )
    
                    if runOnMC_:
                        events_["prefiring_weight_0"]       = events_["prefiring_weight"][ 0 ]
                        events_["prefiring_weight_up_0"]    = events_["prefiring_weight_up"][ 0 ]
                        events_["prefiring_weight_down_0"]  = events_["prefiring_weight_down"][ 0 ]
                        events_["prefiring_weight_ECAL_0"]       = events_["prefiring_weight_ECAL"][ 0 ]
                        events_["prefiring_weight_ECAL_up_0"]    = events_["prefiring_weight_ECAL_up"][ 0 ]
                        events_["prefiring_weight_ECAL_down_0"]  = events_["prefiring_weight_ECAL_down"][ 0 ]
                        events_["prefiring_weight_Muon_0"]       = events_["prefiring_weight_Muon"][ 0 ]
                        events_["prefiring_weight_Muon_up_0"]    = events_["prefiring_weight_Muon_up"][ 0 ]
                        events_["prefiring_weight_Muon_down_0"]  = events_["prefiring_weight_Muon_down"][ 0 ]
                    
                    check_none_ = ak.is_none( events_ )
                    arr_check_none_ = np.array( check_none_ ).astype("int32")
                    print( "check_none", np.sum( arr_check_none_ ), check_none_ )
                    msk_check_none_ = np.invert( check_none_ )
                    print( msk_check_none_ )
                    events_ = events_[ msk_check_none_ ]
    
                    counts_check_none_ = len( events_ )
                    counts_label__ = "check_none"
                    if not counts_label__ in selections:
                        selections = np.concatenate( ( selections, np.array( [ counts_label__ ] ) ) )
                        counts = np.concatenate( ( counts, np.array( [ counts_check_none_ ] ) ) )
                    else:    
                        counts[ selections == counts_label__ ] += counts_check_none_

                    print ( selections )
                    print ( counts )
    
                    for col_ in columns_events:
                        arr__ = events_[ events_keys[ col_ ] ]
                        print ( col_ )
                        # events_list[ col_ ] = np.array( ak.flatten( arr__ ) )
                        events_list[ col_ ] = np.array( arr__ )
                        print ( events_list[ col_ ].shape )
    
                    # arr_size_events_ = len( events_list[ "jet0_pt" ] )
                    arr_size_events_ = events_list[ "jet0_pt" ].size
                    print ( "Flattened array size: {}".format( arr_size_events_ ) )
    
                    dset_events_entries += arr_size_events_
    
                    if dset_events_entries > dset_chunk_size:
                        resize_factor_ = ( dset_events_entries // dset_chunk_size )
                        chunk_resize_  = resize_factor_ * dset_chunk_size
    
                        print ( "Resizing output dataset by {} entries.".format( chunk_resize_ ) )
                        dset_events.resize( ( dset_events.shape[0] + chunk_resize_ ), axis=0 )
                        print ( "Dataset shape: {}".format( dset_events.shape ) )
    
                        dset_events_slice += resize_factor_
                        # Count the rest to the chunk size 
                        dset_events_entries = ( dset_events_entries % dset_chunk_size )
    
                    print ( "Stacking data." )
                    data_events_ = np.stack( list( events_list.values() ), axis=1 )
                    print ( data_events_.shape )
                    print ( data_events_ )
    
                    dset_idx_next_ = dset_events_idx + arr_size_events_
                    print ( "Slice: {}".format( dset_events_slice ) )
                    print ( "Writing in positions ({},{})".format( dset_events_idx, dset_idx_next_ ) )
                    dset_events[ dset_events_idx : dset_idx_next_ ] = data_events_
                    dset_events_idx = dset_idx_next_ 
    
                # Iteration on input files
                root_.close()
    
            # Reduce dataset to its final size 
            print ( "Reduce dataset." )
            dset_events.resize( ( dset_events_idx ), axis=0 ) 
            print ( "Dataset shape: {}".format( dset_events.shape ) )
    
            print ( "Writing column names and event counts.")
    
            columns_events_ = np.array( columns_events, dtype='S' )
            print ( columns_events_ )
    
            event_counts_ = counts
            print ( event_counts_ )
    
            selections_ = np.array( selections, dtype='S' )
            print ( selections_ )
    
            dset_columns_events = f.create_dataset( 'columns_events', data=columns_events_ )
            dset_counts = f.create_dataset( 'event_counts', data=event_counts_ )
            dset_selections = f.create_dataset( 'selections', data=selections_ )
    
            print ( dset_events )
            print ( dset_events[-1] )
    
            print ( dset_columns_events )
            print ( list( dset_columns_events ) )
            print ( dset_counts )
            print ( list( dset_counts ) )
            print ( dset_selections )
            print ( list( dset_selections ) )

