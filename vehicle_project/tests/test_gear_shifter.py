import pytest

from vehicle_project.models.acceleration_pedal import AccelerationPedal
from vehicle_project.models.battery import Battery
from vehicle_project.models.brake_pedal import BrakePedal
from vehicle_project.models.gear_shifter import GearShifter
from vehicle_project.models.signal import Signal
from vehicle_project.resources.signals_id import SignalsId


class TestGearShifter:
    """
    Class contains tests for Gear Shifter
    """

    @pytest.mark.parametrize("battery_state", [Battery.ERROR, Battery.NOT_READY])
    @pytest.mark.parametrize("gear_pos", [GearShifter.PARK, GearShifter.REVERSE, GearShifter.DRIVE])
    def test_with_battery_error_and_not_ready(self, battery_state: str, gear_pos: str):
        Battery.set_battery_state(battery_state)
        Signal.compare_actual_and_expected_signals(SignalsId.BATTERY, battery_state)
        GearShifter.set_gear_shifter_by_pos(gear_pos)
        Signal.compare_actual_and_expected_signals(SignalsId.GEAR_POSITION, GearShifter.NEUTRAL)

    @pytest.mark.parametrize("acc_pedal_pos", [AccelerationPedal.PERCENT_30, AccelerationPedal.PERCENT_50,
                                               AccelerationPedal.PERCENT_100, AccelerationPedal.ERROR])
    @pytest.mark.parametrize("gear_pos", [GearShifter.PARK, GearShifter.REVERSE, GearShifter.DRIVE])
    def test_with_pressed_acc_pedal(self, acc_pedal_pos: str, gear_pos: str):
        BrakePedal.set_brake_pedal_state(BrakePedal.PRESSED)
        Signal.compare_actual_and_expected_signals(SignalsId.BRAKE_PEDAL, BrakePedal.PRESSED)
        AccelerationPedal.set_acc_pedal_pos(acc_pedal_pos)
        GearShifter.set_gear_shifter_by_pos(gear_pos)
        Signal.compare_actual_and_expected_signals(SignalsId.GEAR_POSITION, GearShifter.NEUTRAL)
