import allure
import pytest

from framework.utils.asserts import Asserts
from vehicle_project.models.battery import Battery
from vehicle_project.models.gear_shifter import GearShifter
from vehicle_project.models.pin import Pin
from vehicle_project.models.signal import Signal
from vehicle_project.resources.signals_id import SignalsId
from vehicle_project.resources.test_data import TestData


class TestBattery:
    """
    Class contains tests for battery
    """

    def test_not_ready_state(self):
        Battery.set_battery_state(Battery.NOT_READY)
        Signal.compare_actual_and_expected_signals(SignalsId.BATTERY, Battery.NOT_READY)
        Signal.compare_actual_and_expected_signals(SignalsId.GEAR_POSITION, GearShifter.NEUTRAL)

    def test_error_state(self):
        Battery.set_battery_state(Battery.ERROR)
        Signal.compare_actual_and_expected_signals(SignalsId.BATTERY, Battery.ERROR)
        with allure.step("Comparing actual all pin values with expected"):
            pin_objects_list = Pin.get_all_pins()
            expected_values_list = [0] * len(pin_objects_list)
            actual_voltage_values_list = [pin_object.Voltage for pin_object in pin_objects_list]
            Asserts.soft_assert_for_lists(actual_voltage_values_list, expected_values_list)

    @pytest.mark.parametrize("voltage", TestData.VOLTAGE_BATTERY_VALUES)
    def test_battery_voltage_values(self, voltage: int):
        battery_state_by_voltage = Battery.get_battery_state_by_voltage(voltage)
        Battery.set_battery_state(battery_state_by_voltage)
        Signal.compare_actual_and_expected_signals(SignalsId.BATTERY, battery_state_by_voltage)
