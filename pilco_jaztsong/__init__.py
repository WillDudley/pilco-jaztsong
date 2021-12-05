__version__ = '0.1.0'

from pilco_jaztsong.controllers import LinearController, FakeGPR, RbfController
from pilco_jaztsong.rewards import ExponentialReward, LinearReward, CombinedRewards
from pilco_jaztsong.models.pilco import PILCO
from pilco_jaztsong.models.mgpr import MGPR
