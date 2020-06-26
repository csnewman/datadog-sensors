import sensors
from datadog_checks.base import AgentCheck

class SensorsMon(AgentCheck):
    
    def check(self, instance):
        sensors.init()
        try:
            for chip in sensors.iter_detected_chips():
                for feature in chip:
                    self.gauge("sensors." + feature.label, feature.get_value(), device_name=('%s' % (chip)))
        finally:
            sensors.cleanup()
