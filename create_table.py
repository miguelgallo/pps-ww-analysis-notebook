import uproot4
import awkward1 as ak
import numpy as np
import pandas as pd
import numba as nb
import h5py

def create_table( fileNames, label, random_protons=False, resample_factor=-1, step_size=100000, firstEvent=None, entryStop=None, debug=False ):

    fileNames_ = fileNames
    label_ = label
    random_protons_ = random_protons
    resample_factor_ = resample_factor
    step_size_ = step_size
    firstEvent_ = firstEvent
    entryStop_ = entryStop

    fill_proton_extra_ = True

    how_ = None
    #how_ = "zip"
    
    print ( "Random protons: {}".format( random_protons_ ) )
    
    resample = False
    if resample_factor_ > 1: resample = True
    print ( "Resample: {} / Resample factor: {}".format( resample,  resample_factor_ ) )

    np.random.seed( 42 )

    dset_chunk_size = 50000

    columns_protons = [ "run", "lumiblock", "event", "slice", "xi", "thx", "thy", "t", "ismultirp", "rpid", "arm",
                        "jet0_pt", "jet0_eta", "jet0_phi", "jet0_energy", "jet0_mass", "jet0_corrmass", "jet0_tau1", "jet0_tau2", "jet0_vertexz",
                        "muon0_pt", "muon0_eta", "muon0_phi", "muon0_energy", "muon0_charge", "muon0_iso", "muon0_dxy", "muon0_dz",
                        "met", "met_x", "met_y", "met_phi",
                        "nVertices",
                        "num_bjets_ak8", "num_bjets_ak4", "num_jets_ak4",
                        "pfcand_nextracks", "pfcand_nextracks_noDRl",
                        "recoMWhad", "recoMWlep", "recoMWW", "recoRapidityWW", "dphiWW", "WLeptonicPt", "WLeptonicPhi" ]

    columns_protons_multiRP = columns_protons.copy()

    if fill_proton_extra_:
        columns_protons.extend( [ "trackx1", "tracky1", "trackpixshift1", "rpid1" ] )
        columns_protons_multiRP.extend( [ "trackx1", "tracky1", "trackpixshift1", "rpid1", "trackx2", "tracky2", "trackpixshift2", "rpid2" ] )
   
    columns_ppstracks = [ "run", "lumiblock", "event", "slice", "x", "y", "rpid" ] 

    protons_keys = {}
    for col_ in columns_protons_multiRP:
        protons_keys[ col_ ] = col_
    protons_keys[ "ismultirp" ] = "ismultirp_"

    ppstracks_keys = {}
    for col_ in columns_ppstracks:
        ppstracks_keys[ col_ ] = col_

    counts_label_protons_ = "Proton" if not random_protons_ else "ProtonRnd"

    with h5py.File( 'output-' + label_ + '.h5', 'w') as f:

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
            root_ = uproot4.open( file_ )

            print ( "Number of events in tree: {}".format( np.array( root_["demo/SlimmedNtuple/event"] ).size ) )

            tree_ = root_["demo/SlimmedNtuple"]

            keys_nonproton = [ "run", "event", "lumiblock", "nVertices",
                               "num_bjets_ak8", "num_bjets_ak4", "num_jets_ak4",
                               "pfcand_nextracks", "pfcand_nextracks_noDRl",
                               "recoMWhad", "recoMWlep", "recoMWW", "recoRapidityWW", "dphiWW", "WLeptonicPt", "WLeptonicPhi" ]
            keys_jet = tree_.keys( filter_name="jet*")
            keys_nonproton.extend( keys_jet )
            keys_muon = tree_.keys( filter_name="muon*")
            keys_nonproton.extend( keys_muon )
            keys_met = tree_.keys( filter_name="met*")
            keys_nonproton.extend( keys_met )
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
                print ( "Num muons: {}".format( ak.num( events_["muon_pt"] ) ) )
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

                msk_1muon = msk_1jet & ( ak.num( events_["muon_pt"] ) >= 1 )
                selections_.append( "Muon" )
                counts_.append( np.sum( np.array( msk_1muon ).astype("int32") ) )

                events_ = events_[ msk_1muon ]    

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
                    protons_ = ak.zip( arrays_proton )

                    if fill_proton_extra_:
                        arrays_proton_extra = {}
                        for key_ in keys_proton_extra: arrays_proton_extra[ key_[ len("proton_") : ] ] = events_[ key_ ]
                        protons_extra_ = ak.zip( arrays_proton_extra )

                    arrays_ppstrack = {}
                    for key_ in keys_ppstrack: arrays_ppstrack[ key_[ len("pps_track_") : ] ] = events_[ key_ ]
                    ppstracks_ = ak.zip( arrays_ppstrack )

                # Randomize proton arrays
                if random_protons_:
                    index_rnd_ = np.random.permutation( len( events_ ) )

                    protons_rnd_ = protons_[ index_rnd_ ]
                    ppstracks_rnd_ = ppstracks_[ index_rnd_ ]
                    protons_extra_rnd_ = None
                    if protons_extra_:
                        protons_extra_rnd_ = protons_extra_[ index_rnd_ ]

                    print ( "Num protons: {}".format( ak.num( protons_ ) ) )
                    print ( "Num protons randomized: {}".format( ak.num( protons_rnd_ ) ) )
                    print ( "Num pps tracks: {}".format( ak.num( ppstracks_ ) ) )
                    print ( "Num pps tracks randomized: {}".format( ak.num( ppstracks_rnd_ ) ) )
                    if protons_extra_rnd_:
                        print ( "Num protons extra: {}".format( ak.num( protons_extra_ ) ) )
                        print ( "Num protons extra randomized: {}".format( ak.num( protons_extra_rnd_ ) ) )

                    protons_ = protons_rnd_
                    protons_extra_ = protons_extra_rnd_
                    ppstracks_ = ppstracks_rnd_
                    
                print ( "Num protons: {}".format( ak.num( protons_ ) ) )
                print ( "Num pps tracks: {}".format( ak.num( ppstracks_ ) ) )
                if protons_extra_:
                    print ( "Num protons extra: {}".format( ak.num( protons_extra_ ) ) )

                protons_["run"]                    = events_["run"]
                protons_["lumiblock"]              = events_["lumiblock"]
                protons_["event"]                  = events_["event"]
                protons_["slice"]                  = events_["slice"]
                protons_["jet0_pt"]                = events_[ "jet_pt" ][:,0]
                protons_["jet0_eta"]               = events_[ "jet_eta" ][:,0]
                protons_["jet0_phi"]               = events_[ "jet_phi" ][:,0]
                protons_["jet0_energy"]            = events_[ "jet_energy" ][:,0]
                protons_["jet0_mass"]              = events_[ "jet_mass" ][:,0]
                protons_["jet0_corrmass"]          = events_[ "jet_corrmass" ][:,0]
                protons_["jet0_tau1"]              = events_[ "jet_tau1" ][:,0]
                protons_["jet0_tau2"]              = events_[ "jet_tau2" ][:,0]
                protons_["jet0_vertexz"]           = events_[ "jet_vertexz" ][:,0]
                protons_["muon0_pt"]               = events_[ "muon_pt" ][:,0]
                protons_["muon0_eta"]              = events_[ "muon_eta" ][:,0]
                protons_["muon0_phi"]              = events_[ "muon_phi" ][:,0]
                protons_["muon0_energy"]           = events_[ "muon_e" ][:,0]
                protons_["muon0_charge"]           = events_[ "muon_charge" ][:,0]
                protons_["muon0_iso"]              = events_[ "muon_iso" ][:,0]
                protons_["muon0_dxy"]              = events_[ "muon_dxy" ][:,0]
                protons_["muon0_dz"]               = events_[ "muon_dz" ][:,0]
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
                protons_["WLeptonicPhi"]           = events_["WLeptonicPhi"]
                #protons_["x1"] = -999.
                #protons_["y1"] = -999.
                #protons_["x2"] = -999.
                #protons_["y2"] = -999.
                
                #ppstracks_ = events_["pps_track"]
                ppstracks_["run"] = events_["run"]
                ppstracks_["lumiblock"] = events_["lumiblock"]
                ppstracks_["event"] = events_["event"]
                ppstracks_["slice"] = events_["slice"]

                protons_singleRP_ = protons_[ protons_.ismultirp_ == 0 ]
                protons_multiRP_ = protons_[ protons_.ismultirp_ == 1 ]
                if protons_extra_:
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

                msk_protons  = np.array( ak.num( protons_multiRP_byArm_[ 0 ] ) > 0 )
                msk_protons &= np.array( ak.num( protons_multiRP_byArm_[ 1 ] ) > 0 )

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

