import allure

from vehicle_project.resources.pins_id import PinsId
from vehicle_project.utils.data_converter_utils import get_voltage_dict
from vehicle_project.utils.vehical_api_utils import VehicleApiUtils


class AccelerationPedal:
    """
    Class Acceleration Pedal with positions and methods
    """
    ERROR = "Error"
    PERCENT_0 = "0 %"
    PERCENT_30 = "30 %"
    PERCENT_50 = "50 %"
    PERCENT_100 = "100 %"

    POSITIONS = {ERROR: 0, PERCENT_0: 1.5, PERCENT_30: 2.25, PERCENT_50: 2.75, PERCENT_100: 3.25}

    @staticmethod
    def get_acc_pedal_pos_by_voltage(voltage: int) -> str:
        """
        :param voltage: acceleration pedal voltage value
        :return: acceleration pedal state by voltage
        """
        with allure.step("Return acceleration pedal position value by voltage"):
            if 1 <= voltage < 2:
                return AccelerationPedal.PERCENT_0
            elif 2 <= voltage < 2.5:
                return AccelerationPedal.PERCENT_30
            elif 2.5 <= voltage < 3:
                return AccelerationPedal.PERCENT_50
            elif 3 <= voltage < 3.5:
                return AccelerationPedal.PERCENT_100
            else:
                return AccelerationPedal.ERROR

    @staticmethod
    def set_acc_pedal_pos(position: str):
        """
        Sets Acceleration Pedal position
        :param position: acceleration pedal position value
        """
        with allure.step(f"Setting {position} for acceleration pedal position"):
            if position in AccelerationPedal.POSITIONS.keys():
                VehicleApiUtils.post_pin_by_number(PinsId.ACC_PEDAL,
                                                   get_voltage_dict(AccelerationPedal.POSITIONS[position]))
            else:
                raise ValueError("This position is absent")
