import copy
import re
import warnings

import numpy as np
import pandas as pd
import pint
from pandas import DataFrame, Series
from pandas.api.extensions import (
    ExtensionArray,
    ExtensionDtype,
    register_dataframe_accessor,
    register_extension_dtype,
    register_series_accessor,
)
from pandas.api.types import is_integer, is_list_like, is_object_dtype, is_string_dtype
from pandas.compat import set_function_name
from pandas.core import nanops
from pandas.core.arrays.base import ExtensionOpsMixin
from pandas.core.indexers import check_array_indexer
from pint import compat, errors
from pint.quantity import _Quantity
from pint.unit import _Unit

# TODO 
