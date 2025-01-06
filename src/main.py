from MecaPlanar import MecaPlanar
from mecademicpy.robot import Robot
from constants import *


# Robot setup and activation
pipette = Robot()
vials = Robot()
well = Robot()

pipette.Connect()
vials.Connect()
well.Connect()

pipette.ResetError()
vials.ResetError()
well.ResetError()

pipette.ActivateAndHome()
vials.ActivateAndHome()
well.ActivateAndHome()
pipette.WaitHomed()
vials.WaitHomed()
well.WaitHomed()

pipette.ClearMotion()
vials.ClearMotion()
well.ClearMotion()

pipette.ResumeMotion()
vials.ResumeMotion()
well.ResumeMotion()

pipette.MoveJoints(*PIPETTE_SAFE_POS)
vials.MoveJoints(*VIALS_SAFE_POS)
well.MoveJoints(*WELL_SAFE_POS)


# Planar setup and activation


# Main loop
while True:
    pass
    # Robots swap the parts

    # Robot pipettes the well plate

    # xbots for pipetting swap

    # Robot pipettes the vial

    # xbots swap from swap positions to pipette positions
