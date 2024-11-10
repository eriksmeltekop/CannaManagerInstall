from homeassistant.helpers.entity import ToggleEntity

class GrowLight(ToggleEntity):
    def __init__(self, name):
        self._name = name
        self._is_on = False

    @property
    def name(self):
        return self._name

    @property
    def is_on(self):
        return self._is_on

    def turn_on(self, **kwargs):
        self._is_on = True

    def turn_off(self, **kwargs):
        self._is_on = False