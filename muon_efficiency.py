import numpy as np
import ROOT

class MuonScaleFactor:
    def __init__( self, histos ):
        self.h2D_MuID = histos[ "MuID" ]
    def __call__( self, pt, eta ):
        sf_ = 1.
        unc_ = 0.
        if pt < 120.:
            bin2D_ = self.h2D_MuID.FindBin( pt, np.abs( eta ) )
            sf_ = self.h2D_MuID.GetBinContent( bin2D_ )
            unc_ = self.h2D_MuID.GetBinError( bin2D_ )
        else:
            bin2D_ = self.h2D_MuID.FindBin( self.h2D_MuID.GetXaxis().GetBinCenter( self.h2D_MuID.GetNbinsX() ), np.abs( eta ) )
            sf_ = self.h2D_MuID.GetBinContent( bin2D_ )
            unc_ = self.h2D_MuID.GetBinError( bin2D_ )
        return ( sf_, unc_ )
