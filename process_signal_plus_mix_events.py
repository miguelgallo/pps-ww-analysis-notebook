#!/usr/bin/env python
# coding: utf-8
import numpy as np
import pandas as pd
import h5py

# run_ranges_periods, df_run_ranges, fiducial_cuts, fiducial_cuts_all, aperture_period_map, aperture_parametrisation, check_aperture, get_data, process_data_protons_multiRP
from processing import *

# lepton_type = 'muon'
lepton_type = 'electron'

# data_sample = '2017'
data_sample = '2018'

use_hash_index = True

base_path_ = 'output'
output_dir_ = 'output'

# Signal
labels_signals = []
if data_sample == '2017':
    if lepton_type == 'muon':
        # labels_signals = [ "GGToWW-AQGC-A0W1e-6", "GGToWW-AQGC-A0W2e-6", "GGToWW-AQGC-A0W5e-6" ]
        # labels_signals = [ "GGToWW-AQGC-muon-A0W1e-6", "GGToWW-AQGC-muon-A0W2e-6", "GGToWW-AQGC-muon-A0W5e-6" ]
        # labels_signals = [ "GGToWW-AQGC-muon-A0W1e-6", "GGToWW-AQGC-muon-A0W2e-6", "GGToWW-AQGC-muon-A0W5e-6" ]
        labels_signals = [ "GGToWW-AQGC-2017-muon-A0W1e-6", "GGToWW-AQGC-2017-muon-A0W2e-6", "GGToWW-AQGC-2017-muon-A0W5e-6" ]
    elif lepton_type == 'electron':
        # labels_signals = [ "GGToWW-AQGC-electron-A0W1e-6", "GGToWW-AQGC-electron-A0W2e-6", "GGToWW-AQGC-electron-A0W5e-6" ]
        labels_signals = [ "GGToWW-AQGC-2017-electron-A0W1e-6", "GGToWW-AQGC-2017-electron-A0W2e-6", "GGToWW-AQGC-2017-electron-A0W5e-6" ]
elif data_sample == '2018':
    if lepton_type == 'muon':
        labels_signals = [ "GGToWW-AQGC-2018-muon-A0W5e-7", "GGToWW-AQGC-2018-muon-A0W1e-6", "GGToWW-AQGC-2018-muon-A0W2e-6", "GGToWW-AQGC-2018-muon-A0W5e-6" ]
    elif lepton_type == 'electron':
        labels_signals = [ "GGToWW-AQGC-2018-electron-A0W5e-7", "GGToWW-AQGC-2018-electron-A0W1e-6", "GGToWW-AQGC-2018-electron-A0W2e-6", "GGToWW-AQGC-2018-electron-A0W5e-6" ]

df_counts_signals = {}
df_signals_protons_multiRP_index = {}
df_signals_protons_multiRP_events = {}
for label_ in labels_signals:
    print ( label_ )
    file_path_ = "{}/data-store-{}.h5".format( base_path_, label_ )
    print ( file_path_ )
    with pd.HDFStore( file_path_, 'r' ) as store_:
        print ( list( store_ ) )
        df_counts_signals[ label_ ] = store_[ "counts" ]
        df_signals_protons_multiRP_index[ label_ ] = store_[ "protons_multiRP" ]
        df_signals_protons_multiRP_events[ label_ ] = store_[ "events_multiRP" ]

labels_signals_mix_protons = []
if data_sample == '2017':
    if lepton_type == 'muon':
        # labels_signals_mix_protons = [ "GGToWW-AQGC-mix_protons-A0W1e-6", "GGToWW-AQGC-mix_protons-A0W2e-6", "GGToWW-AQGC-mix_protons-A0W5e-6" ]
        # labels_signals_mix_protons = [ "GGToWW-AQGC-mix_protons-muon-A0W1e-6", "GGToWW-AQGC-mix_protons-muon-A0W2e-6", "GGToWW-AQGC-mix_protons-muon-A0W5e-6" ]
        labels_signals_mix_protons = [ "GGToWW-AQGC-mix_protons-2017-muon-A0W1e-6", "GGToWW-AQGC-mix_protons-2017-muon-A0W2e-6", "GGToWW-AQGC-mix_protons-2017-muon-A0W5e-6" ]
    elif lepton_type == 'electron':
        # labels_signals_mix_protons = [ "GGToWW-AQGC-mix_protons-electron-A0W1e-6", "GGToWW-AQGC-mix_protons-electron-A0W2e-6", "GGToWW-AQGC-mix_protons-electron-A0W5e-6" ]
        labels_signals_mix_protons = [ "GGToWW-AQGC-mix_protons-2017-electron-A0W1e-6", "GGToWW-AQGC-mix_protons-2017-electron-A0W2e-6", "GGToWW-AQGC-mix_protons-2017-electron-A0W5e-6" ]
elif data_sample == '2018':
    if lepton_type == 'muon':
        labels_signals_mix_protons = [ "GGToWW-AQGC-mix_protons-2018-muon-A0W5e-7", "GGToWW-AQGC-mix_protons-2018-muon-A0W1e-6", "GGToWW-AQGC-mix_protons-2018-muon-A0W2e-6", "GGToWW-AQGC-mix_protons-2018-muon-A0W5e-6" ]
    elif lepton_type == 'electron':
        labels_signals_mix_protons = [ "GGToWW-AQGC-mix_protons-2018-electron-A0W5e-7", "GGToWW-AQGC-mix_protons-2018-electron-A0W1e-6", "GGToWW-AQGC-mix_protons-2018-electron-A0W2e-6", "GGToWW-AQGC-mix_protons-2018-electron-A0W5e-6" ]

df_counts_signals_mix_protons = {}
df_signals_protons_multiRP_mix_protons_index = {}
df_signals_protons_multiRP_mix_protons_events = {}
for label_ in labels_signals_mix_protons:
    print ( label_ )
    file_path_ = "{}/data-store-{}.h5".format( base_path_, label_ )
    print ( file_path_ )
    with pd.HDFStore( file_path_, 'r' ) as store_:
        print ( list( store_ ) )
        df_counts_signals_mix_protons[ label_ ] = store_[ "counts" ]
        df_signals_protons_multiRP_mix_protons_index[ label_ ] = store_[ "protons_multiRP" ]
        df_signals_protons_multiRP_mix_protons_events[ label_ ] = store_[ "events_multiRP" ]

label_signal_to_mix_protons = {}
if data_sample == '2017':
    if lepton_type == 'muon':
        label_signal_to_mix_protons = {
             # "GGToWW-AQGC-A0W1e-6" : "GGToWW-AQGC-mix_protons-A0W1e-6",
             # "GGToWW-AQGC-A0W2e-6" : "GGToWW-AQGC-mix_protons-A0W2e-6",
             # "GGToWW-AQGC-A0W5e-6" : "GGToWW-AQGC-mix_protons-A0W5e-6"
             # "GGToWW-AQGC-muon-A0W1e-6" : "GGToWW-AQGC-mix_protons-muon-A0W1e-6",
             # "GGToWW-AQGC-muon-A0W2e-6" : "GGToWW-AQGC-mix_protons-muon-A0W2e-6",
             # "GGToWW-AQGC-muon-A0W5e-6" : "GGToWW-AQGC-mix_protons-muon-A0W5e-6"
             "GGToWW-AQGC-2017-muon-A0W1e-6" : "GGToWW-AQGC-mix_protons-2017-muon-A0W1e-6",
             "GGToWW-AQGC-2017-muon-A0W2e-6" : "GGToWW-AQGC-mix_protons-2017-muon-A0W2e-6",
             "GGToWW-AQGC-2017-muon-A0W5e-6" : "GGToWW-AQGC-mix_protons-2017-muon-A0W5e-6"
        }
    elif lepton_type == 'electron':
        label_signal_to_mix_protons = {
             # "GGToWW-AQGC-electron-A0W1e-6" : "GGToWW-AQGC-mix_protons-electron-A0W1e-6",
             # "GGToWW-AQGC-electron-A0W2e-6" : "GGToWW-AQGC-mix_protons-electron-A0W2e-6",
             # "GGToWW-AQGC-electron-A0W5e-6" : "GGToWW-AQGC-mix_protons-electron-A0W5e-6"
             "GGToWW-AQGC-2017-electron-A0W1e-6" : "GGToWW-AQGC-mix_protons-2017-electron-A0W1e-6",
             "GGToWW-AQGC-2017-electron-A0W2e-6" : "GGToWW-AQGC-mix_protons-2017-electron-A0W2e-6",
             "GGToWW-AQGC-2017-electron-A0W5e-6" : "GGToWW-AQGC-mix_protons-2017-electron-A0W5e-6"
        }
elif data_sample == '2018':
    if lepton_type == 'muon':
        label_signal_to_mix_protons = {
             "GGToWW-AQGC-2018-muon-A0W5e-7" : "GGToWW-AQGC-mix_protons-2018-muon-A0W5e-7",
             "GGToWW-AQGC-2018-muon-A0W1e-6" : "GGToWW-AQGC-mix_protons-2018-muon-A0W1e-6",
             "GGToWW-AQGC-2018-muon-A0W2e-6" : "GGToWW-AQGC-mix_protons-2018-muon-A0W2e-6",
             "GGToWW-AQGC-2018-muon-A0W5e-6" : "GGToWW-AQGC-mix_protons-2018-muon-A0W5e-6"
        }
    elif lepton_type == 'electron':
        label_signal_to_mix_protons = {
             "GGToWW-AQGC-2018-electron-A0W5e-7" : "GGToWW-AQGC-mix_protons-2018-electron-A0W5e-7",
             "GGToWW-AQGC-2018-electron-A0W1e-6" : "GGToWW-AQGC-mix_protons-2018-electron-A0W1e-6",
             "GGToWW-AQGC-2018-electron-A0W2e-6" : "GGToWW-AQGC-mix_protons-2018-electron-A0W2e-6",
             "GGToWW-AQGC-2018-electron-A0W5e-6" : "GGToWW-AQGC-mix_protons-2018-electron-A0W5e-6"
        }

# Signal with event mixing

df_signals_protons_multiRP_eff_sel_index = {}
df_signals_protons_multiRP_sig_plus_mix_index = {}

np.random.seed( 12345 )

index_vars_ = None
if not use_hash_index:
    index_vars_ = ['run', 'lumiblock', 'event', 'slice']
else:
    index_vars_ = ['run', 'lumiblock', 'event', 'hash_id', 'slice']
print ( index_vars_ )

for label_ in labels_signals:
    print ( label_ )
    df_signals_protons_multiRP_mix_protons_index[ label_signal_to_mix_protons[ label_ ] ].loc[ :, "eff_proton_all" ] = 1.0
    df_signals_protons_multiRP_mix_protons_index[ label_signal_to_mix_protons[ label_ ] ].loc[ :, "eff_proton_all_weighted" ] = 1.0
    df_signals_protons_multiRP_mix_protons_index[ label_signal_to_mix_protons[ label_ ] ].loc[ :, "eff_proton_unc" ] = 0.0
    if data_sample == '2017':
        df_signals_protons_multiRP_mix_protons_index[ label_signal_to_mix_protons[ label_ ] ].loc[ :, "eff_multitrack" ] = 1.0
        df_signals_protons_multiRP_mix_protons_index[ label_signal_to_mix_protons[ label_ ] ].loc[ :, "eff_strictzero" ] = 1.0
        df_signals_protons_multiRP_mix_protons_index[ label_signal_to_mix_protons[ label_ ] ].loc[ :, "eff_multitrack_weighted" ] = 1.0
        df_signals_protons_multiRP_mix_protons_index[ label_signal_to_mix_protons[ label_ ] ].loc[ :, "eff_strictzero_weighted" ] = 1.0

    # Random selection by efficiency weights
    msk_eff_proton_ = np.random.rand( df_signals_protons_multiRP_index[ label_ ].shape[0] ) < df_signals_protons_multiRP_index[ label_ ].loc[ :, "eff_proton_all" ]
    print ( msk_eff_proton_ )
    df_signals_protons_multiRP_eff_sel_index[ label_ ] = df_signals_protons_multiRP_index[ label_ ].loc[ msk_eff_proton_ ]

    df_signals_protons_multiRP_sig_plus_mix_index[ label_ ] = pd.concat(
        [ df_signals_protons_multiRP_eff_sel_index[ label_ ],
          df_signals_protons_multiRP_mix_protons_index[ label_signal_to_mix_protons[ label_ ] ] ] ).sort_index()

df_signals_protons_multiRP_sig_plus_mix_2protons = {}
for label_ in labels_signals:
    print ( label_ )
    if data_sample == '2017':
        # df_protons_multiRP_groupby_arm_ = df_signals_protons_multiRP_sig_plus_mix_index[ label_ ][ [ "arm" ] ].groupby( ["run","lumiblock","event","slice"] )
        df_protons_multiRP_groupby_arm_ = df_signals_protons_multiRP_sig_plus_mix_index[ label_ ][ [ "arm" ] ].groupby( index_vars_ )
        msk_2protons_single_proton_ = df_protons_multiRP_groupby_arm_[ "arm" ].transform( lambda s_: ( np.sum( s_ == 0 ) == 1 ) & ( np.sum( s_ == 1 ) == 1 ) )
        print ( msk_2protons_single_proton_, np.sum( msk_2protons_single_proton_ ) )
        df_signals_protons_multiRP_sig_plus_mix_2protons[ label_ ] = df_signals_protons_multiRP_sig_plus_mix_index[ label_ ].loc[ msk_2protons_single_proton_ ]
    elif data_sample == '2018':
        # df_protons_multiRP_groupby_arm_ = df_signals_protons_multiRP_sig_plus_mix_index[ label_ ][ [ "arm" ] ].groupby( ["run","lumiblock","event","slice"] )
        df_protons_multiRP_groupby_arm_ = df_signals_protons_multiRP_sig_plus_mix_index[ label_ ][ [ "arm" ] ].groupby( index_vars_ )
        msk_2protons_ = df_protons_multiRP_groupby_arm_[ "arm" ].transform( lambda s_: ( np.sum( s_ == 0 ) >= 1 ) & ( np.sum( s_ == 1 ) >= 1 ) )
        print ( msk_2protons_, np.sum( msk_2protons_ ) )
        df_signals_protons_multiRP_sig_plus_mix_2protons[ label_ ] = df_signals_protons_multiRP_sig_plus_mix_index[ label_ ].loc[ msk_2protons_ ]

# Divide in categories
df_signals_protons_multiRP_sig_plus_mix_2protons_sig = {}
df_signals_protons_multiRP_sig_plus_mix_1proton_sig_Arm0 = {}
df_signals_protons_multiRP_sig_plus_mix_1proton_sig_Arm1 = {}
df_signals_protons_multiRP_sig_plus_mix_2protons_mix = {}
for label_ in labels_signals:
    print ( label_ )
    
    df__ = df_signals_protons_multiRP_sig_plus_mix_2protons[ label_ ]
    # df_protons_multiRP_groupby__ = df__[ [ "arm", "random" ] ].groupby( ["run","lumiblock","event","slice"] )
    df_protons_multiRP_groupby__ = df__[ [ "arm", "random" ] ].groupby( index_vars_ )
    msk_sig_Arm0_ = df_protons_multiRP_groupby__.apply( lambda __df: np.sum( ( __df[ 'arm' ] == 0 ) & ( __df[ 'random' ] == 0 ) ) == 1 )
    msk_sig_Arm1_ = df_protons_multiRP_groupby__.apply( lambda __df: np.sum( ( __df[ 'arm' ] == 1 ) & ( __df[ 'random' ] == 0 ) ) == 1 )
    msk_2protons_ = ( msk_sig_Arm0_ & msk_sig_Arm1_ )
    msk_1proton_sig_Arm0_ = ( msk_sig_Arm0_ & ~msk_sig_Arm1_ )
    msk_1proton_sig_Arm1_ = ( ~msk_sig_Arm0_ & msk_sig_Arm1_ )
    msk_2protons_mix_ = ( ~msk_sig_Arm0_ & ~msk_sig_Arm1_ )
    print ( msk_2protons_, np.sum( msk_2protons_ ) )
    print ( msk_1proton_sig_Arm0_, np.sum( msk_1proton_sig_Arm0_ ) )
    print ( msk_1proton_sig_Arm1_, np.sum( msk_1proton_sig_Arm1_ ) )
    print ( msk_2protons_mix_, np.sum( msk_2protons_mix_ ) )
    
    df_signals_protons_multiRP_sig_plus_mix_2protons_sig[ label_ ] = df__.loc[ msk_2protons_ ]
    df_signals_protons_multiRP_sig_plus_mix_1proton_sig_Arm0[ label_ ] = df__.loc[ msk_1proton_sig_Arm0_ ]
    df_signals_protons_multiRP_sig_plus_mix_1proton_sig_Arm1[ label_ ] = df__.loc[ msk_1proton_sig_Arm1_ ]
    df_signals_protons_multiRP_sig_plus_mix_2protons_mix[ label_ ] = df__.loc[ msk_2protons_mix_ ]

df_signals_protons_multiRP_sig_plus_mix_2protons_events = {}
df_signals_protons_multiRP_sig_plus_mix_events_categories = {}

for label_ in labels_signals:
    print ( label_ )
    columns_protons_multiRP_ = df_signals_protons_multiRP_index[ label_ ].columns.values
    columns_ = columns_protons_multiRP_
    columns_eff_ = columns_[ [ key_[ : len('eff') ] == 'eff' for key_ in columns_ ] ]
    columns_xi_  = columns_[ [ key_[ : len('xi_') ] == 'xi_' for key_ in columns_ ] ]
    
    columns_drop_ = [ "xi", "thx", "thy", "t", "ismultirp", "rpid", "arm", "random",
                      "trackx1", "tracky1", "trackpixshift1", "rpid1",
                      "trackx2", "tracky2", "trackpixshift2", "rpid2" ]
    columns_drop_eff_xi_ = columns_drop_.copy()
    columns_drop_eff_xi_.extend( columns_eff_ )
    columns_drop_eff_xi_.extend( columns_xi_ )

    # file_path_ = "data-store-signal-plus-mix-events-{}.h5".format( label_ )
    file_path_ = None
    file_name_label_ = "data-store-signal-plus-mix-events-{}.h5".format( label_ )
    if output_dir_ is not None and output_dir_ != "":
        file_path_ = "{}/{}".format( output_dir_, file_name_label_ )
    else:
        file_path_ = file_name_label_
    print ( file_path_ )
    with pd.HDFStore( file_path_, 'w', complevel=5 ) as store_:
        df__ = df_signals_protons_multiRP_sig_plus_mix_2protons[ label_ ]
        df_protons_multiRP_events__, df_protons_multiRP_index_2protons__ = process_events( data_sample, df__, runOnMC=True, mix_protons=False, columns_drop=columns_drop_eff_xi_, use_hash_index=use_hash_index )
        df_signals_protons_multiRP_sig_plus_mix_2protons_events[ label_ ] = df_protons_multiRP_events__

        df_signals_protons_multiRP_sig_plus_mix_events_categories[ label_ ] = {}
        print ( "2protons_sig" )
        df__ = df_signals_protons_multiRP_sig_plus_mix_2protons_sig[ label_ ]
        df_protons_multiRP_events__, df_protons_multiRP_index_2protons__ = process_events( data_sample, df__, runOnMC=True, mix_protons=False, columns_drop=columns_drop_eff_xi_, use_hash_index=use_hash_index )
    #     df_signals_protons_multiRP_sig_plus_mix_2protons_sig_events[ label_ ] = df_protons_multiRP_events__
        df_signals_protons_multiRP_sig_plus_mix_events_categories[ label_ ][ '2protons_sig' ] = df_protons_multiRP_events__
        print ( "1proton_sig_Arm0" )
        df__ = df_signals_protons_multiRP_sig_plus_mix_1proton_sig_Arm0[ label_ ]
        df_protons_multiRP_events__, df_protons_multiRP_index_2protons__ = process_events( data_sample, df__, runOnMC=True, mix_protons=False, columns_drop=columns_drop_eff_xi_, use_hash_index=use_hash_index )
    #     df_signals_protons_multiRP_sig_plus_mix_1proton_sig_Arm0_events[ label_ ] = df_protons_multiRP_events__
        df_signals_protons_multiRP_sig_plus_mix_events_categories[ label_ ][ '1proton_sig_Arm0' ] = df_protons_multiRP_events__
        print ( "1proton_sig_Arm1" )
        df__ = df_signals_protons_multiRP_sig_plus_mix_1proton_sig_Arm1[ label_ ]
        df_protons_multiRP_events__, df_protons_multiRP_index_2protons__ = process_events( data_sample, df__, runOnMC=True, mix_protons=False, columns_drop=columns_drop_eff_xi_, use_hash_index=use_hash_index )
    #     df_signals_protons_multiRP_sig_plus_mix_1proton_sig_Arm1_events[ label_ ] = df_protons_multiRP_events__
        df_signals_protons_multiRP_sig_plus_mix_events_categories[ label_ ][ '1proton_sig_Arm1' ] = df_protons_multiRP_events__
        print ( "2protons_mix" )
        df__ = df_signals_protons_multiRP_sig_plus_mix_2protons_mix[ label_ ]
        df_protons_multiRP_events__, df_protons_multiRP_index_2protons__ = process_events( data_sample, df__, runOnMC=True, mix_protons=False, columns_drop=columns_drop_eff_xi_, use_hash_index=use_hash_index )
    #     df_signals_protons_multiRP_sig_plus_mix_2protons_mix_events[ label_ ] = df_protons_multiRP_events__
        df_signals_protons_multiRP_sig_plus_mix_events_categories[ label_ ][ '2protons_mix' ] = df_protons_multiRP_events__
        
        store_[ "events_multiRP/all" ] = df_signals_protons_multiRP_sig_plus_mix_2protons_events[ label_ ]
        for key_ in df_signals_protons_multiRP_sig_plus_mix_events_categories[ label_ ]:
            store_[ "events_multiRP/{}".format( key_ ) ] = df_signals_protons_multiRP_sig_plus_mix_events_categories[ label_ ][ key_ ]
        print ( list( store_ ) )

