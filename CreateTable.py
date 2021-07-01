from create_table import create_table

class CreateTable:
    def __init__( self, label, fileNames, tree_path ):
        self.label_ = label
        self.fileNames_ = fileNames
        self.tree_path_ = tree_path

    def __call__( self, mix_protons=False, proton_files=None, random_protons=False, resample_factor=-1, runOnMC=False, data_periods=None, step_size=100000, firstEvent=None, entryStop=None, debug=False ):

        for key_ in self.fileNames_:
            import time
            print( time.strftime("%Y/%m/%d %H:%M:%S", time.localtime() ) )
            time_s_ = time.time()

            print ( key_, self.fileNames_[ key_ ] )
            label__ = "{}-{}".format( self.label_, key_ )
            create_table(
                self.fileNames_[ key_ ],
                label=label__,
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
                debug=debug
                )
            
            time_e_ = time.time()
            print ( "Total time elapsed: {:.0f}".format( time_e_ - time_s_ ) )
