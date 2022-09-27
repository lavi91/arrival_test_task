from vehicle_project.models.brake_pedal import BrakePedal
from vehicle_project.models.gear_shifter import GearShifter
from vehicle_project.models.signal import Signal
from vehicle_project.resources.signals_id import SignalsId


class CommonSteps:
    """
    Class contains common steps methods
    """

    @staticmethod
    def switching_gear(gear_pos: str):
        """
        Sets pressed state for brake pedal, switches gear position and sets released state for brake pedal
        :param gear_pos: gear shifter position value
        """
        BrakePedal.set_brake_pedal_state(BrakePedal.PRESSED)
        Signal.compare_actual_and_expected_signals(SignalsId.BRAKE_PEDAL, BrakePedal.PRESSED)
        GearShifter.set_gear_shifter_by_pos(gear_pos)
        Signal.compare_actual_and_expected_signals(SignalsId.GEAR_POSITION, gear_pos)
        BrakePedal.set_brake_pedal_state(BrakePedal.RELEASED)
        Signal.compare_actual_and_expected_signals(SignalsId.BRAKE_PEDAL, BrakePedal.RELEASED)
