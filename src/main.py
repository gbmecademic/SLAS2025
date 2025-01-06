from MecaPlanar import MecaPlanar
from mecademicpy.robot import Robot
from pmclib import pmc_types


# Robot setup and activation


# Planar setup and activation
planar = MecaPlanar()
planar.connect()

ids = planar.get_xbot_ids()


planar.define_stereotype(pmc_types.XbotType.M3_06,
                         1,
                         size_pos_y=0.080,
                         size_neg_y=-0.080)

for bot_id in ids:
    planar.assign_stereotype(bot_id, 1)

# Move everything to starting position


# Main loop
while True:
    pass
    # Robots swap the parts

    # Robot pipettes the well plate

    # xbots for pipetting swap

    # Robot pipettes the vial

    # xbots swap from swap positions to pipette positions
