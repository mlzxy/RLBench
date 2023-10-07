from typing import List
import numpy as np
from pyrep.objects.dummy import Dummy
from pyrep.objects.proximity_sensor import ProximitySensor
from pyrep.objects.shape import Shape
from rlbench.backend.conditions import NothingGrasped, DetectedCondition
from rlbench.backend.task import Task, ENHANCED_RANDOMNESS

MEAT = ['chicken', 'steak']


class MeatOffGrill(Task):

    def init_task(self) -> None:
        self._steak = Shape('steak')
        self._chicken = Shape('chicken')
        self._grill = Shape('grill')
        self._success_sensor = ProximitySensor('success')
        self.register_graspable_objects([self._chicken, self._steak])
        self._w1 = Dummy('waypoint1')
        self._w1z= self._w1.get_position()[2]

    def init_episode(self, index: int) -> List[str]:
        conditions = [NothingGrasped(self.robot.gripper)]
        if ENHANCED_RANDOMNESS:
            pos = self._grill.get_position()
            pos[:2] += np.random.uniform(-0.1, 0.1, size=2) 
            self._grill.set_position(pos)

            # if np.random.uniform() > 0.5:
            #     steak_pos = self._steak.get_pose()
            #     chick_pos = self._chicken.get_pose()
            #     self._chicken.set_pose(steak_pos)
            #     self._steak.set_pose(chick_pos)






        if index == 0:
            if ENHANCED_RANDOMNESS:
                if np.random.uniform() > 0.5:
                    steak_pos = self._steak.get_position()
                    chick_pos = self._chicken.get_position()
                    self._chicken.set_position(steak_pos)
                    self._steak.set_position(chick_pos)
                else:
                    pos = self._chicken.get_position(relative_to=self._chicken)
                    pos[1] += np.random.uniform(-0.05, 0.05)
                    self._chicken.set_position(pos, relative_to=self._chicken)

            x, y, _ = self._chicken.get_position()
            self._w1.set_position([x, y, self._w1z])
            # self._w1.set_orientation(self._chicken.get_orientation())
            conditions.append(
                DetectedCondition(self._chicken, self._success_sensor))
        else:
            if ENHANCED_RANDOMNESS:
                if np.random.uniform() > 0.5:
                    steak_pos = self._steak.get_position()
                    chick_pos = self._chicken.get_position()
                    self._chicken.set_position(steak_pos)
                    self._steak.set_position(chick_pos)
                else:
                    pos = self._steak.get_position(relative_to=self._steak)
                    pos[1] += np.random.uniform(-0.05, 0.05)
                    self._steak.set_position(pos, relative_to=self._steak)
            x, y, _ = self._steak.get_position()
            self._w1.set_position([x, y, self._w1z])
            # self._w1.set_orientation(self._steak.get_orientation())
            conditions.append(
                DetectedCondition(self._steak, self._success_sensor))
        self.register_success_conditions(conditions)
        return ['take the %s off the grill' % MEAT[index],
                'pick up the %s and place it next to the grill' % MEAT[index],
                'remove the %s from the grill and set it down to the side'
                % MEAT[index]]

    def variation_count(self) -> int:
        return 2
