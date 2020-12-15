import uproot4
import awkward1 as ak
import numpy as np
import pandas as pd
import numba as nb
import h5py

def create_table( fileNames, label, random_protons=False, resample_factor=-1, read_size="150MB", firstEvent=None, entryStop=None, debug=False ):

    fileNames_ = fileNames
    label_ = label
    random_protons_ = random_protons
    resample_factor_ = resample_factor
    read_size_ = read_size
    firstEvent_ = firstEvent
    entryStop_ = entryStop

    #how_ = None
    how_ = "zip"
    
    print ( "Random protons: {}".format( random_protons_ ) )
    
    resample = False
    if resample_factor_ > 1: resample = True
    print ( "Resample: {} / Resample factor: {}".format( resample,  resample_factor_ ) )

    np.random.seed( 42 )

    dset_chunk_size = 50000

    columns_protons = ( "run", "lumiblock", "event", "slice", "xi", "thx", "thy", "t", "ismultirp", "rpid", "arm",
                        "jet0_pt", "jet0_eta", "jet0_phi", "jet0_energy", "jet0_mass", "jet0_corrmass", "jet0_tau1", "jet0_tau2", "jet0_vertexz",
                        "muon0_pt", "muon0_eta", "muon0_phi", "muon0_energy", "muon0_charge", "muon0_iso", "muon0_dxy", "muon0_dz",
                        "met", "met_x", "met_y", "met_phi",
                        "nVertices",
                        "num_bjets_ak8", "num_bjets_ak4", "num_jets_ak4",
                        "pfcand_nextracks", "pfcand_nextracks_noDRl",
                        "recoMWhad", "recoMWlep", "recoMWW", "recoRapidityWW", "dphiWW", "WLeptonicPt", "WLeptonicPhi" )

    columns_ppstracks = ( "run", "lumiblock", "event", "slice", "x", "y", "rpid" ) 

    protons_keys = {}
    for col_ in columns_protons:
        protons_keys[ col_ ] = col_

    ppstracks_keys = {}
    for col_ in columns_ppstracks:
        ppstracks_keys[ col_ ] = col_

    counts_label_protons_ = "Proton" if not random_protons_ else "ProtonRnd"

    with h5py.File( 'output-' + label_ + '.h5', 'w') as f:

        dset_protons_multiRP = f.create_dataset( 'protons_multiRP', ( dset_chunk_size, len( columns_protons ) ), compression="gzip", chunks=True, maxshape=( None , len( columns_protons ) ) )
        print ( "Initial dataset shape: {}".format( dset_protons_multiRP.shape ) )

        dset_protons_singleRP = f.create_dataset( 'protons_singleRP', ( dset_chunk_size, len( columns_protons ) ), compression="gzip", chunks=True, maxshape=( None , len( columns_protons ) ) )
        print ( "Initial dataset shape: {}".format( dset_protons_singleRP.shape ) )

        dset_ppstracks = f.create_dataset( 'ppstracks', ( dset_chunk_size, len( columns_ppstracks ) ), compression="gzip", chunks=True, maxshape=( None , len( columns_ppstracks ) ) )
        print ( "Initial dataset shape: {}".format( dset_ppstracks.shape ) )

        protons_multiRP_list = {}
        for col_ in columns_protons:
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
            keys_nonproton.extend( tree_.keys( filter_name="jet*") )
            keys_nonproton.extend( tree_.keys( filter_name="muon*") )
            keys_nonproton.extend( tree_.keys( filter_name="met*") )
            keys = []
            keys.extend( keys_nonproton )
            keys.extend( tree_.keys( filter_name="proton*") )
            keys.extend( tree_.keys( filter_name="pps*") )
            keys_remove = [ 'proton_trackx2', 'proton_tracky2', 'proton_trackpixshift2', 'proton_rpid2' ]
            for key_ in keys_remove:
                if key_ in keys: keys.remove( key_ )
            print ( keys )

            for events_ in tree_.iterate( keys , library="ak", how=how_, step_size=read_size_, entry_start=firstEvent_, entry_stop=entryStop_ ):
                print ( len(events_), events_ )
                print ( "Num jets: {}".format( ak.num( events_["jet"] ) ) )
                print ( "Num muons: {}".format( ak.num( events_["muon"] ) ) )
                print ( "Num protons: {}".format( ak.num( events_["proton"] ) ) )
                print ( "Num pps tracks: {}".format( ak.num( events_["pps_track"] ) ) )

                selections_ = []
                counts_ = []

                selections_.append( "All" )
                counts_.append( len( events_ ) )

                # Event selections
                msk_1jet = ( ak.num( events_["jet"] ) >= 1 )
                selections_.append( "Jet" )
                counts_.append( np.sum( np.array( msk_1jet ).astype("int32") ) )

                msk_1muon = msk_1jet & ( ak.num( events_["muon"] ) >= 1 )
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

                # Randomize proton arrays
                #protons_ = events_["proton"]
                protons_ = None
                ppstracks_ = None
                if random_protons_:
                    protons_ = events_["proton"]
                    ppstracks_ = events_["pps_track"]

                    index_rnd_ = np.random.permutation( len( events_ ) )

                    protons_rnd_ = protons_[ index_rnd_ ]
                    ppstracks_rnd_ = ppstracks_[ index_rnd_ ]

                    events_[ "proton_rnd" ] = protons_rnd_
                    events_[ "pps_track_rnd" ] = ppstracks_rnd_

                    print ( "Num protons: {}".format( ak.num( events_["proton"] ) ) )
                    print ( "Num protons randomized: {}".format( ak.num( events_["proton_rnd"] ) ) )
                    print ( "Num pps tracks: {}".format( ak.num( events_["pps_track"] ) ) )
                    print ( "Num pps tracks randomized: {}".format( ak.num( events_["pps_track_rnd"] ) ) )

                if not random_protons_:
                    protons_ = events_["proton"]
                    ppstracks_ = events_["pps_track"]
                else:
                    protons_ = events_["proton_rnd"]
                    ppstracks_ = events_["pps_track_rnd"]
                    
                print ( "Num protons: {}".format( ak.num( protons_ ) ) )
                print ( "Num pps tracks: {}".format( ak.num( ppstracks_ ) ) )

                protons_["run"]                    = events_["run"]
                protons_["lumiblock"]              = events_["lumiblock"]
                protons_["event"]                  = events_["event"]
                protons_["slice"]                  = events_["slice"]
                protons_["jet0_pt"]                = events_.jet.pt[:,0]
                protons_["jet0_eta"]               = events_.jet.eta[:,0]
                protons_["jet0_phi"]               = events_.jet.phi[:,0]
                protons_["jet0_energy"]            = events_.jet.energy[:,0]
                protons_["jet0_mass"]              = events_.jet.mass[:,0]
                protons_["jet0_corrmass"]          = events_.jet.corrmass[:,0]
                protons_["jet0_tau1"]              = events_.jet.tau1[:,0]
                protons_["jet0_tau2"]              = events_.jet.tau2[:,0]
                protons_["jet0_vertexz"]           = events_.jet.vertexz[:,0]
                protons_["muon0_pt"]               = events_.muon.pt[:,0]
                protons_["muon0_eta"]              = events_.muon.eta[:,0]
                protons_["muon0_phi"]              = events_.muon.phi[:,0]
                protons_["muon0_energy"]           = events_.muon.e[:,0]
                protons_["muon0_charge"]           = events_.muon.charge[:,0]
                protons_["muon0_iso"]              = events_.muon.iso[:,0]
                protons_["muon0_dxy"]              = events_.muon.dxy[:,0]
                protons_["muon0_dz"]               = events_.muon.dz[:,0]
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

                protons_singleRP_ = protons_[ protons_.ismultirp == 0 ]
                protons_multiRP_ = protons_[ protons_.ismultirp == 1 ]

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

                for col_ in columns_protons:
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

        columns_protons_ = np.array( columns_protons, dtype='S' )
        print ( columns_protons_ )

        columns_ppstracks_ = np.array( columns_ppstracks, dtype='S' )
        print ( columns_ppstracks_ )

        event_counts_ = counts
        print ( event_counts_ )

        selections_ = np.array( selections, dtype='S' )
        print ( selections_ )

        dset_columns_protons = f.create_dataset( 'columns_protons', data=columns_protons_ )
        dset_columns_ppstracks = f.create_dataset( 'columns_ppstracks', data=columns_ppstracks_ )
        dset_counts = f.create_dataset( 'event_counts', data=event_counts_ )
        dset_selections = f.create_dataset( 'selections', data=selections_ )

        print ( dset_protons_multiRP )
        print ( dset_protons_multiRP[-1] )
        print ( dset_protons_singleRP )
        print ( dset_protons_singleRP[-1] )   
        print ( dset_ppstracks )
        print ( dset_ppstracks[-1] )   

        print ( dset_columns_protons )
        print ( list( dset_columns_protons ) )
        print ( dset_columns_ppstracks )
        print ( list( dset_columns_ppstracks ) )   
        print ( dset_counts )
        print ( list( dset_counts ) )
        print ( dset_selections )
        print ( list( dset_selections ) )

