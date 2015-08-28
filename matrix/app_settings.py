# -*- coding: utf-8 -*-
from django.conf import settings

PACKAGE_LIST = getattr(
    settings, "MATRIX_PACKAGE_LIST", getattr(
        settings, "INSTALLED_APPS", ''))

FILTER_OPTIONS = {
    'group_name': True,
    'group_index': True,
    'source_name': True,
    'source_index': True,
    'target_name': True,
    'target_index': True,
    'imports': True,
    'cardinal': True,
}

FILTER_OPTIONS.update(getattr(settings, "MATRIX_FILTER_OPTIONS", {}))