from MecaPlanar import MecaPlanar
from utilities import PlanarStateSLAS, XbotType
from constants import *


mp = MecaPlanar()
mp.connect()
mp.initialize()

print(mp.get_num_xbots())
print(mp.get_xbot_ids())


vials1 = XbotType('vial', 2)
vials2 = XbotType('vial', 3)
wells1 = XbotType('well', 1)
wells2 = XbotType('well', 4)

print("pp wp sw sv")
print("w  v  w  v")
state = PlanarStateSLAS([wells1, vials1, wells2, vials2])
print(state.get_id_positions())
state.swap_pipetting()
print(state.get_id_positions())
state.swap_full()
print(state.get_id_positions())
state.swap_pipetting()
print(state.get_id_positions())
state.swap_pipetting()
print(state.get_id_positions())
state.swap_full()
print(state.get_id_positions()[:2])
print(X_POS[:2], Y_POS)

mp.send_auto_move_command(4, state.get_id_positions(), X_POS, Y_POS)
mp.wait_multiple_move_done(state.get_id_positions())
state.swap_pipetting()
mp.send_auto_move_command(2, state.get_id_positions()
                          [:2], X_POS[:2], Y_POS[:2])
mp.wait_multiple_move_done(state.get_id_positions())
state.swap_full()
mp.send_auto_move_command(4, state.get_id_positions(), X_POS, Y_POS)
mp.wait_multiple_move_done(state.get_id_positions())
mp.deactivate_bots()
