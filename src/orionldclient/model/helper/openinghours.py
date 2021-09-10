#!/usr/bin/env python3

# Software Name: python-orion-client
# SPDX-FileCopyrightText: Copyright (c) 2021 Orange
# SPDX-License-Identifier: Apache 2.0
#
# This software is distributed under the Apache 2.0;
# see the NOTICE file for more details.
#
# Author: Fabien BATTELLO <fabien.battelo@orange.com> et al.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations
from dataclasses import dataclass
from datetime import time
from enum import Enum


class WeekDay(Enum):
    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"
    SATURDAY = "Saturday"
    SUNDAY = "Sunday"


@dataclass
class OpeningHoursSpecification:
    """https://schema.org/OpeningHoursSpecification"""

    opens: str
    closes: str
    dayofweek: str

    def to_dict(self):
        return {"opens": self.opens, "closes": self.closes, "dayOfWeek": self.dayofweek}


class OpeningHoursSpecificationBuilder:
    def __init__(self):
        self._oh: dict = {}

    @staticmethod
    def _converttimes(opens, closes) -> tuple[str, str]:
        opens = opens if isinstance(opens, str) else opens.strftime("%H:%M")
        closes = closes if isinstance(closes, str) else closes.strftime("%H:%M")
        return opens, closes

    def monday(self, opens: time | str, closes: time | str):
        opens, closes = OpeningHoursSpecificationBuilder._converttimes(opens, closes)
        self._oh[WeekDay.MONDAY] = OpeningHoursSpecification(
            opens, closes, WeekDay.MONDAY.value
        )
        return self

    def tuesday(self, opens: time | str, closes: time | str):
        opens, closes = OpeningHoursSpecificationBuilder._converttimes(opens, closes)
        self._oh[WeekDay.TUESDAY] = OpeningHoursSpecification(
            opens, closes, WeekDay.TUESDAY.value
        )
        return self

    def wednesday(self, opens: time, closes: time):
        opens, closes = OpeningHoursSpecificationBuilder._converttimes(opens, closes)
        self._oh[WeekDay.WEDNESDAY] = OpeningHoursSpecification(
            opens, closes, WeekDay.WEDNESDAY.value
        )
        return self

    def thursday(self, opens: time, closes: time):
        opens, closes = OpeningHoursSpecificationBuilder._converttimes(opens, closes)
        self._oh[WeekDay.THURSDAY] = OpeningHoursSpecification(
            opens, closes, WeekDay.THURSDAY.value
        )
        return self

    def friday(self, opens: time, closes: time):
        opens, closes = OpeningHoursSpecificationBuilder._converttimes(opens, closes)
        self._oh[WeekDay.FRIDAY] = OpeningHoursSpecification(
            opens, closes, WeekDay.FRIDAY.value
        )
        return self

    def saturday(self, opens: time, closes: time):
        opens, closes = OpeningHoursSpecificationBuilder._converttimes(opens, closes)
        self._oh[WeekDay.SATURDAY] = OpeningHoursSpecification(
            opens, closes, WeekDay.SATURDAY.value
        )
        return self

    def sunday(self, opens: time, closes: time):
        opens, closes = OpeningHoursSpecificationBuilder._converttimes(opens, closes)
        self._oh[WeekDay.SUNDAY] = OpeningHoursSpecification(
            opens, closes, WeekDay.SUNDAY.value
        )
        return self

    def set_days(self, opens: time, closes: time, *days):
        opens, closes = OpeningHoursSpecificationBuilder._converttimes(opens, closes)
        for day in days:
            self._oh[day] = OpeningHoursSpecification(opens, closes, day.value)
        return self

    def build(self) -> dict:
        openingdays = []
        for day in WeekDay:
            if oh := self._oh.get(day, None):
                openingdays.append(oh.to_dict())
        return openingdays
