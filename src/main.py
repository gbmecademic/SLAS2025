from MecaPlanar import MecaPlanar
from mecademicpy.robot import Robot


# Robot setup and activation


# Planar setup and activation
planar = MecaPlanar()
planar.connect()

ids = mp.get_xbot_ids()

state = PlanarState(ids)
mp.initialize()

mp.define_stereotype(pmc_types.XbotType.M3_06,
                     1,
                     size_pos_y=0.080,
                     size_neg_y=-0.080)

# Main loop
while True:
    pass
    # Robots swap the parts

    # Robot pipettes the well plate

    # xbots for pipetting swap

    # Robot pipettes the vial

    # xbots swap from swap positions to pipette positions
