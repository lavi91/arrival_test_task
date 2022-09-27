import allure

from vehicle_project.resources.pins_id import PinsId
from vehicle_project.utils.data_converter_utils import get_voltage_dict
from vehicle_project.utils.vehical_api_utils import VehicleApiUtils


class BrakePedal:
    """
    Class Brake Pedal with states and methods
    """
    ERROR = "Error"
    PRESSED = "Pressed"
    RELEASED = "Released"

    STATES = {ERROR: 0, PRESSED: 1.5, RELEASED: 2.5}

    @staticmethod
    def get_brake_pedal_state_by_voltage(voltage: int) -> str:
        """
        :param voltage: brake pedal voltage value
        :return: brake pedal state by voltage
        """
        with allure.step("Return brake pedal state value by voltage"):
            if 1 <= voltage < 2:
                return BrakePedal.PRESSED
            elif 2 <= voltage < 3:
                return BrakePedal.RELEASED
            else:
                return BrakePedal.ERROR

    @staticmethod
    def set_brake_pedal_state(state: str):
        """
        Sets brake pedal state on the pin
        :param state: brake pedal state value
        """
        with allure.step(f"Setting {state} state for brake pedal"):
            if state in BrakePedal.STATES.keys():
                VehicleApiUtils.post_pin_by_number(PinsId.BRAKE_PEDAL, get_voltage_dict(BrakePedal.STATES[state]))
            else:
                raise ValueError("This state is absent")
