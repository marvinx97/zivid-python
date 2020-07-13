"""Contains capture assistant functions and classes."""
"""Auto generated, do not edit"""
import _zivid
import zivid._settings_converter as _settings_converter

# from zivid._suggest_settings_parameters_converter import (
#     to_internal_suggest_settings_parameters,
#     _to_internal_suggest_settings_parameters_ambient_light_frequency,
# )
import _zivid
import zivid


import _zivid
import zivid

# import zivid._suggest_settings_parameters_converter


"""Auto generated, do not edit"""
import datetime
import types
import collections.abc
import _zivid
import zivid
import zivid._capture_assistant_suggest_settings_parameters_converter
from zivid._capture_assistant_suggest_settings_parameters_converter import (
    to_internal_capture_assistant_suggest_settings_parameters,
)


"""Auto generated, do not edit"""
import datetime
import types
import collections.abc
import _zivid
import zivid

# import zivid._suggest_settings_parameters_converter


class SuggestSettingsParameters:
    class AmbientLightFrequency:
        hz50 = "hz50"
        hz60 = "hz60"
        none = "none"

        _valid_values = {
            "hz50": _zivid.capture_assistant.SuggestSettingsParameters.AmbientLightFrequency.hz50,
            "hz60": _zivid.capture_assistant.SuggestSettingsParameters.AmbientLightFrequency.hz60,
            "none": _zivid.capture_assistant.SuggestSettingsParameters.AmbientLightFrequency.none,
        }

        @classmethod
        def valid_values(cls):
            return [
                cls.hz50,
                cls.hz60,
                cls.none,
            ]

    def __init__(
        self,
        ambient_light_frequency=_zivid.capture_assistant.SuggestSettingsParameters()
        .AmbientLightFrequency()
        .value,
        max_capture_time=_zivid.capture_assistant.SuggestSettingsParameters()
        .MaxCaptureTime()
        .value,
    ):
        if isinstance(
            ambient_light_frequency,
            _zivid.capture_assistant.SuggestSettingsParameters.AmbientLightFrequency.enum,
        ):
            self._ambient_light_frequency = ambient_light_frequency
        elif isinstance(ambient_light_frequency, (str,)):
            self._ambient_light_frequency = _convert_to_internal(
                ambient_light_frequency
            )
        else:
            raise TypeError(
                "Unsupported type, expected: (str,), got {value_type}".format(
                    value_type=type(ambient_light_frequency)
                )
            )
        if isinstance(max_capture_time, (datetime.timedelta,)):
            self._max_capture_time = _zivid.capture_assistant.SuggestSettingsParameters.MaxCaptureTime(
                max_capture_time
            )
        else:
            raise TypeError(
                "Unsupported type, expected: (datetime.timedelta,), got {value_type}".format(
                    value_type=type(max_capture_time)
                )
            )

    @property
    def ambient_light_frequency(self):
        for (
            key,
            value,
        ) in SuggestSettingsParameters.AmbientLightFrequency._valid_values.items():
            if value == self._ambient_light_frequency:
                return key
        raise ValueError(
            "Unsupported value {value}".format(value=self._ambient_light_frequency)
        )

    @property
    def max_capture_time(self):
        return self._max_capture_time.value

    @ambient_light_frequency.setter
    def ambient_light_frequency(self, value):
        if isinstance(value, (str,)):
            self._ambient_light_frequency = _convert_to_internal(value)
        else:
            raise TypeError(
                "Unsupported type, expected: str, got {value_type}".format(
                    value_type=type(value)
                )
            )

    @max_capture_time.setter
    def max_capture_time(self, value):
        if isinstance(value, (collections.abc.Iterable,)):
            self._max_capture_time = _zivid.capture_assistant.SuggestSettingsParameters.MaxCaptureTime(
                value
            )
        else:
            raise TypeError(
                "Unsupported type, expected: collections.abc.Iterable, got {value_type}".format(
                    value_type=type(value)
                )
            )

    def __eq__(self, other):
        if (
            self._ambient_light_frequency == other._ambient_light_frequency
            and self._max_capture_time == other._max_capture_time
        ):
            return True
        return False

    def __str__(self):
        return str(
            zivid._capture_assistant_suggest_settings_parameters_converter.to_internal_capture_assistant_suggest_settings_parameters(
                self
            )
        )


# class SuggestSettingsParameters:
#     class AmbientLightFrequency:
#         hz50 = "hz50"
#         hz60 = "hz60"
#         none = "none"
#
#         _valid_values = {
#             "hz50": _zivid.capture_assistant.SuggestSettingsParameters.AmbientLightFrequency.hz50,
#             "hz60": _zivid.capture_assistant.SuggestSettingsParameters.AmbientLightFrequency.hz60,
#             "none": _zivid.capture_assistant.SuggestSettingsParameters.AmbientLightFrequency.none,
#         }
#
#         @classmethod
#         def valid_values(cls):
#             return [
#                 cls.hz50,
#                 cls.hz60,
#                 cls.none,
#             ]
#     def __init__(
#         self,
#         ambient_light_frequency=_zivid.capture_assistant.SuggestSettingsParameters()
#         .AmbientLightFrequency()
#         .value,
#         max_capture_time=_zivid.capture_assistant.SuggestSettingsParameters()
#         .MaxCaptureTime()
#         .value,
#     ):
#
#         if isinstance(ambient_light_frequency, (str,)):
#             self._ambient_light_frequency = _convert_to_internal(ambient_light_frequency)
#         else:
#             raise TypeError(
#                 "Unsupported type, expected: (str,), got {value_type}".format(
#                     value_type=type(ambient_light_frequency)
#                 )
#             )
#         if isinstance(max_capture_time, (collections.abc.Iterable,)):
#             self._max_capture_time = _zivid.capture_assistant.SuggestSettingsParameters.MaxCaptureTime(
#                 max_capture_time
#             )
#         else:
#             raise TypeError(
#                 "Unsupported type, expected: (collections.abc.Iterable,), got {value_type}".format(
#                     value_type=type(max_capture_time)
#                 )
#             )
#
#     @property
#     def ambient_light_frequency(self):
#         for (
#             key,
#             value,
#         ) in SuggestSettingsParameters.AmbientLightFrequency._valid_values.items():
#             if value == self._ambient_light_frequency:
#                 return key
#         raise ValueError(
#             "Unsupported value {value}".format(value=self._ambient_light_frequency)
#         )
#
#     @property
#     def max_capture_time(self):
#         return self._max_capture_time.value
#
#     @ambient_light_frequency.setter
#     def ambient_light_frequency(self, value):
#         if isinstance(value, (str,)):
#             self._ambient_light_frequency = _convert_to_internal(value)
#         else:
#             raise TypeError(
#                 "Unsupported type, expected: str, got {value_type}".format(
#                     value_type=type(value)
#                 )
#             )
#
#     @max_capture_time.setter
#     def max_capture_time(self, value):
#         if isinstance(value, (collections.abc.Iterable,)):
#             self._max_capture_time = _zivid.capture_assistant.SuggestSettingsParameters.MaxCaptureTime(
#                 value
#             )
#         else:
#             raise TypeError(
#                 "Unsupported type, expected: collections.abc.Iterable, got {value_type}".format(
#                     value_type=type(value)
#                 )
#             )
#
#     def __eq__(self, other):
#         if (
#             self._ambient_light_frequency == other._ambient_light_frequency
#             and self._max_capture_time == other._max_capture_time
#         ):
#             return True
#         return False
#
#     def __str__(self):
#         return str(
#             zivid._capture_assistant.suggest_settings_parameters_converter.to_internal_capture_assistant.suggest_settings_parameters(
#                 self
#             )
#         )


# class SuggestSettingsParameters:
#     class AmbientLightFrequency:
#         hz50 = "hz50"
#         hz60 = "hz60"
#         none = "none"
#
#         _valid_values = {
#             "hz50": _zivid.capture_assistant.SuggestSettingsParameters.AmbientLightFrequency.hz50,
#             "hz60": _zivid.capture_assistant.SuggestSettingsParameters.AmbientLightFrequency.hz60,
#             "none": _zivid.capture_assistant.SuggestSettingsParameters.AmbientLightFrequency.none,
#         }
#
#         @classmethod
#         def valid_values(cls):
#             return [
#                 cls.hz50,
#                 cls.hz60,
#                 cls.none,
#             ]
#
#         def __init__(self, value=none):
#             self._value = value
#
#         def __eq__(self, other):
#             if self.value == other.value:
#                 return True
#             return False
#
#         def __str__(self):
#             return str(
#                 zivid._suggest_settings_parameters_converter.to_internal_ambient_light_frequency(
#                     self
#                 )
#             )
#
#     def __init__(
#         self,
#         max_capture_time=_zivid.capture_assistant.SuggestSettingsParameters()
#         .MaxCaptureTime()
#         .value,
#         ambient_light_frequency="none",
#     ):
#
#         self._max_capture_time = _zivid.capture_assistant.SuggestSettingsParameters.MaxCaptureTime(
#             max_capture_time
#         )
#         self._ambient_light_frequency = _convert_to_internal(ambient_light_frequency)
#         # if ambient_light_frequency is None:
#         #     ambient_light_frequency = (
#         #         zivid.capture_assistant.SuggestSettingsParameters.AmbientLightFrequency()
#         #     )
#         # if not isinstance(
#         #     ambient_light_frequency,
#         #     zivid.capture_assistant.SuggestSettingsParameters.AmbientLightFrequency,
#         # ):
#         #     raise TypeError(
#         #         "Unsupported type: {value}".format(value=type(ambient_light_frequency))
#         #     )
#         # self._ambient_light_frequency = ambient_light_frequency
#
#     @property
#     def max_capture_time(self):
#         return self._max_capture_time.value
#
#     @property
#     def ambient_light_frequency(self):
#         for (
#             key,
#             value,
#         ) in SuggestSettingsParameters.AmbientLightFrequency._valid_values.items():
#             if value == self._ambient_light_frequency:
#                 return key
#         raise ValueError(
#             "Unsupported value {value}".format(value=self._ambient_light_frequency)
#         )
#
#     @max_capture_time.setter
#     def max_capture_time(self, value):
#         self._max_capture_time = _zivid.capture_assistant.SuggestSettingsParameters.MaxCaptureTime(
#             value
#         )
#
#     @ambient_light_frequency.setter
#     def ambient_light_frequency(self, value):
#         self._ambient_light_frequency = _convert_to_internal(value)
#         # if not isinstance(
#         #     value,
#         #     zivid.capture_assistant.SuggestSettingsParameters.AmbientLightFrequency,
#         # ):
#         #     raise TypeError("Unsupported type {value}".format(value=type(value)))
#         # self._ambient_light_frequency = value
#
#     def __eq__(self, other):
#         if (
#             self._max_capture_time == other._max_capture_time
#             and self._ambient_light_frequency == other._ambient_light_frequency
#         ):
#             return True
#         return False
#
#     def __str__(self):
#         return str(
#             zivid._suggest_settings_parameters_converter.to_internal_suggest_settings_parameters(
#                 self
#             )
#         )
#


def _convert_to_internal(ambient_light_frequency):
    if isinstance(ambient_light_frequency, str):
        if (
            ambient_light_frequency
            not in SuggestSettingsParameters.AmbientLightFrequency._valid_values
        ):
            raise TypeError(
                "Unsupported value {value}".format(value=ambient_light_frequency)
            )
        ambient_light_frequency = SuggestSettingsParameters.AmbientLightFrequency._valid_values[
            ambient_light_frequency
        ]
        if not isinstance(
            ambient_light_frequency,
            _zivid.capture_assistant.SuggestSettingsParameters.AmbientLightFrequency.enum,
        ):
            raise TypeError(
                "Unsupported type: {value}".format(value=type(ambient_light_frequency))
            )
        return ambient_light_frequency
    raise TypeError(
        "Unsupported type: {value}".format(value=type(ambient_light_frequency))
    )


#
# class SuggestSettingsParameters:
#     class AmbientLightFrequency:
#         hz50 = "hz50"
#         hz60 = "hz60"
#         none = "none"
#
#         _valid_values = {
#             "hz50": _zivid.capture_assistant.SuggestSettingsParameters.AmbientLightFrequency.hz50,
#             "hz60": _zivid.capture_assistant.SuggestSettingsParameters.AmbientLightFrequency.hz60,
#             "none": _zivid.capture_assistant.SuggestSettingsParameters.AmbientLightFrequency.none,
#         }
#
#         @classmethod
#         def valid_values(cls):
#             return [
#                 cls.hz50,
#                 cls.hz60,
#                 cls.none,
#             ]
#
#     def __init__(
#         self,
#         max_capture_time=_zivid.capture_assistant.SuggestSettingsParameters()
#         .MaxCaptureTime()
#         .value,
#         ambient_light_frequency=none,
#     ):
#
#         if max_capture_time is not None:
#             self._max_capture_time = _zivid.capture_assistant.SuggestSettingsParameters.MaxCaptureTime(
#                 max_capture_time
#             )
#         else:
#             self._max_capture_time = (
#                 _zivid.capture_assistant.SuggestSettingsParameters.MaxCaptureTime()
#             )
#         if ambient_light_frequency is None:
#             ambient_light_frequency = (
#                 _zivid.capture_assistant.SuggestSettingsParameters.AmbientLightFrequency().value
#             )
#         if isinstance(ambient_light_frequency, str):
#             if (
#                 ambient_light_frequency
#                 not in SuggestSettingsParameters.AmbientLightFrequency._valid_values
#             ):
#                 raise TypeError(
#                     "Unsupported value {value}".format(value=ambient_light_frequency)
#                 )
#             ambient_light_frequency = SuggestSettingsParameters.AmbientLightFrequency._valid_values[
#                 ambient_light_frequency
#             ]
#         if not isinstance(
#             ambient_light_frequency,
#             _zivid.capture_assistant.SuggestSettingsParameters.AmbientLightFrequency.enum,
#         ):
#             raise TypeError(
#                 "Unsupported type: {value}".format(value=type(ambient_light_frequency))
#             )
#         self._ambient_light_frequency = ambient_light_frequency
#
#     @property
#     def max_capture_time(self):
#         return self._max_capture_time.value
#
#     @property
#     def ambient_light_frequency(self):
#         for (
#             key,
#             value,
#         ) in SuggestSettingsParameters.AmbientLightFrequency._valid_values.items():
#             if value == self._ambient_light_frequency:
#                 return key
#         raise ValueError(
#             "Unsupported value {value}".format(value=self._ambient_light_frequency)
#         )
#
#     @max_capture_time.setter
#     def max_capture_time(self, value):
#         self._max_capture_time = _zivid.capture_assistant.SuggestSettingsParameters.MaxCaptureTime(
#             value
#         )
#
#     @ambient_light_frequency.setter
#     def ambient_light_frequency(self, value):
#         if not isinstance(value, str):
#             raise TypeError("Unsupported type {value}".format(value=type(value)))
#         if value not in SuggestSettingsParameters.AmbientLightFrequency.valid_values():
#             raise TypeError("Unsupported value {value}".format(value=value))
#
#         ambient_light_frequency = SuggestSettingsParameters.AmbientLightFrequency._valid_values[
#             value
#         ]
#         self._ambient_light_frequency = ambient_light_frequency
#
#     def __eq__(self, other):
#         if (
#             self._max_capture_time == other._max_capture_time
#             and self._ambient_light_frequency == other._ambient_light_frequency
#         ):
#             return True
#         return False
#
#     def __str__(self):
#         return """SuggestSettingsParameters:
#     max_capture_time: {max_capture_time}
#     ambient_light_frequency: {ambient_light_frequency}
#     """.format(
#             max_capture_time=self.max_capture_time,
#             ambient_light_frequency=self.ambient_light_frequency,
#         )


def suggest_settings(camera, suggest_settings_parameters):
    """Find settings for the current scene based on the suggest_settings_parameters.

    The suggested settings returned from this function should be passed into hdr.capture to perform the actual capture.

    Args:
        camera: an instance of zivid.Camera
        suggest_settings_parameters: an instance of zivid.capture_assistant.SuggestSettingsParameters which provides
                                     parameters (e.g., max capture time constraint) to the suggest_settings algorithm.

    Returns:
        Settings instance

    """
    internal_settings = _zivid.capture_assistant.suggest_settings(
        camera._Camera__impl,  # pylint: disable=protected-access
        to_internal_capture_assistant_suggest_settings_parameters(
            suggest_settings_parameters
        ),
    )
    return _settings_converter.to_settings(internal_settings)
