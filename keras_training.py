#!/usr/bin/env python
# coding: utf-8

import os
import numpy as np
import pandas as pd
import h5py
from joblib import dump, load

import sklearn
import tensorflow as tf
from tensorflow import keras

print ( "sklearn: {}".format(sklearn.__version__) )
print ( "tensorflow: {}".format(tf.__version__) )

gpus = tf.config.experimental.list_physical_devices('GPU')
for gpu in gpus:
    tf.config.experimental.set_memory_growth(gpu, True)
if gpus:
    tf.config.experimental.set_visible_devices(gpus[0], 'GPU')
print ( gpus )

# run_ranges_periods, df_run_ranges, fiducial_cuts, fiducial_cuts_all, aperture_period_map, aperture_parametrisation, check_aperture, get_data, process_data_protons_multiRP
from processing import *

run_tables = False
train_model = True
run_grid_search = True
save_model = True

n_iter_search_ = 3
label_ = "test-multiRP"
base_path_ = "/eos/home-a/antoniov/SWAN_projects/pps-ww-analysis"

n_events_signal = None
n_events_bkg = None
#n_events_bkg = 100000

prob_cut_ = 0.40

label_signal = "GGToWW-AQGC-A0W1e-6"
fileNames_signal = [
    "output-GGToWW-AQGC-A0W1e-6.h5"
]
fileNames_signal = [ "{}/{}".format( base_path_, item_ ) for item_ in fileNames_signal ]
print ( fileNames_signal )

resample_factor = 20
label_bkg = "data-random-resample_20"
fileNames_bkg = [
    "output-data-random-resample_20-test-2017B.h5",
    "output-data-random-resample_20-test-2017C.h5",
    "output-data-random-resample_20-test-2017D.h5",
    "output-data-random-resample_20-test-2017E.h5",
    "output-data-random-resample_20-test-2017F.h5"
]
fileNames_bkg = [ "{}/{}".format( base_path_, item_ ) for item_ in fileNames_bkg ]
print ( fileNames_bkg )

# Signal

import time
print( time.strftime("%Y/%m/%d %H:%M:%S", time.localtime() ) )
time_s_ = time.time()

df_counts_signal, df_protons_multiRP_signal, df_protons_singleRP_signal, df_ppstracks_signal = 4 * [None]
df_protons_multiRP_signal_index, df_protons_multiRP_signal_events, df_ppstracks_signal_index = 3 * [None]

fileName_ = "{}/reduced-data-store-{}.h5".format( base_path_, label_signal )
if run_tables:
    with pd.HDFStore( fileName_, complevel=5 ) as store_:

        df_counts_signal, df_protons_multiRP_signal, df_protons_singleRP_signal, df_ppstracks_signal = get_data( fileNames_signal )
        df_protons_multiRP_signal_index, df_protons_multiRP_signal_events, df_ppstracks_signal_index = process_data_protons_multiRP( df_protons_multiRP_signal, df_ppstracks_signal, apply_fiducial=True, runOnMC=True )

        store_[ "counts" ] = df_counts_signal
        store_[ "protons_multiRP"] = df_protons_multiRP_signal_index
        store_[ "events_multiRP" ] = df_protons_multiRP_signal_events

with pd.HDFStore( fileName_, 'r' ) as store_:
    df_counts_signal = store_[ "counts" ]
    df_protons_multiRP_signal_index = store_[ "protons_multiRP" ]
    df_protons_multiRP_signal_events = store_[ "events_multiRP" ]
        
time_e_ = time.time()
print ( "Total time elapsed: {:.0f}".format( time_e_ - time_s_ ) )

df_protons_multiRP_signal_index[:20]
df_protons_multiRP_signal_events[:20]

# Background

import time
print( time.strftime("%Y/%m/%d %H:%M:%S", time.localtime() ) )
time_s_ = time.time()

df_counts_bkg, df_protons_multiRP_bkg, df_protons_singleRP_bkg, df_ppstracks_bkg = 4 * [None]
df_protons_multiRP_bkg_index, df_protons_multiRP_bkg_events, df_ppstracks_bkg_index = 3 * [None]

fileName_ = "{}/reduced-data-store-{}.h5".format( base_path_, label_bkg )
if run_tables:
    with pd.HDFStore( fileName_, complevel=5 ) as store_:

        df_counts_bkg, df_protons_multiRP_bkg, df_protons_singleRP_bkg, df_ppstracks_bkg = get_data( fileNames_bkg )
        df_protons_multiRP_bkg_index, df_protons_multiRP_bkg_events, df_ppstracks_bkg_index = process_data_protons_multiRP( df_protons_multiRP_bkg, df_ppstracks_bkg, apply_fiducial=True, within_aperture=True, runOnMC=False )

        store_[ "counts" ] = df_counts_bkg
        store_[ "protons_multiRP"] = df_protons_multiRP_bkg_index
        store_[ "events_multiRP" ] = df_protons_multiRP_bkg_events

with pd.HDFStore( fileName_, 'r' ) as store_:
    df_counts_bkg = store_[ "counts" ]
    df_protons_multiRP_bkg_index = store_[ "protons_multiRP" ]
    df_protons_multiRP_bkg_events = store_[ "events_multiRP" ]
        
time_e_ = time.time()
print ( "Total time elapsed: {:.0f}".format( time_e_ - time_s_ ) )

df_protons_multiRP_bkg_index[:20]
df_protons_multiRP_bkg_events[:20]

# Select events

msk_bkg = ( ( df_protons_multiRP_bkg_events.loc[ :, "jet0_corrmass"] >= 50.0 ) &
            ( df_protons_multiRP_bkg_events.loc[ :, "jet0_corrmass"] <= 110.0 ) & 
            ( df_protons_multiRP_bkg_events.loc[ :, "num_bjets_ak4"] == 0 ) )
msk_signal = ( ( df_protons_multiRP_signal_events.loc[ :, "jet0_corrmass"] >= 50.0 ) &
               ( df_protons_multiRP_signal_events.loc[ :, "jet0_corrmass"] <= 110.0 ) &
               ( df_protons_multiRP_signal_events.loc[ :, "num_bjets_ak4"] == 0 ) )
df_protons_multiRP_bkg_events = df_protons_multiRP_bkg_events.loc[ msk_bkg ]
df_protons_multiRP_signal_events = df_protons_multiRP_signal_events.loc[ msk_signal ]

# Set aside test sample

from sklearn.model_selection import train_test_split

y_sig_ = np.ones( df_protons_multiRP_signal_events.shape[0] )
y_bkg_ = np.zeros( df_protons_multiRP_bkg_events.shape[0] )

df_protons_multiRP_signal_train, df_protons_multiRP_signal_test, y_sig_train, y_sig_test = train_test_split( df_protons_multiRP_signal_events, y_sig_, test_size=0.40, shuffle=True, random_state=12345 )
df_protons_multiRP_bkg_train, df_protons_multiRP_bkg_test, y_bkg_train, y_bkg_test = train_test_split( df_protons_multiRP_bkg_events, y_bkg_, test_size=0.40, shuffle=True, random_state=12345 )

print ( df_protons_multiRP_signal_train, df_protons_multiRP_signal_test, y_sig_train, y_sig_test )
print ( df_protons_multiRP_bkg_train, df_protons_multiRP_bkg_test, y_bkg_train, y_bkg_test )

print ( [ arr_.shape[0] for arr_ in ( df_protons_multiRP_signal_train, df_protons_multiRP_signal_test, y_sig_train, y_sig_test ) ] )
print ( [ arr_.shape[0] for arr_ in ( df_protons_multiRP_bkg_train, df_protons_multiRP_bkg_test, y_bkg_train, y_bkg_test ) ] )
print ( df_protons_multiRP_signal_test.mean() )
print ( df_protons_multiRP_bkg_test.mean() )

# Select variables

# variables_ = [ 'jet0_pt', 'jet0_eta', 'jet0_phi', 'jet0_tau1', 'jet0_tau2', 'muon0_pt', 'muon0_eta', 'muon0_phi', 'met', 'met_phi',
#                'pfcand_nextracks', 'WLeptonicPt', 'WLeptonicPhi', 'recoMWW', 'recoRapidityWW', 'MX', 'YX' ]
variables_ = [ 'jet0_pt', 'jet0_phi', 'jet0_tau1', 'jet0_tau2', 'pfcand_nextracks', 
                'WLeptonicPt', 'WLeptonicPhi', 'recoMWW', 'recoRapidityWW', 'MX', 'YX' ]

X_sig_train = None
if n_events_signal:
    X_sig_train = df_protons_multiRP_signal_train[ variables_ ].iloc[:n_events_signal]
    y_sig_train = y_sig_train.iloc[:n_events_signal]
else:
    X_sig_train = df_protons_multiRP_signal_train[ variables_ ]
print ( X_sig_train.shape )
print ( X_sig_train[:20] )

X_sig_test = df_protons_multiRP_signal_test[ variables_ ]

X_bkg_train = None
if n_events_bkg:
    X_bkg_train = df_protons_multiRP_bkg_train[ variables_ ].iloc[:n_events_bkg]
    y_bkg_train = y_bkg_train.iloc[:n_events_bkg]
else:
    X_bkg_train = df_protons_multiRP_bkg_train[ variables_ ]
print ( X_bkg_train.shape )
print ( X_bkg_train[:20] )

X_bkg_test = df_protons_multiRP_bkg_test[ variables_ ]

X_ = pd.concat( [X_sig_train, X_bkg_train] ) 
y_ = np.concatenate( [y_sig_train, y_bkg_train] )

X_train, X_valid, y_train, y_valid = train_test_split( X_, y_, test_size=0.20, shuffle=True, random_state=42 )

X_test = pd.concat( [X_sig_test, X_bkg_test] ) 
y_test = np.concatenate( [y_sig_test, y_bkg_test] )

# Scale inputs
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform( X_train )
X_valid_scaled = scaler.transform( X_valid )
X_test_scaled = scaler.transform( X_test )

print ( scaler )
if train_model and save_model:
    import time
    id_ = time.strftime("%Y_%m_%d-%H_%M_%S")
    fileName_ = "standard_scaler_{}_{}.joblib".format( label_, id_ )
    print ( "Saving scaler to {}".format( fileName_ ) )
    dump( scaler, fileName_ )
X_train_scaled[:20]

# Model build function

from keras_model import Model, build_model

# Define training callbacks

def get_run_logdir(log_dir):
    import time
    run_id = time.strftime("run_%Y_%m_%d-%H_%M_%S")
    return os.path.join(log_dir, run_id)

def callbacks(patience=10, log_dir=""):
    callbacks_ = []
    # Early stopping
    if patience > 0:
        early_stopping_cb_ = keras.callbacks.EarlyStopping( patience=patience, restore_best_weights=True )
        callbacks_.append( early_stopping_cb_ )
        
    # TensorBoard
    if log_dir:
        run_logdir = get_run_logdir(log_dir)
        print ( "Log dir: {}".format(run_logdir) )
        tensorboard_cb_ = keras.callbacks.TensorBoard( run_logdir )
        callbacks_.append( tensorboard_cb_ )
    
    return callbacks_

# Hyperparameter scan

learning_rate = 5e-4
epochs_grid_search = 20

grid_search = None
if train_model and run_grid_search:
    import time
    print( time.strftime("%Y/%m/%d %H:%M:%S", time.localtime() ) )
    time_s_ = time.time()
        
    from sklearn.model_selection import RandomizedSearchCV
    #from sklearn.model_selection import GridSearchCV

    build_fn_ = Model( input_shape=X_train_scaled.shape[1:], learning_rate=learning_rate )
    keras_clf = keras.wrappers.scikit_learn.KerasClassifier( build_fn_ )

#     param_grid = [
#         { "n_hidden": np.arange(1,3),
#           "n_neurons": [20,50] }
#         ]

    param_distribs = {
        "n_hidden": np.arange(2,6),
        "n_neurons": 2 ** np.arange(4,8),
        "dropout":  0.1 * np.arange(2,6),
        "batch_size": 2 ** np.arange(5,8)
        }

    #grid_search = GridSearchCV( keras_clf, param_grid, cv=3, scoring='f1', refit=False )
    
    grid_search = RandomizedSearchCV(
        keras_clf,
        param_distribs,
        n_iter=n_iter_search_, cv=4, verbose=20, n_jobs=-1, scoring='f1', refit=False, random_state=42
        )

    callbacks_ = callbacks(patience=5)
    print ( callbacks_ )
    grid_search.fit( X_train_scaled, y_train, epochs=epochs_grid_search, validation_data=(X_valid_scaled, y_valid), callbacks=callbacks_ )
    
    print ( grid_search.best_params_ )
    print ( grid_search.best_score_ )
    print ( grid_search.cv_results_ )

    time_e_ = time.time()
    print ( "Total time elapsed: {:.0f}".format( time_e_ - time_s_ ) )

# Build model

model_final = None

if train_model:
    params = {'n_hidden': 1, 'n_neurons': 50, 'dropout': 0.20}
    batch_size = 32
    if run_grid_search: 
        params = grid_search.best_params_.copy()
        batch_size = params[ 'batch_size' ]
        params.pop( 'batch_size' )
    print ( params, "batch_size: {}".format( batch_size ) )
    
    model_final = build_model(input_shape=X_train_scaled.shape[1:], learning_rate=learning_rate, **params )
    model_final.summary()
    #log_dir="keras_logs"
    #callbacks_ = callbacks(patience=5, log_dir=log_dir)
    callbacks_ = callbacks( patience=5 )
    print ( callbacks_ )
    model_final.fit( X_train_scaled, y_train, epochs=100, batch_size=batch_size, validation_data=(X_valid_scaled, y_valid), callbacks=callbacks_ )
else:
    model_final = keras.models.load_model( "model/keras_model.h5" )
    
model_final.summary()

# Evaluate on training data (without dropout)

model_final.evaluate( X_train_scaled, y_train )

# Re-evaluate on validation data 

model_final.evaluate( X_valid_scaled, y_valid )

# Evaluate on test data

model_final.evaluate( X_test_scaled, y_test )

y_test_proba = model_final.predict( X_test_scaled )
print( y_test_proba )

print ( "Prob. cut: {}".format( prob_cut_ ) )

y_test_pred = ( y_test_proba >= prob_cut_ ).astype( "int32" )
print ( y_test_pred )

from sklearn.metrics import accuracy_score
print ( accuracy_score( y_test, y_test_pred ) )
print ( accuracy_score( y_test[ y_test == 1 ], y_test_pred[ y_test == 1 ] ) )
print ( accuracy_score( y_test[ y_test == 0 ], y_test_pred[ y_test == 0 ] ) )

# Save model

if train_model and save_model:
    import time
    id_ = time.strftime("%Y_%m_%d-%H_%M_%S")
    fileName_ = "keras_model_{}_{}.h5".format( label_, id_ )
    print ( "Saving model to {}".format( fileName_ ) )
    model_final.save( fileName_ )

