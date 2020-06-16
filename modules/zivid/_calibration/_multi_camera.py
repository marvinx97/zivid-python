import _zivid


class MultiCameraResidual:
    def __init__(self, internal_multi_camera_residual):
        if not isinstance(
            internal_multi_camera_residual, _zivid.calibration.MultiCameraResidual
        ):
            raise TypeError(f"Unsupported type: {type(internal_multi_camera_residual)}")
        self.__impl = internal_multi_camera_residual

    def translation(self):
        return self.__impl.translation()

    def __str__(self):
        return str(self.__impl)


class MultiCameraOutput:
    def __init__(self, internal_multi_camera_output):
        if not isinstance(
            internal_multi_camera_output, _zivid.calibration.MultiCameraOutput
        ):
            raise TypeError(f"Unsupported type: {type(internal_multi_camera_output)}")
        self.__impl = internal_multi_camera_output

    def valid(self):
        return self.__impl.valid()

    def __bool__(self):
        return bool(self.__impl)

    def transforms(self):
        return self.__impl.transforms()

    def residuals(self):
        return self.__impl.residuals()

    def __str__(self):
        return str(self.__impl)


def calibrate_multi_camera(detection_results):
    return MultiCameraOutput(
        _zivid.calibration.calibrate_multi_camera(
            [
                detection_result._DetectionResult__impl
                for detection_result in detection_results
            ]
        )
    )


# import zivid.calibration.hand_eye
# zivid.calibration.calibrate_eye_in_hand
#
# from zivid.calibration import calibrate_eye_in_hand
# calibrate_eye_in_hand
