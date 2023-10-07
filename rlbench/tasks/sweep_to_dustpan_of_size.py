import numpy as np
from typing import List
from pyrep.objects.shape import Shape
from pyrep.objects.proximity_sensor import ProximitySensor
from rlbench.backend.task import Task, ENHANCED_RANDOMNESS
from pyrep.objects.object import Object
from pyrep.objects.dummy import Dummy
from rlbench.backend.conditions import DetectedCondition

DIRT_NUM = 5


class SweepToDustpanOfSize(Task):

    def init_task(self) -> None:
        self._dustpan_sizes = ['tall', 'short']
        self.shortpan = Shape('dustpan_short')
        self.tallpan = Shape('dustpan_tall')
        self.dust = Shape('dirt0')
        self.broom = Shape('broom')
        self.register_graspable_objects([self.broom])

        self._waypoint_paths = {
            0: [Dummy('point1a'),
                Dummy('point1b'),
                Dummy('point1c')],

            1: [Dummy('point2a'),
                Dummy('point2b'),
                Dummy('point2c')]
        }

    def init_episode(self, index: int) -> List[str]:
        self._variation_index = index
        dustpan_size = self._dustpan_sizes[self._variation_index]

        if ENHANCED_RANDOMNESS:
            pos = self.shortpan.get_position(self.shortpan)
            pos[1] += np.random.uniform(-0.05, 0.1) 
            self.shortpan.set_position(pos, relative_to=self.shortpan)

            pos = self.tallpan.get_position(self.tallpan)
            pos[1] += np.random.uniform(-0.1, 0.0) 
            self.tallpan.set_position(pos, relative_to=self.tallpan)

            pos = self.broom.get_position(self.broom)
            pos[1] += np.random.uniform(-0.01, 0.03)
            self.broom.set_position(pos, relative_to=self.broom)

        success_sensor = ProximitySensor(f'success_{dustpan_size}')
        dirts = [Shape('dirt' + str(i)) for i in range(DIRT_NUM)]
        conditions = [DetectedCondition(dirt, success_sensor) for dirt in dirts]
        self.register_success_conditions(conditions)

        target_waypoints = self._waypoint_paths[self._variation_index]
        self._waypoints = [Dummy('waypoint%d'%(i))
                           for i in range(2, 5)]

        for i in range(len(target_waypoints)):
            self._waypoints[i].set_pose(target_waypoints[i].get_pose())
        self.register_stop_at_waypoint(2+i+1)

        return ['sweep dirt to the %s dustpan' % (dustpan_size),
                'sweep the dirt up into the %s dustpan' % (dustpan_size),
                'use the broom to brush the dirt into the %s dustpan' % (dustpan_size),
                'clean up the dirt with the %s pan' % (dustpan_size)]

    def variation_count(self) -> int:
        return 2

    # def boundary_root(self) -> Object:
    #     return Shape('boundary_root')
