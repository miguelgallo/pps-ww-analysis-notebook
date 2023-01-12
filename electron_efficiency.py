import numpy as np
import ROOT

# class ElectronScaleFactor:
#     def __init__( self, histos ):
#         self.h2D_EleID = histos[ "EleID" ]
#     def __call__( self, pt, eta ):
#         sf_ = 1.
#         unc_ = 0.
#         bin2D_ = None
#         if pt < 500.:
#             bin2D_ = self.h2D_EleID.FindBin( eta, pt )
#         else:
#             bin2D_ = self.h2D_EleID.FindBin( eta, self.h2D_EleID.GetYaxis().GetBinCenter( self.h2D_EleID.GetNbinsY() ) )
#         sf_ = self.h2D_EleID.GetBinContent( bin2D_ )
#         unc_ = self.h2D_EleID.GetBinError( bin2D_ )
#         return ( sf_, unc_ )

# class ElectronScaleFactor:
#     def __init__( self, histos ):
#         self.h2D_EleID = histos[ "EleID" ]
#         self.ptmax_ = 500.
#     def __call__( self, eta, pt ):
#         sf_ = 1.
#         unc_ = 0.
#         bin2D_ = None
#         if pt < self.ptmax_:
#             bin2D_ = self.h2D_EleID.FindBin( eta, pt )
#         else:
#             bin2D_ = self.h2D_EleID.FindBin( eta, self.h2D_EleID.GetYaxis().GetBinCenter( self.h2D_EleID.GetNbinsY() ) )
#         sf_ = self.h2D_EleID.GetBinContent( bin2D_ )
#         unc_ = self.h2D_EleID.GetBinError( bin2D_ )
#         return ( sf_, unc_ )

class ElectronIDScaleFactor:
    def __init__( self, histos, debug=False ):
        self.debug_ = debug
        self.h2D_EleID = histos[ "EleID" ]
        #self.h2D_EleID_stat = histos[ "EleID_stat" ]
        #self.h2D_EleID_syst = histos[ "EleID_syst" ]
        self.ptmax_ = 500.
    def __call__( self, eta, pt ):
        sf_ = 1.
        unc_ = 0.
        bin2D_ = None
        #bin2D_stat_ = None
        #bin2D_syst_ = None
        if pt < self.ptmax_:
            bin2D_ = self.h2D_EleID.FindBin( eta, pt )
            #bin2D_stat_ = self.h2D_EleID_stat.FindBin( eta, pt )
            #bin2D_syst_ = self.h2D_EleID_syst.FindBin( eta, pt )
        else:
            bin2D_ = self.h2D_EleID.FindBin(
                eta,
                self.h2D_EleID.GetYaxis().GetBinCenter( self.h2D_EleID.GetNbinsY() ) )
            #bin2D_stat_ = self.h2D_EleID_stat.FindBin(
            #    eta,
            #    self.h2D_EleID_stat.GetYaxis().GetBinCenter( self.h2D_EleID_stat.GetNbinsY() ) )
            #bin2D_syst_ = self.h2D_EleID_syst.FindBin(
            #    eta,
            #    self.h2D_EleID_syst.GetYaxis().GetBinCenter( self.h2D_EleID_syst.GetNbinsY() ) )
        sf_ = self.h2D_EleID.GetBinContent( bin2D_ )
        #err_stat_ = self.h2D_EleID_stat.GetBinError( bin2D_stat_ )
        #err_syst_ = self.h2D_EleID_syst.GetBinError( bin2D_syst_ )
        #unc_ = np.sqrt( err_stat_ ** 2 + err_syst_ ** 2 )
        unc_ = self.h2D_EleID.GetBinError( bin2D_ )
        if self.debug_:
            #print ( bin2D_, bin2D_stat_, bin2D_syst_, sf_, err_stat_, err_syst_, unc_ )
            print ( bin2D_, sf_, unc_ )
        return ( sf_, unc_ )

class ElectronTRGScaleFactor:
    def __init__( self, histos, debug=False ):
        self.debug_ = debug
        self.h2D_EleTRG = histos[ "EleTRG" ]
        #self.h2D_EleTRG_stat = histos[ "EleTRG_stat" ]
        #self.h2D_EleTRG_syst = histos[ "EleTRG_syst" ]
        self.ptmax_ = 500.
    def __call__( self, eta, pt ):
        sf_ = 1.
        unc_ = 0.
        bin2D_ = None
        #bin2D_stat_ = None
        #bin2D_syst_ = None
        if pt < self.ptmax_:
            bin2D_ = self.h2D_EleTRG.FindBin( eta, pt )
            #bin2D_stat_ = self.h2D_EleTRG_stat.FindBin( eta, pt )
            #bin2D_syst_ = self.h2D_EleTRG_syst.FindBin( eta, pt )
        else:
            bin2D_ = self.h2D_EleTRG.FindBin(
                eta,
                self.h2D_EleTRG.GetYaxis().GetBinCenter( self.h2D_EleTRG.GetNbinsY() ) )
            #bin2D_stat_ = self.h2D_EleTRG_stat.FindBin(
            #    eta,
            #    self.h2D_EleTRG_stat.GetYaxis().GetBinCenter( self.h2D_EleTRG_stat.GetNbinsY() ) )
            #bin2D_syst_ = self.h2D_EleTRG_syst.FindBin(
            #    eta,
            #    self.h2D_EleTRG_syst.GetYaxis().GetBinCenter( self.h2D_EleTRG_syst.GetNbinsY() ) )
        sf_ = self.h2D_EleTRG.GetBinContent( bin2D_ )
        #err_stat_ = self.h2D_EleTRG_stat.GetBinError( bin2D_stat_ )
        #err_syst_ = self.h2D_EleTRG_syst.GetBinError( bin2D_syst_ )
        #unc_ = np.sqrt( err_stat_ ** 2 + err_syst_ ** 2 )
        unc_ = self.h2D_EleTRG.GetBinError( bin2D_ )
        if self.debug_:
            print ( bin2D_, sf_, unc_ )
        return ( sf_, unc_ )
