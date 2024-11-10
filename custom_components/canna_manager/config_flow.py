from homeassistant import config_entries
from homeassistant.core import callback
import voluptuous as vol

from .const import DOMAIN

@callback
def configured_instances(hass):
    return [
        entry.data.get("name")
        for entry in hass.config_entries.async_entries(DOMAIN)
    ]

class CannabisGrowManagerConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(title=user_input["name"], data=user_input)

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {
                    vol.Required("name", default="My Cannabis Grow"): str,
                    vol.Optional("zones", default=3): int,
                    vol.Optional("enable_irrigation", default=True): bool,
                    vol.Optional("enable_lighting", default=True): bool,
                }
            ),
        )