import allure

from framework.models.base_model import BaseModel
from vehicle_project.utils.vehical_api_utils import VehicleApiUtils


class Pin(BaseModel):
    """
    Class Pin with methods
    """

    @staticmethod
    def get_pin_by_id(pin_id: int) -> str:
        """
        :param pin_id: PinId value
        :return: current PinId information
        """
        with allure.step(
                "Execute Get request for getting pin by PinId and return the json-encoded content of a response"):
            return BaseModel.get_obj_from_json(VehicleApiUtils.get_pin_by_number(pin_id).json())

    @staticmethod
    def get_all_pins() -> str:
        """
        :return: current all pins information
        """
        with allure.step("Execute Get request for getting all pins and return the json-encoded content of a response"):
            return BaseModel.get_obj_from_json(VehicleApiUtils.get_all_pins().json())
