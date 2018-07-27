import sensors
from checks import AgentCheck

class SensorsMon(AgentCheck):
    
    def check(self, instance):
        sensors.init()
        try:
            for chip in sensors.iter_detected_chips():
                #print '%s at %s' % (chip, chip.adapter_name)
                for feature in chip:
                    #print '  %s: %.2f' % (feature.label, feature.get_value())   
                    #try:
                    self.gauge("sensors." + feature.label, feature.get_value(), device_name=('%s' % (chip)))
                    #except KeyError:
        finally:
            sensors.cleanup()
