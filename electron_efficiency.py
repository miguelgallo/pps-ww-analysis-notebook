import numpy as np
import ROOT

class ElectronScaleFactor:
    def __init__( self, histos ):
        self.h2D_EleID = histos[ "EleID" ]
    def __call__( self, pt, eta ):
        sf_ = 1.
        unc_ = 0.
        bin2D_ = None
        if pt < 500.:
            bin2D_ = self.h2D_EleID.FindBin( eta, pt )
        else:
            bin2D_ = self.h2D_EleID.FindBin( eta, self.h2D_EleID.GetYaxis().GetBinCenter( self.h2D_EleID.GetNbinsY() ) )
        sf_ = self.h2D_EleID.GetBinContent( bin2D_ )
        unc_ = self.h2D_EleID.GetBinError( bin2D_ )
        return ( sf_, unc_ )
