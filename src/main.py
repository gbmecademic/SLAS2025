from MecaPlanar import MecaPlanar
from mecademicpy.robot import Robot
from utilities import *
from constants import *
from pmclib import pmc_types


# Robot setup and activation


# Planar setup and activation
planar = MecaPlanar()
planar.connect()
planar.initialize()


wells1 = XbotType('well', 1)
wells2 = XbotType('well', 4)
vials1 = XbotType('vial', 3)
vials2 = XbotType('vial', 2)
state = PlanarStateSLAS([vials1, wells1, vials2, wells2])

# Move everything to starting position
planar.send_auto_move_command(4, state.get_id_positions(), X_POS, Y_POS)
planar.wait_multiple_move_done(state.get_id_positions())

# Main loop
debug_count = 0
swap_side = 'R'
while True:
    pass
    # Robot pipettes the vials

    # Robots start swapping parts

    # Xbots swap pipette
    state.swap_pipetting()
    planar.start_macro(151, state.get_id_positions()[0])
    planar.start_macro(150, state.get_id_positions()[1])
    planar.wait_multiple_move_done(state.get_id_positions()[:2])

    # Xbot starts spinny
    planar.start_macro(160, state.get_id_positions()[1])

    # Robot pipettes well plate

    # Wait for robot and spin to be done
    planar.wait_move_done(state.get_id_positions()[1])

    # Full swap
    state.swap_full()
    planar.send_auto_move_command(4, state.get_id_positions(), X_POS, Y_POS)
    planar.wait_multiple_move_done(state.get_id_positions())

    debug_count += 1
    if debug_count >= 5:
        break
