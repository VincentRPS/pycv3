# MIT License
#
# Copyright (c) 2023 VincentRPS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from typing import Any, Callable, Coroutine, Self, Type

AsyncFunc = Callable[..., Coroutine[Any, Any, Any]]


class Event:
    _filters: dict[str, Any] | None = None

    @classmethod
    def filter(cls, **kwargs: Any) -> Self:
        self = cls()
        self._filters = kwargs
        return self

    async def on(self, data: dict[str, Any]) -> None:
        ...


class _InternalizedEvent:
    __slots__ = ("filters", "event", "callback")

    def __init__(
        self,
        filters: dict[str, Any] | None,
        event: Type[Event] | Event,
        func: AsyncFunc,
    ) -> None:
        self.filters = filters
        self.event = event
        self.callback = func


class EventManager:
    def __init__(self) -> None:
        self._events: dict[Type[Event], list[_InternalizedEvent]] = {}

    def add_event(self, event: Event | Type[Event], func: AsyncFunc) -> None:
        # this isn't a type
        if isinstance(event, Event):
            ev = event.__class__
        else:
            ev = event

        internal = _InternalizedEvent(filters=ev._filters, event=event, func=func)

        if ev in self._events:
            self._events[ev].append(internal)
        else:
            self._events[ev] = [internal]

    def remove_event(self, event: Event | Type[Event], func: AsyncFunc) -> None:
        if event in self._events:
            for i in self._events.copy()[event]:
                if i.callback == func:
                    self._events[event].remove(i)

                    if self._events[event] == []:
                        del self._events[event]
