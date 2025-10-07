from dataclasses import dataclass
from typing import Sequence


@dataclass
class Solution:
    route: Sequence[int]
    cost: float
