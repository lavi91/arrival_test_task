from framework.utils.base_api_utils import BaseApiRequests
from vehicle_project.resources.config_data import ConfigData


class VehicleApiUtils:
    @staticmethod
    def get_pin_by_number(pin_number: int):
        """
        :param pin_number: PinId value
        :return: response with pin information by PinId
        """
        return BaseApiRequests.get(ConfigData.URL + ConfigData.GET_ONE_PIN.format(pin_id=pin_number))

    @staticmethod
    def get_all_pins():
        """
        :return: response with all pins information
        """
        return BaseApiRequests.get(ConfigData.URL + ConfigData.GET_ALL_PINS)

    @staticmethod
    def get_signal_by_number(signal_number: int):
        """
        :param signal_number: SigId value
        :return: response with signal information by SigId
        """
        return BaseApiRequests.get(ConfigData.URL + ConfigData.GET_ONE_SIGNAL.format(sig_id=signal_number))

    @staticmethod
    def get_all_signals():
        """
        :return: response with all signals information
        """
        return BaseApiRequests.get(ConfigData.URL + ConfigData.GET_ALL_SIGNALS)

    @staticmethod
    def post_pin_by_number(pin_number: int, data_dict: dict):
        """
        Execute post request for setting pin data by PinId
        :param pin_number:  PinId value
        :param data_dict: data for pin settings
        """
        return BaseApiRequests.post(ConfigData.URL + ConfigData.POST_ONE_PIN.format(pin_id=pin_number), data=data_dict)

    @staticmethod
    def post_all_pins(data_dict: dict):
        """
        Execute post request for setting several pins
        :param data_dict: data for pins settings
        """
        return BaseApiRequests.post(ConfigData.URL + ConfigData.POST_ALL_PINS, json=data_dict)
