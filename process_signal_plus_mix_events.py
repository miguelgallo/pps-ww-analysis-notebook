#!/usr/bin/env python
# coding: utf-8
import numpy as np
import pandas as pd
import h5py

# run_ranges_periods, df_run_ranges, fiducial_cuts, fiducial_cuts_all, aperture_period_map, aperture_parametrisation, check_aperture, get_data, process_data_protons_multiRP
from processing import *

lepton_type = 'muon'
#lepton_type = 'electron'

# data_sample = '2017'
data_sample = '2018'

use_hash_index_ = True

base_path_ = '/eos/home-m/malvesga/SWAN_projects/Antonio_UL/output_05-07'
output_dir_ = '/eos/home-m/malvesga/SWAN_projects/Antonio_UL/output_05-07'

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
        # labels_signals = [ "GGToWW-AQGC-2018-muon-A0W5e-7", "GGToWW-AQGC-2018-muon-A0W1e-6", "GGToWW-AQGC-2018-muon-A0W2e-6", "GGToWW-AQGC-2018-muon-A0W5e-6" ]
        labels_signals = [ "GGToWW-AQGC-2018-muon-A0W1e-6", "GGToWW-AQGC-2018-muon-A0W2e-6", "GGToWW-AQGC-2018-muon-A0W5e-6" ]
    elif lepton_type == 'electron':
        # labels_signals = [ "GGToWW-AQGC-2018-electron-A0W5e-7", "GGToWW-AQGC-2018-electron-A0W1e-6", "GGToWW-AQGC-2018-electron-A0W2e-6", "GGToWW-AQGC-2018-electron-A0W5e-6" ]
        labels_signals = [ "GGToWW-AQGC-2018-electron-A0W1e-6", "GGToWW-AQGC-2018-electron-A0W2e-6", "GGToWW-AQGC-2018-electron-A0W5e-6" ]

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
        # labels_signals_mix_protons = [ "GGToWW-AQGC-mix_protons-2018-muon-A0W5e-7", "GGToWW-AQGC-mix_protons-2018-muon-A0W1e-6", "GGToWW-AQGC-mix_protons-2018-muon-A0W2e-6", "GGToWW-AQGC-mix_protons-2018-muon-A0W5e-6" ]
        labels_signals_mix_protons = [ "GGToWW-AQGC-mix_protons-2018-muon-A0W1e-6", "GGToWW-AQGC-mix_protons-2018-muon-A0W2e-6", "GGToWW-AQGC-mix_protons-2018-muon-A0W5e-6" ]
    elif lepton_type == 'electron':
        # labels_signals_mix_protons = [ "GGToWW-AQGC-mix_protons-2018-electron-A0W5e-7", "GGToWW-AQGC-mix_protons-2018-electron-A0W1e-6", "GGToWW-AQGC-mix_protons-2018-electron-A0W2e-6", "GGToWW-AQGC-mix_protons-2018-electron-A0W5e-6" ]
        labels_signals_mix_protons = [ "GGToWW-AQGC-mix_protons-2018-electron-A0W1e-6", "GGToWW-AQGC-mix_protons-2018-electron-A0W2e-6", "GGToWW-AQGC-mix_protons-2018-electron-A0W5e-6" ]

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
             # "GGToWW-AQGC-2018-muon-A0W5e-7" : "GGToWW-AQGC-mix_protons-2018-muon-A0W5e-7",
             "GGToWW-AQGC-2018-muon-A0W1e-6" : "GGToWW-AQGC-mix_protons-2018-muon-A0W1e-6",
             "GGToWW-AQGC-2018-muon-A0W2e-6" : "GGToWW-AQGC-mix_protons-2018-muon-A0W2e-6",
             "GGToWW-AQGC-2018-muon-A0W5e-6" : "GGToWW-AQGC-mix_protons-2018-muon-A0W5e-6"
        }
    elif lepton_type == 'electron':
        label_signal_to_mix_protons = {
             # "GGToWW-AQGC-2018-electron-A0W5e-7" : "GGToWW-AQGC-mix_protons-2018-electron-A0W5e-7",
             "GGToWW-AQGC-2018-electron-A0W1e-6" : "GGToWW-AQGC-mix_protons-2018-electron-A0W1e-6",
             "GGToWW-AQGC-2018-electron-A0W2e-6" : "GGToWW-AQGC-mix_protons-2018-electron-A0W2e-6",
             "GGToWW-AQGC-2018-electron-A0W5e-6" : "GGToWW-AQGC-mix_protons-2018-electron-A0W5e-6"
        }

process_signal_plus_mix_events( data_sample=data_sample, labels_signals=labels_signals, labels_signals_mix_protons=labels_signals_mix_protons, label_signal_to_mix_protons=label_signal_to_mix_protons, base_path=base_path_, output_dir=output_dir_, use_hash_index=use_hash_index_ )
