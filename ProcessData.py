import os
from processing import *
from random_experiment import get_systematics_vs_xi_h5
import ROOT

class ProcessData:
    def __init__( self, labels, fileNames, random_protons=False, mix_protons=False, runOnMC=False ):
        self.labels_ = labels
        self.fileNames_ = fileNames
        self.random_protons_ = random_protons 
        self.mix_protons_ = mix_protons
        self.runOnMC_ = runOnMC
        self.data_periods_ = [ "2017B", "2017C1", "2017C2", "2017D", "2017E", "2017F1", "2017F2", "2017F3" ]

        self.jecPars_ = None
        self.jecUncertainty_ = None
        self.systematics_Xi_X_, self.systematics_Xi_Y_ = 2 * [ None ]
        if self.runOnMC_:
            cmssw_release_base_ = os.environ[ 'CMSSW_RELEASE_BASE' ]
            print ( cmssw_release_base_ )
            cmssw_base_ = os.environ[ 'CMSSW_BASE' ]
            print( cmssw_base_ )

            libraries_ = ROOT.gSystem.GetLibraries().split()
            found_ = False
            for item in libraries_:
                if item.find( "libCondFormatsJetMETObjects.so" ) >= 0: found_ = True

            if not found_:
                lib_path_ = cmssw_release_base_ + "/lib/slc7_amd64_gcc900/libCondFormatsJetMETObjects.so"
                print ( "Loading {}".format( lib_path_ ) )
                ROOT.gSystem.Load( lib_path_ )

            self.jecPars_ = ROOT.JetCorrectorParameters( cmssw_base_ + "/src/PhysicsTools/NanoAODTools/data/jme/" + "Fall17_17Nov2017_V32_MC_Uncertainty_AK8PFchs.txt" )
            print ( self.jecPars_ )
            self.jecUncertainty_ = ROOT.JetCorrectionUncertainty( self.jecPars_ )
            print ( self.jecUncertainty_ )

            self.systematics_Xi_X_, self.systematics_Xi_Y_ = get_systematics_vs_xi_h5(
                data_periods=self.data_periods_,
                fileName="reco_characteristics/reco_characteristics_version1.h5"
                )

    def getJetUncertainty( self, jet_eta, jet_pt ):
        self.jecUncertainty_.setJetEta( jet_eta )
        self.jecUncertainty_.setJetPt( jet_pt )
        unc_ = self.jecUncertainty_.getUncertainty(True)
        return unc_

    def getSigmaXi( self, df ):
        df__ = df[ [ 'period', 'random', 'arm', 'xi' ] ]
        msk_random_ = ( df__.loc[ :, "random" ] == 0 )
        print ( msk_random_, np.sum( msk_random_ ) )
        sigma_var_ = np.zeros( df__.shape[0] ) 
        var_ = 'xi'
        # f_low_edge_ = lambda row: np.invert( self.systematics_Xi_X_[ row[ "period" ] ][ row[ "arm" ] ] <= row[ var_ ] ).argmax() - 1
        # f_high_edge_ = lambda row: ( self.systematics_Xi_X_[ row[ "period" ] ][ row[ "arm" ] ] >= row[ var_ ] ).argmax()
        f_low_edge_ = lambda row: np.invert( self.systematics_Xi_X_[ row[ "period" ] ][ row[ "arm" ] ] <= row[ var_ ] ).argmax() - 1
        f_high_edge_ = lambda row: ( self.systematics_Xi_X_[ row[ "period" ] ][ row[ "arm" ] ] > row[ var_ ] ).argmax()
        if np.sum( msk_random_ ) > 0:
            sigma_var_[ msk_random_ ] = df__.loc[ msk_random_ ].apply(
                lambda row:
                    ( ( self.systematics_Xi_Y_[ row[ "period" ] ][ row[ "arm" ] ][ f_high_edge_( row ) ] -
                        self.systematics_Xi_Y_[ row[ "period" ] ][ row[ "arm" ] ][ f_low_edge_( row ) ] ) /
                      ( self.systematics_Xi_X_[ row[ "period" ] ][ row[ "arm" ] ][ f_high_edge_( row ) ] -
                        self.systematics_Xi_X_[ row[ "period" ] ][ row[ "arm" ] ][ f_low_edge_( row ) ] ) *
                      ( row[ var_ ] - self.systematics_Xi_X_[ row[ "period" ] ][ row[ "arm" ] ][ f_low_edge_( row ) ] ) +
                        self.systematics_Xi_Y_[ row[ "period" ] ][ row[ "arm" ] ][ f_low_edge_( row ) ] ),
                axis=1 ).values 
        print ( sigma_var_, sigma_var_.size )
        return sigma_var_

    def fetchDataPeriod( self, df ):
        run_str_ = "run"
        if self.random_protons_ or self.mix_protons_:
            run_str_ = "run_rnd"
        elif self.runOnMC_ and not self.mix_protons_:
            run_str_ = "run_mc"

        if "period" not in df.columns:
            df.loc[ :, "period" ] = np.nan
            for idx_ in range( df_run_ranges.shape[0] ):
                msk_period_ = ( ( df.loc[ :, run_str_ ] >= df_run_ranges.iloc[ idx_ ][ "min" ] ) & ( df.loc[ :, run_str_ ] <= df_run_ranges.iloc[ idx_ ][ "max" ] ) )
                sum_period_ = np.sum( msk_period_ )
                if sum_period_ > 0:
                    period_key_ = df_run_ranges.index[ idx_ ]
                    df.loc[ :, "period" ].loc[ msk_period_ ] = period_key_
                    print ( "{}: {}".format( period_key_, sum_period_ ) )
            print ( df.loc[ :, "period" ] )

    def calculateXiSmeared( self, df ):
        # Gaussian shift
        sigma_xi_ = self.getSigmaXi( df )
        df_arr_xi_ = df.loc[ :, "xi" ]
        smeared_xi_arr_ = df_arr_xi_.values + ( 0. + np.random.randn( df_arr_xi_.size ) * sigma_xi_ )
        print ( smeared_var_arr_, smeared_var_arr_.size )
        df.loc[ :, "sigma_xi" ] = sigma_xi_
        df.loc[ :, "xi_smeared" ] = smeared_xi_arr_

    def calculateJets( self, df ):
        label_ = "_nom"
        df.loc[ :, "jet0_pt" + label_ ]       = df.loc[ :, "jet0_pt" ]
        df.loc[ :, "jet0_energy" + label_ ]   = df.loc[ :, "jet0_energy" ]
        df.loc[ :, "jet0_mass" + label_ ]     = df.loc[ :, "jet0_mass" ]
        df.loc[ :, "jet0_corrmass" + label_ ] = df.loc[ :, "jet0_corrmass" ]
        df.loc[ :, "jet0_px" + label_ ]       = ( df.loc[ :, "jet0_pt" + label_ ] * np.cos( df.loc[ :, "jet0_phi" ] ) )
        df.loc[ :, "jet0_py" + label_ ]       = ( df.loc[ :, "jet0_pt" + label_ ] * np.sin( df.loc[ :, "jet0_phi" ] ) )
        df.loc[ :, "jet0_pz" + label_ ]       = ( df.loc[ :, "jet0_pt" + label_ ] * np.sinh( df.loc[ :, "jet0_eta" ] ) )
        if self.runOnMC_:
            label_ = "_jes_up"
            df.loc[ :, "jet0_pt" + label_ ]       = df.loc[ :, "jet0_pt" ] * ( 1. + df.loc[ :, "jet0_unc" ] ) 
            df.loc[ :, "jet0_energy" + label_ ]   = df.loc[ :, "jet0_energy" ] * ( 1. + df.loc[ :, "jet0_unc" ] ) 
            df.loc[ :, "jet0_mass" + label_ ]     = df.loc[ :, "jet0_mass" ] * ( 1. + df.loc[ :, "jet0_unc" ] )
            df.loc[ :, "jet0_corrmass" + label_ ] = df.loc[ :, "jet0_corrmass" ] * ( 1. + df.loc[ :, "jet0_unc" ] )
            df.loc[ :, "jet0_px" + label_ ]       = ( df.loc[ :, "jet0_pt" + label_ ] * np.cos( df.loc[ :, "jet0_phi" ] ) )
            df.loc[ :, "jet0_py" + label_ ]       = ( df.loc[ :, "jet0_pt" + label_ ] * np.sin( df.loc[ :, "jet0_phi" ] ) )
            df.loc[ :, "jet0_pz" + label_ ]       = ( df.loc[ :, "jet0_pt" + label_ ] * np.sinh( df.loc[ :, "jet0_eta" ] ) )
            label_ = "_jes_dw"
            df.loc[ :, "jet0_pt" + label_ ]       = df.loc[ :, "jet0_pt" ] * ( 1. - df.loc[ :, "jet0_unc" ] ) 
            df.loc[ :, "jet0_energy" + label_ ]   = df.loc[ :, "jet0_energy" ] * ( 1. - df.loc[ :, "jet0_unc" ] ) 
            df.loc[ :, "jet0_mass" + label_ ]     = df.loc[ :, "jet0_mass" ] * ( 1. - df.loc[ :, "jet0_unc" ] )
            df.loc[ :, "jet0_corrmass" + label_ ] = df.loc[ :, "jet0_corrmass" ] * ( 1. - df.loc[ :, "jet0_unc" ] )
            df.loc[ :, "jet0_px" + label_ ]       = ( df.loc[ :, "jet0_pt" + label_ ] * np.cos( df.loc[ :, "jet0_phi" ] ) )
            df.loc[ :, "jet0_py" + label_ ]       = ( df.loc[ :, "jet0_pt" + label_ ] * np.sin( df.loc[ :, "jet0_phi" ] ) )
            df.loc[ :, "jet0_pz" + label_ ]       = ( df.loc[ :, "jet0_pt" + label_ ] * np.sinh( df.loc[ :, "jet0_eta" ] ) )

    def calculateMuons( self, df ):
        label_ = "_nom"
        df.loc[ :, "muon0_pt" + label_ ]     = df.loc[ :, "muon0_pt" ]
        df.loc[ :, "muon0_energy" + label_ ] = df.loc[ :, "muon0_energy" ]
        df.loc[ :, "muon0_px" + label_ ]     = ( df.loc[ :, "muon0_pt" + label_ ] * np.cos( df.loc[ :, "muon0_phi" ] ) )
        df.loc[ :, "muon0_py" + label_ ]     = ( df.loc[ :, "muon0_pt" + label_ ] * np.sin( df.loc[ :, "muon0_phi" ] ) )
        df.loc[ :, "muon0_pz" + label_ ]     = ( df.loc[ :, "muon0_pt" + label_ ] * np.sinh( df.loc[ :, "muon0_eta" ] ) )
        if self.runOnMC_: pass

    def calculateWLep( self, df ):
        label_ = "_nom"
        df.loc[ :, "WLeptonicPt" + label_ ]  = df.loc[ :, "WLeptonicPt" ]
        df.loc[ :, "WLeptonicPx" + label_ ]  = ( df.loc[ :, "WLeptonicPt" + label_ ] * np.cos( df.loc[ :, "WLeptonicPhi" ] ) )
        df.loc[ :, "WLeptonicPy" + label_ ]  = ( df.loc[ :, "WLeptonicPt" + label_ ] * np.sin( df.loc[ :, "WLeptonicPhi" ] ) )
        df.loc[ :, "WLeptonicPz" + label_ ]  = ( df.loc[ :, "WLeptonicPt" + label_ ] * np.sinh( df.loc[ :, "WLeptonicEta" ] ) )
        df.loc[ :, "WLeptonicE" + label_ ]   = ( np.sqrt( ( df.loc[ :, "WLeptonicPt" + label_ ] * np.cosh( df.loc[ :, "WLeptonicEta" ] ) )**2 + df.loc[ :, "recoMWlep" ] **2 ) )
        df.loc[ :, "WLeptonicM" + label_ ]   = ( np.sqrt( df.loc[ :, "WLeptonicE" + label_ ]**2 -
                                                 df.loc[ :, "WLeptonicPx" + label_ ]**2 -
                                                 df.loc[ :, "WLeptonicPy" + label_ ]**2 -
                                                 df.loc[ :, "WLeptonicPz" + label_ ]**2 ) ) 
        if self.runOnMC_: pass

    def calculateWW( self, df ):
        label_ = "_nom"
        df.loc[ :, "WW_energy" + label_ ]  = ( df.loc[ :, "WLeptonicE" + label_ ] + df.loc[ :, "jet0_energy" + label_ ] )
        df.loc[ :, "WW_pz" + label_ ]      = ( df.loc[ :, "WLeptonicPz" + label_ ] + df.loc[ :, "jet0_pz" + label_ ] )
        df.loc[ :, "MWW" + label_ ]   = ( np.sqrt( ( df.loc[ :, "WW_energy" + label_ ] )**2 -
                                                   ( df.loc[ :, "WLeptonicPx" + label_ ] + df.loc[ :, "jet0_px" + label_ ] )**2 -
                                                   ( df.loc[ :, "WLeptonicPy" + label_ ] + df.loc[ :, "jet0_py" + label_ ] )**2 -
                                                   ( df.loc[ :, "WW_pz" + label_ ] )**2 ) )
        df.loc[ :, "YWW" + label_ ]   = ( 0.5 * np.log( ( df.loc[ :, "WW_energy" + label_ ] + df.loc[ :, "WW_pz" + label_ ] ) / ( df.loc[ :, "WW_energy" + label_ ] - df.loc[ :, "WW_pz" + label_ ] ) ) )
        if self.runOnMC_:
            label_ = "_jes_up"
            df.loc[ :, "WW_energy" + label_ ]  = ( df.loc[ :, "WLeptonicE" + "_nom" ] + df.loc[ :, "jet0_energy" + label_ ] )
            df.loc[ :, "WW_pz" + label_ ]      = ( df.loc[ :, "WLeptonicPz" + "_nom" ] + df.loc[ :, "jet0_pz" + label_ ] )
            df.loc[ :, "MWW" + label_ ]   = ( np.sqrt( ( df.loc[ :, "WW_energy" + "_nom" ] )**2 -
                                                       ( df.loc[ :, "WLeptonicPx" + "_nom" ] + df.loc[ :, "jet0_px" + label_ ] )**2 -
                                                       ( df.loc[ :, "WLeptonicPy" + "_nom" ] + df.loc[ :, "jet0_py" + label_ ] )**2 -
                                                       ( df.loc[ :, "WW_pz" + "_nom" ] )**2 ) )
            df.loc[ :, "YWW" + label_ ]   = ( 0.5 * np.log( ( df.loc[ :, "WW_energy" + label_ ] + df.loc[ :, "WW_pz" + label_ ] ) / ( df.loc[ :, "WW_energy" + label_ ] - df.loc[ :, "WW_pz" + label_ ] ) ) )
            label_ = "_jes_dw"
            df.loc[ :, "WW_energy" + label_ ]  = ( df.loc[ :, "WLeptonicE" + "_nom" ] + df.loc[ :, "jet0_energy" + label_ ] )
            df.loc[ :, "WW_pz" + label_ ]      = ( df.loc[ :, "WLeptonicPz" + "_nom" ] + df.loc[ :, "jet0_pz" + label_ ] )
            df.loc[ :, "MWW" + label_ ]   = ( np.sqrt( ( df.loc[ :, "WW_energy" + "_nom" ] )**2 -
                                                       ( df.loc[ :, "WLeptonicPx" + "_nom" ] + df.loc[ :, "jet0_px" + label_ ] )**2 -
                                                       ( df.loc[ :, "WLeptonicPy" + "_nom" ] + df.loc[ :, "jet0_py" + label_ ] )**2 -
                                                       ( df.loc[ :, "WW_pz" + "_nom" ] )**2 ) )
            df.loc[ :, "YWW" + label_ ]   = ( 0.5 * np.log( ( df.loc[ :, "WW_energy" + label_ ] + df.loc[ :, "WW_pz" + label_ ] ) / ( df.loc[ :, "WW_energy" + label_ ] - df.loc[ :, "WW_pz" + label_ ] ) ) )

    def calculateXiCMS( self, df ):
        label_ = "_nom"
        df.loc[ :, "xiCMS_45" + label_ ] = ( 1. / 13000 ) * ( df.loc[ :, "WLeptonicPt" + "_nom" ] * np.exp( df.loc[ :, "WLeptonicEta" ] ) +
                                                              df.loc[ :, "jet0_pt" + "_nom" ] * np.exp( df.loc[ :, "jet0_eta" ] ) )
        df.loc[ :, "xiCMS_56" + label_ ] = ( 1. / 13000 ) * ( df.loc[ :, "WLeptonicPt" + "_nom" ] * np.exp( -df.loc[ :, "WLeptonicEta" ] ) +
                                                              df.loc[ :, "jet0_pt" + "_nom" ] * np.exp( -df.loc[ :, "jet0_eta" ] ) )
        if self.runOnMC_:
           label_ = "_jes_up"
           df.loc[ :, "xiCMS_45" + label_ ] = ( 1. / 13000 ) * ( df.loc[ :, "WLeptonicPt" + "_nom" ] * np.exp( df.loc[ :, "WLeptonicEta" ] ) +
                                                                 df.loc[ :, "jet0_pt" + label_ ] * np.exp( df.loc[ :, "jet0_eta" ] ) )
           df.loc[ :, "xiCMS_56" + label_ ] = ( 1. / 13000 ) * ( df.loc[ :, "WLeptonicPt" + "_nom" ] * np.exp( -df.loc[ :, "WLeptonicEta" ] ) +
                                                                 df.loc[ :, "jet0_pt" + label_ ] * np.exp( -df.loc[ :, "jet0_eta" ] ) )
           label_ = "_jes_dw"
           df.loc[ :, "xiCMS_45" + label_ ] = ( 1. / 13000 ) * ( df.loc[ :, "WLeptonicPt" + "_nom" ] * np.exp( df.loc[ :, "WLeptonicEta" ] ) +
                                                                 df.loc[ :, "jet0_pt" + label_ ] * np.exp( df.loc[ :, "jet0_eta" ] ) )
           df.loc[ :, "xiCMS_56" + label_ ] = ( 1. / 13000 ) * ( df.loc[ :, "WLeptonicPt" + "_nom" ] * np.exp( -df.loc[ :, "WLeptonicEta" ] ) +
                                                                 df.loc[ :, "jet0_pt" + label_ ] * np.exp( -df.loc[ :, "jet0_eta" ] ) )

    def calculateProtons( self, df ):
        df_arr_xi_ = df.loc[ :, "xi" ]
        df.loc[ :, "xi" + "_nom" ] = df_arr_xi_
        if self.runOnMC_:
           sigma_xi_ = self.getSigmaXi( df )
           # variations_ = [ 0.10, 0.30, 0.60, 1.0 ]
           # names_varplus_ = [ "_p10", "_p30", "_p60", "_p100" ]
           # names_varminus_ = [ "_m10", "_m30", "_m60", "_m100" ]
           variations_ = [ 1.0 ]
           names_varplus_ = [ "_p100" ]
           names_varminus_ = [ "_m100" ]
           for idx_, val_ in enumerate( variations_ ):
               df.loc[ :, "xi" + names_varplus_[ idx_ ] ] = df_arr_xi_ + val_ * sigma_xi_
               df.loc[ :, "xi" + names_varminus_[ idx_ ] ] = df_arr_xi_ - val_ * sigma_xi_
           df.loc[ :, "sigma_xi" ] = sigma_xi_

    def __call__( self, apply_fiducial=True, within_aperture=False, select_2protons=True ):

        df_counts = {}
        df_protons_multiRP_index = {}
        df_protons_multiRP_events = {}
        
        for label_ in self.labels_:
            import time
            print( time.strftime("%Y/%m/%d %H:%M:%S", time.localtime() ) )
            time_s_ = time.time()
        
            with pd.HDFStore( "reduced-data-store-{}.h5".format( label_ ), complevel=5 ) as store_:
        
                df_counts_, df_protons_multiRP_, df_protons_singleRP_, df_ppstracks_ = get_data( self.fileNames_[ label_ ] )

                self.fetchDataPeriod( df_protons_multiRP_ ) 

                if self.runOnMC_:
                    f_jecUncertainty_ = lambda row_: self.getJetUncertainty( row_[ "jet0_eta" ], row_[ "jet0_pt" ] )
                    df_protons_multiRP_.loc[ :, "jet0_unc" ] = df_protons_multiRP_[ [ "jet0_pt", "jet0_eta" ] ].apply( f_jecUncertainty_, axis=1 )
                    print ( df_protons_multiRP_.loc[ :, "jet0_unc" ] )
                    # df_protons_multiRP_.loc[ :, "jet0_pt_up" ] = df_protons_multiRP_.loc[ :, "jet0_pt" ] * ( 1. + df_protons_multiRP_.loc[ :, "jet0_unc" ] )
                    # df_protons_multiRP_.loc[ :, "jet0_pt_dw" ] = df_protons_multiRP_.loc[ :, "jet0_pt" ] * ( 1. - df_protons_multiRP_.loc[ :, "jet0_unc" ] )
                self.calculateJets( df_protons_multiRP_ )
                self.calculateMuons( df_protons_multiRP_ )
                self.calculateWLep( df_protons_multiRP_ )
                self.calculateWW( df_protons_multiRP_ )
                self.calculateXiCMS( df_protons_multiRP_ )

                self.calculateProtons( df_protons_multiRP_ )

                df_protons_multiRP_index_, df_protons_multiRP_events_, df_ppstracks_index_ = process_data_protons_multiRP(
                    df_protons_multiRP_, df_ppstracks_,
                    apply_fiducial=apply_fiducial,
                    within_aperture=within_aperture,
                    random_protons=self.random_protons_,
                    mix_protons=self.mix_protons_,
                    select_2protons=select_2protons,
                    runOnMC=self.runOnMC_
                    )

                store_[ "counts" ] = df_counts_
                store_[ "protons_multiRP"] = df_protons_multiRP_index_
                store_[ "events_multiRP" ] = df_protons_multiRP_events_
            
            time_e_ = time.time()
            print ( "Total time elapsed: {:.0f}".format( time_e_ - time_s_ ) )

            with pd.HDFStore( "reduced-data-store-{}.h5".format( label_ ), 'r' ) as store_:
                print ( list( store_ ) )
