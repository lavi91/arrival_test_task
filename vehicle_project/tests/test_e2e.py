from vehicle_project.common_steps.steps import CommonSteps
from vehicle_project.models.acceleration_pedal import AccelerationPedal
from vehicle_project.models.gear_shifter import GearShifter
from vehicle_project.models.req_torque import ReqTorque
from vehicle_project.models.signal import Signal
from vehicle_project.resources.signals_id import SignalsId


class TestE2E:
    """
    Class contains end-to-end tests
    """

    def test_drive_park(self):
        CommonSteps.switching_gear(GearShifter.DRIVE)
        AccelerationPedal.set_acc_pedal_pos(AccelerationPedal.PERCENT_30)
        Signal.compare_actual_and_expected_signals(SignalsId.ACC_PEDAL, AccelerationPedal.PERCENT_30)
        Signal.compare_actual_and_expected_signals(SignalsId.REQ_TORQUE, ReqTorque.NM_3000)
        AccelerationPedal.set_acc_pedal_pos(AccelerationPedal.PERCENT_0)
        Signal.compare_actual_and_expected_signals(SignalsId.ACC_PEDAL, AccelerationPedal.PERCENT_0)
        Signal.compare_actual_and_expected_signals(SignalsId.REQ_TORQUE, ReqTorque.NM_0)
        CommonSteps.switching_gear(GearShifter.PARK)
        Signal.compare_actual_and_expected_signals(SignalsId.GEAR_POSITION, GearShifter.PARK)
