import numpy as np
from typing import List
from rlbench.backend.task import Task, ENHANCED_RANDOMNESS
from rlbench.const import colors
from rlbench.backend.conditions import NothingGrasped, DetectedCondition
from pyrep.objects.shape import Shape
from pyrep.objects.proximity_sensor import ProximitySensor


class ReachAndDrag(Task):

    def init_task(self) -> None:
        self.stick = Shape('stick')
        self.register_graspable_objects([self.stick])
        self.cube = Shape('cube')
        self.target = Shape('target0')
        self.distractor1 = Shape('distractor1')
        self.distractor2 = Shape('distractor2')
        self.distractor3 = Shape('distractor3')

    def init_episode(self, index: int) -> List[str]:
        self.register_success_conditions([
            DetectedCondition(self.cube, ProximitySensor('success0'))])
        color_name, color_rgb = colors[index]
        self.target.set_color(color_rgb)

        _, distractor1_rgb = colors[(index + 5) % len(colors)]
        self.distractor1.set_color(distractor1_rgb)

        _, distractor2_rgb = colors[(index + 6) % len(colors)]
        self.distractor2.set_color(distractor2_rgb)

        _, distractor3_rgb = colors[(index + 7) % len(colors)]
        self.distractor3.set_color(distractor3_rgb)

        if ENHANCED_RANDOMNESS:
            position = self.stick.get_position()
            position[:2] += np.random.uniform(-0.1, 0.1, size=2)
            self.stick.set_position(position)

            if np.random.randint(0, 2) == 0:
                v = np.random.randint(0, 3)
                if v == 0:
                    self.distractor1.remove()
                elif v == 1:
                    self.distractor2.remove()
                elif v == 2:
                    self.distractor3.remove()


        return ['use the stick to drag the cube onto the %s target'
                % color_name,
                'pick up the stick and use it to push or pull the cube '
                'onto the %s target' % color_name,
                'drag the block towards the %s square on the table top'
                % color_name,
                'grasping the stick by one end, pick it up and use the its '
                'other end to move the block onto the %s target' % color_name]

    def variation_count(self) -> int:
        return len(colors)
