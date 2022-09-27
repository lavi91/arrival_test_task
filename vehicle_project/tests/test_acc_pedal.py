import pytest

from vehicle_project.common_steps.steps import CommonSteps
from vehicle_project.models.acceleration_pedal import AccelerationPedal
from vehicle_project.models.gear_shifter import GearShifter
from vehicle_project.models.req_torque import ReqTorque
from vehicle_project.models.signal import Signal
from vehicle_project.resources.signals_id import SignalsId
from vehicle_project.resources.test_data import TestData


class TestAccPedal:
    """
    Class contains tests for AccPedal and ReqTorque
    """

    @pytest.mark.parametrize("voltage", TestData.VOLTAGE_ACC_PEDAL_VALUES)
    def test_acc_pedal_voltage_values(self, voltage: int):
        acc_pedal_pos_by_voltage = AccelerationPedal.get_acc_pedal_pos_by_voltage(voltage)
        AccelerationPedal.set_acc_pedal_pos(acc_pedal_pos_by_voltage)
        Signal.compare_actual_and_expected_signals(SignalsId.ACC_PEDAL, acc_pedal_pos_by_voltage)

    @pytest.mark.parametrize("gear_pos", [GearShifter.DRIVE, GearShifter.REVERSE])
    @pytest.mark.parametrize("acc_pedal_pos", AccelerationPedal.POSITIONS)
    def test_req_torque_by_acc_pedal_pos(self, gear_pos: str, acc_pedal_pos: str):
        CommonSteps.switching_gear(gear_pos)
        AccelerationPedal.set_acc_pedal_pos(acc_pedal_pos)
        req_torque_value_by_acc_pedal = ReqTorque.get_req_torque_by_acc_pedal_pos(acc_pedal_pos)
        Signal.compare_actual_and_expected_signals(SignalsId.REQ_TORQUE, req_torque_value_by_acc_pedal)
