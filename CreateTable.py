from create_table import create_table

class CreateTable:
    def __init__( self, label, lepton_type, data_sample, fileNames, tree_path, output_dir="" ):
        self.label_ = label
        self.data_sample_ = data_sample
        self.lepton_type_ = lepton_type
        self.fileNames_ = fileNames
        self.tree_path_ = tree_path
        self.output_dir_ = None
        if output_dir is not None and output_dir != "": self.output_dir_ = output_dir

    def __call__( self, mix_protons=False, proton_files=None, random_protons=False, resample_factor=-1, runOnMC=False, data_periods=None, step_size=100000, firstEvent=None, entryStop=None, debug=False ):

        for key_ in self.fileNames_:
            import time
            print( time.strftime("%Y/%m/%d %H:%M:%S", time.localtime() ) )
            time_s_ = time.time()

            print ( key_, self.fileNames_[ key_ ] )
            label__ = "{}-{}".format( self.label_, key_ )
            if firstEvent is not None and firstEvent >= 0:
                label__ = label__ + "-{}".format( firstEvent )
            if entryStop is not None and entryStop >= 0:
                label__ = label__ + "-{}".format( entryStop )

            create_table(
                self.fileNames_[ key_ ],
                label=label__,
                lepton_type=self.lepton_type_,
                data_sample=self.data_sample_,
                tree_path=self.tree_path_,
                mix_protons=mix_protons,
                proton_files=proton_files,
                random_protons=random_protons,
                resample_factor=resample_factor,
                runOnMC=runOnMC,
                data_periods=data_periods,
                step_size=step_size,
                firstEvent=firstEvent,
                entryStop=entryStop,
                debug=debug,
                output_dir=self.output_dir_
                )
            
            time_e_ = time.time()
            print ( "Total time elapsed: {:.0f}".format( time_e_ - time_s_ ) )
