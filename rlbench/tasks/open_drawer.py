from typing import List, Tuple
import numpy as np
from pyrep.objects.dummy import Dummy
from pyrep.objects.joint import Joint
from rlbench.backend.conditions import JointCondition
from rlbench.backend.task import Task, ENHANCED_RANDOMNESS
from pyrep.objects.shape import Shape


class OpenDrawer(Task):

    def init_task(self) -> None:
        self._options = ['bottom', 'middle', 'top']
        self._anchors = [Dummy('waypoint_anchor_%s' % opt)
                         for opt in self._options]
        self._joints = [Joint('drawer_joint_%s' % opt)
                        for opt in self._options]
        self._waypoint1 = Dummy('waypoint1')
        self._drawer = Shape('drawer_frame')

    def init_episode(self, index: int) -> List[str]:
        if ENHANCED_RANDOMNESS:
            pos = self._drawer.get_position()
            pos[:2] += np.random.uniform(-0.1, 0.1, size=2)
            self._drawer.set_position(pos)

        option = self._options[index]
        self._waypoint1.set_position(self._anchors[index].get_position())
        self.register_success_conditions(
            [JointCondition(self._joints[index], 0.15)])
        return ['open the %s drawer' % option,
                'grip the %s handle and pull the %s drawer open' % (
                    option, option),
                'slide the %s drawer open' % option]

    def variation_count(self) -> int:
        return 3

    def base_rotation_bounds(self) -> Tuple[List[float], List[float]]:
        d = 4 if ENHANCED_RANDOMNESS else 8
        return [0, 0, - np.pi / d], [0, 0, np.pi / d]
