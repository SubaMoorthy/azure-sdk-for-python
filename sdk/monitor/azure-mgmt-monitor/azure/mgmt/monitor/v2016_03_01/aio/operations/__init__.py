# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._alert_rule_incidents_operations import AlertRuleIncidentsOperations
from ._alert_rules_operations import AlertRulesOperations
from ._log_profiles_operations import LogProfilesOperations
from ._metric_definitions_operations import MetricDefinitionsOperations

from ._patch import __all__ as _patch_all
from ._patch import *  # type: ignore # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk
__all__ = [
    'AlertRuleIncidentsOperations',
    'AlertRulesOperations',
    'LogProfilesOperations',
    'MetricDefinitionsOperations',
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()