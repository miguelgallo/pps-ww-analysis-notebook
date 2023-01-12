### Columnar data format
#### Data
python3 create_table_data.py

#### Signal
python3 create_table_signal.py

(condor) python3 create_table_signal_mix_protons.py

#### Background (proton mixing)
(condor)

python3 create_table_data_random_protons.py --period=2018A

python3 create_table_data_random_protons.py --period=2018B

python3 create_table_data_random_protons.py --period=2018C

python3 create_table_data_random_protons.py --period=2018D --start=0 --stop=200000

python3 create_table_data_random_protons.py --period=2018D --start=200000 --stop=400000

python3 create_table_data_random_protons.py --period=2018D --start=400000 --stop=600000

python3 create_table_data_random_protons.py --period=2018D --start=600000 --stop=800000

python3 create_table_data_random_protons.py --period=2018D --start=800000 --stop=1000000

python3 create_table_data_random_protons.py --period=2018D --start=1000000

### Data processing
#### Data
python3 process_data.py

#### Signal
python3 process_signal.py

python3 process_signal_mix_protons.py

python3 process_signal_plus_mix_events.py

#### Background (proton mixing)
(condor)

python3 process_data_random_protons.py --period=2018A

python3 process_data_random_protons.py --period=2018B

python3 process_data_random_protons.py --period=2018C

python3 process_data_random_protons.py --period=2018D-1

python3 process_data_random_protons.py --period=2018D-2

python3 process_data_random_protons.py --period=2018D-3

python3 process_data_random_protons.py --period=2018D-4

python3 process_data_random_protons.py --period=2018D-5

python3 process_data_random_protons.py --period=2018D-6
