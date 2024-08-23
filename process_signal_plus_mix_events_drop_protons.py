#!/usr/bin/env python
# coding: utf-8
import numpy as np
import pandas as pd
import h5py

from processing import *

#lepton_type = 'muon'
lepton_type = 'electron'

# data_sample = '2017'
data_sample = '2018'

use_hash_index_ = True

base_path_ = '/eos/home-m/malvesga/SWAN_projects/Antonio_UL/output-final'
output_dir_ = '/eos/home-m/malvesga/SWAN_projects/Antonio_UL/output-final'

# Signal
labels_signals = []
if data_sample == '2017':
    if lepton_type == 'muon':
        labels_signals = [
            "GGToWW-AQGC-2017-muon-A0W1e-6-Arm0", "GGToWW-AQGC-2017-muon-A0W2e-6-Arm0", "GGToWW-AQGC-2017-muon-A0W5e-6-Arm0",
            "GGToWW-AQGC-2017-muon-A0W1e-6-Arm1", "GGToWW-AQGC-2017-muon-A0W2e-6-Arm1", "GGToWW-AQGC-2017-muon-A0W5e-6-Arm1"
        ]
    elif lepton_type == 'electron':
        labels_signals = [
            "GGToWW-AQGC-2017-electron-A0W1e-6-Arm0", "GGToWW-AQGC-2017-electron-A0W2e-6-Arm0", "GGToWW-AQGC-2017-electron-A0W5e-6-Arm0",
            "GGToWW-AQGC-2017-electron-A0W1e-6-Arm1", "GGToWW-AQGC-2017-electron-A0W2e-6-Arm1", "GGToWW-AQGC-2017-electron-A0W5e-6-Arm1"
        ]
elif data_sample == '2018':
    if lepton_type == 'muon':
        labels_signals = [
            "GGToWW-AQGC-2018-muon-ACW5e-7-Arm0", "GGToWW-AQGC-2018-muon-ACW1e-6-Arm0", "GGToWW-AQGC-2018-muon-ACW2e-6-Arm0", 
            "GGToWW-AQGC-2018-muon-ACW5e-6-Arm0", "GGToWW-AQGC-2018-muon-ACW1e-5-Arm0", "GGToWW-AQGC-2018-muon-ACW2e-5-Arm0",
            "GGToWW-AQGC-2018-muon-ACW5e-7-Arm1", "GGToWW-AQGC-2018-muon-ACW1e-6-Arm1", "GGToWW-AQGC-2018-muon-ACW2e-6-Arm1", 
            "GGToWW-AQGC-2018-muon-ACW5e-6-Arm1", "GGToWW-AQGC-2018-muon-ACW1e-5-Arm1", "GGToWW-AQGC-2018-muon-ACW2e-5-Arm1",
            "GGToWW-AQGC-2018-muon-A0W1e-7-Arm0", "GGToWW-AQGC-2018-muon-A0W2e-7-Arm0", "GGToWW-AQGC-2018-muon-A0W5e-7-Arm0", 
            "GGToWW-AQGC-2018-muon-A0W1e-6-Arm0", "GGToWW-AQGC-2018-muon-A0W2e-6-Arm0", "GGToWW-AQGC-2018-muon-A0W5e-6-Arm0",
            "GGToWW-AQGC-2018-muon-A0W1e-7-Arm1", "GGToWW-AQGC-2018-muon-A0W2e-7-Arm1", "GGToWW-AQGC-2018-muon-A0W5e-7-Arm1",
            "GGToWW-AQGC-2018-muon-A0W1e-6-Arm1", "GGToWW-AQGC-2018-muon-A0W2e-6-Arm1", "GGToWW-AQGC-2018-muon-A0W5e-6-Arm1"
        ]
#        labels_signals = [ "GGToWW-AQGC-2018-muon-ACW5e-7-Arm0", "GGToWW-AQGC-2018-muon-ACW5e-7-Arm1" ]
    elif lepton_type == 'electron':
        labels_signals = [
            "GGToWW-AQGC-2018-electron-ACW5e-7-Arm0", "GGToWW-AQGC-2018-electron-ACW1e-6-Arm0", "GGToWW-AQGC-2018-electron-ACW2e-6-Arm0", 
            "GGToWW-AQGC-2018-electron-ACW5e-6-Arm0", "GGToWW-AQGC-2018-electron-ACW1e-5-Arm0", "GGToWW-AQGC-2018-electron-ACW2e-5-Arm0",
            "GGToWW-AQGC-2018-electron-ACW5e-7-Arm1", "GGToWW-AQGC-2018-electron-ACW1e-6-Arm1", "GGToWW-AQGC-2018-electron-ACW2e-6-Arm1", 
            "GGToWW-AQGC-2018-electron-ACW5e-6-Arm1", "GGToWW-AQGC-2018-electron-ACW1e-5-Arm1", "GGToWW-AQGC-2018-electron-ACW2e-5-Arm1",
            "GGToWW-AQGC-2018-electron-A0W1e-7-Arm0", "GGToWW-AQGC-2018-electron-A0W2e-7-Arm0", "GGToWW-AQGC-2018-electron-A0W5e-7-Arm0", 
            "GGToWW-AQGC-2018-electron-A0W1e-6-Arm0", "GGToWW-AQGC-2018-electron-A0W2e-6-Arm0", "GGToWW-AQGC-2018-electron-A0W5e-6-Arm0",
            "GGToWW-AQGC-2018-electron-A0W1e-7-Arm1", "GGToWW-AQGC-2018-electron-A0W2e-7-Arm1", "GGToWW-AQGC-2018-electron-A0W5e-7-Arm1",
            "GGToWW-AQGC-2018-electron-A0W1e-6-Arm1", "GGToWW-AQGC-2018-electron-A0W2e-6-Arm1", "GGToWW-AQGC-2018-electron-A0W5e-6-Arm1"
        ]
        #labels_signals = [ "GGToWW-AQGC-2018-electron-ACW5e-7-Arm0", "GGToWW-AQGC-2018-electron-ACW5e-7-Arm1" ]

labels_signals_mix_protons = []
if data_sample == '2017':
    if lepton_type == 'muon':
        labels_signals_mix_protons = [ "GGToWW-AQGC-mix_protons-2017-muon-A0W1e-6", "GGToWW-AQGC-mix_protons-2017-muon-A0W2e-6", "GGToWW-AQGC-mix_protons-2017-muon-A0W5e-6" ]
    elif lepton_type == 'electron':
        labels_signals_mix_protons = [ "GGToWW-AQGC-mix_protons-2017-electron-A0W1e-6", "GGToWW-AQGC-mix_protons-2017-electron-A0W2e-6", "GGToWW-AQGC-mix_protons-2017-electron-A0W5e-6" ]
elif data_sample == '2018':
    if lepton_type == 'muon':
        #labels_signals_mix_protons = [ "GGToWW-AQGC-mix_protons-2018-muon-ACW5e-7", "GGToWW-AQGC-mix_protons-2018-muon-ACW5e-6", "GGToWW-AQGC-mix_protons-2018-muon-ACW8e-6", "GGToWW-AQGC-mix_protons-2018-muon-ACW2e-5" ]
        #labels_signals_mix_protons = [ "GGToWW-AQGC-mix_protons-2018-muon-A0W1e-6", "GGToWW-AQGC-mix_protons-2018-muon-A0W2e-6", "GGToWW-AQGC-mix_protons-2018-muon-A0W5e-6" ]
        labels_signals_mix_protons = [ "GGToWW-AQGC-mix_protons-2018-muon-A0W1e-7", "GGToWW-AQGC-mix_protons-2018-muon-A0W2e-7", "GGToWW-AQGC-mix_protons-2018-muon-A0W5e-7", "GGToWW-AQGC-mix_protons-2018-muon-A0W1e-6", "GGToWW-AQGC-mix_protons-2018-muon-A0W2e-6", "GGToWW-AQGC-mix_protons-2018-muon-A0W5e-6", "GGToWW-AQGC-mix_protons-2018-muon-ACW5e-7", "GGToWW-AQGC-mix_protons-2018-muon-ACW1e-6", "GGToWW-AQGC-mix_protons-2018-muon-ACW2e-6", "GGToWW-AQGC-mix_protons-2018-muon-ACW5e-6", "GGToWW-AQGC-mix_protons-2018-muon-ACW1e-5", "GGToWW-AQGC-mix_protons-2018-muon-ACW2e-5" ]
        #labels_signals_mix_protons = [ "GGToWW-AQGC-mix_protons-2018-muon-ACW5e-7" ]
    elif lepton_type == 'electron':
        #labels_signals_mix_protons = [ "GGToWW-AQGC-mix_protons-2018-electron-ACW5e-7", "GGToWW-AQGC-mix_protons-2018-electron-ACW5e-6", "GGToWW-AQGC-mix_protons-2018-electron-ACW8e-6", "GGToWW-AQGC-mix_protons-2018-electron-ACW2e-5" ]
        #labels_signals_mix_protons = [ "GGToWW-AQGC-mix_protons-2018-electron-A0W1e-6", "GGToWW-AQGC-mix_protons-2018-electron-A0W2e-6", "GGToWW-AQGC-mix_protons-2018-electron-A0W5e-6" ]
        labels_signals_mix_protons = [ "GGToWW-AQGC-mix_protons-2018-electron-A0W1e-7", "GGToWW-AQGC-mix_protons-2018-electron-A0W2e-7", "GGToWW-AQGC-mix_protons-2018-electron-A0W5e-7", "GGToWW-AQGC-mix_protons-2018-electron-A0W1e-6", "GGToWW-AQGC-mix_protons-2018-electron-A0W2e-6", "GGToWW-AQGC-mix_protons-2018-electron-A0W5e-6", "GGToWW-AQGC-mix_protons-2018-electron-ACW5e-7", "GGToWW-AQGC-mix_protons-2018-electron-ACW1e-6", "GGToWW-AQGC-mix_protons-2018-electron-ACW2e-6", "GGToWW-AQGC-mix_protons-2018-electron-ACW5e-6", "GGToWW-AQGC-mix_protons-2018-electron-ACW1e-5", "GGToWW-AQGC-mix_protons-2018-electron-ACW2e-5" ]
        #labels_signals_mix_protons = [ "GGToWW-AQGC-mix_protons-2018-electron-ACW5e-7" ]

label_signal_to_mix_protons = {}
if data_sample == '2017':
    if lepton_type == 'muon':
        label_signal_to_mix_protons = {
             "GGToWW-AQGC-2017-muon-A0W1e-6-Arm0" : "GGToWW-AQGC-mix_protons-2017-muon-A0W1e-6",
             "GGToWW-AQGC-2017-muon-A0W2e-6-Arm0" : "GGToWW-AQGC-mix_protons-2017-muon-A0W2e-6",
             "GGToWW-AQGC-2017-muon-A0W5e-6-Arm0" : "GGToWW-AQGC-mix_protons-2017-muon-A0W5e-6",
             "GGToWW-AQGC-2017-muon-A0W1e-6-Arm1" : "GGToWW-AQGC-mix_protons-2017-muon-A0W1e-6",
             "GGToWW-AQGC-2017-muon-A0W2e-6-Arm1" : "GGToWW-AQGC-mix_protons-2017-muon-A0W2e-6",
             "GGToWW-AQGC-2017-muon-A0W5e-6-Arm1" : "GGToWW-AQGC-mix_protons-2017-muon-A0W5e-6"
        }
    elif lepton_type == 'electron':
        label_signal_to_mix_protons = {
             "GGToWW-AQGC-2017-electron-A0W1e-6-Arm0" : "GGToWW-AQGC-mix_protons-2017-electron-A0W1e-6",
             "GGToWW-AQGC-2017-electron-A0W2e-6-Arm0" : "GGToWW-AQGC-mix_protons-2017-electron-A0W2e-6",
             "GGToWW-AQGC-2017-electron-A0W5e-6-Arm0" : "GGToWW-AQGC-mix_protons-2017-electron-A0W5e-6",
             "GGToWW-AQGC-2017-electron-A0W1e-6-Arm1" : "GGToWW-AQGC-mix_protons-2017-electron-A0W1e-6",
             "GGToWW-AQGC-2017-electron-A0W2e-6-Arm1" : "GGToWW-AQGC-mix_protons-2017-electron-A0W2e-6",
             "GGToWW-AQGC-2017-electron-A0W5e-6-Arm1" : "GGToWW-AQGC-mix_protons-2017-electron-A0W5e-6"
        }
elif data_sample == '2018':
    if lepton_type == 'muon':
        label_signal_to_mix_protons = {
             "GGToWW-AQGC-2018-muon-A0W1e-7-Arm0" : "GGToWW-AQGC-mix_protons-2018-muon-A0W1e-7",
             "GGToWW-AQGC-2018-muon-A0W2e-7-Arm0" : "GGToWW-AQGC-mix_protons-2018-muon-A0W2e-7",
             "GGToWW-AQGC-2018-muon-A0W5e-7-Arm0" : "GGToWW-AQGC-mix_protons-2018-muon-A0W5e-7",
             "GGToWW-AQGC-2018-muon-A0W1e-6-Arm0" : "GGToWW-AQGC-mix_protons-2018-muon-A0W1e-6",
             "GGToWW-AQGC-2018-muon-A0W2e-6-Arm0" : "GGToWW-AQGC-mix_protons-2018-muon-A0W2e-6",
             "GGToWW-AQGC-2018-muon-A0W5e-6-Arm0" : "GGToWW-AQGC-mix_protons-2018-muon-A0W5e-6",
             "GGToWW-AQGC-2018-muon-A0W1e-7-Arm1" : "GGToWW-AQGC-mix_protons-2018-muon-A0W1e-7",
             "GGToWW-AQGC-2018-muon-A0W2e-7-Arm1" : "GGToWW-AQGC-mix_protons-2018-muon-A0W2e-7",
             "GGToWW-AQGC-2018-muon-A0W5e-7-Arm1" : "GGToWW-AQGC-mix_protons-2018-muon-A0W5e-7",
             "GGToWW-AQGC-2018-muon-A0W1e-6-Arm1" : "GGToWW-AQGC-mix_protons-2018-muon-A0W1e-6",
             "GGToWW-AQGC-2018-muon-A0W2e-6-Arm1" : "GGToWW-AQGC-mix_protons-2018-muon-A0W2e-6",
             "GGToWW-AQGC-2018-muon-A0W5e-6-Arm1" : "GGToWW-AQGC-mix_protons-2018-muon-A0W5e-6",
             "GGToWW-AQGC-2018-muon-ACW5e-7-Arm0" : "GGToWW-AQGC-mix_protons-2018-muon-ACW5e-7",
             "GGToWW-AQGC-2018-muon-ACW1e-6-Arm0" : "GGToWW-AQGC-mix_protons-2018-muon-ACW1e-6",
             "GGToWW-AQGC-2018-muon-ACW2e-6-Arm0" : "GGToWW-AQGC-mix_protons-2018-muon-ACW2e-6",
             "GGToWW-AQGC-2018-muon-ACW5e-6-Arm0" : "GGToWW-AQGC-mix_protons-2018-muon-ACW5e-6",
             "GGToWW-AQGC-2018-muon-ACW1e-5-Arm0" : "GGToWW-AQGC-mix_protons-2018-muon-ACW1e-5",
             "GGToWW-AQGC-2018-muon-ACW2e-5-Arm0" : "GGToWW-AQGC-mix_protons-2018-muon-ACW2e-5",
             "GGToWW-AQGC-2018-muon-ACW5e-7-Arm1" : "GGToWW-AQGC-mix_protons-2018-muon-ACW5e-7",
             "GGToWW-AQGC-2018-muon-ACW1e-6-Arm1" : "GGToWW-AQGC-mix_protons-2018-muon-ACW1e-6",
             "GGToWW-AQGC-2018-muon-ACW2e-6-Arm1" : "GGToWW-AQGC-mix_protons-2018-muon-ACW2e-6",
             "GGToWW-AQGC-2018-muon-ACW5e-6-Arm1" : "GGToWW-AQGC-mix_protons-2018-muon-ACW5e-6",
             "GGToWW-AQGC-2018-muon-ACW1e-5-Arm1" : "GGToWW-AQGC-mix_protons-2018-muon-ACW1e-5",
             "GGToWW-AQGC-2018-muon-ACW2e-5-Arm1" : "GGToWW-AQGC-mix_protons-2018-muon-ACW2e-5"
        }
    elif lepton_type == 'electron':
        label_signal_to_mix_protons = {
             "GGToWW-AQGC-2018-electron-A0W1e-7-Arm0" : "GGToWW-AQGC-mix_protons-2018-electron-A0W1e-7",
             "GGToWW-AQGC-2018-electron-A0W2e-7-Arm0" : "GGToWW-AQGC-mix_protons-2018-electron-A0W2e-7",
             "GGToWW-AQGC-2018-electron-A0W5e-7-Arm0" : "GGToWW-AQGC-mix_protons-2018-electron-A0W5e-7",
             "GGToWW-AQGC-2018-electron-A0W1e-6-Arm0" : "GGToWW-AQGC-mix_protons-2018-electron-A0W1e-6",
             "GGToWW-AQGC-2018-electron-A0W2e-6-Arm0" : "GGToWW-AQGC-mix_protons-2018-electron-A0W2e-6",
             "GGToWW-AQGC-2018-electron-A0W5e-6-Arm0" : "GGToWW-AQGC-mix_protons-2018-electron-A0W5e-6",
             "GGToWW-AQGC-2018-electron-A0W1e-7-Arm1" : "GGToWW-AQGC-mix_protons-2018-electron-A0W1e-7",
             "GGToWW-AQGC-2018-electron-A0W2e-7-Arm1" : "GGToWW-AQGC-mix_protons-2018-electron-A0W2e-7",
             "GGToWW-AQGC-2018-electron-A0W5e-7-Arm1" : "GGToWW-AQGC-mix_protons-2018-electron-A0W5e-7",
             "GGToWW-AQGC-2018-electron-A0W1e-6-Arm1" : "GGToWW-AQGC-mix_protons-2018-electron-A0W1e-6",
             "GGToWW-AQGC-2018-electron-A0W2e-6-Arm1" : "GGToWW-AQGC-mix_protons-2018-electron-A0W2e-6",
             "GGToWW-AQGC-2018-electron-A0W5e-6-Arm1" : "GGToWW-AQGC-mix_protons-2018-electron-A0W5e-6",
             "GGToWW-AQGC-2018-electron-ACW5e-7-Arm0" : "GGToWW-AQGC-mix_protons-2018-electron-ACW5e-7",
             "GGToWW-AQGC-2018-electron-ACW1e-6-Arm0" : "GGToWW-AQGC-mix_protons-2018-electron-ACW1e-6",
             "GGToWW-AQGC-2018-electron-ACW2e-6-Arm0" : "GGToWW-AQGC-mix_protons-2018-electron-ACW2e-6",
             "GGToWW-AQGC-2018-electron-ACW5e-6-Arm0" : "GGToWW-AQGC-mix_protons-2018-electron-ACW5e-6",
             "GGToWW-AQGC-2018-electron-ACW1e-5-Arm0" : "GGToWW-AQGC-mix_protons-2018-electron-ACW1e-5",
             "GGToWW-AQGC-2018-electron-ACW2e-5-Arm0" : "GGToWW-AQGC-mix_protons-2018-electron-ACW2e-5",
             "GGToWW-AQGC-2018-electron-ACW5e-7-Arm1" : "GGToWW-AQGC-mix_protons-2018-electron-ACW5e-7",
             "GGToWW-AQGC-2018-electron-ACW1e-6-Arm1" : "GGToWW-AQGC-mix_protons-2018-electron-ACW1e-6",
             "GGToWW-AQGC-2018-electron-ACW2e-6-Arm1" : "GGToWW-AQGC-mix_protons-2018-electron-ACW2e-6",
             "GGToWW-AQGC-2018-electron-ACW5e-6-Arm1" : "GGToWW-AQGC-mix_protons-2018-electron-ACW5e-6",
             "GGToWW-AQGC-2018-electron-ACW1e-5-Arm1" : "GGToWW-AQGC-mix_protons-2018-electron-ACW1e-5",
             "GGToWW-AQGC-2018-electron-ACW2e-5-Arm1" : "GGToWW-AQGC-mix_protons-2018-electron-ACW2e-5"
        }

process_signal_plus_mix_events( data_sample=data_sample, labels_signals=labels_signals, labels_signals_mix_protons=labels_signals_mix_protons, label_signal_to_mix_protons=label_signal_to_mix_protons, base_path=base_path_, output_dir=output_dir_, use_hash_index=use_hash_index_ )
