from vehicle_project.resources.pins_id import PinsId


def get_voltage_dict(voltage_value: int) -> dict:
    """
    :param voltage_value: voltage value
    :return: dictionary for setting voltage value on the pin
    """
    return {"Voltage": voltage_value}


def get_dict_for_set_gear_pos(gear_1_voltage: float, gear_2_voltage: float):
    """
    :param gear_1_voltage: Gear_1 voltage value
    :param gear_2_voltage: Gear_2 voltage value
    :return: dictionary for setting value for Gear_1 and Gear_2
    """
    return {"Pins": [{"PinId": PinsId.GEAR_1, "Voltage": gear_1_voltage},
                     {"PinId": PinsId.GEAR_2, "Voltage": gear_2_voltage}]}
