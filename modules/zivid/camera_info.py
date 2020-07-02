"""Auto generated, do not edit"""
import _zivid
import zivid
import zivid._camera_info_converter


class CameraInfo:
    class Revision:
        def __init__(
            self,
            major=_zivid.CameraInfo().Revision().Major().value,
            minor=_zivid.CameraInfo().Revision().Minor().value,
        ):

            self._major = _zivid.CameraInfo.Revision.Major(major)
            self._minor = _zivid.CameraInfo.Revision.Minor(minor)

        @property
        def major(self):
            return self._major.value

        @property
        def minor(self):
            return self._minor.value

        @major.setter
        def major(self, value):
            self._major = _zivid.CameraInfo.Revision.Major(value)

        @minor.setter
        def minor(self, value):
            self._minor = _zivid.CameraInfo.Revision.Minor(value)

        def __eq__(self, other):
            if self._major == other._major and self._minor == other._minor:
                return True
            return False

        def __str__(self):
            return str(zivid._camera_info_converter.to_internal_revision(self))

    class UserData:
        def __init__(
            self, max_size_bytes=_zivid.CameraInfo().UserData().MaxSizeBytes().value,
        ):

            self._max_size_bytes = _zivid.CameraInfo.UserData.MaxSizeBytes(
                max_size_bytes
            )

        @property
        def max_size_bytes(self):
            return self._max_size_bytes.value

        @max_size_bytes.setter
        def max_size_bytes(self, value):
            self._max_size_bytes = _zivid.CameraInfo.UserData.MaxSizeBytes(value)

        def __eq__(self, other):
            if self._max_size_bytes == other._max_size_bytes:
                return True
            return False

        def __str__(self):
            return str(zivid._camera_info_converter.to_internal_user_data(self))

    def __init__(
        self,
        firmware_version=_zivid.CameraInfo().FirmwareVersion().value,
        model_name=_zivid.CameraInfo().ModelName().value,
        serial_number=_zivid.CameraInfo().SerialNumber().value,
        revision=None,
        user_data=None,
    ):

        self._firmware_version = _zivid.CameraInfo.FirmwareVersion(firmware_version)
        self._model_name = _zivid.CameraInfo.ModelName(model_name)
        self._serial_number = _zivid.CameraInfo.SerialNumber(serial_number)
        if revision is None:
            revision = zivid.CameraInfo.Revision()
        if not isinstance(revision, zivid.CameraInfo.Revision):
            raise TypeError("Unsupported type: {value}".format(value=type(revision)))
        self._revision = revision
        if user_data is None:
            user_data = zivid.CameraInfo.UserData()
        if not isinstance(user_data, zivid.CameraInfo.UserData):
            raise TypeError("Unsupported type: {value}".format(value=type(user_data)))
        self._user_data = user_data

    @property
    def firmware_version(self):
        return self._firmware_version.value

    @property
    def model_name(self):
        return self._model_name.value

    @property
    def serial_number(self):
        return self._serial_number.value

    @property
    def revision(self):
        return self._revision

    @property
    def user_data(self):
        return self._user_data

    @firmware_version.setter
    def firmware_version(self, value):
        self._firmware_version = _zivid.CameraInfo.FirmwareVersion(value)

    @model_name.setter
    def model_name(self, value):
        self._model_name = _zivid.CameraInfo.ModelName(value)

    @serial_number.setter
    def serial_number(self, value):
        self._serial_number = _zivid.CameraInfo.SerialNumber(value)

    @revision.setter
    def revision(self, value):
        if not isinstance(value, zivid.CameraInfo.Revision):
            raise TypeError("Unsupported type {value}".format(value=type(value)))
        self._revision = value

    @user_data.setter
    def user_data(self, value):
        if not isinstance(value, zivid.CameraInfo.UserData):
            raise TypeError("Unsupported type {value}".format(value=type(value)))
        self._user_data = value

    def __eq__(self, other):
        if (
            self._firmware_version == other._firmware_version
            and self._model_name == other._model_name
            and self._serial_number == other._serial_number
            and self._revision == other._revision
            and self._user_data == other._user_data
        ):
            return True
        return False

    def __str__(self):
        return str(zivid._camera_info_converter.to_internal_camera_info(self))
