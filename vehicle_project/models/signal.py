import allure

from framework.models.base_model import BaseModel
from framework.utils.asserts import Asserts
from vehicle_project.utils.vehical_api_utils import VehicleApiUtils


class Signal(BaseModel):

    @staticmethod
    def get_signal_by_id(sig_id: int) -> BaseModel:
        """
        :param sig_id: SigId value
        :return: current signal information by SigId
        """
        with allure.step(
                "Execute Get request for getting signal by SigId and return the json-encoded content of a response"):
            return BaseModel.get_obj_from_json(VehicleApiUtils.get_signal_by_number(sig_id).json())

    @staticmethod
    def get_all_signals() -> str:
        """
        :return: current all signals information
        """
        with allure.step(
                "Execute Get request for getting all signals and return the json-encoded content of a response"):
            return BaseModel.get_obj_from_json(VehicleApiUtils.get_all_signals().json())

    @staticmethod
    def compare_actual_and_expected_signals(sig_id: int, expected_sig_value: str, safe: bool = False):
        """
        Compare actual signal value by SigId with expected
        :param sig_id: SigId value
        :param expected_sig_value: expected SigId value
        """
        with allure.step("Compare actual signal value by SigId with expected"):
            current_signal = Signal.get_signal_by_id(sig_id)
            if not safe:
                Asserts.assert_equal_objects(current_signal.Value, expected_sig_value)
            return current_signal == expected_sig_value
