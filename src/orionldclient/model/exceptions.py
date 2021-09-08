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

from ..exceptions import NgsiError


class NgsiMissingIdError(NgsiError):
    pass


class NgsiMissingTypeError(NgsiError):
    pass

class NgsiMissingContextError(NgsiError):
    pass

class NgsiUnmatchedAttributeTypeError(NgsiError):
    pass


class NgsiJsonError(NgsiError):
    pass


class NgsiUnsupportedFormatError(NgsiError):
    pass
