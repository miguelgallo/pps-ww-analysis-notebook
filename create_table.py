import uproot
import awkward as ak
import numpy as np
import pandas as pd
import numba as nb
import h5py

# from processing import run_ranges_periods_2017, run_ranges_periods_2018, lumi_periods_2017, lumi_periods_2018
from processing import df_run_ranges_2017, df_run_ranges_2018, df_run_ranges_mixing_2017, df_run_ranges_mixing_2018, lumi_periods_2017, lumi_periods_2018

def create_table( fileNames, label, lepton_type, data_sample, tree_path="demo/SlimmedNtuple", mix_protons=False, proton_files=None, random_protons=False, resample_factor=-1, runOnMC=False, data_periods=None, step_size=100000, firstEvent=None, entryStop=None, debug=False, output_dir="" ):

    if lepton_type not in ( 'muon', 'electron' ):
        raise RuntimeError( "Invalid lepton_type argument." )

    if data_sample not in ( '2017', '2018' ):
        raise RuntimeError( "Invalid data_sample argument." )

    if mix_protons and random_protons:
        raise RuntimeError( "Cannot set mix_protons and random_protons simultaneously." )
    
    fileNames_ = fileNames
    label_ = label
    lepton_type_ = lepton_type
    data_sample_ = data_sample
    # tree_path_ = "demo/SlimmedNtuple"
    # tree_path_ = "SlimmedNtuple"
    tree_path_ = tree_path
    tree_path_proton_files_ = "SlimmedNtuple"
    # output_path_ = "output"
    output_dir_ = None
    if output_dir is not None and output_dir != "": output_dir_ = output_dir

    df_run_ranges_ = None
    df_run_ranges_mixing_ = None
    if data_sample_ == '2017':
        # df_run_ranges_ = pd.DataFrame( run_ranges_periods_2017, index=("min","max") ).transpose()
        df_run_ranges_ = df_run_ranges_2017
        df_run_ranges_mixing_ = df_run_ranges_mixing_2017
    elif data_sample_ == '2018':
        # df_run_ranges_ = pd.DataFrame( run_ranges_periods_2018, index=("min","max") ).transpose()
        df_run_ranges_ = df_run_ranges_2018
        df_run_ranges_mixing_ = df_run_ranges_mixing_2018
    print ( df_run_ranges_ )
    print ( df_run_ranges_mixing_ )

    runOnMC_ = runOnMC
    data_periods_ = data_periods if ( runOnMC_ and data_periods is not None and len(data_periods) > 0 ) else None
    if runOnMC_ and not data_periods_:
        # if data_sample_ == '2017':
        #     data_periods_ = list( run_ranges_periods_2017.keys() )
        # elif data_sample_ == '2018':
        #     data_periods_ = list( run_ranges_periods_2018.keys() )
        data_periods_ = list( df_run_ranges_.index )

    # df_run_ranges_ = None
    # if data_sample_ == '2017':
    #     df_run_ranges_ = pd.DataFrame( run_ranges_periods_2017, index=("min","max") ).transpose()
    # elif data_sample_ == '2018':
    #     df_run_ranges_ = pd.DataFrame( run_ranges_periods_2018, index=("min","max") ).transpose()

    mix_protons_ = mix_protons
    proton_files_ = proton_files if ( mix_protons_ and proton_files is not None and len(proton_files) > 0 ) else None
    if mix_protons_ and not proton_files_:
        raise RuntimeError( "Invalid proton_files argument." )
 
    random_protons_ = random_protons
    resample_factor_ = resample_factor
    step_size_ = step_size
    firstEvent_ = firstEvent
    entryStop_ = entryStop

    fill_proton_extra_ = True

    how_ = None
    #how_ = "zip"
    
    print ( "Run on MC: {}".format( runOnMC_ ) )

    lumi_periods_ = None
    if data_sample_ == '2017':
        if lepton_type_ == 'muon':
            lumi_periods_ = lumi_periods_2017[ 'muon' ]
        elif lepton_type_ == 'electron':
            lumi_periods_ = lumi_periods_2017[ 'electron' ]
    elif data_sample_ == '2018':
        if lepton_type_ == 'muon':
            lumi_periods_ = lumi_periods_2018[ 'muon' ]
        elif lepton_type_ == 'electron':
            lumi_periods_ = lumi_periods_2018[ 'electron' ]

    lumi_weights_ = None
    probs_lumi_ = None
    if runOnMC_:
        print ( "Data periods: ", data_periods_ )
        # lumi_periods_sel_ = {}
        # lumi_values_ = []
        # for key_ in data_periods_:
        #     lumi_periods_sel_[ key_ ] = lumi_periods[ key_ ]
        #     lumi_values_.append( lumi_periods[ key_ ] )
        # print ( "Lumi: ", lumi_periods_sel_ )
        lumi_weights_ = pd.Series( lumi_periods_ )
        lumi_weights_ = lumi_weights_.loc[ data_periods_ ]
        probs_lumi_ = lumi_weights_ / lumi_weights_.sum()
        print ( "Data periods: ", data_periods_ )
        print ( "Lumi values: ", lumi_weights_)
        probs_lumi_ = lumi_weights_ / np.sum( lumi_weights_ )
        print ( "Prob. lumi: ", probs_lumi_ ) 

    print ( "Mix protons: {}".format( mix_protons_ ) )

    if mix_protons_:
        print ( "Proton files: {}".format( proton_files_ ) )

    print ( "Random protons: {}".format( random_protons_ ) )
    
    resample = False
    if resample_factor_ > 1: resample = True
    print ( "Resample: {} / Resample factor: {}".format( resample,  resample_factor_ ) )

    np.random.seed( 42 )

    # ranges_crossing_angles_ = ( 100. + np.arange( 11 ) * 10. )
    # ranges_crossing_angles_ = [ 100., 130., 140., 150., 200. ]
    ranges_crossing_angles_ = None
    if data_sample_ == '2017':
        ranges_crossing_angles_ = [ 100., 130., 140., 150., 200. ]
    elif data_sample_ == '2018':
        ranges_crossing_angles_ = [ 120., 140., 150., 170. ]

    # Read proton files
    protons_mix_all_ = None
    protons_extra_mix_all_ = None
    ppstracks_mix_all_ = None
    if mix_protons_:
        protons_mix_all_ = {}
        if fill_proton_extra_:
            protons_extra_mix_all_ = {}
        ppstracks_mix_all_ = {}

        for file_ in proton_files_:
            print ( file_ ) 
            root_ = uproot.open( file_ )
        
            print ( "Number of events in tree: {}".format( np.array( root_[ tree_path_proton_files_ + "/event" ] ).size ) )
        
            tree_ = root_[ tree_path_proton_files_ ]

            keys_nonproton_ = [ "run", "event", "lumiblock", "crossingAngle", "betaStar" ]
            keys_proton_ = tree_.keys( filter_name="proton*")
            keys_ppstrack_ = tree_.keys( filter_name="pps_track*")
            keys_proton_extra_ = [ 'proton_trackx2', 'proton_tracky2', 'proton_trackpixshift2', 'proton_rpid2' ]
            keys_ = []
            keys_.extend( keys_nonproton_ )
            keys_.extend( keys_proton_ )
            keys_.extend( keys_ppstrack_ )
            if how_ == "zip":
                for key_ in keys_proton_extra_:
                    if key_ in keys_: keys_.remove( key_ )
            print ( keys_ )
            
            for events_ in tree_.iterate( keys_ , library="ak", how=how_, step_size=100000 ):
                print ( events_, len( events_ ) )
                
                # Fetch protons
                protons_ = None
                protons_extra_ = None
                ppstracks_ = None
                if how_ == "zip":
                    protons_ = events_["proton"]
                    ppstracks_ = events_["pps_track"]
                elif how_ is None:
                    keys_proton_ = keys_proton_.copy()
                    for key_ in keys_proton_extra_:
                        if key_ in keys_proton_: keys_proton_.remove( key_ )
        
                    arrays_proton_ = {}
                    for key_ in keys_proton_: arrays_proton_[ key_[ len("proton_") : ] ] = events_[ key_ ]
                    arrays_proton_[ "random" ] = ak.ones_like( arrays_proton_[ "arm" ] )
                    protons_ = ak.zip( arrays_proton_ )
        
                    if fill_proton_extra_:
                        arrays_proton_extra_ = {}
                        for key_ in keys_proton_extra_: arrays_proton_extra_[ key_[ len("proton_") : ] ] = events_[ key_ ]
                        protons_extra_ = ak.zip( arrays_proton_extra_ )
        
                    arrays_ppstrack_ = {}
                    for key_ in keys_ppstrack_: arrays_ppstrack_[ key_[ len("pps_track_") : ] ] = events_[ key_ ]
                    ppstracks_ = ak.zip( arrays_ppstrack_ )        
 
                protons_[ "run_rnd" ] = events_[ "run" ]
                protons_[ "lumiblock_rnd" ] = events_[ "lumiblock" ]
                protons_[ "event_rnd" ] = events_[ "event" ]
                protons_[ "crossingAngle_rnd" ] = events_[ "crossingAngle" ]
                protons_[ "betaStar_rnd" ] = events_[ "betaStar" ]
                ppstracks_[ "run_rnd" ] = events_[ "run" ]
                ppstracks_[ "lumiblock_rnd" ] = events_[ "lumiblock" ]
                ppstracks_[ "event_rnd" ] = events_[ "event" ]
                ppstracks_[ "crossingAngle_rnd" ] = events_[ "crossingAngle" ]
                ppstracks_[ "betaStar_rnd" ] = events_[ "betaStar" ]
                   
                print ( protons_, len( protons_ ), ak.num( protons_ ) )
                if fill_proton_extra_:
                    print ( protons_extra_, len( protons_extra_ ), ak.num( protons_extra_ ) )
                print ( ppstracks_, len( ppstracks_ ), ak.num( ppstracks_ ) )                
                # for key_ in df_run_ranges_.index:
                for key_ in df_run_ranges_mixing_.index:
                    msk_period_ = ( ( events_[ "run" ] >= df_run_ranges_mixing_.loc[ key_ ][ "min" ] ) & ( events_[ "run" ] <= df_run_ranges_mixing_.loc[ key_ ][ "max" ] ) )
                    print ( msk_period_, np.sum( msk_period_ ) )

                    if len( events_[ msk_period_ ] ) > 0:
                        # if key_ not in protons_mix_all_.keys():
                        #     protons_mix_all_[ key_ ] = protons_[ msk_period_ ]
                        # else:
                        #     protons_mix_all_[ key_ ] = ak.concatenate( [ protons_mix_all_[ key_ ], protons_[ msk_period_ ] ], axis=0 )

                        # if fill_proton_extra_:    
                        #     if key_ not in protons_extra_mix_all_.keys():
                        #         protons_extra_mix_all_[ key_ ] = protons_extra_[ msk_period_ ]
                        #     else:
                        #         protons_extra_mix_all_[ key_ ] = ak.concatenate( [ protons_extra_mix_all_[ key_ ], protons_extra_[ msk_period_ ] ], axis=0 )

                        # if key_ not in ppstracks_mix_all_.keys():
                        #     ppstracks_mix_all_[ key_ ] = ppstracks_[ msk_period_ ]
                        # else:
                        #     ppstracks_mix_all_[ key_ ] = ak.concatenate( [ ppstracks_mix_all_[ key_ ], ppstracks_[ msk_period_ ] ], axis=0 )
                        if key_ not in protons_mix_all_.keys(): protons_mix_all_[ key_ ] = {}
                        if fill_proton_extra_:
                            if key_ not in protons_extra_mix_all_.keys(): protons_extra_mix_all_[ key_ ] = {}
                        if key_ not in ppstracks_mix_all_.keys(): ppstracks_mix_all_[ key_ ] = {}
                        for idx_, xangle_ in enumerate( ranges_crossing_angles_[:-1] ):
                            msk_xangle_ = ( ( events_[ "crossingAngle" ][ msk_period_ ] >= xangle_ ) &
                                            ( events_[ "crossingAngle" ][ msk_period_ ] < ranges_crossing_angles_[ idx_ + 1 ] ) )
                            print ( msk_xangle_, np.sum( msk_xangle_ ) )

                            if len( events_[ msk_period_ ][ msk_xangle_ ] ) > 0:
                                key_xangle_ = int( xangle_ )

                                if key_xangle_ not in protons_mix_all_[ key_ ].keys():
                                    protons_mix_all_[ key_ ][ key_xangle_ ] = protons_[ msk_period_ ][ msk_xangle_ ]
                                else:
                                    protons_mix_all_[ key_ ][ key_xangle_ ] = ak.concatenate( [ protons_mix_all_[ key_ ][ key_xangle_ ], protons_[ msk_period_ ][ msk_xangle_ ] ], axis=0 )
                                if fill_proton_extra_:
                                    if key_xangle_ not in protons_extra_mix_all_[ key_ ].keys():
                                        protons_extra_mix_all_[ key_ ][ key_xangle_ ] = protons_extra_[ msk_period_ ][ msk_xangle_ ]
                                    else:
                                        protons_extra_mix_all_[ key_ ][ key_xangle_ ] = ak.concatenate( [ protons_extra_mix_all_[ key_ ][ key_xangle_ ], protons_extra_[ msk_period_ ][ msk_xangle_ ] ], axis=0 )

                                if key_xangle_ not in ppstracks_mix_all_[ key_ ].keys():
                                    ppstracks_mix_all_[ key_ ][ key_xangle_ ] = ppstracks_[ msk_period_ ][ msk_xangle_ ]
                                else:
                                    ppstracks_mix_all_[ key_ ][ key_xangle_ ] = ak.concatenate( [ ppstracks_mix_all_[ key_ ][ key_xangle_ ], ppstracks_[ msk_period_ ][ msk_xangle_ ] ], axis=0 )

            # end iterate
        # end loop files
        
        print ( "Collections concatenated:" )
        print ( protons_mix_all_ )
        if fill_proton_extra_:
            print ( protons_extra_mix_all_ )
        print ( ppstracks_mix_all_ )
        # for key_ in df_run_ranges_.index:
        for key_ in df_run_ranges_mixing_.index:
            print ( key_ )
            # print ( protons_mix_all_[ key_ ], len( protons_mix_all_[ key_ ] ), ak.num( protons_mix_all_[ key_ ] ) )
            # if fill_proton_extra_:
            #     print ( protons_extra_mix_all_[ key_ ], len( protons_extra_mix_all_[ key_ ] ), ak.num( protons_extra_mix_all_[ key_ ] ) )
            # print ( ppstracks_mix_all_[ key_ ], len( ppstracks_mix_all_[ key_ ] ), ak.num( ppstracks_mix_all_[ key_ ] ) )
            if key_ in protons_mix_all_.keys():
                for xangle_ in ranges_crossing_angles_[:-1]:
                    key_xangle_ = int( xangle_ )
                    print ( key_xangle_ )
                    if key_xangle_ in protons_mix_all_[ key_ ].keys():
                        print ( protons_mix_all_[ key_ ][ key_xangle_ ], len( protons_mix_all_[ key_ ][ key_xangle_ ] ), ak.num( protons_mix_all_[ key_ ][ key_xangle_ ] ) )
                        if fill_proton_extra_:
                            print ( protons_extra_mix_all_[ key_ ][ key_xangle_ ], len( protons_extra_mix_all_[ key_ ][ key_xangle_ ] ), ak.num( protons_extra_mix_all_[ key_ ][ key_xangle_ ] ) )
                        print ( ppstracks_mix_all_[ key_ ][ key_xangle_ ], len( ppstracks_mix_all_[ key_ ][ key_xangle_ ] ), ak.num( ppstracks_mix_all_[ key_ ][ key_xangle_ ] ) )

        # Randomize
        # for key_ in run_ranges_periods:
        #     index_rnd_ = np.random.permutation( len( protons_mix_all_[ key_ ] ) )
        #     protons_mix_all_rnd_ = protons_mix_all_[ key_ ][ index_rnd_ ]
        #     if fill_proton_extra_:
        #         protons_extra_mix_all_rnd_ = protons_extra_mix_all_[ key_ ][ index_rnd_ ]
        #     ppstracks_mix_all_rnd_ = ppstracks_mix_all_[ key_ ][ index_rnd_ ]

        #     print ( "Collections randomized:" )
        #     print ( protons_mix_all_rnd_, len( protons_mix_all_rnd_ ), ak.num( protons_mix_all_rnd_ ) )
        #     if fill_proton_extra_:
        #         print ( protons_extra_mix_all_rnd_, len( protons_extra_mix_all_rnd_ ), ak.num( protons_extra_mix_all_rnd_ ) )
        #     print ( ppstracks_mix_all_rnd_, len( ppstracks_mix_all_rnd_ ), ak.num( ppstracks_mix_all_rnd_ ) )

        #     protons_mix_all_[ key_ ] = protons_mix_all_rnd_
        #     if fill_proton_extra_:
        #         protons_extra_mix_all_[ key_ ] = protons_extra_mix_all_rnd_
        #     ppstracks_mix_all_[ key_ ] = ppstracks_mix_all_rnd_

    dset_chunk_size = 50000

    # columns_protons = [ "run", "lumiblock", "event", "slice", "crossingAngle", "betaStar", "instLumi", "xi", "thx", "thy", "t", "ismultirp", "rpid", "arm", "random",
    #                     "jet0_pt", "jet0_eta", "jet0_phi", "jet0_energy", "jet0_mass", "jet0_corrmass", "jet0_tau1", "jet0_tau2", "jet0_vertexz",
    #                     "jet0_px", "jet0_py", "jet0_pz",
    #                     "muon0_pt", "muon0_eta", "muon0_phi", "muon0_energy", "muon0_charge", "muon0_iso", "muon0_dxy", "muon0_dz",
    #                     "met", "met_x", "met_y", "met_phi",
    #                     "nVertices",
    #                     "num_bjets_ak8", "num_bjets_ak4", "num_jets_ak4",
    #                     "pfcand_nextracks", "pfcand_nextracks_noDRl",
    #                     "recoMWhad", "recoMWlep", "recoMWW", "recoRapidityWW", "dphiWW", "WLeptonicPt", "WLeptonicEta", "WLeptonicPhi" ]
    columns_protons = [ "run", "lumiblock", "event", "slice", "crossingAngle", "betaStar", "instLumi", "xi", "thx", "thy", "t", "ismultirp", "rpid", "arm", "random",
                        "jet0_pt", "jet0_eta", "jet0_phi", "jet0_energy", "jet0_mass", "jet0_corrmass", "jet0_tau1", "jet0_tau2", "jet0_vertexz",
                        "jet0_px", "jet0_py", "jet0_pz",
                        "calo_met", "met", "met_x", "met_y", "met_phi",
                        "nVertices",
                        "num_bjets_ak8", "num_bjets_ak4", "num_jets_ak4",
                        "pfcand_nextracks", "pfcand_nextracks_noDRl",
                        "recoMWhad", "recoMWlep", "recoMWW", "recoRapidityWW", "dphiWW", "WLeptonicPt", "WLeptonicEta", "WLeptonicPhi" ]
    if lepton_type_ == 'muon':
        columns_protons.extend( [ "muon0_pt", "muon0_eta", "muon0_phi", "muon0_energy", "muon0_charge", "muon0_iso", "muon0_dxy", "muon0_dz", "muon0_trackerLayersWithMeasurement" ] )
    elif lepton_type_ == 'electron':
        columns_protons.extend( [ "electron0_pt", "electron0_eta", "electron0_phi", "electron0_energy", "electron0_charge", "electron0_dxy", "electron0_dz", 'electron0_corr', 'electron0_ecalTrkEnPostCorr', 'electron0_ecalTrkEnErrPostCorr', 'electron0_ecalTrkEnPreCorr', 'electron0_energyScaleUp', 'electron0_energyScaleDown' ] )

    columns_protons_multiRP = columns_protons.copy()

    if runOnMC_:
        columns_runOnMC_  = []

        columns_runOnMC_.extend( [ "run_mc" ] )

        # if data_sample_ == '2017':
        #     columns_runOnMC_.extend( [ "pileupWeight", "mc_pu_trueinteractions", "mcWeight", 'prefiring_weight', 'prefiring_weight_up', 'prefiring_weight_down', 'prefiring_weight_ECAL', 'prefiring_weight_ECAL_up', 'prefiring_weight_ECAL_down', 'prefiring_weight_Muon', 'prefiring_weight_Muon_up', 'prefiring_weight_Muon_down' ] )
        # else:
        #     columns_runOnMC_.extend( [ "pileupWeight", "mc_pu_trueinteractions", "mcWeight", 'prefiring_weight', 'prefiring_weight_up', 'prefiring_weight_down', 'prefiring_weight_ECAL', 'prefiring_weight_ECAL_up', 'prefiring_weight_ECAL_down', 'prefiring_weight_Muon', 'prefiring_weight_Muon_up', 'prefiring_weight_Muon_down' ] )
        columns_runOnMC_.extend( [ "pileupWeight", "mc_pu_trueinteractions", "mcWeight", 'prefiring_weight', 'prefiring_weight_up', 'prefiring_weight_down', 'prefiring_weight_ECAL', 'prefiring_weight_ECAL_up', 'prefiring_weight_ECAL_down', 'prefiring_weight_Muon', 'prefiring_weight_Muon_up', 'prefiring_weight_Muon_down' ] )

        columns_runOnMC_.extend( [ "jet0_jer_res", "jet0_jer_sf", "jet0_jer_sfup", "jet0_jer_sfdown", 'jet0_cjer', 'jet0_cjer_up', 'jet0_cjer_down' ] )

        if lepton_type_ == 'electron':
            columns_runOnMC_.extend( [ 'electron0_energySigmaUp', 'electron0_energySigmaDown' ] )

        columns_runOnMC_.extend( [ 'met_ptJER_Up', 'met_ptJER_Down', 'met_phiJER_Up', 'met_phiJER_Down', 'met_ptJES_Up', 'met_ptJES_Down', 'met_phiJES_Up', 'met_phiJES_Down' ] )
        columns_runOnMC_.extend( [ "gen_jet0_pt", "gen_jet0_eta", "gen_jet0_phi", "gen_jet0_energy" ] )
        if lepton_type_ == 'muon':
            columns_runOnMC_.extend( [ "gen_muon0_pt", "gen_muon0_eta", "gen_muon0_phi", "gen_muon0_energy", "gen_muon0_charge", "gen_muon0_mass" ] )
        elif lepton_type_ == 'electron':
            columns_runOnMC_.extend( [ "gen_electron0_pt", "gen_electron0_eta", "gen_electron0_phi", "gen_electron0_energy", "gen_electron0_charge", "gen_electron0_mass" ] )

        columns_protons.extend( columns_runOnMC_ )
        columns_protons_multiRP.extend( columns_runOnMC_ )

    if random_protons_ or mix_protons_:
        # columns_protons.extend( [ "run_rnd", "lumiblock_rnd", "event_rnd", "slice_rnd" ] )
        # columns_protons_multiRP.extend( [ "run_rnd", "lumiblock_rnd", "event_rnd", "slice_rnd" ] )
        columns_protons.extend( [ "run_rnd", "lumiblock_rnd", "event_rnd", "crossingAngle_rnd", "betaStar_rnd" ] )
        columns_protons_multiRP.extend( [ "run_rnd", "lumiblock_rnd", "event_rnd", "crossingAngle_rnd", "betaStar_rnd" ] )

    if fill_proton_extra_:
        columns_protons.extend( [ "trackx1", "tracky1", "trackpixshift1", "rpid1" ] )
        columns_protons_multiRP.extend( [ "trackx1", "tracky1", "trackpixshift1", "rpid1", "trackx2", "tracky2", "trackpixshift2", "rpid2" ] )
   
    columns_ppstracks = [ "run", "lumiblock", "event", "slice", "crossingAngle", "betaStar", "x", "y", "rpid" ] 

    if runOnMC_:
        columns_ppstracks.extend( [ "run_mc" ] )

    if random_protons_ or mix_protons_:
        # columns_ppstracks.extend( [ "run_rnd", "lumiblock_rnd", "event_rnd", "slice_rnd" ] )
        columns_ppstracks.extend( [ "run_rnd", "lumiblock_rnd", "event_rnd", "crossingAngle_rnd", "betaStar_rnd" ] )

    protons_keys = {}
    for col_ in columns_protons_multiRP:
        protons_keys[ col_ ] = col_
    protons_keys[ "ismultirp" ] = "ismultirp_"

    ppstracks_keys = {}
    for col_ in columns_ppstracks:
        ppstracks_keys[ col_ ] = col_

    counts_label_protons_ = "Proton" if not ( random_protons_ or mix_protons_ ) else "ProtonRnd"

    # output_file_path_ = ( output_path_ + '/' + 'output-' + label_ + '.h5' )
    file_name_label_ = 'output-{}.h5'.format( label_ )
    if output_dir_ is not None and output_dir_ != "":
        output_file_path_ = '{}/{}'.format( output_dir_ , file_name_label_ )
    else:
        output_file_path_ = file_name_label_
    print ( output_file_path_ )
    with h5py.File( output_file_path_, 'w') as f:

        dset_protons_multiRP = f.create_dataset( 'protons_multiRP', ( dset_chunk_size, len( columns_protons_multiRP ) ), compression="gzip", chunks=True, maxshape=( None , len( columns_protons_multiRP ) ) )
        print ( "Initial dataset shape: {}".format( dset_protons_multiRP.shape ) )

        dset_protons_singleRP = f.create_dataset( 'protons_singleRP', ( dset_chunk_size, len( columns_protons ) ), compression="gzip", chunks=True, maxshape=( None , len( columns_protons ) ) )
        print ( "Initial dataset shape: {}".format( dset_protons_singleRP.shape ) )

        dset_ppstracks = f.create_dataset( 'ppstracks', ( dset_chunk_size, len( columns_ppstracks ) ), compression="gzip", chunks=True, maxshape=( None , len( columns_ppstracks ) ) )
        print ( "Initial dataset shape: {}".format( dset_ppstracks.shape ) )

        protons_multiRP_list = {}
        for col_ in columns_protons_multiRP:
            protons_multiRP_list[ col_ ] = []           

        protons_singleRP_list = {}
        for col_ in columns_protons:
            protons_singleRP_list[ col_ ] = []           

        ppstracks_list = {}
        for col_ in columns_ppstracks:
            ppstracks_list[ col_ ] = []           

        selections = None
        counts = None

        dset_multiRP_slice = 0
        dset_multiRP_idx = 0
        dset_multiRP_entries = 0

        dset_singleRP_slice = 0
        dset_singleRP_idx = 0
        dset_singleRP_entries = 0

        dset_ppstracks_slice = 0
        dset_ppstracks_idx = 0
        dset_ppstracks_entries = 0

        for file_ in fileNames_:
            print ( file_ ) 
            root_ = uproot.open( file_ )

            print ( "Number of events in tree: {}".format( np.array( root_[ tree_path_ + "/event" ] ).size ) )

            tree_ = root_[ tree_path_ ]

            keys_nonproton = [ "run", "event", "lumiblock", "crossingAngle", "betaStar", "instLumi", "nVertices",
                               "num_bjets_ak8", "num_bjets_ak4", "num_jets_ak4",
                               "pfcand_nextracks", "pfcand_nextracks_noDRl",
                               "recoMWhad", "recoMWlep", "recoMWW", "recoRapidityWW", "dphiWW", "WLeptonicPt", "WLeptonicEta", "WLeptonicPhi",
                               "pileupWeight", "mc_pu_trueinteractions", "mcWeight" ]
            keys_jet = tree_.keys( filter_name="jet*")
            keys_nonproton.extend( keys_jet )
            keys_genjet = tree_.keys( filter_name="gen_jet*")
            keys_genmuon = tree_.keys( filter_name="gen_muon*")
            keys_genelectron = tree_.keys( filter_name="gen_electron*")
            keys_nonproton.extend( keys_genjet )
            keys_nonproton.extend( keys_genmuon )
            keys_nonproton.extend( keys_genelectron )
            if lepton_type_ == 'muon':
                keys_muon_ = tree_.keys( filter_name="muon*")
                keys_nonproton.extend( keys_muon_ )
            elif lepton_type_ == 'electron':
                keys_electron_ = tree_.keys( filter_name="electron*")
                keys_nonproton.extend( keys_electron_ )
            keys_met = tree_.keys( filter_name="met*")
            keys_calomet = tree_.keys( filter_name="calo_met*")
            keys_nonproton.extend( keys_met )
            keys_nonproton.extend( keys_calomet )
            keys_prefiring = tree_.keys( filter_name="prefiring*")
            keys_nonproton.extend( keys_prefiring )

            keys_proton = tree_.keys( filter_name="proton*")
            keys_ppstrack = tree_.keys( filter_name="pps_track*")
            keys = []
            keys.extend( keys_nonproton )
            keys.extend( keys_proton )
            keys.extend( keys_ppstrack )
            keys_proton_extra = [ 'proton_trackx2', 'proton_tracky2', 'proton_trackpixshift2', 'proton_rpid2' ]
            if how_ == "zip":
                for key_ in keys_proton_extra:
                    if key_ in keys: keys.remove( key_ )

            print ( keys )

            for events_ in tree_.iterate( keys , library="ak", how=how_, step_size=step_size_, entry_start=firstEvent_, entry_stop=entryStop_ ):
                print ( len(events_), events_ )

                print ( "Num jets: {}".format( ak.num( events_["jet_pt"] ) ) )
                if lepton_type_ == 'muon':
                    print ( "Num muons: {}".format( ak.num( events_["muon_pt"] ) ) )
                elif lepton_type_ == 'electron':
                    print ( "Num electrons: {}".format( ak.num( events_["electron_pt"] ) ) )
                print ( "Num protons: {}".format( ak.num( events_["proton_xi"] ) ) )
                print ( "Num pps tracks: {}".format( ak.num( events_["pps_track_x"] ) ) )

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
                if lepton_type_ == 'muon':
                    lepton_var_ = "muon_pt"
                    lepton_sel_name_ = 'Muon'
                elif lepton_type_ == 'electron':
                    lepton_var_ = "electron_pt"
                    lepton_sel_name_ = 'Electron'

                msk_1lep = msk_1jet & ( ak.num( events_[ lepton_var_ ] ) >= 1 )
                selections_.append( lepton_sel_name_ )
                counts_.append( np.sum( np.array( msk_1lep ).astype("int32") ) )

                events_ = events_[ msk_1lep ]    

                # selections_.append( "check_none" )
                # counts_.append( 0 )
                
                selections_ = np.array( selections_ )
                counts_ = np.array( counts_ )

                # Repeat events by resample factor
                if resample:
                    counts_ = counts_ * resample_factor_

                if selections is None:
                    selections = selections_
                    counts = counts_
                else:
                    msk_selections = np.full_like( selections, False, dtype='bool' )
                    for key in selections_:
                        msk_selections |= ( selections == key )
                    counts[ msk_selections ] += counts_

                # Repeat events by resample factor
                slices_ = np.zeros( len( events_ ), dtype=np.int32 )
                if resample:
                    events_size_ = len( events_ )
                    events_ = ak.concatenate( ( [events_] * resample_factor_ ), axis=0 )
                    slices_ = np.zeros( resample_factor_ * events_size_, dtype=np.int32 )
                    for idx_ in range( resample_factor_ ):
                        slices_[ ( idx_ * events_size_ ) : ( ( idx_ + 1 ) * events_size_ ) ] = idx_

                events_[ "slice" ] = slices_

                if runOnMC_:
                    sample_idx_arr_ = np.random.choice( np.arange( probs_lumi_.index.size ), len( events_ ), p=probs_lumi_ )
                    print ( "Sampled index: ", sample_idx_arr_ )
                    run_arr_ = np.apply_along_axis( lambda idx_: df_run_ranges_.loc[ probs_lumi_.index[ idx_ ] ][ "min" ], 0, sample_idx_arr_ )
                    print ( "Run numbers: ", run_arr_ )
                    events_[ "run_mc" ] = run_arr_

                print ( "Run: {}".format( events_[ "run" ] ) ) 
                print ( "Lumi: {}".format( events_[ "lumiblock" ] ) ) 
                print ( "Event: {}".format( events_[ "event" ] ) ) 
                print ( "Slice: {}".format( events_[ "slice" ] ) ) 
                print ( "Crossing angle: {}".format( events_[ "crossingAngle" ] ) ) 
                print ( "Num jets: {}".format( ak.num( events_["jet_pt"] ) ) )
                if lepton_type_ == 'muon':
                    print ( "Num muons: {}".format( ak.num( events_["muon_pt"] ) ) )
                elif lepton_type_ == 'electron':
                    print ( "Num electrons: {}".format( ak.num( events_["electron_pt"] ) ) )
                print ( "Num protons: {}".format( ak.num( events_["proton_xi"] ) ) )
                print ( "Num pps tracks: {}".format( ak.num( events_["pps_track_x"] ) ) )

                if runOnMC_:
                    print ( "Run MC: {}".format( events_[ "run_mc" ] ) )

                if debug:
                    print ( ak.to_list( events_ ) )

                # Fetch protons
                protons_ = None
                protons_extra_ = None
                ppstracks_ = None
                if how_ == "zip":
                    protons_ = events_["proton"]
                    ppstracks_ = events_["pps_track"]
                elif how_ is None:
                    keys_proton_ = keys_proton.copy()
                    for key_ in keys_proton_extra:
                        if key_ in keys_proton_: keys_proton_.remove( key_ )
    
                    arrays_proton = {}
                    for key_ in keys_proton_: arrays_proton[ key_[ len("proton_") : ] ] = events_[ key_ ]
                    if random_protons_:
                        arrays_proton[ "random" ] = ak.ones_like( arrays_proton[ "arm" ] )
                    else:
                        arrays_proton[ "random" ] = ak.zeros_like( arrays_proton[ "arm" ] )
                    protons_ = ak.zip( arrays_proton )

                    if fill_proton_extra_:
                        arrays_proton_extra = {}
                        for key_ in keys_proton_extra: arrays_proton_extra[ key_[ len("proton_") : ] ] = events_[ key_ ]
                        protons_extra_ = ak.zip( arrays_proton_extra )

                    arrays_ppstrack = {}
                    for key_ in keys_ppstrack: arrays_ppstrack[ key_[ len("pps_track_") : ] ] = events_[ key_ ]
                    ppstracks_ = ak.zip( arrays_ppstrack )

                # Randomize proton arrays (option random_protons)
                run_rnd_ = None
                lumiblock_rnd_ = None
                event_rnd_ = None
                # slice_rnd_ = None
                crossingAngle_rnd_ = None
                betaStar_rnd_ = None
                if random_protons_:
                    index_rnd_ = np.random.permutation( len( events_ ) )

                    events_run_ = events_[ "run" ]
                    events_lumiblock_ = events_[ "lumiblock" ]
                    events_event_ = events_[ "event" ]
                    # events_slice_ = events_[ "slice" ]
                    events_crossingAngle_ = events_[ "crossingAngle" ]
                    events_betaStar_ = events_[ "betaStar" ]
                    run_rnd_ = events_run_[ index_rnd_ ]
                    lumiblock_rnd_ = events_lumiblock_[ index_rnd_ ]
                    event_rnd_ = events_event_[ index_rnd_ ]
                    # slice_rnd_ = events_slice_[ index_rnd_ ]
                    crossingAngle_rnd_ = events_crossingAngle_[ index_rnd_ ]
                    betaStar_rnd_ = events_betaStar_[ index_rnd_ ]

                    protons_rnd_ = protons_[ index_rnd_ ]
                    ppstracks_rnd_ = ppstracks_[ index_rnd_ ]
                    protons_extra_rnd_ = None
                    if protons_extra_ is not None:
                        protons_extra_rnd_ = protons_extra_[ index_rnd_ ]

                    print ( "Run: {}".format( events_run_ ) ) 
                    print ( "Run randomized: {}".format( run_rnd_ ) ) 
                    print ( "Lumi: {}".format( events_lumiblock_ ) ) 
                    print ( "Lumi randomized: {}".format( lumiblock_rnd_ ) ) 
                    print ( "Event: {}".format( events_event_ ) ) 
                    print ( "Event randomized: {}".format( event_rnd_ ) ) 
                    # print ( "Slice: {}".format( events_slice_ ) ) 
                    # print ( "Slice randomized: {}".format( slice_rnd_ ) ) 
                    print ( "Crossing angle: {}".format( events_crossingAngle_ ) ) 
                    print ( "Crossing angle randomized: {}".format( crossingAngle_rnd_ ) ) 
                    print ( "Beta*: {}".format( events_betaStar_ ) ) 
                    print ( "Beta* randomized: {}".format( betaStar_rnd_ ) ) 
                    print ( "Num protons: {}".format( ak.num( protons_ ) ) )
                    print ( "Num protons randomized: {}".format( ak.num( protons_rnd_ ) ) )
                    print ( "Num pps tracks: {}".format( ak.num( ppstracks_ ) ) )
                    print ( "Num pps tracks randomized: {}".format( ak.num( ppstracks_rnd_ ) ) )
                    if protons_extra_rnd_ is not None:
                        print ( "Num protons extra: {}".format( ak.num( protons_extra_ ) ) )
                        print ( "Num protons extra randomized: {}".format( ak.num( protons_extra_rnd_ ) ) )

                    protons_ = protons_rnd_
                    if protons_extra_rnd_ is not None:
                        protons_extra_ = protons_extra_rnd_
                    ppstracks_ = ppstracks_rnd_
                # Mix protons randomly (option mix_protons)
                elif mix_protons_:
                    # Match size of proton arrays to main event arrays
                    # events_size_ = len( events_ )
                    # protons_mix_size_ = len( protons_mix_all_ ) # Number of events
                    # protons_mix_resized_ = None
                    # protons_extra_mix_resized_ = None
                    # ppstracks_mix_resized_ = None
                    # if events_size_ > protons_mix_size_:
                    #     floor_division_ = ( events_size_ // protons_mix_size_ ) 
                    #     protons_resample_factor_ = floor_division_ if ( events_size_ % protons_mix_size_ == 0 ) else ( floor_division_ + 1 )
                    #     protons_mix_concat_ = ak.concatenate( ( [protons_mix_all_] * protons_resample_factor_ ), axis=0 )
                    #     protons_mix_resized_ = protons_mix_concat_[ : events_size_ ]
                    #     if fill_proton_extra_:
                    #         protons_extra_mix_concat_ = ak.concatenate( ( [protons_extra_mix_all_] * protons_resample_factor_ ), axis=0 )
                    #         protons_extra_mix_resized_ = protons_extra_mix_concat_[ : events_size_ ]
                    #     ppstracks_mix_concat_ = ak.concatenate( ( [ppstracks_mix_all_] * protons_resample_factor_ ), axis=0 )
                    #     ppstracks_mix_resized_ = ppstracks_mix_concat_[ : events_size_ ]
                    # else:    
                    #     protons_mix_resized_ = protons_mix_all_[ : events_size_ ]
                    #     if fill_proton_extra_:
                    #         protons_extra_mix_resized_ = protons_extra_mix_all_[ : events_size_ ]
                    #     ppstracks_mix_resized_ = ppstracks_mix_all_[ : events_size_ ]
                    # print ( "Num protons: {}".format( ak.num( protons_ ) ) )
                    # print ( "Num protons mixed: {}".format( ak.num( protons_mix_resized_ ) ) )
                    # print ( "Num pps tracks: {}".format( ak.num( ppstracks_ ) ) )
                    # print ( "Num pps tracks mixed: {}".format( ak.num( ppstracks_mix_resized_ ) ) )
                    # if fill_proton_extra_:
                    #     print ( "Num protons extra: {}".format( ak.num( protons_extra_ ) ) )
                    #     print ( "Num protons extra mixed: {}".format( ak.num( protons_extra_mix_resized_ ) ) )
                    # protons_ = protons_mix_resized_
                    # if fill_proton_extra_:
                    #     protons_extra_ = protons_extra_mix_resized_
                    # ppstracks_ = ppstracks_mix_resized_
                    print ( "Num protons: {}".format( ak.num( protons_ ) ) )
                    if fill_proton_extra_:
                        print ( "Num protons extra: {}".format( ak.num( protons_extra_ ) ) )
                    print ( "Num pps tracks: {}".format( ak.num( ppstracks_ ) ) )
                    run_str_ = "run_mc" if runOnMC_ else "run"
                    events_mix_ = {}
                    protons_mix_ = {}
                    protons_extra_mix_ = {}
                    ppstracks_mix_ = {}
                    # for key_ in df_run_ranges_.index:
                    for key_ in df_run_ranges_mixing_.index:
                        print ( key_ )
                        msk_period_ = ( ( events_[ run_str_ ] >= df_run_ranges_mixing_.loc[ key_ ][ "min" ] ) & ( events_[ run_str_ ] <= df_run_ranges_mixing_.loc[ key_ ][ "max" ] ) )
                        print ( msk_period_ )

                        # protons_mix_size_ = len( protons_mix_all_[ key_ ] )

                        # events_size_ = len( events_[ msk_period_ ] )
                        # if events_size_ > 0:
                        #     index_rnd_ = np.random.randint( protons_mix_size_, size=events_size_ )

                        #     if key_ not in events_mix_.keys():
                        #         events_mix_[ key_ ] = events_[ msk_period_ ]
                        #     else:
                        #         events_mix_[ key_ ] = ak.concatenate( [ events_mix_[ key_ ], events_[ msk_period_ ] ], axis=0 )

                        #     protons_mix__ = protons_mix_all_[ key_ ][ index_rnd_ ] 
                        #     if key_ not in protons_mix_.keys():
                        #         protons_mix_[ key_ ] = protons_mix__
                        #     else:
                        #         protons_mix_[ key_ ] = ak.concatenate( [ protons_mix_[ key_ ], protons_mix__ ], axis=0 )

                        #     protons_extra_mix__ = protons_extra_mix_all_[ key_ ][ index_rnd_ ]
                        #     if fill_proton_extra_:
                        #         if key_ not in protons_extra_mix_.keys():
                        #             protons_extra_mix_[ key_ ] = protons_extra_mix__
                        #         else:
                        #             protons_extra_mix_[ key_ ] = ak.concatenate( [ protons_extra_mix_[ key_ ], protons_extra_mix__ ], axis=0 )

                        #     ppstracks_mix__ = ppstracks_mix_all_[ key_ ][ index_rnd_ ]
                        #     if key_ not in ppstracks_mix_.keys():
                        #         ppstracks_mix_[ key_ ] = ppstracks_mix__
                        #     else:
                        #         ppstracks_mix_[ key_ ] = ak.concatenate( [ ppstracks_mix_[ key_ ], ppstracks_mix__ ], axis=0 )

                        if len( events_[ msk_period_ ] ) > 0:
                            if key_ not in events_mix_.keys(): events_mix_[ key_ ] = {}
                            if key_ not in protons_mix_.keys(): protons_mix_[ key_ ] = {}
                            if fill_proton_extra_:
                                if key_ not in protons_extra_mix_.keys(): protons_extra_mix_[ key_ ] = {}
                            if key_ not in ppstracks_mix_.keys(): ppstracks_mix_[ key_ ] = {}

                            for idx_, xangle_ in enumerate( ranges_crossing_angles_[:-1] ):
                                msk_xangle_ = ( ( events_[ "crossingAngle" ][ msk_period_ ] >= xangle_ ) &
                                                ( events_[ "crossingAngle" ][ msk_period_ ] < ranges_crossing_angles_[ idx_ + 1 ] ) )
                                print ( msk_xangle_, np.sum( msk_xangle_ ) )

                                events_size_ = len( events_[ msk_period_ ][ msk_xangle_ ] )
                                if events_size_ > 0:
                                    key_xangle_ = int( xangle_ )
                                    protons_mix_size_ = len( protons_mix_all_[ key_ ][ key_xangle_ ] )
                                    index_rnd_ = np.random.randint( protons_mix_size_, size=events_size_ )

                                    events_mix__ = events_[ msk_period_ ][ msk_xangle_ ]
                                    if key_xangle_ not in events_mix_[ key_ ].keys():
                                        events_mix_[ key_ ][ key_xangle_ ] = events_mix__
                                    else:
                                        events_mix_[ key_ ][ key_xangle_ ] = ak.concatenate( [ events_mix_[ key_ ][ key_xangle_ ], events_mix__ ], axis=0 )

                                    protons_mix__ = protons_mix_all_[ key_ ][ key_xangle_ ][ index_rnd_ ] 
                                    if key_xangle_ not in protons_mix_[ key_ ].keys():
                                        protons_mix_[ key_ ][ key_xangle_ ] = protons_mix__
                                    else:
                                        protons_mix_[ key_ ][ key_xangle_ ] = ak.concatenate( [ protons_mix_[ key_ ][ key_xangle_ ], protons_mix__ ], axis=0 )

                                    if fill_proton_extra_:
                                        protons_extra_mix__ = protons_extra_mix_all_[ key_ ][ key_xangle_ ][ index_rnd_ ]
                                        if key_xangle_ not in protons_extra_mix_[ key_ ].keys():
                                            protons_extra_mix_[ key_ ][ key_xangle_ ] = protons_extra_mix__
                                        else:
                                            protons_extra_mix_[ key_ ][ key_xangle_ ] = ak.concatenate( [ protons_extra_mix_[ key_ ][ key_xangle_ ], protons_extra_mix__ ], axis=0 )

                                    ppstracks_mix__ = ppstracks_mix_all_[ key_ ][ key_xangle_ ][ index_rnd_ ]
                                    if key_xangle_ not in ppstracks_mix_[ key_ ].keys():
                                        ppstracks_mix_[ key_ ][ key_xangle_ ] = ppstracks_mix__
                                    else:
                                        ppstracks_mix_[ key_ ][ key_xangle_ ] = ak.concatenate( [ ppstracks_mix_[ key_ ][ key_xangle_ ], ppstracks_mix__ ], axis=0 )

                    events_mix_all_periods_ = None
                    protons_mix_all_periods_ = None
                    protons_extra_mix_all_periods_ = None
                    ppstracks_mix_all_periods_ = None
                    # for key_ in df_run_ranges_.index:
                    for key_ in df_run_ranges_mixing_.index:

                        # if events_mix_all_periods_ is None:
                        #     events_mix_all_periods_ = events_mix_[ key_ ]
                        # else:
                        #     events_mix_all_periods_ = ak.concatenate( [ events_mix_all_periods_, events_mix_[ key_ ] ], axis=0 ) 

                        # if protons_mix_all_periods_ is None:
                        #     protons_mix_all_periods_ = protons_mix_[ key_ ]
                        # else:
                        #     protons_mix_all_periods_ = ak.concatenate( [ protons_mix_all_periods_, protons_mix_[ key_ ] ], axis=0 )

                        # if fill_proton_extra_:
                        #     if protons_extra_mix_all_periods_ is None:
                        #         protons_extra_mix_all_periods_ = protons_extra_mix_[ key_ ]
                        #     else:
                        #         protons_extra_mix_all_periods_ = ak.concatenate( [ protons_extra_mix_all_periods_, protons_extra_mix_[ key_ ] ], axis=0 )

                        # if ppstracks_mix_all_periods_ is None:
                        #     ppstracks_mix_all_periods_ = ppstracks_mix_[ key_ ]
                        # else:
                        #     ppstracks_mix_all_periods_ = ak.concatenate( [ ppstracks_mix_all_periods_, ppstracks_mix_[ key_ ] ], axis=0 )

                        for xangle_ in ranges_crossing_angles_[:-1]:
                            key_xangle_ = int( xangle_ )

                            events_mix__ = events_mix_[ key_ ][ key_xangle_ ]
                            if events_mix_all_periods_ is None:
                                events_mix_all_periods_ = events_mix__
                            else:
                                events_mix_all_periods_ = ak.concatenate( [ events_mix_all_periods_, events_mix__ ], axis=0 ) 

                            protons_mix__ = protons_mix_[ key_ ][ key_xangle_ ]
                            if protons_mix_all_periods_ is None:
                                protons_mix_all_periods_ = protons_mix__
                            else:
                                protons_mix_all_periods_ = ak.concatenate( [ protons_mix_all_periods_, protons_mix__ ], axis=0 )

                            if fill_proton_extra_:
                                protons_extra_mix__ = protons_extra_mix_[ key_ ][ key_xangle_ ]
                                if protons_extra_mix_all_periods_ is None:
                                    protons_extra_mix_all_periods_ = protons_extra_mix__
                                else:
                                    protons_extra_mix_all_periods_ = ak.concatenate( [ protons_extra_mix_all_periods_, protons_extra_mix__ ], axis=0 )

                            ppstracks_mix__ = ppstracks_mix_[ key_ ][ key_xangle_ ]
                            if ppstracks_mix_all_periods_ is None:
                                ppstracks_mix_all_periods_ = ppstracks_mix__
                            else:
                                ppstracks_mix_all_periods_ = ak.concatenate( [ ppstracks_mix_all_periods_, ppstracks_mix__ ], axis=0 )

                    events_ = events_mix_all_periods_
                    protons_ = protons_mix_all_periods_
                    if fill_proton_extra_:
                        protons_extra_ = protons_extra_mix_all_periods_
                    ppstracks_ = ppstracks_mix_all_periods_

                    if runOnMC_:
                        print ( "Run MC: {}".format( events_[ "run_mc" ] ) )
                    else:
                        print ( "Run: {}".format( events_[ "run" ] ) )
                    print ( "Run mixed: {}".format( protons_[ "run_rnd" ] ) ) 

                    print ( "Num protons mixed: {}".format( ak.num( protons_ ) ) )
                    if fill_proton_extra_:
                        print ( "Num protons extra mixed: {}".format( ak.num( protons_extra_ ) ) )
                    print ( "Num pps tracks mixed: {}".format( ak.num( ppstracks_ ) ) )

                print ( "Num protons: {}".format( ak.num( protons_ ) ) )
                if protons_extra_ is not None:
                    print ( "Num protons extra: {}".format( ak.num( protons_extra_ ) ) )
                print ( "Num pps tracks: {}".format( ak.num( ppstracks_ ) ) )

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

                        if lepton_type_ == 'muon':
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
                        elif lepton_type_ == 'electron':
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

                protons_["run"]                    = events_["run"]
                protons_["lumiblock"]              = events_["lumiblock"]
                protons_["event"]                  = events_["event"]
                protons_["slice"]                  = events_["slice"]
                protons_["crossingAngle"]          = events_["crossingAngle"]
                protons_["betaStar"]               = events_["betaStar"]
                protons_["instLumi"]               = events_["instLumi"]
                if runOnMC_:
                    protons_["run_mc"] = events_["run_mc"]

                if random_protons_:
                    protons_["run_rnd"] = run_rnd_
                    protons_["lumiblock_rnd"] = lumiblock_rnd_
                    protons_["event_rnd"] = event_rnd_
                    # protons_["slice_rnd"] = slice_rnd_
                    protons_["crossingAngle_rnd"] = crossingAngle_rnd_
                    protons_["betaStar_rnd"] = betaStar_rnd_

                protons_["jet0_pt"]                = events_[ "jet_pt" ][:,0]
                protons_["jet0_eta"]               = events_[ "jet_eta" ][:,0]
                protons_["jet0_phi"]               = events_[ "jet_phi" ][:,0]
                protons_["jet0_energy"]            = events_[ "jet_energy" ][:,0]
                protons_["jet0_mass"]              = events_[ "jet_mass" ][:,0]
                protons_["jet0_corrmass"]          = events_[ "jet_corrmass" ][:,0]
                protons_["jet0_tau1"]              = events_[ "jet_tau1" ][:,0]
                protons_["jet0_tau2"]              = events_[ "jet_tau2" ][:,0]
                protons_["jet0_vertexz"]           = events_[ "jet_vertexz" ][:,0]
                protons_["jet0_px"]                = events_[ "jet_px" ][:,0]
                protons_["jet0_py"]                = events_[ "jet_py" ][:,0]
                protons_["jet0_pz"]                = events_[ "jet_pz" ][:,0]
                if runOnMC_:
                    protons_["jet0_jer_res"]       = events_[ "jet_jer_res" ][:,0]
                    protons_["jet0_jer_sf"]        = events_[ "jet_jer_sf" ][:,0]
                    protons_["jet0_jer_sfup"]      = events_[ "jet_jer_sfup" ][:,0]
                    protons_["jet0_jer_sfdown"]    = events_[ "jet_jer_sfdown" ][:,0]
                    protons_["jet0_cjer"]           = events_[ "jet_cjer" ][:,0]
                    protons_["jet0_cjer_up"]        = events_[ "jet_cjer_up" ][:,0]
                    protons_["jet0_cjer_down"]      = events_[ "jet_cjer_down" ][:,0]
                    # protons_["gen_jet0_pt"]                = events_[ "gen_jet_pt" ][:,0]
                    # protons_["gen_jet0_eta"]               = events_[ "gen_jet_eta" ][:,0]
                    # protons_["gen_jet0_phi"]               = events_[ "gen_jet_phi" ][:,0]
                    # protons_["gen_jet0_energy"]            = events_[ "gen_jet_energy" ][:,0]
                    protons_["gen_jet0_pt"]        = genjets_sel_[ "pt" ][:,0]
                    protons_["gen_jet0_eta"]       = genjets_sel_[ "eta" ][:,0]
                    protons_["gen_jet0_phi"]       = genjets_sel_[ "phi" ][:,0]
                    protons_["gen_jet0_energy"]    = genjets_sel_[ "energy" ][:,0]

                if lepton_type_ == 'muon':
                    protons_["muon0_pt"]                           = events_[ "muon_pt" ][:,0]
                    protons_["muon0_eta"]                          = events_[ "muon_eta" ][:,0]
                    protons_["muon0_phi"]                          = events_[ "muon_phi" ][:,0]
                    protons_["muon0_energy"]                       = events_[ "muon_e" ][:,0]
                    protons_["muon0_charge"]                       = events_[ "muon_charge" ][:,0]
                    protons_["muon0_iso"]                          = events_[ "muon_iso" ][:,0]
                    protons_["muon0_dxy"]                          = events_[ "muon_dxy" ][:,0]
                    protons_["muon0_dz"]                           = events_[ "muon_dz" ][:,0]
                    protons_["muon0_trackerLayersWithMeasurement"] = events_[ "muon_trackerLayersWithMeasurement" ][:,0]
                    if runOnMC_:
                        protons_["gen_muon0_pt"]        = genmuons_sel_[ "pt" ][:,0]
                        protons_["gen_muon0_eta"]       = genmuons_sel_[ "eta" ][:,0]
                        protons_["gen_muon0_phi"]       = genmuons_sel_[ "phi" ][:,0]
                        protons_["gen_muon0_energy"]    = genmuons_sel_[ "energy" ][:,0]
                        protons_["gen_muon0_charge"]    = genmuons_sel_[ "charge" ][:,0]
                        protons_["gen_muon0_mass"]      = genmuons_sel_[ "mass" ][:,0]
                elif lepton_type_ == 'electron':
                    protons_["electron0_pt"]                   = events_[ "electron_pt" ][:,0]
                    protons_["electron0_eta"]                  = events_[ "electron_eta" ][:,0]
                    protons_["electron0_phi"]                  = events_[ "electron_phi" ][:,0]
                    protons_["electron0_energy"]               = events_[ "electron_e" ][:,0]
                    protons_["electron0_charge"]               = events_[ "electron_charge" ][:,0]
                    protons_["electron0_dxy"]                  = events_[ "electron_dxy" ][:,0]
                    protons_["electron0_dz"]                   = events_[ "electron_dz" ][:,0]
                    protons_["electron0_corr"]                 = events_[ "electron_corr" ][:,0]
                    protons_["electron0_ecalTrkEnPostCorr"]    = events_[ "electron_ecalTrkEnPostCorr" ][:,0]
                    protons_["electron0_ecalTrkEnErrPostCorr"] = events_[ "electron_ecalTrkEnErrPostCorr" ][:,0]
                    protons_["electron0_ecalTrkEnPreCorr"]     = events_[ "electron_ecalTrkEnPreCorr" ][:,0]
                    protons_["electron0_energyScaleUp"]        = events_[ "electron_energyScaleUp" ][:,0]
                    protons_["electron0_energyScaleDown"]      = events_[ "electron_energyScaleDown" ][:,0]
                    if runOnMC_:
                        protons_["electron0_energySigmaUp"]    = events_[ "electron_energySigmaUp" ][:,0]
                        protons_["electron0_energySigmaDown"]  = events_[ "electron_energySigmaDown" ][:,0]
                        protons_["gen_electron0_pt"]        = genelectrons_sel_[ "pt" ][:,0]
                        protons_["gen_electron0_eta"]       = genelectrons_sel_[ "eta" ][:,0]
                        protons_["gen_electron0_phi"]       = genelectrons_sel_[ "phi" ][:,0]
                        protons_["gen_electron0_energy"]    = genelectrons_sel_[ "energy" ][:,0]
                        protons_["gen_electron0_charge"]    = genelectrons_sel_[ "charge" ][:,0]
                        protons_["gen_electron0_mass"]      = genelectrons_sel_[ "mass" ][:,0]

                protons_["calo_met"]               = events_["calo_met"]
                protons_["met"]                    = events_["met"]
                protons_["met_x"]                  = events_["met_x"]
                protons_["met_y"]                  = events_["met_y"]
                protons_["met_phi"]                = events_["met_phi"]
                protons_["nVertices"]              = events_["nVertices"]
                protons_["num_bjets_ak8"]          = events_["num_bjets_ak8"]
                protons_["num_bjets_ak4"]          = events_["num_bjets_ak4"]
                protons_["num_jets_ak4"]           = events_["num_jets_ak4"]
                protons_["pfcand_nextracks"]       = events_["pfcand_nextracks"]
                protons_["pfcand_nextracks_noDRl"] = events_["pfcand_nextracks_noDRl"]
                protons_["recoMWhad"]              = events_["recoMWhad"]
                protons_["recoMWlep"]              = events_["recoMWlep"]
                protons_["recoMWW"]                = events_["recoMWW"]
                protons_["recoRapidityWW"]         = events_["recoRapidityWW"]
                protons_["dphiWW"]                 = events_["dphiWW"]
                protons_["WLeptonicPt"]            = events_["WLeptonicPt"]
                protons_["WLeptonicEta"]           = events_["WLeptonicEta"]
                protons_["WLeptonicPhi"]           = events_["WLeptonicPhi"]
                if runOnMC_:
                    protons_["met_ptJER_Up"]           = events_["met_ptJER_Up"]
                    protons_["met_ptJER_Down"]         = events_["met_ptJER_Down"]
                    protons_["met_phiJER_Up"]          = events_["met_phiJER_Up"]
                    protons_["met_phiJER_Down"]        = events_["met_phiJER_Down"]
                    protons_["met_ptJES_Up"]           = events_["met_ptJES_Up"]
                    protons_["met_ptJES_Down"]         = events_["met_ptJES_Down"]
                    protons_["met_phiJES_Up"]          = events_["met_phiJES_Up"]
                    protons_["met_phiJES_Down"]        = events_["met_phiJES_Down"]
                    protons_["pileupWeight"]           = events_["pileupWeight"]
                    protons_["mc_pu_trueinteractions"] = events_["mc_pu_trueinteractions"]
                    protons_["mcWeight"]               = events_["mcWeight"]
                    # if data_sample_ == '2017':
                    #     protons_["prefiring_weight"]       = events_["prefiring_weight"]
                    #     protons_["prefiring_weight_up"]    = events_["prefiring_weight_up"]
                    #     protons_["prefiring_weight_down"]  = events_["prefiring_weight_down"]
                    protons_["prefiring_weight"]       = events_["prefiring_weight"][ 0 ]
                    protons_["prefiring_weight_up"]    = events_["prefiring_weight_up"][ 0 ]
                    protons_["prefiring_weight_down"]  = events_["prefiring_weight_down"][ 0 ]
                    protons_["prefiring_weight_ECAL"]       = events_["prefiring_weight_ECAL"][ 0 ]
                    protons_["prefiring_weight_ECAL_up"]    = events_["prefiring_weight_ECAL_up"][ 0 ]
                    protons_["prefiring_weight_ECAL_down"]  = events_["prefiring_weight_ECAL_down"][ 0 ]
                    protons_["prefiring_weight_Muon"]       = events_["prefiring_weight_Muon"][ 0 ]
                    protons_["prefiring_weight_Muon_up"]    = events_["prefiring_weight_Muon_up"][ 0 ]
                    protons_["prefiring_weight_Muon_down"]  = events_["prefiring_weight_Muon_down"][ 0 ]
                #protons_["x1"] = -999.
                #protons_["y1"] = -999.
                #protons_["x2"] = -999.
                #protons_["y2"] = -999.
                
                #ppstracks_ = events_["pps_track"]
                ppstracks_["run"] = events_["run"]
                ppstracks_["lumiblock"] = events_["lumiblock"]
                ppstracks_["event"] = events_["event"]
                ppstracks_["slice"] = events_["slice"]
                ppstracks_["crossingAngle"] = events_["crossingAngle"]
                ppstracks_["betaStar"] = events_["betaStar"]
                ppstracks_["instLumi"] = events_["instLumi"]
                if runOnMC_:
                    ppstracks_["run_mc"] = events_["run_mc"]

                if random_protons_:
                    ppstracks_["run_rnd"] = run_rnd_
                    ppstracks_["lumiblock_rnd"] = lumiblock_rnd_
                    ppstracks_["event_rnd"] = event_rnd_
                    # ppstracks_["slice_rnd"] = slice_rnd_
                    ppstracks_["crossingAngle_rnd"] = crossingAngle_rnd_
                    ppstracks_["betaStar_rnd"] = betaStar_rnd_

                check_none_ = ak.is_none( protons_ )
                arr_check_none_ = np.array( check_none_ ).astype("int32")
                print( "check_none", np.sum( arr_check_none_ ), check_none_ )
                msk_check_none_ = np.invert( check_none_ )
                print( msk_check_none_ )
                protons_ = protons_[ msk_check_none_ ]
                ppstracks_ = ppstracks_[ msk_check_none_ ]
                protons_extra_ = protons_extra_[ msk_check_none_ ]

                counts_protons_check_none_ = len( protons_ )
                counts_label__ = counts_label_protons_ + "_check_none"
                if not counts_label__ in selections:
                    selections = np.concatenate( ( selections, np.array( [ counts_label__ ] ) ) )
                    counts = np.concatenate( ( counts, np.array( [ counts_protons_check_none_ ] ) ) )
                else:    
                    counts[ selections == counts_label__ ] += counts_protons_check_none_

                protons_singleRP_ = protons_[ protons_.ismultirp_ == 0 ]
                protons_multiRP_ = protons_[ protons_.ismultirp_ == 1 ]
                if protons_extra_ is not None:
                    protons_multiRP_[ "trackx2" ] = protons_extra_[ "trackx2" ]
                    protons_multiRP_[ "tracky2" ] = protons_extra_[ "tracky2" ]
                    protons_multiRP_[ "trackpixshift2" ] = protons_extra_[ "trackpixshift2" ]
                    protons_multiRP_[ "rpid2" ] = protons_extra_[ "rpid2" ]

                protons_singleRP_byRP_ = {}
                ppstracks_byRP_ = {}
                protons_multiRP_byArm_ = {}
                for rpid in ( 3, 23, 103, 123 ):
                    #arm = -1
                    #if   rpid == 3   or rpid == 23 : arm = 0
                    #elif rpid == 103 or rpid == 123 : arm = 1
                    #print ( "Arm: {}".format( arm ) )

                    protons_singleRP_byRP_[ rpid ] =  protons_singleRP_[ protons_singleRP_.rpid == rpid ]
                    ppstracks_byRP_[ rpid ] = ppstracks_[ ppstracks_.rpid == rpid ]
                    #protons_singleRP_byRP_[ rpid ]["x1"] = ppstracks_byRP_[ rpid ].x
                    #protons_singleRP_byRP_[ rpid ]["y1"] = ppstracks_byRP_[ rpid ].y

                    print ( "\nNum protons RP {}: {}".format( rpid, ak.num( protons_singleRP_byRP_[ rpid ] ) ) )
                    if debug:
                        print ( ak.to_list( protons_singleRP_byRP_[ rpid ] ) )
                        print ("\n")
                        print ( ak.to_list( ppstracks_byRP_[ rpid ] ) )

                for arm in ( 0, 1 ):
                    protons_multiRP_byArm_[ arm ] = protons_multiRP_[ protons_multiRP_.arm == arm ]

                    print ( "\nNum multi-RP protons Arm {}: {}".format( arm, ak.num( protons_multiRP_byArm_[ arm ] ) ) )
                    if debug:
                        print ( ak.to_list( protons_multiRP_byArm_[ arm ] ) )

                #msk  =  np.array( ak.num( protons_singleRP_byRP_[ 3 ].xi ) == 1 )
                #msk &= np.array( ak.num( protons_singleRP_byRP_[ 23 ].xi ) == 1 )
                #msk &= np.array( ak.num( protons_singleRP_byRP_[ 103 ].xi ) == 1 )
                #msk &= np.array( ak.num( protons_singleRP_byRP_[ 123 ].xi ) == 1 )    

                # msk_protons  = np.array( ak.num( protons_multiRP_byArm_[ 0 ] ) > 0 )
                # msk_protons &= np.array( ak.num( protons_multiRP_byArm_[ 1 ] ) > 0 )
                msk_protons  = np.array( ak.num( protons_multiRP_byArm_[ 0 ] ) > 0 )
                msk_protons |= np.array( ak.num( protons_multiRP_byArm_[ 1 ] ) > 0 )

                protons_multiRP_sel_ = protons_multiRP_[ msk_protons ]
                protons_singleRP_sel_ = protons_singleRP_[ msk_protons ]
                ppstracks_sel_ = ppstracks_[ msk_protons ]
                print ("\n")
                if debug:
                    print ( msk_protons )
                print ( len( protons_multiRP_sel_ ) )
                print ( ak.num( protons_multiRP_sel_ ) )
                if debug:
                    print ("\n")
                    print ( ak.to_list( protons_multiRP_sel_ ) )
                    print ("\n")
                    print ( ak.to_list( protons_singleRP_sel_ ) )
                    print ("\n")
                    print ( ak.to_list( ppstracks_sel_ ) )

                counts_protons_ = len( protons_[ msk_protons ] )
                if not counts_label_protons_ in selections:
                    selections = np.concatenate( ( selections, np.array( [ counts_label_protons_ ] ) ) )
                    counts = np.concatenate( ( counts, np.array( [counts_protons_] ) ) )
                else:    
                    counts[ selections == counts_label_protons_ ] += counts_protons_ 

                print ( selections )
                print ( counts )

                for col_ in columns_protons_multiRP:
                    protons_multiRP_list[ col_ ] = np.array( ak.flatten( protons_multiRP_sel_[ protons_keys[ col_ ] ] ) )

                arr_size_multiRP_ = len( protons_multiRP_list[ "xi" ] )
                print ( "Flattened array size multi-RP: {}".format( arr_size_multiRP_ ) )

                for col_ in columns_protons:
                    protons_singleRP_list[ col_ ] = np.array( ak.flatten( protons_singleRP_sel_[ protons_keys[ col_ ] ] ) )

                arr_size_singleRP_ = len( protons_singleRP_list[ "xi" ] )
                print ( "Flattened array size single-RP: {}".format( arr_size_singleRP_ ) )

                for col_ in columns_ppstracks:
                    ppstracks_list[ col_ ] = np.array( ak.flatten( ppstracks_sel_[ ppstracks_keys[ col_ ] ] ) )

                arr_size_ppstracks_ = len( ppstracks_list[ "x" ] )
                print ( "Flattened array size tracks: {}".format( arr_size_ppstracks_ ) )

                dset_multiRP_entries += arr_size_multiRP_
                dset_singleRP_entries += arr_size_singleRP_
                dset_ppstracks_entries += arr_size_ppstracks_

                if dset_multiRP_entries > dset_chunk_size:
                    resize_factor_ = ( dset_multiRP_entries // dset_chunk_size )
                    chunk_resize_  = resize_factor_ * dset_chunk_size

                    print ( "Resizing output dataset by {} entries.".format( chunk_resize_ ) )
                    dset_protons_multiRP.resize( ( dset_protons_multiRP.shape[0] + chunk_resize_ ), axis=0 )
                    print ( "Dataset shape: {}".format( dset_protons_multiRP.shape ) )

                    dset_multiRP_slice += resize_factor_
                    # Count the rest to the chunk size 
                    dset_multiRP_entries = ( dset_multiRP_entries % dset_chunk_size )

                if dset_singleRP_entries > dset_chunk_size:
                    resize_factor_ = ( dset_singleRP_entries // dset_chunk_size )
                    chunk_resize_  = resize_factor_ * dset_chunk_size

                    print ( "Resizing output dataset by {} entries.".format( chunk_resize_ ) )
                    dset_protons_singleRP.resize( ( dset_protons_singleRP.shape[0] + chunk_resize_ ), axis=0 )
                    print ( "Dataset shape: {}".format( dset_protons_singleRP.shape ) )

                    dset_singleRP_slice += resize_factor_
                    # Count the rest to the chunk size 
                    dset_singleRP_entries = ( dset_singleRP_entries % dset_chunk_size )

                if dset_ppstracks_entries > dset_chunk_size:
                    resize_factor_ = ( dset_ppstracks_entries // dset_chunk_size )
                    chunk_resize_  = resize_factor_ * dset_chunk_size

                    print ( "Resizing output dataset by {} entries.".format( chunk_resize_ ) )
                    dset_ppstracks.resize( ( dset_ppstracks.shape[0] + chunk_resize_ ), axis=0 )
                    print ( "Dataset shape: {}".format( dset_ppstracks.shape ) )

                    dset_ppstracks_slice += resize_factor_
                    # Count the rest to the chunk size 
                    dset_ppstracks_entries = ( dset_ppstracks_entries % dset_chunk_size )

                print ( "Stacking data." )
                data_protons_multiRP_ = np.stack( list( protons_multiRP_list.values() ), axis=1 )
                print ( data_protons_multiRP_.shape )
                print ( data_protons_multiRP_ )

                data_protons_singleRP_ = np.stack( list( protons_singleRP_list.values() ), axis=1 )
                print ( data_protons_singleRP_.shape )
                print ( data_protons_singleRP_ )

                data_ppstracks_ = np.stack( list( ppstracks_list.values() ), axis=1 )
                print ( data_ppstracks_.shape )
                print ( data_ppstracks_ )

                dset_idx_next_ = dset_multiRP_idx + arr_size_multiRP_
                print ( "Slice: {}".format( dset_multiRP_slice ) )
                print ( "Writing in positions ({},{})".format( dset_multiRP_idx, dset_idx_next_ ) )
                dset_protons_multiRP[ dset_multiRP_idx : dset_idx_next_ ] = data_protons_multiRP_
                dset_multiRP_idx = dset_idx_next_ 

                dset_idx_next_ = dset_singleRP_idx + arr_size_singleRP_
                print ( "Slice: {}".format( dset_singleRP_slice ) )
                print ( "Writing in positions ({},{})".format( dset_singleRP_idx, dset_idx_next_ ) )
                dset_protons_singleRP[ dset_singleRP_idx : dset_idx_next_ ] = data_protons_singleRP_
                dset_singleRP_idx = dset_idx_next_ 

                dset_idx_next_ = dset_ppstracks_idx + arr_size_ppstracks_
                print ( "Slice: {}".format( dset_ppstracks_slice ) )
                print ( "Writing in positions ({},{})".format( dset_ppstracks_idx, dset_idx_next_ ) )
                dset_ppstracks[ dset_ppstracks_idx : dset_idx_next_ ] = data_ppstracks_
                dset_ppstracks_idx = dset_idx_next_ 

            # Iteration on input files
            root_.close()

        # Reduce dataset to its final size 
        print ( "Reduce dataset." )
        dset_protons_multiRP.resize( ( dset_multiRP_idx ), axis=0 ) 
        print ( "Dataset shape: {}".format( dset_protons_multiRP.shape ) )

        dset_protons_singleRP.resize( ( dset_singleRP_idx ), axis=0 ) 
        print ( "Dataset shape: {}".format( dset_protons_singleRP.shape ) )

        dset_ppstracks.resize( ( dset_ppstracks_idx ), axis=0 ) 
        print ( "Dataset shape: {}".format( dset_ppstracks.shape ) )

        print ( "Writing column names and event counts.")

        columns_protons_multiRP_ = np.array( columns_protons_multiRP, dtype='S' )
        print ( columns_protons_multiRP_ )

        columns_protons_singleRP_ = np.array( columns_protons, dtype='S' )
        print ( columns_protons_singleRP_ )

        columns_ppstracks_ = np.array( columns_ppstracks, dtype='S' )
        print ( columns_ppstracks_ )

        event_counts_ = counts
        print ( event_counts_ )

        selections_ = np.array( selections, dtype='S' )
        print ( selections_ )

        dset_columns_protons_multiRP = f.create_dataset( 'columns_protons_multiRP', data=columns_protons_multiRP_ )
        dset_columns_protons_singleRP = f.create_dataset( 'columns_protons_singleRP', data=columns_protons_singleRP_ )
        dset_columns_ppstracks = f.create_dataset( 'columns_ppstracks', data=columns_ppstracks_ )
        dset_counts = f.create_dataset( 'event_counts', data=event_counts_ )
        dset_selections = f.create_dataset( 'selections', data=selections_ )

        print ( dset_protons_multiRP )
        print ( dset_protons_multiRP[-1] )
        print ( dset_protons_singleRP )
        print ( dset_protons_singleRP[-1] )   
        print ( dset_ppstracks )
        print ( dset_ppstracks[-1] )   

        print ( dset_columns_protons_multiRP )
        print ( list( dset_columns_protons_multiRP ) )
        print ( dset_columns_protons_singleRP )
        print ( list( dset_columns_protons_singleRP ) )
        print ( dset_columns_ppstracks )
        print ( list( dset_columns_ppstracks ) )   
        print ( dset_counts )
        print ( list( dset_counts ) )
        print ( dset_selections )
        print ( list( dset_selections ) )

