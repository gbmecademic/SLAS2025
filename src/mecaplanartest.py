from MecaPlanar import MecaPlanar
from utilities import PlanarStateSLAS, XbotType


mp = MecaPlanar()
mp.connect()
mp.activate_bots()
mp.start_macro(0, 0)
mp.wait_move_done(0)
