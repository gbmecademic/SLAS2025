from enum import IntEnum


class PlanarPositions(IntEnum):
    UNDEF_POS = -1
    ROBOT_1_POS = 0
    ROBOT_2_POS = 1
    ROBOT_3_POS = 2
    ROBOT_4_POS = 3

    def shift_next(self):
        v = self.value + 1
        if v > 3:
            v = 0
        return PlanarPositions(v)

    def shift_prev(self):
        v = self.value - 1
        if v < 0:
            v = 3
        return PlanarPositions(v)


class PlanarState():
    def __init__(self, idx_list: list[int], pos_tol: float = 0.001) -> None:
        self.xbot_dict = {}
        for idx in idx_list:
            self.xbot_dict[idx] = PlanarPositions.UNDEF_POS
        self.pos_tol = pos_tol

    def validate_position(self, xbot_pos: list[float] | tuple[float], target_pos: list[float] | tuple[float]) -> bool:
        if target_pos[0]-self.pos_tol < xbot_pos[0] < target_pos[0]+self.pos_tol:
            if target_pos[1]-self.pos_tol < xbot_pos[1] < target_pos[1]+self.pos_tol:
                return True
        return False

    def get_idx_list(self) -> list[int]:
        return list(self.xbot_dict.keys())

    def set_pos_state(self, id: int, state: PlanarPositions) -> None:
        self.xbot_dict[id] = state

    def get_pos_state(self, id: int) -> PlanarPositions:
        return self.xbot_dict[id]

    def get_id_pos_order(self) -> list[int]:
        output = []
        for idx in sorted(self.xbot_dict, key=self.xbot_dict.get):
            output.append(idx)
        return output

    def shift_all_pos_next(self):
        for key in self.xbot_dict:
            self.xbot_dict[key] = self.xbot_dict[key].shift_next()

    def shift_all_pos_prev(self):
        for key in self.xbot_dict:
            self.xbot_dict[key] = self.xbot_dict[key].shift_prev()
