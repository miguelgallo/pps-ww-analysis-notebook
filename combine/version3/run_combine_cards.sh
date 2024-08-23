#!/bin/bash

echo "2017 A0W1e-6"
combineCards.py muon_2017=datacard_counting_muon-2017_sig-2017-muon-AQGC-A0W1e-6.txt electron_2017=datacard_counting_electron-2017_sig-2017-electron-AQGC-A0W1e-6.txt  > datacard_counting_2017-AQGC-A0W1e-6.txt

echo "2017 A0W2e-6"
combineCards.py muon_2017=datacard_counting_muon-2017_sig-2017-muon-AQGC-A0W2e-6.txt electron_2017=datacard_counting_electron-2017_sig-2017-electron-AQGC-A0W2e-6.txt  > datacard_counting_2017-AQGC-A0W2e-6.txt

echo "2017 A0W5e-6"
combineCards.py muon_2017=datacard_counting_muon-2017_sig-2017-muon-AQGC-A0W5e-6.txt electron_2017=datacard_counting_electron-2017_sig-2017-electron-AQGC-A0W5e-6.txt  > datacard_counting_2017-AQGC-A0W5e-6.txt

echo "2018 A0W5e-7"
combineCards.py muon_2018=datacard_counting_muon-2018_sig-2018-muon-AQGC-A0W5e-7.txt electron_2018=datacard_counting_electron-2018_sig-2018-electron-AQGC-A0W5e-7.txt  > datacard_counting_2018-AQGC-A0W5e-7.txt

echo "2018 A0W1e-6"
combineCards.py muon_2018=datacard_counting_muon-2018_sig-2018-muon-AQGC-A0W1e-6.txt electron_2018=datacard_counting_electron-2018_sig-2018-electron-AQGC-A0W1e-6.txt  > datacard_counting_2018-AQGC-A0W1e-6.txt

echo "2018 A0W2e-6"
combineCards.py muon_2018=datacard_counting_muon-2018_sig-2018-muon-AQGC-A0W2e-6.txt electron_2018=datacard_counting_electron-2018_sig-2018-electron-AQGC-A0W2e-6.txt  > datacard_counting_2018-AQGC-A0W2e-6.txt

echo "2018 A0W5e-6"
combineCards.py muon_2018=datacard_counting_muon-2018_sig-2018-muon-AQGC-A0W5e-6.txt electron_2018=datacard_counting_electron-2018_sig-2018-electron-AQGC-A0W5e-6.txt  > datacard_counting_2018-AQGC-A0W5e-6.txt

echo "2017-2018 A0W1e-6"
combineCards.py muon_2017=datacard_counting_muon-2017_sig-2017-muon-AQGC-A0W1e-6.txt electron_2017=datacard_counting_electron-2017_sig-2017-electron-AQGC-A0W1e-6.txt muon_2018=datacard_counting_muon-2018_sig-2018-muon-AQGC-A0W1e-6.txt electron_2018=datacard_counting_electron-2018_sig-2018-electron-AQGC-A0W1e-6.txt  > datacard_counting_2017-2018-AQGC-A0W1e-6.txt

echo "2017-2018 A0W2e-6"
combineCards.py muon_2017=datacard_counting_muon-2017_sig-2017-muon-AQGC-A0W2e-6.txt electron_2017=datacard_counting_electron-2017_sig-2017-electron-AQGC-A0W2e-6.txt muon_2018=datacard_counting_muon-2018_sig-2018-muon-AQGC-A0W2e-6.txt electron_2018=datacard_counting_electron-2018_sig-2018-electron-AQGC-A0W2e-6.txt  > datacard_counting_2017-2018-AQGC-A0W2e-6.txt

echo "2017-2018 A0W5e-6"
combineCards.py muon_2017=datacard_counting_muon-2017_sig-2017-muon-AQGC-A0W5e-6.txt electron_2017=datacard_counting_electron-2017_sig-2017-electron-AQGC-A0W5e-6.txt muon_2018=datacard_counting_muon-2018_sig-2018-muon-AQGC-A0W5e-6.txt electron_2018=datacard_counting_electron-2018_sig-2018-electron-AQGC-A0W5e-6.txt  > datacard_counting_2017-2018-AQGC-A0W5e-6.txt
