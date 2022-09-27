import allure

from vehicle_project.resources.pins_id import PinsId
from vehicle_project.utils.data_converter_utils import get_dict_for_set_gear_pos
from vehicle_project.utils.vehical_api_utils import VehicleApiUtils


class GearShifter:
    """
    Class Gear Shifter with gear positions and methods
    """

    PARK = "Park"
    NEUTRAL = "Neutral"
    REVERSE = "Reverse"
    DRIVE = "Drive"

    POSITIONS = {PARK: (0.67, 3.12), NEUTRAL: (1.48, 2.28), REVERSE: (2.28, 1.48), DRIVE: (3.12, 0.67)}

    @staticmethod
    def set_gear_shifter_by_pos(position: str):
        """
        Sets gear position
        :param position: gear position value
        """
        with allure.step(f"Setting gear position to {position} state"):
            if position in GearShifter.POSITIONS.keys():
                VehicleApiUtils.post_all_pins(get_dict_for_set_gear_pos(*GearShifter.POSITIONS[position]))
            else:
                raise ValueError("This state is absent")

    @staticmethod
    def get_current_gear_pos() -> tuple:
        """
        :return: current gear information
        """
        with allure.step("Get current gear position by response"):
            response = VehicleApiUtils.get_all_pins()
            return response.json()[PinsId.GEAR_1 - 1], response.json()[PinsId.GEAR_2 - 1]
