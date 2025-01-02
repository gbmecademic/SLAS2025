from pmclib import system_commands as sys   # PMC System related commands
from pmclib import xbot_commands as bot     # PMC Mover related commands
from pmclib import pmc_types                # PMC API Types

import time


class PlanarMotorMove():
    def __init__(self, bot_id, xpos: float, ypos: float, vel: float, acc: float, ending_speed: float = 0) -> None:
        self.bot_id = bot_id
        self.xpos = xpos
        self.ypos = ypos
        self.vel = vel
        self.acc = acc
        self.end_speed = ending_speed


class MecaPlanar():
    def __init__(self) -> None:
        self.is_connected = False

    def connect(self, auto_connect: bool = True, ip: str = '192.168.10.100') -> bool:
        if auto_connect:
            connection_state = sys.auto_connect_to_pmc()
            self.is_connected = connection_state
            return connection_state
        else:
            connection_state = sys.connect_to_pmc(ip)
            self.is_connected = connection_state
            return connection_state

    def initialize(self, timeout: float = 10.0):
        if not sys.is_master:
            sys.gain_mastership()
        bot.activate_xbots()
        maxTime = time.time() + timeout
        while sys.get_pmc_status() is not pmc_types.PmcStatus.PMC_FULLCTRL:
            time.sleep(0.5)
            if time.time() > maxTime:
                raise TimeoutError("PMC Activation timeout")

    def activate_bots(self, timeout: float = 10.0):
        bot.activate_xbots()
        maxTime = time.time() + timeout
        while sys.get_pmc_status() is not pmc_types.PmcStatus.PMC_FULLCTRL:
            time.sleep(0.5)
            if time.time() > maxTime:
                raise TimeoutError("PMC Activation timeout")

    def deactivate_bots(self, timeout: float = 10.0):
        bot.deactivate_xbots()
        maxTime = time.time() + timeout
        while sys.get_pmc_status() is not pmc_types.PmcStatus.PMC_INACTIVE:
            time.sleep(0.5)
            if time.time() > maxTime:
                raise TimeoutError("PMC Deactivation timeout")

    def get_pmc_status(self) -> pmc_types.PmcStatus:
        return sys.get_pmc_status()

    def get_num_xbots(self) -> int:
        return len(bot.get_all_xbot_info(0))

    def get_xbots_state(self) -> dict:
        status = bot.get_all_xbot_info(0)
        states = {}
        for stat in status:
            states[stat.xbot_id] = stat.xbot_state
        return states

    def get_xbots_pos(self) -> dict:
        status = bot.get_all_xbot_info(0)
        pos = {}
        for stat in status:
            pos[stat.xbot_id] = (stat.x_pos, stat.y_pos)

    def send_single_linear_command(self, xbot_id: int, xpos: float, ypos: float, vel: float = 1.0, acc: float = 10.0):
        bot.linear_motion_si(xbot_id, xpos, ypos, vel, acc)

    def send_multi_linear_commands(self, moves: list[PlanarMotorMove]):
        for move in moves:
            bot.linear_motion_si(move.bot_id, move.xpos,
                                 move.ypos, move.vel, move.acc, final_speed=move.end_speed)

    def wait_move_done(self, bot_id: int, timeout: float = 10.0) -> pmc_types.XbotState:
        while bot.get_xbot_status(xbot_id=bot_id).xbot_state is not pmc_types.XbotState.XBOT_IDLE:
            if bot.get_xbot_status(xbot_id=bot_id).xbot_state == pmc_types.XbotState.XBOT_OBSTACLE_DETECTED:
                return pmc_types.XbotState.XBOT_OBSTACLE_DETECTED
            time.sleep(0.5)
        return pmc_types.XbotState.XBOT_IDLE
