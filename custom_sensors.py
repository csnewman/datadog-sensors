import sensors

try:
    # first, try to import the base class from old versions of the Agent...
    from checks import AgentCheck
except ImportError:
    # ...if the above failed, the check is running in Agent version 6 or later
    from datadog_checks.checks import AgentCheck

class SensorsMon(AgentCheck):

    def check(self, instance):
        sensors.init()
        try:
            for chip in sensors.iter_detected_chips():
                for feature in chip:
                    self.gauge("sensors." + feature.label, feature.get_value(), device_name=('%s' % (chip)))
        finally:
            sensors.cleanup()
