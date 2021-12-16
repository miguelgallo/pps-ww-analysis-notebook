import numpy as np
import ROOT

# class MuonScaleFactor:
#     def __init__( self, histos ):
#         self.h2D_MuID = histos[ "MuID" ]
#     def __call__( self, pt, eta ):
#         sf_ = 1.
#         unc_ = 0.
#         if pt < 120.:
#             bin2D_ = self.h2D_MuID.FindBin( pt, np.abs( eta ) )
#             sf_ = self.h2D_MuID.GetBinContent( bin2D_ )
#             unc_ = self.h2D_MuID.GetBinError( bin2D_ )
#         else:
#             bin2D_ = self.h2D_MuID.FindBin( self.h2D_MuID.GetXaxis().GetBinCenter( self.h2D_MuID.GetNbinsX() ), np.abs( eta ) )
#             sf_ = self.h2D_MuID.GetBinContent( bin2D_ )
#             unc_ = self.h2D_MuID.GetBinError( bin2D_ )
#         return ( sf_, unc_ )

class MuonScaleFactor:
    def __init__( self, histos, debug=False ):
        self.debug_ = debug
        self.h2D_MuID = histos[ "MuID" ]
        self.h2D_MuID_stat = histos[ "MuID_stat" ]
        self.h2D_MuID_syst = histos[ "MuID_syst" ]
    def __call__( self, pt, eta ):
        sf_ = 1.
        unc_ = 0.
        bin2D_ = None
        bin2D_stat_ = None
        bin2D_syst_ = None
        if pt < 120.:
            bin2D_ = self.h2D_MuID.FindBin( pt, np.abs( eta ) )
            bin2D_stat_ = self.h2D_MuID_stat.FindBin( pt, np.abs( eta ) )
            bin2D_syst_ = self.h2D_MuID_syst.FindBin( pt, np.abs( eta ) )
        else:
            bin2D_ = self.h2D_MuID.FindBin(
                self.h2D_MuID.GetXaxis().GetBinCenter( self.h2D_MuID.GetNbinsX() ), np.abs( eta ) )
            bin2D_stat_ = self.h2D_MuID_stat.FindBin(
                self.h2D_MuID_stat.GetXaxis().GetBinCenter( self.h2D_MuID_stat.GetNbinsX() ), np.abs( eta ) )
            bin2D_syst_ = self.h2D_MuID_syst.FindBin(
                self.h2D_MuID_syst.GetXaxis().GetBinCenter( self.h2D_MuID_syst.GetNbinsX() ), np.abs( eta ) )
        sf_ = self.h2D_MuID.GetBinContent( bin2D_ )
        err_stat_ = self.h2D_MuID_stat.GetBinError( bin2D_stat_ )
        err_syst_ = self.h2D_MuID_syst.GetBinError( bin2D_syst_ )
        unc_ = np.sqrt( err_stat_ ** 2 + err_syst_ ** 2 )
        if self.debug_:
            print ( bin2D_, bin2D_stat_, bin2D_syst_, sf_, err_stat_, err_syst_, unc_ )
        return ( sf_, unc_ )

