import allure

from vehicle_project.resources.pins_id import PinsId
from vehicle_project.utils.data_converter_utils import get_voltage_dict
from vehicle_project.utils.vehical_api_utils import VehicleApiUtils


class Battery:
    """
    Class Battery with states and methods
    """
    READY = "Ready"
    NOT_READY = "NotReady"
    ERROR = "Error"

    STATES = {READY: 600, NOT_READY: 200, ERROR: 0}

    @staticmethod
    def get_battery_state_by_voltage(voltage: int) -> str:
        """
        :param voltage: battery voltage value
        :return: battery state by voltage
        """
        with allure.step("Return battery state value by voltage"):
            if 800 >= voltage > 400:
                return Battery.READY
            elif 0 < voltage <= 400:
                return Battery.NOT_READY
            else:
                return Battery.ERROR

    @staticmethod
    def set_battery_state(state: str):
        """
        Sets battery state on the pin
        :param state: battery state value
        """
        with allure.step(f"Setting {state} state for battery"):
            if state in Battery.STATES.keys():
                VehicleApiUtils.post_pin_by_number(PinsId.BATTERY, get_voltage_dict(Battery.STATES[state]))
            else:
                raise ValueError("This state is absent")
