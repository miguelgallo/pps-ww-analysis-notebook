#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd
import h5py
from joblib import dump, load

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier

# run_ranges_periods, df_run_ranges, fiducial_cuts, fiducial_cuts_all, aperture_period_map, aperture_parametrisation, check_aperture, get_data, process_data_protons_multiRP
from processing import *

run_tables = False
train_model = True
run_grid_search = True
save_model = True
n_iter_search_ = 30
label_ = "test-multiRP"
base_path_ = "/eos/home-a/antoniov/SWAN_projects/pps-ww-analysis"

n_events_signal = None
#n_events_bkg = None
n_events_bkg = 100000

prob_cut_ = 0.40

label_signal = "GGToWW-AQGC-test-A0W1e-6"
fileNames_signal = [
    "output-GGToWW-AQGC-test-A0W1e-6.h5"
]

resample_factor = 20
label_bkg = "data-random-resample_20"
fileNames_bkg = [
    "output-data-random-resample_20-test-2017B.h5",
    "output-data-random-resample_20-test-2017C.h5",
    "output-data-random-resample_20-test-2017D.h5",
    "output-data-random-resample_20-test-2017E.h5",
    "output-data-random-resample_20-test-2017F.h5"
]

# Signal
df_counts_signal, df_protons_multiRP_signal, df_protons_singleRP_signal, df_ppstracks_signal = 4 * [None]
df_protons_multiRP_signal_index, df_protons_multiRP_signal_events, df_ppstracks_signal_index = 3 * [None]

fileName_ = "{}/reduced-data-store-{}.h5".format( base_path_, label_signal )
if run_tables:
    print ( fileName_ )
    with pd.HDFStore( fileName_, complevel=5 ) as store_:

        df_counts_signal, df_protons_multiRP_signal, df_protons_singleRP_signal, df_ppstracks_signal = get_data( fileNames_signal )
        df_protons_multiRP_signal_index, df_protons_multiRP_signal_events, df_ppstracks_signal_index = process_data_protons_multiRP( df_protons_multiRP_signal, df_ppstracks_signal, apply_fiducial=True, runOnMC=True )

        store_[ "counts" ] = df_counts_signal
        store_[ "protons_multiRP"] = df_protons_multiRP_signal_index
        store_[ "events_multiRP" ] = df_protons_multiRP_signal_events
else:
    with pd.HDFStore( fileName_, 'r' ) as store_:
        df_counts_signal = store_[ "counts" ]
        df_protons_multiRP_signal_index = store_[ "protons_multiRP" ]
        df_protons_multiRP_signal_events = store_[ "events_multiRP" ]
df_protons_multiRP_signal_index[:20]
df_protons_multiRP_signal_events[:20]

# Background

df_counts_bkg, df_protons_multiRP_bkg, df_protons_singleRP_bkg, df_ppstracks_bkg = 4 * [None]
df_protons_multiRP_bkg_index, df_protons_multiRP_bkg_events, df_ppstracks_bkg_index = 3 * [None]

fileName_ = "{}/reduced-data-store-{}.h5".format( base_path_, label_bkg )
if run_tables:
    print ( fileName_ )
    with pd.HDFStore( fileName_, complevel=5 ) as store_:

        df_counts_bkg, df_protons_multiRP_bkg, df_protons_singleRP_bkg, df_ppstracks_bkg = get_data( fileNames_bkg )
        df_protons_multiRP_bkg_index, df_protons_multiRP_bkg_events, df_ppstracks_bkg_index = process_data_protons_multiRP( df_protons_multiRP_bkg, df_ppstracks_bkg, apply_fiducial=True, within_aperture=True, runOnMC=False )

        store_[ "counts" ] = df_counts_bkg
        store_[ "protons_multiRP"] = df_protons_multiRP_bkg_index
        store_[ "events_multiRP" ] = df_protons_multiRP_bkg_events
else:
    with pd.HDFStore( fileName_, 'r' ) as store_:
        df_counts_bkg = store_[ "counts" ]
        df_protons_multiRP_bkg_index = store_[ "protons_multiRP" ]
        df_protons_multiRP_bkg_events = store_[ "events_multiRP" ]
df_protons_multiRP_bkg_index[:20]
df_protons_multiRP_bkg_events[:20]

# Select variables

msk_bkg = ( ( df_protons_multiRP_bkg_events.loc[ :, "jet0_corrmass"] >= 50.0 ) & ( df_protons_multiRP_bkg_events.loc[ :, "jet0_corrmass"] <= 110.0 ) )
msk_signal = ( ( df_protons_multiRP_signal_events.loc[ :, "jet0_corrmass"] >= 50.0 ) & ( df_protons_multiRP_signal_events.loc[ :, "jet0_corrmass"] <= 110.0 ) )
df_protons_multiRP_bkg_events = df_protons_multiRP_bkg_events.loc[ msk_bkg ]
df_protons_multiRP_signal_events = df_protons_multiRP_signal_events.loc[ msk_signal ]

# variables_ = [ 'jet0_pt', 'jet0_phi', 'jet0_tau1', 'jet0_tau2', 'muon0_pt', 'muon0_phi', 'met', 'met_phi',
#                'pfcand_nextracks', 'WLeptonicPt', 'WLeptonicPhi', 'recoMWW', 'recoRapidityWW' ]
variables_ = [ 'jet0_pt', 'jet0_phi', 'jet0_tau1', 'jet0_tau2', 'muon0_pt', 'muon0_phi', 'met', 'met_phi',
               'pfcand_nextracks', 'WLeptonicPt', 'WLeptonicPhi', 'recoMWW', 'recoRapidityWW', 'MX', 'YX' ]

if n_events_signal:
    X_sig = df_protons_multiRP_signal_events[ variables_ ].iloc[:n_events_signal]
else:
    X_sig = df_protons_multiRP_signal_events[ variables_ ]
print ( X_sig.shape )
print ( X_sig[:20] )

if n_events_bkg:
    X_bkg = df_protons_multiRP_bkg_events[ variables_ ].iloc[:n_events_bkg]
else:
    X_bkg = df_protons_multiRP_bkg_events[ variables_ ]
print ( X_bkg.shape )
print ( X_bkg[:20] )

y_sig = np.ones( len(X_sig) )
y_bkg = np.zeros( len(X_bkg) )

X = pd.concat( [X_sig, X_bkg] ) 
y = np.concatenate( [y_sig, y_bkg] )

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.2, shuffle=True, random_state=42 )

# Hyperparameter scan

grid_search = None
if train_model and run_grid_search:
    from sklearn.model_selection import RandomizedSearchCV
    #from sklearn.model_selection import GridSearchCV
    #from scipy.stats import uniform

    param_distribs = {
        "base_estimator__max_depth": np.arange(2,9),
        "base_estimator__min_samples_split": np.arange(2,9),
        "n_estimators": 100 * np.arange(2,6),
        "learning_rate": 0.1 * np.arange(4,11)
        }
    #param_grid = [
    #    { "max_depth": np.arange(2,10),
    #      "n_estimators": 100 * np.arange(1,6),
    #      "learning_rate": 0.1 * np.arange(5,11) }
    #    ]

    grid_search = RandomizedSearchCV(
        AdaBoostClassifier(
            DecisionTreeClassifier(),
            algorithm="SAMME.R"
            ),
        param_distribs,
        n_iter=n_iter_search_, cv=4, verbose=20, n_jobs=-1, random_state=42
        )
    grid_search.fit( X_train, y_train )

    print ( grid_search.best_params_ )
    print ( grid_search.best_score_ )
    print ( grid_search.cv_results_ )

# Build model

model_final = None

if train_model:
    if run_grid_search: 
        print ( grid_search.best_estimator_)
        model_final = grid_search.best_estimator_
    else:
        model_final = AdaBoostClassifier(
                DecisionTreeClassifier(
                    max_depth=4,
                    min_samples_split=5
                ),
                n_estimators = 400,
                algorithm="SAMME.R",
                learning_rate = 0.4
                )
        model_final.fit( X_train, y_train )
else:
    model_final = load( "model/ada_clf.joblib" )
    
print ( model_final )

# Evaluate on test data

y_test_proba = model_final.predict_proba( X_test )[:,1]
print ( y_test_proba )

print ( "Prob. cut: {}".format( prob_cut_ ) )

y_test_pred = ( y_test_proba >= prob_cut_ ).astype( "int32" )
print ( y_test_pred )

from sklearn.metrics import accuracy_score
print ( accuracy_score( y_test, y_test_pred ) )
print ( accuracy_score( y_test[ y_test == 1 ], y_test_pred[ y_test == 1 ] ) )
print ( accuracy_score( y_test[ y_test == 0 ], y_test_pred[ y_test == 0 ] ) )

test_errors = []
for test_predict_proba in model_final.staged_predict_proba( X_test ):
    test_errors.append( 1. - accuracy_score( ( test_predict_proba[:,1] >= prob_cut_ ), y_test ) )

n_trees = len( model_final )

estimator_errors = model_final.estimator_errors_[:n_trees]

print ( test_errors )
print ( estimator_errors )

# Save model

if train_model and save_model:
    import time
    id_ = time.strftime("%Y_%m_%d-%H_%M_%S")
    fileName_ = "adaboost_clf_{}_{}.joblib".format( label_, id_ )
    print ( "Saving model to {}".format( fileName_ ) )
    dump( model_final, fileName_ )

