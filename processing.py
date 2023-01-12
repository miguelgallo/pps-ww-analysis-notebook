import numpy as np
import pandas as pd
import h5py
# import ROOT

run_ranges_periods_2017 = {}
run_ranges_periods_2017[ "2017B" ]  = (297020,299329)
run_ranges_periods_2017[ "2017C1" ] = (299337,300785)
run_ranges_periods_2017[ "2017C2" ] = (300806,302029)
run_ranges_periods_2017[ "2017D" ]  = (302030,303434)
run_ranges_periods_2017[ "2017E" ]  = (303435,304826)
run_ranges_periods_2017[ "2017F1" ] = (304911,305114)
run_ranges_periods_2017[ "2017F2" ] = (305178,305902)
run_ranges_periods_2017[ "2017F3" ] = (305965,306462)
df_run_ranges_2017 = pd.DataFrame( run_ranges_periods_2017, index=("min","max") ).transpose()
run_ranges_periods_mixing_2017 = run_ranges_periods_2017
df_run_ranges_mixing_2017 = df_run_ranges_2017
run_ranges_periods_2018 = {}
run_ranges_periods_2018[ "2018A" ]  = (315252,316995)
run_ranges_periods_2018[ "2018B1" ] = (316998,317696)
run_ranges_periods_2018[ "2018B2" ] = (318622,319312)
run_ranges_periods_2018[ "2018C" ]  = (319313,320393)
run_ranges_periods_2018[ "2018D1" ] = (320394,322633)
run_ranges_periods_2018[ "2018D2" ] = (323363,325273)
df_run_ranges_2018 = pd.DataFrame( run_ranges_periods_2018, index=("min","max") ).transpose()
run_ranges_periods_mixing_2018 = {}
run_ranges_periods_mixing_2018[ "2018A" ]  = (315252,316995)
run_ranges_periods_mixing_2018[ "2018B" ]  = (316998,319312)
run_ranges_periods_mixing_2018[ "2018C" ]  = (319313,320393)
run_ranges_periods_mixing_2018[ "2018D1" ] = (320394,322633)
run_ranges_periods_mixing_2018[ "2018D2" ] = (323363,325273)
df_run_ranges_mixing_2018 = pd.DataFrame( run_ranges_periods_mixing_2018, index=("min","max") ).transpose()

# L_2017B = 2.360904801;
# L_2017C1 = 5.313012839;
# L_2017E = 8.958810514;
# L_2017F1 = 1.708478656;
# L_2017C2 = 3.264135878;
# L_2017D = 4.074723964;
# L_2017F2 = 7.877903151;
# L_2017F3 = 3.632463163;
L_2017B = 4.799881474;
L_2017C1 = 5.785813941;
L_2017E = 9.312832062;
L_2017F1 = 1.738905587;
L_2017C2 = 3.786684323;
L_2017D = 4.247682053;
L_2017F2 = 8.125575961;
L_2017F3 = 3.674404546;
lumi_periods_2017 = {}
lumi_periods_2017[ 'muon' ] = {}
lumi_periods_2017[ 'muon' ][ "2017B" ]  = L_2017B
lumi_periods_2017[ 'muon' ][ "2017C1" ] = L_2017C1
lumi_periods_2017[ 'muon' ][ "2017C2" ] = L_2017C2
lumi_periods_2017[ 'muon' ][ "2017D" ]  = L_2017D
lumi_periods_2017[ 'muon' ][ "2017E" ]  = L_2017E
lumi_periods_2017[ 'muon' ][ "2017F1" ] = L_2017F1
lumi_periods_2017[ 'muon' ][ "2017F2" ] = L_2017F2
lumi_periods_2017[ 'muon' ][ "2017F3" ] = L_2017F3
lumi_periods_2017[ 'electron' ] = {}
lumi_periods_2017[ 'electron' ][ "2017B" ]  = L_2017B * 0.957127
lumi_periods_2017[ 'electron' ][ "2017C1" ] = L_2017C1 * 0.954282
lumi_periods_2017[ 'electron' ][ "2017C2" ] = L_2017C2 * 0.954282
lumi_periods_2017[ 'electron' ][ "2017D" ]  = L_2017D * 0.9539
lumi_periods_2017[ 'electron' ][ "2017E" ]  = L_2017E * 0.956406
lumi_periods_2017[ 'electron' ][ "2017F1" ] = L_2017F1 * 0.953733
lumi_periods_2017[ 'electron' ][ "2017F2" ] = L_2017F2 * 0.953733
lumi_periods_2017[ 'electron' ][ "2017F3" ] = L_2017F3 * 0.953733
print ( lumi_periods_2017 )
print ( "Luminosity 2017 muon: {}".format( np.sum( list( lumi_periods_2017[ 'muon' ].values() ) ) ) )
print ( "Luminosity 2017 electron: {}".format( np.sum( list( lumi_periods_2017[ 'electron' ].values() ) ) ) )

# L_2018A  = 12.10
# L_2018B1 = 6.38
# L_2018B2 = 0.40
# L_2018C  = 6.5297
# L_2018D1 = 19.88
# L_2018D2 = 10.4157
L_2018A  = 14.027047499
L_2018B1 = 6.629673574
L_2018B2 = 0.430948924
L_2018C  = 6.891747024
L_2018D1 = 20.962647459
L_2018D2 = 10.868724698
lumi_periods_2018 = {}
lumi_periods_2018[ 'muon' ] = {}
lumi_periods_2018[ 'muon' ][ "2018A" ]  = L_2018A * 0.999913
lumi_periods_2018[ 'muon' ][ "2018B1" ] = L_2018B1 * 0.998672
lumi_periods_2018[ 'muon' ][ "2018B2" ] = L_2018B2 * 0.998672
lumi_periods_2018[ 'muon' ][ "2018C" ]  = L_2018C * 0.999991
lumi_periods_2018[ 'muon' ][ "2018D1" ] = L_2018D1 * 0.998915
lumi_periods_2018[ 'muon' ][ "2018D2" ] = L_2018D2 * 0.998915
lumi_periods_2018[ 'electron' ] = {}
lumi_periods_2018[ 'electron' ][ "2018A" ]  = L_2018A * 0.933083
lumi_periods_2018[ 'electron' ][ "2018B1" ] = L_2018B1 * 0.999977
lumi_periods_2018[ 'electron' ][ "2018B2" ] = L_2018B2 * 0.999977
lumi_periods_2018[ 'electron' ][ "2018C" ]  = L_2018C * 0.999978
lumi_periods_2018[ 'electron' ][ "2018D1" ] = L_2018D1 * 0.999389
lumi_periods_2018[ 'electron' ][ "2018D2" ] = L_2018D2 * 0.999389
print ( lumi_periods_2018 )
print ( "Luminosity 2018 muon: {}".format( np.sum( list( lumi_periods_2018[ 'muon' ].values() ) ) ) )
print ( "Luminosity 2018 electron: {}".format( np.sum( list( lumi_periods_2018[ 'electron' ].values() ) ) ) )

aperture_period_map = {
    "2016_preTS2"  : "2016_preTS2",
    "2016_postTS2" : "2016_postTS2",
    "2017B"        : "2017_preTS2",
    "2017C1"       : "2017_preTS2",
    "2017C2"       : "2017_preTS2",
    "2017D"        : "2017_preTS2",
    "2017E"        : "2017_postTS2",
    "2017F1"       : "2017_postTS2",
    "2017F2"       : "2017_postTS2",
    "2017F3"       : "2017_postTS2",
    "2018A"        : "2018",
    "2018B1"       : "2018",
    "2018B2"       : "2018",
    "2018C"        : "2018",
    "2018D1"       : "2018",
    "2018D2"       : "2018"
}
reco_period_map = {
    "2016_preTS2"  : "2016_preTS2",
    "2016_postTS2" : "2016_postTS2",
    "2017B"        : "2017_preTS2",
    "2017C1"       : "2017_preTS2",
    "2017C2"       : "2017_preTS2",
    "2017D"        : "2017_preTS2",
    "2017E"        : "2017_postTS2",
    "2017F1"       : "2017_postTS2",
    "2017F2"       : "2017_postTS2",
    "2017F3"       : "2017_postTS2",
    "2018A"        : "2018_preTS1",
    "2018B1"       : "2018_TS1_TS2",
    "2018B2"       : "2018_TS1_TS2",
    "2018C"        : "2018_TS1_TS2",
    "2018D1"       : "2018_postTS2",
    "2018D2"       : "2018_postTS2"
}

# Fiducial cuts (UL)
# Periods: "2017B", "2017C1", "2017E", "2017F1", "2018A", "2018B1", "2018B2", "2018C", "2018D1", "2018D2"
def fiducial_cuts():
    # Per data period, arm=(0,1), station=(0,2)
    fiducialXLow_ = {}
    fiducialXHigh_ = {}
    fiducialYLow_ = {}
    fiducialYHigh_ = {}

    # data_periods = [ "2017B", "2017C1", "2017E", "2017F1", "2018A", "2018B1", "2018B2", "2018C", "2018D1", "2018D2" ]
    data_periods = [ "2017B", "2017C1", "2017C2", "2017D", "2017E", "2017F1", "2017F2", "2017F3", "2018A", "2018B1", "2018B2", "2018C", "2018D1", "2018D2" ]

    for period_ in data_periods:
        fiducialXLow_[ period_ ] = {}
        fiducialXLow_[ period_ ][ 0 ] = {}
        fiducialXLow_[ period_ ][ 1 ] = {}
        fiducialXHigh_[ period_ ] = {}
        fiducialXHigh_[ period_ ][ 0 ] = {}
        fiducialXHigh_[ period_ ][ 1 ] = {}
        fiducialYLow_[ period_ ] = {}
        fiducialYLow_[ period_ ][ 0 ] = {}
        fiducialYLow_[ period_ ][ 1 ] = {}
        fiducialYHigh_[ period_ ] = {}
        fiducialYHigh_[ period_ ][ 0 ] = {}
        fiducialYHigh_[ period_ ][ 1 ] = {}
        
    # 2017B
    # Sector 45, RP 220
    fiducialXLow_[ "2017B" ][ 0 ][ 2 ]  =   1.995;
    fiducialXHigh_[ "2017B" ][ 0 ][ 2 ] =  24.479;
    fiducialYLow_[ "2017B" ][ 0 ][ 2 ]  = -11.098;
    fiducialYHigh_[ "2017B" ][ 0 ][ 2 ] =   4.298;
    # Sector 56, RP 220
    fiducialXLow_[ "2017B" ][ 1 ][ 2 ]  =   2.422;
    fiducialXHigh_[ "2017B" ][ 1 ][ 2 ] =  24.620;
    fiducialYLow_[ "2017B" ][ 1 ][ 2 ]  = -10.698;
    fiducialYHigh_[ "2017B" ][ 1 ][ 2 ] =   4.698;

    # 2017C1
    # Sector 45, RP 220
    fiducialXLow_[ "2017C1" ][ 0 ][ 2 ]  =   1.860;
    fiducialXHigh_[ "2017C1" ][ 0 ][ 2 ] =  24.334;
    fiducialYLow_[ "2017C1" ][ 0 ][ 2 ]  = -11.098;
    fiducialYHigh_[ "2017C1" ][ 0 ][ 2 ] =   4.298;
    # Sector 56, RP 220
    fiducialXLow_[ "2017C1" ][ 1 ][ 2 ]  =   2.422;
    fiducialXHigh_[ "2017C1" ][ 1 ][ 2 ] =  24.620;
    fiducialYLow_[ "2017C1" ][ 1 ][ 2 ]  = -10.698;
    fiducialYHigh_[ "2017C1" ][ 1 ][ 2 ] =   4.698;

    # 2017C2
    # Sector 45, RP 220
    fiducialXLow_[ "2017C2" ][ 0 ][ 2 ]  =   1.860;
    fiducialXHigh_[ "2017C2" ][ 0 ][ 2 ] =  24.334;
    fiducialYLow_[ "2017C2" ][ 0 ][ 2 ]  = -11.098;
    fiducialYHigh_[ "2017C2" ][ 0 ][ 2 ] =   4.298;
    # Sector 56, RP 220
    fiducialXLow_[ "2017C2" ][ 1 ][ 2 ]  =   2.422;
    fiducialXHigh_[ "2017C2" ][ 1 ][ 2 ] =  24.620;
    fiducialYLow_[ "2017C2" ][ 1 ][ 2 ]  = -10.698;
    fiducialYHigh_[ "2017C2" ][ 1 ][ 2 ] =   4.698;

    # 2017D
    # Sector 45, RP 220
    fiducialXLow_[ "2017D" ][ 0 ][ 2 ]  =   1.860;
    fiducialXHigh_[ "2017D" ][ 0 ][ 2 ] =  24.334;
    fiducialYLow_[ "2017D" ][ 0 ][ 2 ]  = -11.098;
    fiducialYHigh_[ "2017D" ][ 0 ][ 2 ] =   4.298;
    # Sector 56, RP 220
    fiducialXLow_[ "2017D" ][ 1 ][ 2 ]  =   2.422;
    fiducialXHigh_[ "2017D" ][ 1 ][ 2 ] =  24.620;
    fiducialYLow_[ "2017D" ][ 1 ][ 2 ]  = -10.698;
    fiducialYHigh_[ "2017D" ][ 1 ][ 2 ] =   4.698;

    # 2017E
    # Sector 45, RP 220
    fiducialXLow_[ "2017E" ][ 0 ][ 2 ]  =   1.995;
    fiducialXHigh_[ "2017E" ][ 0 ][ 2 ] =  24.479;
    fiducialYLow_[ "2017E" ][ 0 ][ 2 ]  = -10.098;
    fiducialYHigh_[ "2017E" ][ 0 ][ 2 ] =   4.998;
    # Sector 56, RP 220
    fiducialXLow_[ "2017E" ][ 1 ][ 2 ]  =  2.422;
    fiducialXHigh_[ "2017E" ][ 1 ][ 2 ] = 24.620;
    fiducialYLow_[ "2017E" ][ 1 ][ 2 ]  = -9.698;
    fiducialYHigh_[ "2017E" ][ 1 ][ 2 ] =  5.398;

    # 2017F1
    # Sector 45, RP 220
    fiducialXLow_[ "2017F1" ][ 0 ][ 2 ]  =   1.995;
    fiducialXHigh_[ "2017F1" ][ 0 ][ 2 ] =  24.479;
    fiducialYLow_[ "2017F1" ][ 0 ][ 2 ]  = -10.098;
    fiducialYHigh_[ "2017F1" ][ 0 ][ 2 ] =   4.998;
    # Sector 56, RP 220
    fiducialXLow_[ "2017F1" ][ 1 ][ 2 ]  =  2.422;
    fiducialXHigh_[ "2017F1" ][ 1 ][ 2 ] = 24.620;
    fiducialYLow_[ "2017F1" ][ 1 ][ 2 ]  = -9.698;
    fiducialYHigh_[ "2017F1" ][ 1 ][ 2 ] =  5.398;

    # 2017F2
    # Sector 45, RP 220
    fiducialXLow_[ "2017F2" ][ 0 ][ 2 ]  =   1.995;
    fiducialXHigh_[ "2017F2" ][ 0 ][ 2 ] =  24.479;
    fiducialYLow_[ "2017F2" ][ 0 ][ 2 ]  = -10.098;
    fiducialYHigh_[ "2017F2" ][ 0 ][ 2 ] =   4.998;
    # Sector 56, RP 220
    fiducialXLow_[ "2017F2" ][ 1 ][ 2 ]  =  2.422;
    fiducialXHigh_[ "2017F2" ][ 1 ][ 2 ] = 24.620;
    fiducialYLow_[ "2017F2" ][ 1 ][ 2 ]  = -9.698;
    fiducialYHigh_[ "2017F2" ][ 1 ][ 2 ] =  5.398;

    # 2017F3
    # Sector 45, RP 220
    fiducialXLow_[ "2017F3" ][ 0 ][ 2 ]  =   1.995;
    fiducialXHigh_[ "2017F3" ][ 0 ][ 2 ] =  24.479;
    fiducialYLow_[ "2017F3" ][ 0 ][ 2 ]  = -10.098;
    fiducialYHigh_[ "2017F3" ][ 0 ][ 2 ] =   4.998;
    # Sector 56, RP 220
    fiducialXLow_[ "2017F3" ][ 1 ][ 2 ]  =  2.422;
    fiducialXHigh_[ "2017F3" ][ 1 ][ 2 ] = 24.620;
    fiducialYLow_[ "2017F3" ][ 1 ][ 2 ]  = -9.698;
    fiducialYHigh_[ "2017F3" ][ 1 ][ 2 ] =  5.398;

    # 2018A
    # Sector 45, RP 210
    fiducialXLow_[ "2018A" ][ 0 ][ 0 ]  =   2.850;
    fiducialXHigh_[ "2018A" ][ 0 ][ 0 ] =  17.927;
    fiducialYLow_[ "2018A" ][ 0 ][ 0 ]  = -11.598;
    fiducialYHigh_[ "2018A" ][ 0 ][ 0 ] =   3.698;
    # Sector 45, RP 220
    fiducialXLow_[ "2018A" ][ 0 ][ 2 ]  =   2.421;
    fiducialXHigh_[ "2018A" ][ 0 ][ 2 ] =  24.620;
    fiducialYLow_[ "2018A" ][ 0 ][ 2 ]  = -10.898;
    fiducialYHigh_[ "2018A" ][ 0 ][ 2 ] =   4.398;
    # Sector 56, RP 210
    fiducialXLow_[ "2018A" ][ 1 ][ 0 ]  =   3.275;
    fiducialXHigh_[ "2018A" ][ 1 ][ 0 ] =  18.498;
    fiducialYLow_[ "2018A" ][ 1 ][ 0 ]  = -11.298;
    fiducialYHigh_[ "2018A" ][ 1 ][ 0 ] =   3.298;
    # Sector 56, RP 220
    fiducialXLow_[ "2018A" ][ 1 ][ 2 ]  =   2.421;
    fiducialXHigh_[ "2018A" ][ 1 ][ 2 ] =  20.045;
    fiducialYLow_[ "2018A" ][ 1 ][ 2 ]  = -10.398;
    fiducialYHigh_[ "2018A" ][ 1 ][ 2 ] =   5.098;

    # 2018B1
    # Sector 45, RP 210
    fiducialXLow_[ "2018B1" ][ 0 ][ 0 ]  =   2.850;
    fiducialXHigh_[ "2018B1" ][ 0 ][ 0 ] =  17.927;
    fiducialYLow_[ "2018B1" ][ 0 ][ 0 ]  = -11.598;
    fiducialYHigh_[ "2018B1" ][ 0 ][ 0 ] =   3.698;
    # Sector 45, RP 220
    fiducialXLow_[ "2018B1" ][ 0 ][ 2 ]  =   2.421;
    fiducialXHigh_[ "2018B1" ][ 0 ][ 2 ] =  24.620;
    fiducialYLow_[ "2018B1" ][ 0 ][ 2 ]  = -10.898;
    fiducialYHigh_[ "2018B1" ][ 0 ][ 2 ] =   4.198;
    # Sector 56, RP 210
    fiducialXLow_[ "2018B1" ][ 1 ][ 0 ]  =   3.275;
    fiducialXHigh_[ "2018B1" ][ 1 ][ 0 ] =  18.070;
    fiducialYLow_[ "2018B1" ][ 1 ][ 0 ]  = -11.198;
    fiducialYHigh_[ "2018B1" ][ 1 ][ 0 ] =   4.098;
    # Sector 56, RP 220
    fiducialXLow_[ "2018B1" ][ 1 ][ 2 ]  =   2.564;
    fiducialXHigh_[ "2018B1" ][ 1 ][ 2 ] =  20.045;
    fiducialYLow_[ "2018B1" ][ 1 ][ 2 ]  = -10.398;
    fiducialYHigh_[ "2018B1" ][ 1 ][ 2 ] =   5.098;

    # 2018B2
    # Sector 45, RP 210
    fiducialXLow_[ "2018B2" ][ 0 ][ 0 ]  =   2.564;
    fiducialXHigh_[ "2018B2" ][ 0 ][ 0 ] =  17.640;
    fiducialYLow_[ "2018B2" ][ 0 ][ 0 ]  = -11.598;
    fiducialYHigh_[ "2018B2" ][ 0 ][ 0 ] =   4.198;
    # Sector 45, RP 220
    fiducialXLow_[ "2018B2" ][ 0 ][ 2 ]  =   2.140;
    fiducialXHigh_[ "2018B2" ][ 0 ][ 2 ] =  24.479;
    fiducialYLow_[ "2018B2" ][ 0 ][ 2 ]  = -11.398;
    fiducialYHigh_[ "2018B2" ][ 0 ][ 2 ] =   3.798;
    # Sector 56, RP 210
    fiducialXLow_[ "2018B2" ][ 1 ][ 0 ]  =   3.275;
    fiducialXHigh_[ "2018B2" ][ 1 ][ 0 ] =  17.931;
    fiducialYLow_[ "2018B2" ][ 1 ][ 0 ]  = -10.498;
    fiducialYHigh_[ "2018B2" ][ 1 ][ 0 ] =   4.098;
    # Sector 56, RP 220
    fiducialXLow_[ "2018B2" ][ 1 ][ 2 ]  =   2.279;
    fiducialXHigh_[ "2018B2" ][ 1 ][ 2 ] =  24.760;
    fiducialYLow_[ "2018B2" ][ 1 ][ 2 ]  = -10.598;
    fiducialYHigh_[ "2018B2" ][ 1 ][ 2 ] =   4.498;

    # 2018C
    # Sector 45, RP 210
    fiducialXLow_[ "2018C" ][ 0 ][ 0 ]  =   2.564;
    fiducialXHigh_[ "2018C" ][ 0 ][ 0 ] =  17.930;
    fiducialYLow_[ "2018C" ][ 0 ][ 0 ]  = -11.098;
    fiducialYHigh_[ "2018C" ][ 0 ][ 0 ] =   4.198;
    # Sector 45, RP 220
    fiducialXLow_[ "2018C" ][ 0 ][ 2 ]  =   2.421;
    fiducialXHigh_[ "2018C" ][ 0 ][ 2 ] =  24.620;
    fiducialYLow_[ "2018C" ][ 0 ][ 2 ]  = -11.398;
    fiducialYHigh_[ "2018C" ][ 0 ][ 2 ] =   3.698;
    # Sector 56, RP 210
    fiducialXLow_[ "2018C" ][ 1 ][ 0 ]  =   3.275;
    fiducialXHigh_[ "2018C" ][ 1 ][ 0 ] =  17.931;
    fiducialYLow_[ "2018C" ][ 1 ][ 0 ]  = -10.498;
    fiducialYHigh_[ "2018C" ][ 1 ][ 0 ] =   4.698;
    # Sector 56, RP 220
    fiducialXLow_[ "2018C" ][ 1 ][ 2 ]  =   2.279;
    fiducialXHigh_[ "2018C" ][ 1 ][ 2 ] =  24.760;
    fiducialYLow_[ "2018C" ][ 1 ][ 2 ]  = -10.598;
    fiducialYHigh_[ "2018C" ][ 1 ][ 2 ] =   4.398;

    # 2018D1
    # Sector 45, RP 210
    fiducialXLow_[ "2018D1" ][ 0 ][ 0 ]  =   2.850;
    fiducialXHigh_[ "2018D1" ][ 0 ][ 0 ] =  17.931;
    fiducialYLow_[ "2018D1" ][ 0 ][ 0 ]  = -11.098;
    fiducialYHigh_[ "2018D1" ][ 0 ][ 0 ] =   4.098;
    # Sector 45, RP 220
    fiducialXLow_[ "2018D1" ][ 0 ][ 2 ]  =   2.421;
    fiducialXHigh_[ "2018D1" ][ 0 ][ 2 ] =  24.620;
    fiducialYLow_[ "2018D1" ][ 0 ][ 2 ]  = -11.398;
    fiducialYHigh_[ "2018D1" ][ 0 ][ 2 ] =   3.698;
    # Sector 56, RP 210
    fiducialXLow_[ "2018D1" ][ 1 ][ 0 ]  =   3.275;
    fiducialXHigh_[ "2018D1" ][ 1 ][ 0 ] =  17.931;
    fiducialYLow_[ "2018D1" ][ 1 ][ 0 ]  = -10.498;
    fiducialYHigh_[ "2018D1" ][ 1 ][ 0 ] =   4.698;
    # Sector 56, RP 220
    fiducialXLow_[ "2018D1" ][ 1 ][ 2 ]  =   2.279;
    fiducialXHigh_[ "2018D1" ][ 1 ][ 2 ] =  24.760;
    fiducialYLow_[ "2018D1" ][ 1 ][ 2 ]  = -10.598;
    fiducialYHigh_[ "2018D1" ][ 1 ][ 2 ] =   4.398;

    # 2018D2
    # Sector 45, RP 210
    fiducialXLow_[ "2018D2" ][ 0 ][ 0 ]  =   2.850;
    fiducialXHigh_[ "2018D2" ][ 0 ][ 0 ] =  17.931;
    fiducialYLow_[ "2018D2" ][ 0 ][ 0 ]  = -10.598;
    fiducialYHigh_[ "2018D2" ][ 0 ][ 0 ] =   4.498;
    # Sector 45, RP 220
    fiducialXLow_[ "2018D2" ][ 0 ][ 2 ]  =   2.421;
    fiducialXHigh_[ "2018D2" ][ 0 ][ 2 ] =  24.620;
    fiducialYLow_[ "2018D2" ][ 0 ][ 2 ]  = -11.698;
    fiducialYHigh_[ "2018D2" ][ 0 ][ 2 ] =   3.298;
    # Sector 56, RP 210
    fiducialXLow_[ "2018D2" ][ 1 ][ 0 ]  =  3.275;
    fiducialXHigh_[ "2018D2" ][ 1 ][ 0 ] = 17.931;
    fiducialYLow_[ "2018D2" ][ 1 ][ 0 ]  = -9.998;
    fiducialYHigh_[ "2018D2" ][ 1 ][ 0 ] =  4.698;
    # Sector 56, RP 220
    fiducialXLow_[ "2018D2" ][ 1 ][ 2 ]  =   2.279;
    fiducialXHigh_[ "2018D2" ][ 1 ][ 2 ] =  24.760;
    fiducialYLow_[ "2018D2" ][ 1 ][ 2 ]  = -10.598;
    fiducialYHigh_[ "2018D2" ][ 1 ][ 2 ] =   3.898;
      
    return (  fiducialXLow_, fiducialXHigh_, fiducialYLow_, fiducialYHigh_ )


def fiducial_cuts_all( data_sample ):

    data_periods = None
    if data_sample == '2017':
        # data_periods = [ "2017B", "2017C1", "2017E", "2017F1" ]
        data_periods = [ "2017B", "2017C1", "2017C2", "2017D", "2017E", "2017F1", "2017F2", "2017F3" ]
    elif data_sample == '2018':
        data_periods = [ "2018A", "2018B1", "2018B2", "2018C", "2018D1", "2018D2" ]

    fiducialXLow_, fiducialXHigh_, fiducialYLow_, fiducialYHigh_ = fiducial_cuts()
    print ( fiducialXLow_, fiducialXHigh_, fiducialYLow_, fiducialYHigh_ )
    
    # Per data period, arm=(0,1), station=(0,2)
    fiducialXLow_all = {}
    fiducialXHigh_all = {}
    fiducialYLow_all = {}
    fiducialYHigh_all = {}
    for arm_ in (0,1):
        fiducialXLow_all[ arm_ ] = {}
        fiducialXLow_all[ arm_ ][ 2 ] = []
        fiducialXHigh_all[ arm_ ] = {}
        fiducialXHigh_all[ arm_ ][ 2 ] = []
        fiducialYLow_all[ arm_ ] = {}
        fiducialYLow_all[ arm_ ][ 2 ] = []
        fiducialYHigh_all[ arm_ ] = {}
        fiducialYHigh_all[ arm_ ][ 2 ] = []

    for period_ in data_periods:
        for arm_ in (0,1):
            fiducialXLow_all[ arm_ ][ 2 ].append( fiducialXLow_[ period_ ][ arm_][ 2 ] )
            fiducialXHigh_all[ arm_ ][ 2 ].append( fiducialXHigh_[ period_ ][ arm_][ 2 ] )
            fiducialYLow_all[ arm_ ][ 2 ].append( fiducialYLow_[ period_ ][ arm_][ 2 ] )
            fiducialYHigh_all[ arm_ ][ 2 ].append( fiducialYHigh_[ period_ ][ arm_][ 2 ] )

    for arm_ in (0,1):
        fiducialXLow_all[ arm_ ][ 2 ] = np.max( fiducialXLow_all[ arm_ ][ 2 ] )
        fiducialXHigh_all[ arm_ ][ 2 ] = np.min( fiducialXHigh_all[ arm_ ][ 2 ] )
        fiducialYLow_all[ arm_ ][ 2 ] = np.max( fiducialYLow_all[ arm_ ][ 2 ] )
        fiducialYHigh_all[ arm_ ][ 2 ] = np.min( fiducialYHigh_all[ arm_ ][ 2 ] )

    print ( fiducialXLow_all, fiducialXHigh_all, fiducialYLow_all, fiducialYHigh_all )
    
    return ( fiducialXLow_all, fiducialXHigh_all, fiducialYLow_all, fiducialYHigh_all )


# Per data period, arm=(0,1)
# Periods: "2016_preTS2", "2016_postTS2", "2017_preTS2", "2017_postTS2", "2018"
def aperture_parametrisation( period, arm, xangle, xi ):

    #https://github.com/cms-sw/cmssw/tree/916cb3d20213734a0465240720c8c8c392b92eac/Validation/CTPPS/python/simu_config

    if (period == "2016_preTS2"):
        if   (arm == 0): return 3.76296E-05+((xi<0.117122)*0.00712775+(xi>=0.117122)*0.0148651)*(xi-0.117122);
        elif (arm == 1): return 1.85954E-05+((xi<0.14324)*0.00475349+(xi>=0.14324)*0.00629514)*(xi-0.14324);
    elif (period == "2016_postTS2"):
        if   (arm == 0): return 6.10374E-05+((xi<0.113491)*0.00795942+(xi>=0.113491)*0.01935)*(xi-0.113491);
        elif (arm == 1): return (xi-0.110)/130.0;
    elif (period == "2017_preTS2"):
        if   (arm == 0): return -(8.71198E-07*xangle-0.000134726)+((xi<(0.000264704*xangle+0.081951))*-(4.32065E-05*xangle-0.0130746)+(xi>=(0.000264704*xangle+0.081951))*-(0.000183472*xangle-0.0395241))*(xi-(0.000264704*xangle+0.081951));
        elif (arm == 1): return 3.43116E-05+((xi<(0.000626936*xangle+0.061324))*0.00654394+(xi>=(0.000626936*xangle+0.061324))*-(0.000145164*xangle-0.0272919))*(xi-(0.000626936*xangle+0.061324));
    elif (period == "2017_postTS2"):
        if   (arm == 0): return -(8.92079E-07*xangle-0.000150214)+((xi<(0.000278622*xangle+0.0964383))*-(3.9541e-05*xangle-0.0115104)+(xi>=(0.000278622*xangle+0.0964383))*-(0.000108249*xangle-0.0249303))*(xi-(0.000278622*xangle+0.0964383));
        elif (arm == 1): return 4.56961E-05+((xi<(0.00075625*xangle+0.0643361))*-(3.01107e-05*xangle-0.00985126)+(xi>=(0.00075625*xangle+0.0643361))*-(8.95437e-05*xangle-0.0169474))*(xi-(0.00075625*xangle+0.0643361));
    elif (period == "2018"):
        if   (arm == 0): return -(8.44219E-07*xangle-0.000100957)+((xi<(0.000247185*xangle+0.101599))*-(1.40289E-05*xangle-0.00727237)+(xi>=(0.000247185*xangle+0.101599))*-(0.000107811*xangle-0.0261867))*(xi-(0.000247185*xangle+0.101599));
        elif (arm == 1): return -(-4.74758E-07*xangle+3.0881E-05)+((xi<(0.000727859*xangle+0.0722653))*-(2.43968E-05*xangle-0.0085461)+(xi>=(0.000727859*xangle+0.0722653))*-(7.19216E-05*xangle-0.0148267))*(xi-(0.000727859*xangle+0.0722653));
    else:
        return -999.

def check_aperture( period, arm, xangle, xi, theta_x ):
    return ( theta_x < -aperture_parametrisation( period, arm, xangle, xi ) )


def get_data( fileNames, runMin=None, runMax=None ):

    if runMin is not None and runMin <= 0:
        raise RuntimeError( "Invalid data_sample argument." )
    if runMax is not None and runMax <= 0:
        raise RuntimeError( "Invalid data_sample argument." )

    runMin_ = runMin
    runMax_ = runMax

    df_protons_multiRP_list = []
    df_protons_singleRP_list = []
    df_ppstracks_list = []
    df_counts_list = []

    for file_ in fileNames:
        print ( file_ )
        with h5py.File( file_, 'r' ) as f:
            print ( list(f.keys()) )

            dset_protons_multiRP = f['protons_multiRP']
            print ( dset_protons_multiRP.shape )
            print ( dset_protons_multiRP[:,:] )

            dset_protons_singleRP = f['protons_singleRP']
            print ( dset_protons_singleRP.shape )
            print ( dset_protons_singleRP[:,:] )

            dset_ppstracks = f['ppstracks']
            print ( dset_ppstracks.shape )
            print ( dset_ppstracks[:,:] )

            dset_columns_protons_multiRP = f['columns_protons_multiRP']
            print ( dset_columns_protons_multiRP.shape )
            columns_protons_multiRP = [ item.decode("utf-8") for item in list( dset_columns_protons_multiRP ) ]
            print ( columns_protons_multiRP )

            dset_columns_protons_singleRP = f['columns_protons_singleRP']
            print ( dset_columns_protons_singleRP.shape )
            columns_protons_singleRP = [ item.decode("utf-8") for item in list( dset_columns_protons_singleRP ) ]
            print ( columns_protons_singleRP )
            
            dset_columns_ppstracks = f['columns_ppstracks']
            print ( dset_columns_ppstracks.shape )
            columns_ppstracks = [ item.decode("utf-8") for item in list( dset_columns_ppstracks ) ]
            print ( columns_ppstracks )

            dset_selections = f['selections']
            selections_ = [ item.decode("utf-8") for item in dset_selections ]
            print ( selections_ )

            dset_counts = f['event_counts']
            df_counts_list.append( pd.Series( dset_counts, index=selections_ ) )
            print ( df_counts_list[-1] )

            chunk_size = 1000000
            entries_protons_multiRP = dset_protons_multiRP.shape[0]
            start_ = list( range( 0, entries_protons_multiRP, chunk_size ) )
            stop_ = start_[1:]
            stop_.append( entries_protons_multiRP )
            print ( start_ )
            print ( stop_ )
            astype_dict_protons_ = {
                "run": "int64", "lumiblock": "int64", "event": "int64", "slice": "int32",
                "ismultirp": "int32", "rpid": "int32", "arm": "int32", "random": "int32",
                "nVertices": "int32",
                "num_bjets_ak8": "int32", "num_bjets_ak4": "int32", "num_jets_ak4": "int32",
                "pfcand_nextracks": "int32", "pfcand_nextracks_noDRl": "int32",
                "trackpixshift1": "int32", "rpid1": "int32"
                }
            astype_dict_multiRP_ = astype_dict_protons_.copy()

            if "muon0_charge" in columns_protons_multiRP:
                astype_dict_multiRP_.update( { "muon0_charge": "int32" } )
 
            if "electron0_charge" in columns_protons_multiRP:
                astype_dict_multiRP_.update( { "electron0_charge": "int32" } )

            if "rpid2" in columns_protons_multiRP: 
                astype_dict_multiRP_.update( { "trackpixshift2": "int32", "rpid2": "int32" } )

            if "run_mc" in columns_protons_multiRP:
                astype_dict_multiRP_.update( { "run_mc": "int64" } )

            if "run_rnd" in columns_protons_multiRP: 
                # astype_dict_multiRP_.update( { "run_rnd": "int64", "lumiblock_rnd": "int64", "event_rnd": "int64", "slice_rnd": "int32" } )
                astype_dict_multiRP_.update( { "run_rnd": "int64", "lumiblock_rnd": "int64", "event_rnd": "int64" } )

            for idx in range( len( start_ ) ):
                print ( start_[idx], stop_[idx] )
                #print ( dset[ start_[idx] : stop_[idx] ] )
                df_ = pd.DataFrame( dset_protons_multiRP[ start_[idx] : stop_[idx] ], columns=columns_protons_multiRP ).astype( astype_dict_multiRP_ )

                if runMin_ is not None:
                    msk__ = ( df_.loc[ 'run' ] >= runMin_ )
                    print ( msk__ )
                    df_ = df_.loc[ msk__ ]
                if runMax_ is not None and df_.shape[0] > 0:
                    msk__ = ( df_.loc[ 'run' ] <= runMax_ )
                    print ( msk__ )
                    df_ = df_.loc[ msk__ ]

                if df_.shape[0] > 0:
                    df_protons_multiRP_list.append( df_ )
                    print ( df_protons_multiRP_list[-1].head() )
                    print ( "Data set size: {}".format( len( df_protons_multiRP_list[-1] ) ) )

            entries_protons_singleRP = dset_protons_singleRP.shape[0]
            start_ = list( range( 0, entries_protons_singleRP, chunk_size ) )
            stop_ = start_[1:]
            stop_.append( entries_protons_singleRP )
            print ( start_ )
            print ( stop_ )
            astype_dict_singleRP_ = astype_dict_protons_.copy()

            if "run_mc" in columns_protons_singleRP:
                astype_dict_singleRP_.update( { "run_mc": "int64" } )

            if "run_rnd" in columns_protons_singleRP: 
                # astype_dict_singleRP_.update( { "run_rnd": "int64", "lumiblock_rnd": "int64", "event_rnd": "int64", "slice_rnd": "int32" } )
                astype_dict_singleRP_.update( { "run_rnd": "int64", "lumiblock_rnd": "int64", "event_rnd": "int64" } )

            for idx in range( len( start_ ) ):
                print ( start_[idx], stop_[idx] )
                #print ( dset[ start_[idx] : stop_[idx] ] )
                df_ = pd.DataFrame( dset_protons_singleRP[ start_[idx] : stop_[idx] ], columns=columns_protons_singleRP ).astype( astype_dict_singleRP_ )

                if runMin_ is not None:
                    msk__ = ( df_.loc[ 'run' ] >= runMin_ )
                    print ( msk__ )
                    df_ = df_.loc[ msk__ ]
                if runMax_ is not None and df_.shape[0] > 0:
                    msk__ = ( df_.loc[ 'run' ] <= runMax_ )
                    print ( msk__ )
                    df_ = df_.loc[ msk__ ]

                if df_.shape[0] > 0:
                    df_protons_singleRP_list.append( df_ )
                    print ( df_protons_singleRP_list[-1].head() )
                    print ( "Data set size: {}".format( len( df_protons_singleRP_list[-1] ) ) )

            entries_ppstracks = dset_ppstracks.shape[0]
            start_ = list( range( 0, entries_ppstracks, chunk_size ) )
            stop_ = start_[1:]
            stop_.append( entries_ppstracks )
            print ( start_ )
            print ( stop_ )
            astype_dict_ppstracks_ = { "run": "int64", "lumiblock": "int64", "event": "int64", "slice": "int32", "rpid": "int32" }

            if "run_mc" in columns_ppstracks:
                astype_dict_ppstracks_.update( { "run_mc": "int64" } )

            if "run_rnd" in columns_ppstracks: 
                # astype_dict_ppstracks_.update( { "run_rnd": "int64", "lumiblock_rnd": "int64", "event_rnd": "int64", "slice_rnd": "int32" } )
                astype_dict_ppstracks_.update( { "run_rnd": "int64", "lumiblock_rnd": "int64", "event_rnd": "int64" } )

            for idx in range( len( start_ ) ):
                print ( start_[idx], stop_[idx] )
                #print ( dset[ start_[idx] : stop_[idx] ] )
                df_ = pd.DataFrame( dset_ppstracks[ start_[idx] : stop_[idx] ], columns=columns_ppstracks ).astype( astype_dict_ppstracks_ )

                if runMin_ is not None:
                    msk__ = ( df_.loc[ 'run' ] >= runMin_ )
                    print ( msk__ )
                    df_ = df_.loc[ msk__ ]
                if runMax_ is not None and df_.shape[0] > 0:
                    msk__ = ( df_.loc[ 'run' ] <= runMax_ )
                    print ( msk__ )
                    df_ = df_.loc[ msk__ ]

                if df_.shape[0] > 0:
                    df_ppstracks_list.append( df_ )
                    print ( df_ppstracks_list[-1].head() )
                    print ( "Data set size: {}".format( len( df_ppstracks_list[-1] ) ) )

    df_counts = df_counts_list[0]
    for idx in range( 1, len( df_counts_list ) ):
        df_counts = df_counts.add( df_counts_list[idx] )
    print ( df_counts )

    df_protons_multiRP = pd.concat( df_protons_multiRP_list )
    print (df_protons_multiRP)

    df_protons_singleRP = pd.concat( df_protons_singleRP_list )
    print (df_protons_singleRP)

    df_ppstracks = pd.concat( df_ppstracks_list )
    print (df_ppstracks)
    
    return (df_counts, df_protons_multiRP, df_protons_singleRP, df_ppstracks)


def process_data_protons_multiRP( lepton_type, data_sample, df_protons_multiRP, df_ppstracks=None, apply_fiducial=True, within_aperture=False, random_protons=False, mix_protons=False, select_2protons=True, runOnMC=False, use_hash_index=False ):

    # if runOnMC and not mix_protons:
    #     print ( "Turning within_aperture OFF for MC." )
    #     within_aperture = False

    fiducialXLow_all = None
    fiducialXHigh_all = None
    fiducialYLow_all = None
    fiducialYHigh_all = None
    if apply_fiducial:
        # fiducialXLow_all, fiducialXHigh_all, fiducialYLow_all, fiducialYHigh_all = fiducial_cuts_all()
        fiducialXLow_all, fiducialXHigh_all, fiducialYLow_all, fiducialYHigh_all = fiducial_cuts_all( data_sample )
    
    df_ppstracks_index = None
    if df_ppstracks is not None:
        index_vars_ = None
        if not use_hash_index:
            index_vars_ = ['run', 'lumiblock', 'event', 'slice']
        else:
            from pandas.util import hash_array
            arr_hash_id_ppstracks_x_ = hash_array( df_ppstracks.loc[ :, 'x' ].values  )
            df_ppstracks.loc[ :, "hash_id" ] = arr_hash_id_ppstracks_x_
            print ( df_ppstracks.loc[ :, "hash_id" ] )
            index_vars_ = ['run', 'lumiblock', 'event', 'hash_id', 'slice']
        print ( index_vars_ )
        # df_ppstracks_index = df_ppstracks.set_index( ['run', 'lumiblock', 'event', 'slice'] )
        df_ppstracks_index = df_ppstracks.set_index( index_vars_ )
#        
#        df_protons_multiRP_index.loc[ :, "track_x1" ] = np.nan
#        df_protons_multiRP_index.loc[ :, "track_x2" ] = np.nan
#        df_protons_multiRP_index.loc[ :, "track_y1" ] = np.nan
#        df_protons_multiRP_index.loc[ :, "track_y2" ] = np.nan
#        
#        df_protons_multiRP_index.loc[ :, "track_x1" ].loc[ df_protons_multiRP_index.loc[ :, "arm" ] == 0 ] = df_ppstracks_index.loc[:, "x"].loc[ df_ppstracks_index.loc[ :, "rpid" ] == 3 ]
#        df_protons_multiRP_index.loc[ :, "track_x2" ].loc[ df_protons_multiRP_index.loc[ :, "arm" ] == 0 ] = df_ppstracks_index.loc[:, "x"].loc[ df_ppstracks_index.loc[ :, "rpid" ] == 23 ]
#        df_protons_multiRP_index.loc[ :, "track_y1" ].loc[ df_protons_multiRP_index.loc[ :, "arm" ] == 0 ] = df_ppstracks_index.loc[:, "y"].loc[ df_ppstracks_index.loc[ :, "rpid" ] == 3 ]
#        df_protons_multiRP_index.loc[ :, "track_y2" ].loc[ df_protons_multiRP_index.loc[ :, "arm" ] == 0 ] = df_ppstracks_index.loc[:, "y"].loc[ df_ppstracks_index.loc[ :, "rpid" ] == 23 ]
#        df_protons_multiRP_index.loc[ :, "track_x1" ].loc[ df_protons_multiRP_index.loc[ :, "arm" ] == 1 ] = df_ppstracks_index.loc[:, "x"].loc[ df_ppstracks_index.loc[ :, "rpid" ] == 103 ]
#        df_protons_multiRP_index.loc[ :, "track_x2" ].loc[ df_protons_multiRP_index.loc[ :, "arm" ] == 1 ] = df_ppstracks_index.loc[:, "x"].loc[ df_ppstracks_index.loc[ :, "rpid" ] == 123 ]
#        df_protons_multiRP_index.loc[ :, "track_y1" ].loc[ df_protons_multiRP_index.loc[ :, "arm" ] == 1 ] = df_ppstracks_index.loc[:, "y"].loc[ df_ppstracks_index.loc[ :, "rpid" ] == 103 ]
#        df_protons_multiRP_index.loc[ :, "track_y2" ].loc[ df_protons_multiRP_index.loc[ :, "arm" ] == 1 ] = df_ppstracks_index.loc[:, "y"].loc[ df_ppstracks_index.loc[ :, "rpid" ] == 123 ]

    # run_str_ = "run_rnd" if ( random_protons or mix_protons ) else "run"
    run_str_ = "run"
    if random_protons or mix_protons:
        run_str_ = "run_rnd"
    elif runOnMC and not mix_protons:
        run_str_ = "run_mc"

    xangle_str_ = "crossingAngle"
    if random_protons or mix_protons:
        xangle_str_ = "crossingAngle_rnd"

    if "period" not in df_protons_multiRP.columns:
        df_protons_multiRP.loc[ :, "period" ] = np.nan
        for idx_ in range( df_run_ranges.shape[0] ):
            msk_period_ = ( ( df_protons_multiRP.loc[ :, run_str_ ] >= df_run_ranges.iloc[ idx_ ][ "min" ] ) & ( df_protons_multiRP.loc[ :, run_str_ ] <= df_run_ranges.iloc[ idx_ ][ "max" ] ) )
            sum_period_ = np.sum( msk_period_ )
            if sum_period_ > 0:
                period_key_ = df_run_ranges.index[ idx_ ]
                df_protons_multiRP.loc[ :, "period" ].loc[ msk_period_ ] = period_key_
                print ( "{}: {}".format( period_key_, sum_period_ ) )
        print ( df_protons_multiRP.loc[ :, "period" ] )

    if within_aperture:
        # df_protons_multiRP.loc[ :, "period" ] = np.nan
        # for idx_ in range( df_run_ranges.shape[0] ):
        #     msk_period_ = ( ( df_protons_multiRP.loc[ :, run_str_ ] >= df_run_ranges.iloc[ idx_ ][ "min" ] ) & ( df_protons_multiRP.loc[ :, run_str_ ] <= df_run_ranges.iloc[ idx_ ][ "max" ] ) )
        #     sum_period_ = np.sum( msk_period_ )
        #     if sum_period_ > 0:
        #         period_key_ = df_run_ranges.index[ idx_ ]
        #         df_protons_multiRP.loc[ :, "period" ].loc[ msk_period_ ] = period_key_
        #         print ( "{}: {}".format( period_key_, sum_period_ ) )

        # df_protons_multiRP.loc[ :, "within_aperture" ] = df_protons_multiRP[ [ "period", "arm", "xi", "thx" ] ].apply(
        #         lambda row: check_aperture( aperture_period_map[ row["period"] ], row["arm"], 120., row["xi"], row["thx"] ), # FIXME
        #         axis=1
        #         )
        df_protons_multiRP.loc[ :, "within_aperture" ] = df_protons_multiRP[ [ "period", xangle_str_, "arm", "xi", "thx" ] ].apply(
                lambda row: check_aperture( aperture_period_map[ row[ "period" ] ], row[ "arm" ], row[ xangle_str_ ], row[ "xi" ], row[ "thx" ] ),
                axis=1
                )
        print ( df_protons_multiRP.loc[ :, "within_aperture" ] )
        print ( "Within aperture: {}".format( np.sum( df_protons_multiRP.loc[ :, "within_aperture" ] ) ) )
    
    index_vars_ = None
    if not use_hash_index:
        index_vars_ = ['run', 'lumiblock', 'event', 'slice']
    else:
        from pandas.util import hash_array
        arr_hash_id_protons_multiRP_jet0_pt_ = hash_array( df_protons_multiRP.loc[ :, 'jet0_pt' ].values  )
        df_protons_multiRP.loc[ :, "hash_id" ] = arr_hash_id_protons_multiRP_jet0_pt_
        print ( df_protons_multiRP.loc[ :, "hash_id" ] )
        index_vars_ = ['run', 'lumiblock', 'event', 'hash_id', 'slice']
    print ( index_vars_ )
    # df_protons_multiRP_index = df_protons_multiRP.set_index( ['run', 'lumiblock', 'event', 'slice'] )
    df_protons_multiRP_index = df_protons_multiRP.set_index( index_vars_ )

    msk_multiRP = ( df_protons_multiRP_index[ "ismultirp" ] == 1 )
    df_protons_multiRP_index = df_protons_multiRP_index.loc[ msk_multiRP ]

    msk1_arm = ( df_protons_multiRP_index[ "arm" ] == 0 )
    msk2_arm = ( df_protons_multiRP_index[ "arm" ] == 1 )

    msk_pixshift = ( ( df_protons_multiRP_index[ "trackpixshift1" ] == 0 ) &
                     ( df_protons_multiRP_index[ "trackpixshift2" ] == 0 ) )

#    track_angle_cut_ = 0.02
    msk_fid = None
    if apply_fiducial:
        df_protons_multiRP_index.loc[ :, "xlow" ] = np.nan
        df_protons_multiRP_index.loc[ :, "xhigh" ] = np.nan
        df_protons_multiRP_index.loc[ :, "ylow" ] = np.nan
        df_protons_multiRP_index.loc[ :, "yhigh" ] = np.nan
        df_protons_multiRP_index.loc[ :, "xlow" ].where( ~msk1_arm, fiducialXLow_all[ 0 ][ 2 ] , inplace=True )
        df_protons_multiRP_index.loc[ :, "xhigh" ].where( ~msk1_arm, fiducialXHigh_all[ 0 ][ 2 ] , inplace=True )
        df_protons_multiRP_index.loc[ :, "ylow" ].where( ~msk1_arm, fiducialYLow_all[ 0 ][ 2 ] , inplace=True )
        df_protons_multiRP_index.loc[ :, "yhigh" ].where( ~msk1_arm, fiducialYHigh_all[ 0 ][ 2 ] , inplace=True )
        df_protons_multiRP_index.loc[ :, "xlow" ].where( ~msk2_arm, fiducialXLow_all[ 1 ][ 2 ] , inplace=True )
        df_protons_multiRP_index.loc[ :, "xhigh" ].where( ~msk2_arm, fiducialXHigh_all[ 1 ][ 2 ] , inplace=True )
        df_protons_multiRP_index.loc[ :, "ylow" ].where( ~msk2_arm, fiducialYLow_all[ 1 ][ 2 ] , inplace=True )
        df_protons_multiRP_index.loc[ :, "yhigh" ].where( ~msk2_arm, fiducialYHigh_all[ 1 ][ 2 ] , inplace=True )

#        msk_fid = ( ( np.abs(df_protons_multiRP_index[""]) <= track_angle_cut_ ) &
#                    ( np.abs(df_protons_multiRP_index[""]) <= track_angle_cut_ ) )

        msk_fid = ( ( df_protons_multiRP_index.loc[ :, "trackx2"] >= df_protons_multiRP_index.loc[ :, "xlow" ] ) &
                    ( df_protons_multiRP_index.loc[ :, "trackx2"] <= df_protons_multiRP_index.loc[ :, "xhigh" ] ) &
                    ( df_protons_multiRP_index.loc[ :, "tracky2"] >= df_protons_multiRP_index.loc[ :, "ylow" ] ) &
                    ( df_protons_multiRP_index.loc[ :, "tracky2"] <= df_protons_multiRP_index.loc[ :, "yhigh" ] ) )

    msk_aperture = None
    if within_aperture:
        msk_aperture = df_protons_multiRP_index.loc[ :, "within_aperture" ]

    msk1 = msk1_arm & msk_pixshift
    msk2 = msk2_arm & msk_pixshift
    if msk_fid is not None:
        msk1 = msk1 & msk_fid
        msk2 = msk2 & msk_fid
    if msk_aperture is not None:
        msk1 = msk1 & msk_aperture
        msk2 = msk2 & msk_aperture

    df_protons_multiRP_index = df_protons_multiRP_index.loc[ msk1 | msk2 ]

    # df_protons_multiRP_groupby = df_protons_multiRP_index[ [ "arm" ] ].groupby( ["run","lumiblock","event","slice"] )
    # msk_2protons = df_protons_multiRP_groupby[ "arm" ].transform( lambda s_: ( np.sum( s_ == 0 ) >= 1 ) & ( np.sum( s_ == 1 ) >= 1 ) )
    # df_protons_multiRP_index = df_protons_multiRP_index.loc[ msk_2protons ]

    columns_eff_ = []

    # if runOnMC:
    #     if lepton_type == 'muon': 
    #         # Muon scale factor
    #         from muon_efficiency import MuonScaleFactor
    #         file_eff_MuID = ROOT.TFile.Open( "efficiencies/muon/RunBCDEF_SF_MuID.root", "READ" )
    #         muon_scale_factor_ = MuonScaleFactor( histos={ "MuID": file_eff_MuID.Get( "NUM_TightID_DEN_genTracks_pt_abseta" ) } )
    #         f_sf_muon_id_ = lambda row: muon_scale_factor_( row["muon0_pt"], row["muon0_eta"] )[ 0 ]
    #         f_sf_muon_id_unc_ = lambda row: muon_scale_factor_( row["muon0_pt"], row["muon0_eta"] )[ 1 ]
    #         df_protons_multiRP_index.loc[ :, 'sf_muon_id' ] = df_protons_multiRP_index[ ["muon0_pt", "muon0_eta"] ].apply( f_sf_muon_id_, axis=1 )
    #         df_protons_multiRP_index.loc[ :, 'sf_muon_id_unc' ] = df_protons_multiRP_index[ ["muon0_pt", "muon0_eta"] ].apply( f_sf_muon_id_unc_, axis=1 )
    #         df_protons_multiRP_index.loc[ :, 'sf_muon_id_up' ] = ( df_protons_multiRP_index.loc[ :, 'sf_muon_id' ] + df_protons_multiRP_index.loc[ :, 'sf_muon_id_unc' ] )
    #         df_protons_multiRP_index.loc[ :, 'sf_muon_id_dw' ] = ( df_protons_multiRP_index.loc[ :, 'sf_muon_id' ] - df_protons_multiRP_index.loc[ :, 'sf_muon_id_unc' ] )
    #     elif lepton_type == 'electron': 
    #         # Electron scale factor
    #         from electron_efficiency import ElectronScaleFactor
    #         file_eff_EleID = ROOT.TFile.Open( "efficiencies/electron/2017_ElectronTight.root", "READ" )
    #         electron_scale_factor_ = ElectronScaleFactor( histos={ "EleID": file_eff_EleID.Get( "EGamma_SF2D" ) } )
    #         f_sf_electron_id_ = lambda row: electron_scale_factor_( row["electron0_pt"], row["electron0_eta"] )[ 0 ]
    #         f_sf_electron_id_unc_ = lambda row: electron_scale_factor_( row["electron0_pt"], row["electron0_eta"] )[ 1 ]
    #         df_protons_multiRP_index.loc[ :, 'sf_electron_id' ] = df_protons_multiRP_index[ ["electron0_pt", "electron0_eta"] ].apply( f_sf_electron_id_, axis=1 )
    #         df_protons_multiRP_index.loc[ :, 'sf_electron_id_unc' ] = df_protons_multiRP_index[ ["electron0_pt", "electron0_eta"] ].apply( f_sf_electron_id_unc_, axis=1 )
    #         df_protons_multiRP_index.loc[ :, 'sf_electron_id_up' ] = ( df_protons_multiRP_index.loc[ :, 'sf_electron_id' ] + df_protons_multiRP_index.loc[ :, 'sf_electron_id_unc' ] )
    #         df_protons_multiRP_index.loc[ :, 'sf_electron_id_dw' ] = ( df_protons_multiRP_index.loc[ :, 'sf_electron_id' ] - df_protons_multiRP_index.loc[ :, 'sf_electron_id_unc' ] )

    if runOnMC and not mix_protons:
        if data_sample == '2017': 
            # efficiencies_2017
            from proton_efficiency import efficiencies_2017, strict_zero_efficiencies, proton_efficiency_uncertainty
            strips_multitrack_efficiency, strips_sensor_efficiency, multiRP_efficiency, file_eff_strips, file_eff_multiRP = efficiencies_2017()
            sz_efficiencies = strict_zero_efficiencies()

            data_periods = [ "2017B", "2017C1", "2017C2", "2017D", "2017E", "2017F1", "2017F2", "2017F3" ]

            lumi_periods_ = None
            if lepton_type == 'muon':
                lumi_periods_ = lumi_periods_2017[ 'muon' ]
            elif lepton_type == 'electron':
                lumi_periods_ = lumi_periods_2017[ 'electron' ]

            proton_eff_unc_per_arm_ = proton_efficiency_uncertainty[ "2017" ]

            df_protons_multiRP_index.loc[ :, 'eff_proton_all_weighted' ] = 0.
            # df_protons_multiRP_index.loc[ :, 'eff_all_weighted' ] = 0.
            df_protons_multiRP_index.loc[ :, 'eff_multitrack_weighted' ] = 0.
            df_protons_multiRP_index.loc[ :, 'eff_strictzero_weighted' ] = 0.
            for period_ in data_periods:
                f_eff_strips_multitrack_ = lambda row: strips_multitrack_efficiency[ period_ ][ "45" if row["arm"] == 0 else "56" ].GetBinContent( 1 )
    
                f_eff_strips_sensor_     = lambda row: strips_sensor_efficiency[ period_ ][ "45" if row["arm"] == 0 else "56" ].GetBinContent(
                                                strips_sensor_efficiency[ period_ ][ "45" if row["arm"] == 0 else "56" ].FindBin( row["trackx2"], row["tracky2"] )
                                                )
    
                f_eff_multiRP_           = lambda row: multiRP_efficiency[ period_ ][ "45" if row["arm"] == 0 else "56" ].GetBinContent(
                                                multiRP_efficiency[ period_ ][ "45" if row["arm"] == 0 else "56" ].FindBin( row["trackx1"], row["tracky1"] )
                                                )
    
                f_eff_strips_strictzero_ = lambda row: sz_efficiencies[ period_ ][ "45" if row["arm"] == 0 else "56" ][ int( ( row["crossingAngle"] // 10 ) * 10 ) ]

                f_eff_proton_all_        = lambda row: f_eff_strips_sensor_(row) * f_eff_multiRP_(row)

                # f_eff_all_               = lambda row: f_eff_strips_sensor_(row) * f_eff_multiRP_(row) * f_eff_strips_multitrack_(row)

                df_protons_multiRP_index.loc[ :, 'eff_proton_all_' + period_ ] = df_protons_multiRP_index[ ["arm", "trackx1", "tracky1", "trackx2", "tracky2"] ].apply( f_eff_proton_all_, axis=1 )
                df_protons_multiRP_index.loc[ :, 'eff_proton_all_weighted' ] = df_protons_multiRP_index.loc[ :, 'eff_proton_all_weighted' ] + lumi_periods_[ period_ ] * df_protons_multiRP_index.loc[ :, 'eff_proton_all_' + period_ ]
                # df_protons_multiRP_index.loc[ :, 'eff_all_' + period_ ] = df_protons_multiRP_index[ ["arm", "trackx1", "tracky1", "trackx2", "tracky2"] ].apply( f_eff_all_, axis=1 )
                # df_protons_multiRP_index.loc[ :, 'eff_all_weighted' ] = df_protons_multiRP_index.loc[ :, 'eff_all_weighted' ] + lumi_periods_[ period_ ] * df_protons_multiRP_index.loc[ :, 'eff_all_' + period_ ]
                df_protons_multiRP_index.loc[ :, 'eff_multitrack_' + period_ ] = df_protons_multiRP_index[ [ "arm" ] ].apply( f_eff_strips_multitrack_, axis=1 )
                df_protons_multiRP_index.loc[ :, 'eff_multitrack_weighted' ] = df_protons_multiRP_index.loc[ :, 'eff_multitrack_weighted' ] + lumi_periods_[ period_ ] * df_protons_multiRP_index.loc[ :, 'eff_multitrack_' + period_ ]
                df_protons_multiRP_index.loc[ :, 'eff_strictzero_' + period_ ] = df_protons_multiRP_index[ [ "arm", "crossingAngle" ] ].apply( f_eff_strips_strictzero_, axis=1 )
                df_protons_multiRP_index.loc[ :, 'eff_strictzero_weighted' ] = df_protons_multiRP_index.loc[ :, 'eff_strictzero_weighted' ] + lumi_periods_[ period_ ] * df_protons_multiRP_index.loc[ :, 'eff_strictzero_' + period_ ]
                columns_eff_.append( 'eff_proton_all_' + period_ )        
                # columns_eff_.append( 'eff_all_' + period_ )        
                columns_eff_.append( 'eff_multitrack_' + period_ )        
                columns_eff_.append( 'eff_strictzero_' + period_ )        
            columns_eff_.append( 'eff_proton_all_weighted' ) 
            # columns_eff_.append( 'eff_all_weighted' ) 
            columns_eff_.append( 'eff_multitrack_weighted' ) 
            columns_eff_.append( 'eff_strictzero_weighted' )

            lumi_ = np.sum( list( lumi_periods_.values() ) )
            df_protons_multiRP_index.loc[ :, 'eff_proton_all_weighted' ] = df_protons_multiRP_index.loc[ :, 'eff_proton_all_weighted' ] / lumi_
            # df_protons_multiRP_index.loc[ :, 'eff_all_weighted' ] = df_protons_multiRP_index.loc[ :, 'eff_all_weighted' ] / lumi_
            df_protons_multiRP_index.loc[ :, 'eff_multitrack_weighted' ] = df_protons_multiRP_index.loc[ :, 'eff_multitrack_weighted' ] / lumi_
            df_protons_multiRP_index.loc[ :, 'eff_strictzero_weighted' ] = df_protons_multiRP_index.loc[ :, 'eff_strictzero_weighted' ] / lumi_

            f_eff_strips_multitrack_ = lambda row: strips_multitrack_efficiency[ row["period"] ][ "45" if row["arm"] == 0 else "56" ].GetBinContent( 1 )
    
            f_eff_strips_sensor_     = lambda row: strips_sensor_efficiency[ row["period"] ][ "45" if row["arm"] == 0 else "56" ].GetBinContent(
                                            strips_sensor_efficiency[ row["period"] ][ "45" if row["arm"] == 0 else "56" ].FindBin( row["trackx2"], row["tracky2"] )
                                            )
    
            f_eff_multiRP_           = lambda row: multiRP_efficiency[ row["period"] ][ "45" if row["arm"] == 0 else "56" ].GetBinContent(
                                            multiRP_efficiency[ row["period"] ][ "45" if row["arm"] == 0 else "56" ].FindBin( row["trackx1"], row["tracky1"] )
                                            )
    
            f_eff_strips_strictzero_ = lambda row: sz_efficiencies[ row["period"] ][ "45" if row["arm"] == 0 else "56" ][ int( ( row["crossingAngle"] // 10 ) * 10 ) ]

            f_eff_proton_all_        = lambda row: f_eff_strips_sensor_(row) * f_eff_multiRP_(row)
            df_protons_multiRP_index.loc[ :, 'eff_proton_all' ] = df_protons_multiRP_index[ [ "period", "arm", "trackx1", "tracky1", "trackx2", "tracky2" ] ].apply( f_eff_proton_all_, axis=1 )
            df_protons_multiRP_index.loc[ :, 'eff_multitrack' ] = df_protons_multiRP_index[ [ "period", "arm" ] ].apply( f_eff_strips_multitrack_, axis=1 )
            df_protons_multiRP_index.loc[ :, 'eff_strictzero' ] = df_protons_multiRP_index[ [ "period", "arm", "crossingAngle" ] ].apply( f_eff_strips_strictzero_, axis=1 )
            columns_eff_.append( 'eff_proton_all' ) 
            columns_eff_.append( 'eff_multitrack' ) 
            columns_eff_.append( 'eff_strictzero' )

            f_eff_proton_unc_ = lambda row: proton_eff_unc_per_arm_[ "45" if row["arm"] == 0 else "56" ]
            df_protons_multiRP_index.loc[ :, 'eff_proton_unc' ] = df_protons_multiRP_index[ [ "arm" ] ].apply( f_eff_proton_unc_, axis=1 )
            columns_eff_.append( 'eff_proton_unc' ) 
        elif data_sample == '2018': 
            # efficiencies_2018
            from proton_efficiency import efficiencies_2018, proton_efficiency_uncertainty
            sensor_near_efficiency, multiRP_efficiency, file_eff_rad_near, file_eff_multiRP = efficiencies_2018()

            data_periods = [ "2018A", "2018B1", "2018B2", "2018C", "2018D1", "2018D2" ]

            lumi_periods_ = None
            if lepton_type == 'muon':
                lumi_periods_ = lumi_periods_2018[ 'muon' ]
            elif lepton_type == 'electron':
                lumi_periods_ = lumi_periods_2018[ 'electron' ]

            proton_eff_unc_per_arm_ = proton_efficiency_uncertainty[ "2018" ]

            df_protons_multiRP_index.loc[ :, 'eff_proton_all_weighted' ] = 0.
            for period_ in data_periods:
                f_eff_sensor_near_       = lambda row: sensor_near_efficiency[ period_ ][ "45" if row["arm"] == 0 else "56" ].GetBinContent(
                                                sensor_near_efficiency[ period_ ][ "45" if row["arm"] == 0 else "56" ].FindBin( row["trackx1"], row["tracky1"] )
                                                )
    
                f_eff_multiRP_           = lambda row: multiRP_efficiency[ period_ ][ "45" if row["arm"] == 0 else "56" ].GetBinContent(
                                                multiRP_efficiency[ period_ ][ "45" if row["arm"] == 0 else "56" ].FindBin( row["trackx1"], row["tracky1"] )
                                                )

                f_eff_proton_all_        = lambda row: f_eff_sensor_near_(row) * f_eff_multiRP_(row)

                df_protons_multiRP_index.loc[ :, 'eff_proton_all_' + period_ ] = df_protons_multiRP_index[ ["arm", "trackx1", "tracky1"] ].apply( f_eff_proton_all_, axis=1 )
                df_protons_multiRP_index.loc[ :, 'eff_proton_all_weighted' ] = df_protons_multiRP_index.loc[ :, 'eff_proton_all_weighted' ] + lumi_periods_[ period_ ] * df_protons_multiRP_index.loc[ :, 'eff_proton_all_' + period_ ]
                columns_eff_.append( 'eff_proton_all_' + period_ )        
            columns_eff_.append( 'eff_proton_all_weighted' ) 

            lumi_ = np.sum( list( lumi_periods_.values() ) )
            df_protons_multiRP_index.loc[ :, 'eff_proton_all_weighted' ] = df_protons_multiRP_index.loc[ :, 'eff_proton_all_weighted' ] / lumi_

            f_eff_sensor_near_       = lambda row: sensor_near_efficiency[ row["period"] ][ "45" if row["arm"] == 0 else "56" ].GetBinContent(
                                            sensor_near_efficiency[ row["period"] ][ "45" if row["arm"] == 0 else "56" ].FindBin( row["trackx1"], row["tracky1"] )
                                            )
    
            f_eff_multiRP_           = lambda row: multiRP_efficiency[ row["period"] ][ "45" if row["arm"] == 0 else "56" ].GetBinContent(
                                            multiRP_efficiency[ row["period"] ][ "45" if row["arm"] == 0 else "56" ].FindBin( row["trackx1"], row["tracky1"] )
                                            )
    
            f_eff_proton_all_        = lambda row: f_eff_sensor_near_(row) * f_eff_multiRP_(row)
            df_protons_multiRP_index.loc[ :, 'eff_proton_all' ] = df_protons_multiRP_index[ [ "period", "arm", "trackx1", "tracky1" ] ].apply( f_eff_proton_all_, axis=1 )
            columns_eff_.append( 'eff_proton_all' ) 

            f_eff_proton_unc_ = lambda row: proton_eff_unc_per_arm_[ "45" if row["arm"] == 0 else "56" ]
            df_protons_multiRP_index.loc[ :, 'eff_proton_unc' ] = df_protons_multiRP_index[ [ "arm" ] ].apply( f_eff_proton_unc_, axis=1 )
            columns_eff_.append( 'eff_proton_unc' ) 

    columns_drop_ = [ "xi", "thx", "thy", "t", "ismultirp", "rpid", "arm", "random",
                      "trackx1", "tracky1", "trackpixshift1", "rpid1",
                      "trackx2", "tracky2", "trackpixshift2", "rpid2" ]
    if runOnMC:
        columns_drop_.extend( columns_eff_ )
    print ( columns_drop_ )

    # df_protons_multiRP_events, df_protons_multiRP_index_2protons = process_events( data_sample, df_protons_multiRP_index, runOnMC=runOnMC, mix_protons=mix_protons, columns_drop=columns_drop_ )
    df_protons_multiRP_events, df_protons_multiRP_index_2protons = process_events( data_sample, df_protons_multiRP_index, runOnMC=runOnMC, mix_protons=mix_protons, columns_drop=columns_drop_, use_hash_index=use_hash_index )

    if select_2protons:
        df_protons_multiRP_index = df_protons_multiRP_index_2protons

    print ( df_protons_multiRP_index )

    return (df_protons_multiRP_index, df_protons_multiRP_events, df_ppstracks_index)

def process_events( data_sample, df_protons_multiRP_index, runOnMC=False, mix_protons=False, columns_drop=None, use_hash_index=False ):

    index_vars_ = None
    if not use_hash_index:
        index_vars_ = ['run', 'lumiblock', 'event', 'slice']
    else:
        index_vars_ = ['run', 'lumiblock', 'event', 'hash_id', 'slice']
    print ( index_vars_ )
   
    # df_protons_multiRP_groupby_byarm_xi_max = df_protons_multiRP_index[ [ "arm", "xi" ] ].groupby( ["run","lumiblock","event","slice","arm"] )
    groupby_vars_ = index_vars_.copy()
    groupby_vars_.append( 'arm' )
    df_protons_multiRP_groupby_byarm_xi_max = df_protons_multiRP_index[ [ "arm", "xi" ] ].groupby( groupby_vars_ )
    msk_xi_max = df_protons_multiRP_groupby_byarm_xi_max[ "xi" ].transform( lambda s_: ( s_ == s_.max() ) )
    print ( msk_xi_max )
    df_protons_multiRP_index_xi_max = df_protons_multiRP_index.loc[ msk_xi_max ]

    # df_protons_multiRP_groupby_arm = df_protons_multiRP_index[ [ "arm" ] ].groupby( ["run","lumiblock","event","slice"] )
    # msk_2protons = df_protons_multiRP_groupby_arm[ "arm" ].transform( lambda s_: ( np.sum( s_ == 0 ) >= 1 ) & ( np.sum( s_ == 1 ) >= 1 ) )
    # print ( msk_2protons )
    # df_protons_multiRP_index_2protons = df_protons_multiRP_index.loc[ msk_2protons ]
    # df_protons_multiRP_groupby_arm = df_protons_multiRP_index_xi_max[ [ "arm" ] ].groupby( ["run","lumiblock","event","slice"] )
    df_protons_multiRP_groupby_arm = df_protons_multiRP_index_xi_max[ [ "arm" ] ].groupby( index_vars_ )
    msk_2protons = df_protons_multiRP_groupby_arm[ "arm" ].transform( lambda s_: ( np.sum( s_ == 0 ) == 1 ) & ( np.sum( s_ == 1 ) == 1 ) )
    print ( msk_2protons )
    df_protons_multiRP_index_2protons = df_protons_multiRP_index_xi_max.loc[ msk_2protons ]

    var_list_ = None
    if data_sample == '2017':
        var_list_ = [ "arm", "xi", "eff_proton_all_weighted", "eff_multitrack_weighted", "eff_strictzero_weighted", "eff_proton_all", "eff_multitrack", "eff_strictzero", "eff_proton_unc" ] if ( runOnMC and not mix_protons ) else [ "arm", "xi" ]
    elif data_sample == '2018':
        var_list_ = [ "arm", "xi", "eff_proton_all_weighted", "eff_proton_all", "eff_proton_unc" ] if ( runOnMC and not mix_protons ) else [ "arm", "xi" ]

    # labels_xi_ = [ "_nom", "_p10", "_p30", "_p60", "_p100", "_m10", "_m30", "_m60", "_m100" ]
    labels_xi_ = [ "_nom", "_p100", "_m100" ]
    if runOnMC:
        var_list_.extend( [ "xi" + label_ for label_ in labels_xi_ ] )

    # df_protons_multiRP_2protons_groupby = df_protons_multiRP_index_2protons[ var_list_ ].groupby( ["run","lumiblock","event","slice"] )
    df_protons_multiRP_2protons_groupby = df_protons_multiRP_index_2protons[ var_list_ ].groupby( index_vars_ )

    if runOnMC:
        columns_drop.extend( [ "xi" + label_ for label_ in labels_xi_ ] )

    df_protons_multiRP_events = df_protons_multiRP_index_2protons.drop( columns=columns_drop )
    df_protons_multiRP_events = df_protons_multiRP_events[ ~df_protons_multiRP_events.index.duplicated(keep='first') ]
    print ( "Number of events: {}".format( df_protons_multiRP_events.shape[0] ) )

    # df_protons_multiRP_events.loc[ :, "MX" ] = df_protons_multiRP_2protons_groupby[ "xi" ].agg(
    #     lambda s_: 13000. * np.sqrt( s_.iloc[0] * s_.iloc[1] )
    #     )
    df_protons_multiRP_events.loc[ :, "MX" ] = df_protons_multiRP_2protons_groupby[ "xi" ].agg(
        lambda s_: 13000. * np.sqrt( s_.iloc[0] * s_.iloc[1] )
        )
    print ( df_protons_multiRP_events.loc[ :, "MX" ] )
    df_protons_multiRP_events.loc[ :, "YX" ] = df_protons_multiRP_2protons_groupby[ ["arm", "xi"] ].apply(
        lambda df__: 0.5 * np.log( df__[ "xi" ][ df__[ "arm" ] == 0 ].iloc[0] / df__[ "xi" ][ df__[ "arm" ] == 1 ].iloc[0] )
        )
    print ( df_protons_multiRP_events.loc[ :, "YX" ] )
    df_protons_multiRP_events.loc[ :, "diffMWW_MX" ]  = df_protons_multiRP_events[ "recoMWW" ] - df_protons_multiRP_events[ "MX" ]
    df_protons_multiRP_events.loc[ :, "ratioMWW_MX" ] = df_protons_multiRP_events[ "recoMWW" ] / df_protons_multiRP_events[ "MX" ]
    df_protons_multiRP_events.loc[ :, "shiftedRatioMWW_MX" ] = df_protons_multiRP_events[ "ratioMWW_MX" ] - 1.
    df_protons_multiRP_events.loc[ :, "diffYWW_YX" ]  = df_protons_multiRP_events[ "recoRapidityWW" ] - df_protons_multiRP_events[ "YX" ]
    df_protons_multiRP_events.loc[ :, "MX" + "_nom" ] = df_protons_multiRP_events.loc[ :, "MX" ]
    df_protons_multiRP_events.loc[ :, "YX" + "_nom" ] = df_protons_multiRP_events.loc[ :, "YX" ]
    df_protons_multiRP_events.loc[ :, "R_MWW_MX" + "_nom" ] = ( df_protons_multiRP_events.loc[ :, "MWW" + "_nom" ] / df_protons_multiRP_events.loc[ :, "MX" + "_nom" ] )
    df_protons_multiRP_events.loc[ :, "Diff_YWW_YX" + "_nom" ] = ( df_protons_multiRP_events.loc[ :, "YWW" + "_nom" ] - df_protons_multiRP_events.loc[ :, "YX" + "_nom" ] )

    if runOnMC:
        # for label_ in [ "_jes_up", "_jes_dw" ]:
        for label_ in [ "_jes_up", "_jes_dw", "_jer_up", "_jer_dw" ]:
            df_protons_multiRP_events.loc[ :, "R_MWW_MX" + label_ ] = ( df_protons_multiRP_events.loc[ :, "MWW" + label_ ] / df_protons_multiRP_events.loc[ :, "MX" + "_nom" ] ) 
            df_protons_multiRP_events.loc[ :, "Diff_YWW_YX" + label_ ] = ( df_protons_multiRP_events.loc[ :, "YWW" + label_ ] - df_protons_multiRP_events.loc[ :, "YX" + "_nom" ] )

        for label0_ in labels_xi_:
            for label1_ in labels_xi_:
                vars__ = [ "arm", "xi" + label0_ ] if label0_ == label1_  else [ "arm", "xi" + label0_, "xi" + label1_ ]
                print ( "MX" + label0_ + label1_ )
                df_protons_multiRP_2protons_groupby_apply_MX_ = df_protons_multiRP_2protons_groupby[ vars__ ].apply(
                    lambda df__: 13000. * np.sqrt( df__[ "xi" + label0_ ][ df__[ "arm" ] == 0 ].iloc[0] * df__[ "xi" + label1_ ][ df__[ "arm" ] == 1 ].iloc[0] )
                    )
                df_protons_multiRP_events.loc[ :, "MX" + label0_ + label1_ ] = df_protons_multiRP_2protons_groupby_apply_MX_
                # print ( df_protons_multiRP_events.loc[ :, "MX" + label0_ + label1_ ] )
                print ( "YX" + label0_ + label1_ )
                df_protons_multiRP_2protons_groupby_apply_YX_ = df_protons_multiRP_2protons_groupby[ vars__ ].apply(
                    lambda df__: 0.5 * np.log( df__[ "xi" + label0_ ][ df__[ "arm" ] == 0 ].iloc[0] / df__[ "xi" + label1_ ][ df__[ "arm" ] == 1 ].iloc[0] )
                    )
                df_protons_multiRP_events.loc[ :, "YX" + label0_ + label1_ ] = df_protons_multiRP_2protons_groupby_apply_YX_
                # print ( df_protons_multiRP_events.loc[ :, "YX" + label0_ + label1_ ] )
                print ( "R_MWW_MX" + label0_ + label1_ )
                df_protons_multiRP_events.loc[ :, "R_MWW_MX" + label0_ + label1_ ] = ( df_protons_multiRP_events.loc[ :, "MWW" + "_nom" ] / df_protons_multiRP_events.loc[ :, "MX" + label0_ + label1_ ] )
                # print ( df_protons_multiRP_events.loc[ :, "R_MWW_MX" + label0_ + label1_ ] )
                print ( "Diff_YWW_YX" + label0_ + label1_ )
                df_protons_multiRP_events.loc[ :, "Diff_YWW_YX" + label0_ + label1_ ] = ( df_protons_multiRP_events.loc[ :, "YWW" + "_nom" ] - df_protons_multiRP_events.loc[ :, "YX" + label0_ + label1_ ] )
                # print ( df_protons_multiRP_events.loc[ :, "Diff_YWW_YX" + label0_ + label1_ ] )

    if runOnMC and not mix_protons:
        df_protons_multiRP_events.loc[ :, "eff_proton_all_weighted" ] = df_protons_multiRP_2protons_groupby[ "eff_proton_all_weighted" ].agg(
            lambda s_: ( s_.iloc[0] * s_.iloc[1] )
            )
        print ( df_protons_multiRP_events.loc[ :, "eff_proton_all_weighted" ] )
        # df_protons_multiRP_events.loc[ :, "eff_all_weighted" ] = df_protons_multiRP_2protons_groupby[ "eff_all_weighted" ].agg(
        #     lambda s_: ( s_.iloc[0] * s_.iloc[1] )
        #     )
        # print ( df_protons_multiRP_events.loc[ :, "eff_all_weighted" ] )
        if data_sample == '2017':
            df_protons_multiRP_events.loc[ :, "eff_multitrack_weighted" ] = df_protons_multiRP_2protons_groupby[ "eff_multitrack_weighted" ].agg(
                lambda s_: ( s_.iloc[0] * s_.iloc[1] )
                )
            print ( df_protons_multiRP_events.loc[ :, "eff_multitrack_weighted" ] )
            df_protons_multiRP_events.loc[ :, "eff_strictzero_weighted" ] = df_protons_multiRP_2protons_groupby[ "eff_strictzero_weighted" ].agg(
                lambda s_: ( s_.iloc[0] * s_.iloc[1] )
                )
            print ( df_protons_multiRP_events.loc[ :, "eff_strictzero_weighted" ] )

        df_protons_multiRP_events.loc[ :, "eff_proton_all" ] = df_protons_multiRP_2protons_groupby[ "eff_proton_all" ].agg(
            lambda s_: ( s_.iloc[0] * s_.iloc[1] )
            )
        print ( df_protons_multiRP_events.loc[ :, "eff_proton_all" ] )
        if data_sample == '2017':
            df_protons_multiRP_events.loc[ :, "eff_multitrack" ] = df_protons_multiRP_2protons_groupby[ "eff_multitrack" ].agg(
                lambda s_: ( s_.iloc[0] * s_.iloc[1] )
                )
            print ( df_protons_multiRP_events.loc[ :, "eff_multitrack" ] )
            df_protons_multiRP_events.loc[ :, "eff_strictzero" ] = df_protons_multiRP_2protons_groupby[ "eff_strictzero" ].agg(
                lambda s_: ( s_.iloc[0] * s_.iloc[1] )
                )
            print ( df_protons_multiRP_events.loc[ :, "eff_strictzero" ] )

        df_protons_multiRP_events.loc[ :, "eff_proton_unc" ] = df_protons_multiRP_2protons_groupby[ "eff_proton_unc" ].agg(
            lambda s_: np.sqrt( s_.iloc[0] ** 2 + s_.iloc[1] ** 2 )
            )
        print ( df_protons_multiRP_events.loc[ :, "eff_proton_unc" ] )
        df_protons_multiRP_events.loc[ :, "eff_proton_var_up" ] = ( 1. + df_protons_multiRP_events.loc[ :, "eff_proton_unc" ] )
        df_protons_multiRP_events.loc[ :, "eff_proton_var_dw" ] = ( 1. - df_protons_multiRP_events.loc[ :, "eff_proton_unc" ] )
        print ( df_protons_multiRP_events.loc[ :, "eff_proton_var_up" ] )
        print ( df_protons_multiRP_events.loc[ :, "eff_proton_var_dw" ] )

    return ( df_protons_multiRP_events, df_protons_multiRP_index_2protons )

