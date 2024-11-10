from homeassistant.helpers.entity import Entity

class TaskCalendar(Entity):
    def __init__(self, name, tasks):
        self._name = name
        self._tasks = tasks

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return "tasks_pending" if self._tasks else "no_tasks"

    @property
    def extra_state_attributes(self):
        return {"tasks": self._tasks}