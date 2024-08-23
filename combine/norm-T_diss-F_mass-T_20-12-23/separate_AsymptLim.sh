combine -M AsymptoticLimits datacard_counting_norm_to_1fb-mass_cut_electron-2018_sig-2018-electron-AQGC-A0W1e-7.txt --run blind --name electron_a0W1e7 -m 1
combine -M AsymptoticLimits datacard_counting_norm_to_1fb-mass_cut_electron-2018_sig-2018-electron-AQGC-A0W2e-7.txt --run blind --name electron_a0W2e7 -m 2
combine -M AsymptoticLimits datacard_counting_norm_to_1fb-mass_cut_electron-2018_sig-2018-electron-AQGC-A0W1e-6.txt --run blind --name electron_a0W1e6 -m 10
combine -M AsymptoticLimits datacard_counting_norm_to_1fb-mass_cut_electron-2018_sig-2018-electron-AQGC-A0W2e-6.txt --run blind --name electron_a0W2e6 -m 20
combine -M AsymptoticLimits datacard_counting_norm_to_1fb-mass_cut_electron-2018_sig-2018-electron-AQGC-A0W5e-6.txt --run blind --name electron_a0W5e6 -m 50
combine -M AsymptoticLimits datacard_counting_norm_to_1fb-mass_cut_electron-2018_sig-2018-electron-AQGC-ACW5e-7.txt --run blind --name electron_aCW5e7 -m 5
combine -M AsymptoticLimits datacard_counting_norm_to_1fb-mass_cut_electron-2018_sig-2018-electron-AQGC-ACW5e-6.txt --run blind --name electron_aCW5e6 -m 50
combine -M AsymptoticLimits datacard_counting_norm_to_1fb-mass_cut_electron-2018_sig-2018-electron-AQGC-ACW8e-6.txt --run blind --name electron_aCW8e6 -m 80
combine -M AsymptoticLimits datacard_counting_norm_to_1fb-mass_cut_electron-2018_sig-2018-electron-AQGC-ACW2e-5.txt --run blind --name electron_aCW2e5 -m 200
combine -M AsymptoticLimits datacard_counting_norm_to_1fb-mass_cut_muon-2018_sig-2018-muon-AQGC-A0W1e-7.txt --run blind --name muon_a0W1e7 -m 1
combine -M AsymptoticLimits datacard_counting_norm_to_1fb-mass_cut_muon-2018_sig-2018-muon-AQGC-A0W2e-7.txt --run blind --name muon_a0W2e7 -m 2
combine -M AsymptoticLimits datacard_counting_norm_to_1fb-mass_cut_muon-2018_sig-2018-muon-AQGC-A0W1e-6.txt --run blind --name muon_a0W1e6 -m 10
combine -M AsymptoticLimits datacard_counting_norm_to_1fb-mass_cut_muon-2018_sig-2018-muon-AQGC-A0W2e-6.txt --run blind --name muon_a0W2e6 -m 20
combine -M AsymptoticLimits datacard_counting_norm_to_1fb-mass_cut_muon-2018_sig-2018-muon-AQGC-A0W5e-6.txt --run blind --name muon_a0W5e6 -m 50
combine -M AsymptoticLimits datacard_counting_norm_to_1fb-mass_cut_muon-2018_sig-2018-muon-AQGC-ACW5e-7.txt --run blind --name muon_aCW5e7 -m 5
combine -M AsymptoticLimits datacard_counting_norm_to_1fb-mass_cut_muon-2018_sig-2018-muon-AQGC-ACW5e-6.txt --run blind --name muon_aCW5e6 -m 50
combine -M AsymptoticLimits datacard_counting_norm_to_1fb-mass_cut_muon-2018_sig-2018-muon-AQGC-ACW8e-6.txt --run blind --name muon_aCW8e6 -m 80
combine -M AsymptoticLimits datacard_counting_norm_to_1fb-mass_cut_muon-2018_sig-2018-muon-AQGC-ACW2e-5.txt --run blind --name muon_aCW2e5 -m 200
combineTool.py -M CollectLimits *electron_a0W*AsymptoticLimits* --use-dirs -o limits.json; mv limits_default.json limits_electron_a0W.json
combineTool.py -M CollectLimits *electron_aCW*AsymptoticLimits* --use-dirs -o limits.json; mv limits_default.json limits_electron_aCW.json
combineTool.py -M CollectLimits *muon_a0W*AsymptoticLimits* --use-dirs -o limits.json; mv limits_default.json limits_muon_a0W.json
combineTool.py -M CollectLimits *muon_aCW*AsymptoticLimits* --use-dirs -o limits.json; mv limits_default.json limits_muon_aCW.json
python plotLimitsAQGC.py limits_electron_a0W.json --show exp --logy --x-title '|a^{W}_{0}/#Lambda^{2} (#times 10^{-7} GeV^{-2})|'; mv limit.png limit_electron_a0W.png; mv limit.pdf limit_electron_a0W.pdf
python plotLimitsAQGC.py limits_electron_aCW.json --show exp --logy --x-title '|a^{W}_{C}/#Lambda^{2} (#times 10^{-7} GeV^{-2})|'; mv limit.png limit_electron_aCW.png; mv limit.pdf limit_electron_aCW.pdf
python plotLimitsAQGC.py limits_muon_a0W.json --show exp --logy --x-title '|a^{W}_{0}/#Lambda^{2} (#times 10^{-7} GeV^{-2})|'; mv limit.png limit_muon_a0W.png; mv limit.pdf limit_muon_a0W.pdf
python plotLimitsAQGC.py limits_muon_aCW.json --show exp --logy --x-title '|a^{W}_{C}/#Lambda^{2} (#times 10^{-7} GeV^{-2})|'; mv limit.png limit_muon_aCW.png; mv limit.pdf limit_muon_aCW.pdf
