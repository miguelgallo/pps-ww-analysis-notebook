#!/bin/bash

echo "2018 A0W1e-6"
combineCards.py muon_2018=datacard_counting_norm_to_1fb_muon-2018_sig-2018-muon-AQGC-A0W1e-6.txt electron_2018=datacard_counting_norm_to_1fb_electron-2018_sig-2018-electron-AQGC-A0W1e-6.txt  > datacard_counting_norm_to_1fb_2018-AQGC-A0W1e-6.txt

echo "2018 A0W2e-6"
combineCards.py muon_2018=datacard_counting_norm_to_1fb_muon-2018_sig-2018-muon-AQGC-A0W2e-6.txt electron_2018=datacard_counting_norm_to_1fb_electron-2018_sig-2018-electron-AQGC-A0W2e-6.txt  > datacard_counting_norm_to_1fb_2018-AQGC-A0W2e-6.txt

echo "2018 A0W5e-6"
combineCards.py muon_2018=datacard_counting_norm_to_1fb_muon-2018_sig-2018-muon-AQGC-A0W5e-6.txt electron_2018=datacard_counting_norm_to_1fb_electron-2018_sig-2018-electron-AQGC-A0W5e-6.txt  > datacard_counting_norm_to_1fb_2018-AQGC-A0W5e-6.txt
