from typing import List, Tuple
import os

import numpy as np
from pyrep.objects.dummy import Dummy
from pyrep.objects.joint import Joint
from pyrep.objects.proximity_sensor import ProximitySensor
from pyrep.objects.shape import Shape
from rlbench.backend.conditions import DetectedCondition
from rlbench.backend.task import Task, ENHANCED_RANDOMNESS




class PutItemInDrawer(Task):

    def init_task(self) -> None:
        self._options = ['bottom', 'middle', 'top']
        self._anchors = [Dummy('waypoint_anchor_%s' % opt)
                         for opt in self._options]
        self._joints = [Joint('drawer_joint_%s' % opt)
                        for opt in self._options]
        self._waypoint1 = Dummy('waypoint2')
        self._item = Shape('item')
        self._drawer = Shape('drawer_frame')
        self.register_graspable_objects([self._item])

    def init_episode(self, index) -> List[str]:
        option = self._options[index]
        anchor = self._anchors[index]

        if ENHANCED_RANDOMNESS:
            # pos = self._drawer.get_position()
            # pos[:2] += np.random.uniform(-0.1, 0.1, size=2)
            # self._drawer.set_position(pos)

            drawer_box = np.array(self._drawer.get_bounding_box())
            drawer_box *= 0.6
            xshift, yshift = np.random.uniform(drawer_box[0], drawer_box[1]), \
                np.random.uniform(drawer_box[2], drawer_box[3])
            item_position = self._item.get_position()
            item_position[0] += max(drawer_box[:2]) #xshift
            item_position[1] += min(drawer_box[2:4]) #yshift
            self._item.set_position(item_position)

        self._waypoint1.set_position(anchor.get_position())
        success_sensor = ProximitySensor('success_' + option)
        self.register_success_conditions(
            [DetectedCondition(self._item, success_sensor)])
        return ['put the item in the %s drawer' % option,
                'put the block away in the %s drawer' % option,
                'open the %s drawer and place the block inside of it' % option,
                'leave the block in the %s drawer' % option]

    def variation_count(self) -> int:
        return 3

    def base_rotation_bounds(self) -> Tuple[List[float], List[float]]:
        divider = 4 if ENHANCED_RANDOMNESS else 8
        return [0, 0, - np.pi / divider], [0, 0, np.pi / divider] # 4
