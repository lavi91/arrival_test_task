import allure
import pytest

from vehicle_project.models.acceleration_pedal import AccelerationPedal
from vehicle_project.models.battery import Battery
from vehicle_project.models.brake_pedal import BrakePedal
from vehicle_project.models.gear_shifter import GearShifter


@pytest.fixture(autouse=True)
def set_default_state_of_system():
    """
    Pytest fixture for installing default system settings
    """
    with allure.step("Set default sittings for system"):
        Battery.set_battery_state(Battery.READY)
        BrakePedal.set_brake_pedal_state(BrakePedal.RELEASED)
        AccelerationPedal.set_acc_pedal_pos(AccelerationPedal.PERCENT_0)
        GearShifter.set_gear_shifter_by_pos(GearShifter.NEUTRAL)
