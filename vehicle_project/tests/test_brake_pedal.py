import allure
import pytest

from framework.utils.asserts import Asserts
from vehicle_project.common_steps.steps import CommonSteps
from vehicle_project.models.acceleration_pedal import AccelerationPedal
from vehicle_project.models.brake_pedal import BrakePedal
from vehicle_project.models.gear_shifter import GearShifter
from vehicle_project.models.req_torque import ReqTorque
from vehicle_project.models.signal import Signal
from vehicle_project.resources.signals_id import SignalsId
from vehicle_project.resources.test_data import TestData


class TestBrakePedal:
    """
    Class contains tests for Brake Pedal
    """

    @pytest.mark.parametrize("gear_pos", GearShifter.POSITIONS.keys())
    def test_gear_with_error_state(self, gear_pos):
        BrakePedal.set_brake_pedal_state(BrakePedal.ERROR)
        Signal.compare_actual_and_expected_signals(SignalsId.BRAKE_PEDAL, BrakePedal.ERROR)
        Signal.compare_actual_and_expected_signals(SignalsId.GEAR_POSITION, GearShifter.NEUTRAL)
        Signal.compare_actual_and_expected_signals(SignalsId.REQ_TORQUE, ReqTorque.NM_0)
        GearShifter.set_gear_shifter_by_pos(gear_pos)
        Signal.compare_actual_and_expected_signals(SignalsId.GEAR_POSITION, GearShifter.NEUTRAL)

    @pytest.mark.parametrize("brake_pedal_state", [BrakePedal.ERROR, BrakePedal.PRESSED])
    @pytest.mark.parametrize("gear_pos", [GearShifter.DRIVE, GearShifter.REVERSE])
    @pytest.mark.parametrize("acc_pedal_pos", AccelerationPedal.POSITIONS.keys())
    def test_req_torque_with_error_and_pressed(self, gear_pos: str, acc_pedal_pos: str, brake_pedal_state: str):
        CommonSteps.switching_gear(gear_pos)
        Signal.compare_actual_and_expected_signals(SignalsId.BRAKE_PEDAL, BrakePedal.RELEASED)
        with allure.step(f"Setting {acc_pedal_pos} for acceleration pedal position"):
            AccelerationPedal.set_acc_pedal_pos(acc_pedal_pos)
        with allure.step(f"Comparing actual req torque signal with expected"):
            current_req_torque_signal = Signal.get_signal_by_id(SignalsId.REQ_TORQUE)
            req_torque_value_bu_acc_pos = ReqTorque.get_req_torque_by_acc_pedal_pos(acc_pedal_pos)
            Asserts.assert_equal_objects(current_req_torque_signal.Value, req_torque_value_bu_acc_pos)
        BrakePedal.set_brake_pedal_state(brake_pedal_state)
        Signal.compare_actual_and_expected_signals(SignalsId.BRAKE_PEDAL, brake_pedal_state)
        Signal.compare_actual_and_expected_signals(SignalsId.REQ_TORQUE, ReqTorque.NM_0)

    @pytest.mark.parametrize("gear_pos", GearShifter.POSITIONS.keys())
    def test_gear_with_released_state(self, gear_pos: str):
        GearShifter.set_gear_shifter_by_pos(gear_pos)
        Signal.compare_actual_and_expected_signals(SignalsId.GEAR_POSITION, GearShifter.NEUTRAL)

    @pytest.mark.parametrize("gear_pos", GearShifter.POSITIONS.keys())
    def test_gear_with_pressed_state(self, gear_pos: str):
        BrakePedal.set_brake_pedal_state(BrakePedal.PRESSED)
        Signal.compare_actual_and_expected_signals(SignalsId.BRAKE_PEDAL, BrakePedal.PRESSED)
        GearShifter.set_gear_shifter_by_pos(gear_pos)
        Signal.compare_actual_and_expected_signals(SignalsId.GEAR_POSITION, gear_pos)

    @pytest.mark.parametrize("voltage", TestData.VOLTAGE_BRAKE_PEDAL_VALUES)
    def test_brake_pedal_voltage_values(self, voltage: int):
        brake_pedal_state_by_voltage = BrakePedal.get_brake_pedal_state_by_voltage(voltage)
        BrakePedal.set_brake_pedal_state(brake_pedal_state_by_voltage)
        Signal.compare_actual_and_expected_signals(SignalsId.BRAKE_PEDAL, brake_pedal_state_by_voltage)
