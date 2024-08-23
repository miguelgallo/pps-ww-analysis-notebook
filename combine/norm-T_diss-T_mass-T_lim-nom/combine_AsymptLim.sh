combine -M AsymptoticLimits datacard_counting_2018-AQGC-A0W1e-7.txt --run blind --name a0W1e7 -m 1
combine -M AsymptoticLimits datacard_counting_2018-AQGC-A0W2e-7.txt --run blind --name a0W2e7 -m 2
combine -M AsymptoticLimits datacard_counting_2018-AQGC-A0W5e-7.txt --run blind --name a0W5e7 -m 5
combine -M AsymptoticLimits datacard_counting_2018-AQGC-A0W1e-6.txt --run blind --name a0W1e6 -m 10
combine -M AsymptoticLimits datacard_counting_2018-AQGC-A0W2e-6.txt --run blind --name a0W2e6 -m 20
combine -M AsymptoticLimits datacard_counting_2018-AQGC-A0W5e-6.txt --run blind --name a0W5e6 -m 50
combine -M AsymptoticLimits datacard_counting_2018-AQGC-ACW5e-7.txt --run blind --name aCW5e7 -m 5
combine -M AsymptoticLimits datacard_counting_2018-AQGC-ACW1e-6.txt --run blind --name aCW1e6 -m 10
combine -M AsymptoticLimits datacard_counting_2018-AQGC-ACW2e-6.txt --run blind --name aCW2e6 -m 20
combine -M AsymptoticLimits datacard_counting_2018-AQGC-ACW5e-6.txt --run blind --name aCW5e6 -m 50
combine -M AsymptoticLimits datacard_counting_2018-AQGC-ACW1e-5.txt --run blind --name aCW1e5 -m 100
combine -M AsymptoticLimits datacard_counting_2018-AQGC-ACW2e-5.txt --run blind --name aCW2e5 -m 200
combineTool.py -M CollectLimits *a0W*AsymptoticLimits* --use-dirs -o limits.json; mv limits_default.json limits_a0W.json
combineTool.py -M CollectLimits *aCW*AsymptoticLimits* --use-dirs -o limits.json; mv limits_default.json limits_aCW.json
python plotLimitsAQGC.py limits_a0W.json --show exp --logy --x-title '|a^{W}_{0}/#Lambda^{2} (#times 10^{-7} GeV^{-2})|' --y-title '\^{\sigma}(\gamma\gamma \rightarrow WW) (fb)'; mv limit.png limit_a0W.png; mv limit.pdf limit_a0W.pdf
python plotLimitsAQGC.py limits_aCW.json --show exp --logy --x-title '|a^{W}_{C}/#Lambda^{2} (#times 10^{-7} GeV^{-2})|' --y-title '\^{\sigma}(\gamma\gamma \rightarrow WW) (fb)'; mv limit.png limit_aCW.png; mv limit.pdf limit_aCW.pdf

