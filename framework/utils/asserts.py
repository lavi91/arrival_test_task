from typing import Any


class Asserts:
    """
    Class contains assert methods
    """

    @staticmethod
    def soft_assert_for_lists(actual_list: list[Any], expected_list: list[Any]):
        """
        Utility for comparing all values from lists
        :param expected_list: expected list
        :param actual_list: actual list
        :return: True if not errors
        """
        messages = []
        if len(expected_list) != len(actual_list):
            raise ValueError("Different length of lists")

        for index in range(0, len(expected_list)):
            if expected_list[index] != actual_list[index]:
                messages.append(f"Different values. Expected: {expected_list[index]}. Actual: {actual_list[index]} ")

        if messages:
            raise AssertionError(''.join(messages))

    @staticmethod
    def assert_equal_objects(actual: Any, expected: Any):
        """
        Utility for comparing objects
        :param actual: actual data
        :param expected: expected data
        :return:
        """
        assert actual == expected, f"Different values. Expected {expected}. Actual: {actual} "
