from MecaPlanar import MecaPlanar
from utilities import PlanarStateSLAS, XbotType


mp = MecaPlanar()
mp.connect()
mp.initialize()

print(mp.get_num_xbots())
print(mp.get_xbot_ids())
mp.send_single_linear_command(1, 0.840, 0.120)
mp.wait_move_done(1)
print("Duck")
mp.send_single_linear_command(1, 0.12, 0.12)
mp.wait_move_done(1)
