""" 
   Code for creating the app class of ScopeFoundry for the Orca Flash 4V3
   
   @authors: Elena Corbetta, Andrea Bassi. Politecnico di Milano
   10/21
"""

from ScopeFoundry import BaseMicroscopeApp
 
class ModulatedApp(BaseMicroscopeApp):
    
    name = 'ModulatedApp'
    
      
    
    def setup(self):
        
        from Hamamatsu_ScopeFoundry.CameraHardware import HamamatsuHardware
        self.add_hardware(HamamatsuHardware(self))
        

        from VialuxDMD_ScopeFoundry.DMD_hw import VialuxDmdHW
        self.add_hardware(VialuxDmdHW(self))
        
        from TexasInstrumentsDMD_ScopeFoundry.DMDHardware import TexasInstrumentsDmdHW
        self.add_hardware(TexasInstrumentsDmdHW(self))
        
        print("Adding Hardware Components")
        
        from modulated_measure_doubleDMD import ModulatedMeasure
        self.add_measurement(ModulatedMeasure(self))
        print("Adding measurement components")
        
        self.ui.show()
        self.ui.activateWindow()
   

if __name__ == '__main__':
            
    import sys
    app = ModulatedApp(sys.argv)
    sys.exit(app.exec_())
        
