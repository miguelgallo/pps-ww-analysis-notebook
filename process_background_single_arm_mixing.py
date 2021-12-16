#!/usr/bin/env python
# coding: utf-8
import numpy as np
import pandas as pd
import h5py

# run_ranges_periods, df_run_ranges, fiducial_cuts, fiducial_cuts_all, aperture_period_map, aperture_parametrisation, check_aperture, get_data, process_data_protons_multiRP
from processing import *

lepton_type = 'muon'
# lepton_type = 'electron'

# resample_factor = 20
resample_factor = 50

labels_background = []
fileNames_bkg = {}
if lepton_type == 'muon':
    labels_background = [
        "data-random-resample_50-single-arm-muon-2017B",
        "data-random-resample_50-single-arm-muon-2017C",
        "data-random-resample_50-single-arm-muon-2017D",
        "data-random-resample_50-single-arm-muon-2017E",
        "data-random-resample_50-single-arm-muon-2017F"
    ]
    fileNames_bkg = {
        "data-random-resample_50-single-arm-muon-2017B": "data-store-data-random-resample_50-single-arm-2017B.h5",
        "data-random-resample_50-single-arm-muon-2017C": "data-store-data-random-resample_50-single-arm-2017C.h5",
        "data-random-resample_50-single-arm-muon-2017D": "data-store-data-random-resample_50-single-arm-2017D.h5",
        "data-random-resample_50-single-arm-muon-2017E": "data-store-data-random-resample_50-single-arm-2017E.h5",
        "data-random-resample_50-single-arm-muon-2017F": "data-store-data-random-resample_50-single-arm-2017F.h5"
    }
elif lepton_type == 'electron':
    labels_background = [
        "data-random-resample_50-single-arm-electron-2017B",
        "data-random-resample_50-single-arm-electron-2017C",
        "data-random-resample_50-single-arm-electron-2017D",
        "data-random-resample_50-single-arm-electron-2017E",
        "data-random-resample_50-single-arm-electron-2017F"
    ]
    fileNames_bkg = {
        "data-random-resample_50-single-arm-electron-2017B": "data-store-data-random-resample_50-single-arm-electron-2017B.h5",
        "data-random-resample_50-single-arm-electron-2017C": "data-store-data-random-resample_50-single-arm-electron-2017C.h5",
        "data-random-resample_50-single-arm-electron-2017D": "data-store-data-random-resample_50-single-arm-electron-2017D.h5",
        "data-random-resample_50-single-arm-electron-2017E": "data-store-data-random-resample_50-single-arm-electron-2017E.h5",
        "data-random-resample_50-single-arm-electron-2017F": "data-store-data-random-resample_50-single-arm-electron-2017F.h5"
    }

base_path_ = "output"

for label_ in fileNames_bkg:
    fileNames_bkg[ label_ ] = "{}/{}".format( base_path_, fileNames_bkg[ label_ ] )

print ( fileNames_bkg )

# Data

label_data = ""
if lepton_type == 'muon':
    label_data = "data-single-arm"
elif lepton_type == 'electron':
    label_data = "data-single-arm-electron"

base_path_ = "output"
file_path_ = "{}/data-store-{}.h5".format( base_path_, label_data )
print ( file_path_ )

df_counts_data = None
df_protons_multiRP_data_index = None
# df_protons_multiRP_data_events = None
with pd.HDFStore( file_path_, 'r' ) as store_:
    print ( list( store_ ) )
    df_counts_data = store_[ "counts" ]
    df_protons_multiRP_data_index = store_[ "protons_multiRP" ]
#     df_protons_multiRP_data_events = store_[ "events_multiRP" ]

df_protons_multiRP_data_newindex = df_protons_multiRP_data_index.reset_index().set_index( [ 'run', 'lumiblock', 'event' ] )

df_protons_multiRP_data_arm0 = df_protons_multiRP_data_newindex.loc[ df_protons_multiRP_data_newindex.loc[ :, "arm" ] == 0 ]

df_protons_multiRP_data_arm1 = df_protons_multiRP_data_newindex.loc[ df_protons_multiRP_data_newindex.loc[ :, "arm" ] == 1 ]
df_protons_multiRP_data_arm1

index_data_arm0 = df_protons_multiRP_data_arm0.index
index_data_arm1 = df_protons_multiRP_data_arm1.index

# df_counts_bkg = None
# df_protons_multiRP_bkg_index = None
# df_protons_multiRP_bkg_events = None
# 
# df_counts_bkg_list_ = []
# df_protons_multiRP_bkg_index_list_ = []
# df_protons_multiRP_bkg_events_list_ = []

for label_ in labels_background:
    print ( label_ )
    file_path_ = fileNames_bkg[ label_ ]
    print ( file_path_ )
    df_protons_multiRP_bkg_mix_arm0_events_ = None
    df_protons_multiRP_bkg_mix_arm1_events_ = None
    with pd.HDFStore( file_path_, 'r' ) as store_:
        print ( list( store_ ) )
        
        df_counts_bkg_ = store_[ "counts" ]
        df_protons_multiRP_bkg_index_  = store_[ "protons_multiRP" ]
        df_protons_multiRP_bkg_events_ = store_[ "events_multiRP" ]
        # df_counts_bkg_list_.append( df_counts_bkg_ )
        # df_protons_multiRP_bkg_index_list_.append( df_protons_multiRP_bkg_index_ )
        # df_protons_multiRP_bkg_events_list_.append( df_protons_multiRP_bkg_events_ )

        df_protons_multiRP_bkg_newindex_ = df_protons_multiRP_bkg_index_.reset_index().set_index( [ 'run', 'lumiblock', 'event' ] )

        df_protons_multiRP_bkg_arm0_ = df_protons_multiRP_bkg_newindex_.loc[ df_protons_multiRP_bkg_newindex_.loc[ :, "arm" ] == 0 ]

        df_protons_multiRP_bkg_arm1_ = df_protons_multiRP_bkg_newindex_.loc[ df_protons_multiRP_bkg_newindex_.loc[ :, "arm" ] == 1 ]

        index_bkg_arm0_ = df_protons_multiRP_bkg_arm0_.index
        index_bkg_arm1_ = df_protons_multiRP_bkg_arm1_.index

        msk_bkg_arm0_in_data_arm1_ = index_bkg_arm0_.isin( index_data_arm1 )
        msk_bkg_arm1_in_data_arm0_ = index_bkg_arm1_.isin( index_data_arm0 )
        msk_data_arm0_in_bkg_arm1_ = index_data_arm0.isin( index_bkg_arm1_ )
        msk_data_arm1_in_bkg_arm0_ = index_data_arm1.isin( index_bkg_arm0_ )
        print ( msk_bkg_arm0_in_data_arm1_.size, np.sum( msk_bkg_arm0_in_data_arm1_ ) )
        print ( msk_bkg_arm1_in_data_arm0_.size, np.sum( msk_bkg_arm1_in_data_arm0_ ) )
        print ( msk_data_arm0_in_bkg_arm1_.size, np.sum( msk_data_arm0_in_bkg_arm1_ ) )
        print ( msk_data_arm1_in_bkg_arm0_.size, np.sum( msk_data_arm1_in_bkg_arm0_ ) )

        df__ = df_protons_multiRP_bkg_arm0_.join( df_protons_multiRP_data_arm1, how='inner', lsuffix='_bkg' ).sort_index()
        df__ = df__.drop( columns=['slice'] ).rename( columns={ "slice_bkg": "slice"} )
        msk_columns_bkg_ = [ key_.find('_bkg') >= 0 for key_ in df__.columns.values ]
        columns_bkg_ = df__.columns.values[ msk_columns_bkg_ ]
        df__ = df__.drop( columns=columns_bkg_ )
        df_protons_multiRP_bkg_arm0_in_data_arm1_ = df__

        df__ = df_protons_multiRP_bkg_arm1_.join( df_protons_multiRP_data_arm0, how='inner', lsuffix='_bkg' ).sort_index()
        df__ = df__.drop( columns=['slice'] ).rename( columns={ "slice_bkg": "slice"} )
        msk_columns_bkg_ = [ key_.find('_bkg') >= 0 for key_ in df__.columns.values ]
        columns_bkg_ = df__.columns.values[ msk_columns_bkg_ ]
        df__ = df__.drop( columns=columns_bkg_ )
        df_protons_multiRP_bkg_arm1_in_data_arm0_ = df__

        df_protons_multiRP_bkg_mix_arm0_ = pd.concat( [ df_protons_multiRP_bkg_arm0_.reset_index(), df_protons_multiRP_bkg_arm0_in_data_arm1_.reset_index() ], axis=0 ).set_index( [ 'run', 'lumiblock', 'event', 'slice' ] ).sort_index()

        df_protons_multiRP_bkg_mix_arm1_ = pd.concat( [ df_protons_multiRP_bkg_arm1_.reset_index(), df_protons_multiRP_bkg_arm1_in_data_arm0_.reset_index() ], axis=0 ).set_index( [ 'run', 'lumiblock', 'event', 'slice' ] ).sort_index()

        columns_drop_ = [ "xi", "thx", "thy", "t", "ismultirp", "rpid", "arm", "random",
                              "trackx1", "tracky1", "trackpixshift1", "rpid1",
                              "trackx2", "tracky2", "trackpixshift2", "rpid2" ]
        df_protons_multiRP_events__, df_protons_multiRP_index_2protons__ = process_events( df_protons_multiRP_bkg_mix_arm0_, columns_drop=columns_drop_ )
        df_protons_multiRP_bkg_mix_arm0_events_ = df_protons_multiRP_events__

        df_protons_multiRP_events__, df_protons_multiRP_index_2protons__ = process_events( df_protons_multiRP_bkg_mix_arm1_, columns_drop=columns_drop_ )
        df_protons_multiRP_bkg_mix_arm1_events_ = df_protons_multiRP_events__

    print ( df_protons_multiRP_bkg_mix_arm0_events_ )
    print ( df_protons_multiRP_bkg_mix_arm1_events_ )

    file_path_ = "data-store-single-arm-mixing-events-{}.h5".format( label_ )
    print ( file_path_ )
    with pd.HDFStore( file_path_, 'w', complevel=5 ) as store_:
        store_[ "events_multiRP/mix_arm0" ] = df_protons_multiRP_bkg_mix_arm0_events_
        store_[ "events_multiRP/mix_arm1" ] = df_protons_multiRP_bkg_mix_arm1_events_
        print ( list( store_ ) )

