from homeassistant.helpers.entity import ToggleEntity

class IrrigationZone(ToggleEntity):
    def __init__(self, name, zone_id):
        self._name = name
        self._zone_id = zone_id
        self._is_on = False

    @property
    def name(self):
        return f"Irrigation {self._zone_id}"

    @property
    def is_on(self):
        return self._is_on

    def turn_on(self, **kwargs):
        self._is_on = True

    def turn_off(self, **kwargs):
        self._is_on = False