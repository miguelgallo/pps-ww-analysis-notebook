import ROOT
import os
cmssw_release_base_ = os.environ[ 'CMSSW_RELEASE_BASE' ]
print ( cmssw_release_base_ )
cmssw_base_ = os.environ[ 'CMSSW_BASE' ]
print( cmssw_base_ )

if "/RoccoR_cc.so" not in ROOT.gSystem.GetLibraries():
    path_ = 'muon_scale/RoccoR/RoccoR.cc'
    print ( "Loading C++ helper from " + path_ )
    ROOT.gROOT.ProcessLine('.L ' + path_)

roccor_ = ROOT.RoccoR( "muon_scale/RoccoR/RoccoR2017.txt" )
print ( roccor_ )

# eta_ = 1.2
# pt_  = 50.
