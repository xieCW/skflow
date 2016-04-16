"""Main Scikit Flow module."""
#  Copyright 2015-present Scikit Flow Authors. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import pkg_resources as pkg_rs
import warnings
import numpy as np

try:
    from tensorflow.contrib.learn import *
    warnings.warn("skflow as separate library is deprecated. "
                  "Use import tensorflow.contrib.learn as skflow instead.", DeprecationWarning)
except ImportError:
    raise ImportError("Update your Tensorflow to 0.8+ to use latest skflow.")

