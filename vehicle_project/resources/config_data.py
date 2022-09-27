class ConfigData:
    """
    Class contains configuration parameters
    """
    PORT = 8099
    URL = f"http://localhost:{PORT}/api"
    GET_ONE_PIN = "/pins/{pin_id}"
    GET_ALL_PINS = "/pins"
    POST_ONE_PIN = "/pins/{pin_id}/update_pin"
    POST_ALL_PINS = "/pins/update_pins"
    GET_ONE_SIGNAL = "/signals/{sig_id}"
    GET_ALL_SIGNALS = "/signals"
