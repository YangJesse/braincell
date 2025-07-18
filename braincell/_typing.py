# Copyright 2024 BDP Ecosystem Limited. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

from typing import Union, Callable, Hashable, Tuple, Dict
from typing import Union, Callable, Hashable, Tuple, Dict

import brainstate
import brainunit as u
import jax

Initializer = Union[brainstate.typing.ArrayLike, Callable]
SectionName = Hashable
T = u.Quantity[u.second]
DT = u.Quantity[u.second]
VectorFiled = Callable
Y0 = jax.Array
Y1 = jax.Array
Jacobian = jax.Array
Args = Tuple
Aux = Dict
Path = Tuple[str, ...]
