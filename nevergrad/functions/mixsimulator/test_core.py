# Copyright (c) Meta Platforms, Inc. and affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

import numpy as np
from . import core


def test_mixsimulator() -> None:
    func = core.OptimizeMix()
    x = 2 * np.random.rand(func.dimension)
    value = func(x)  # should not touch boundaries, so value should be < np.inf
    assert isinstance(value, float)
    assert value < np.inf
