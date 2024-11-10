import logging
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = {}

    hass.async_create_task(hass.config_entries.async_forward_entry_setup(entry, "calendar"))
    hass.async_create_task(hass.config_entries.async_forward_entry_setup(entry, "light"))
    hass.async_create_task(hass.config_entries.async_forward_entry_setup(entry, "switch"))
    hass.async_create_task(hass.config_entries.async_forward_entry_setup(entry, "sensor"))

    _LOGGER.info("Cannabis Grow Manager integration setup complete.")
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    unload_ok = await hass.config_entries.async_forward_entry_unload(entry, "calendar")
    unload_ok = unload_ok and await hass.config_entries.async_forward_entry_unload(entry, "light")
    unload_ok = unload_ok and await hass.config_entries.async_forward_entry_unload(entry, "switch")
    unload_ok = unload_ok and await hass.config_entries.async_forward_entry_unload(entry, "sensor")

    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id)
    return unload_ok