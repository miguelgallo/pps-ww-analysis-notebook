import ROOT
import os
cmssw_release_base_ = os.environ[ 'CMSSW_RELEASE_BASE' ]
print ( cmssw_release_base_ )
cmssw_base_ = os.environ[ 'CMSSW_BASE' ]
print( cmssw_base_ )
ROOT.gSystem.Load( cmssw_release_base_ + "/lib/slc7_amd64_gcc900/libCondFormatsJetMETObjects.so" )

jecPars = ROOT.JetCorrectorParameters( cmssw_base_ + "/src/PhysicsTools/NanoAODTools/data/jme/" + "Fall17_17Nov2017_V32_MC_Uncertainty_AK8PFchs.txt" )
print ( jecPars )
jecUncertainty = ROOT.JetCorrectionUncertainty( jecPars )
print ( jecUncertainty )

eta_ = -1.2
pt_  = 200.
jecUncertainty.setJetEta( eta_ )
jecUncertainty.setJetPt( pt_ )
unc_ = jecUncertainty.getUncertainty(True)
print ( eta_, pt_ )
print ( pt_, pt_ * ( 1. + unc_ ), pt_ * ( 1. - unc_ ) )
