import _zivid
import numpy as np


class Pose:
    def __init__(self, transformation_matrix):
        # if isinstance(transformation_matrix, np.array):
        #     print("this is array")
        if isinstance(transformation_matrix, np.ndarray):
            print("this is ndarray")
        self.__impl = _zivid.calibration.Pose(transformation_matrix)

    def to_matrix(self):
        print(dir(self.__impl))

    def __str__(self):
        return str(self.__impl)


# namespace Zivid
# {
#     namespace Calibration
#     {
#         /// <summary>
#         /// Describes a robot pose
#         /// </summary>
#         class Pose
#         {
#         public:
#             /// <summary>Pose constructor taking a 4x4 transform.</summary>
#             /// <remarks>
#             /// Translation part of transform should be in units of millimeters.
#             /// The constructor throws if the input transform does not describe pure rotation and translation.
#             /// </remarks>
#             /// <param name="transform">Provides orientation (rotation) and location (translation) for the pose.</param>
#             ZIVID_CORE_EXPORT Pose(const Matrix4x4 &transform);
#
#             /// <summary>Converts robot pose to a 4x4 matrix.</summary>
#             /// <returns>4 by 4 matrix.</returns>
#             ZIVID_CORE_EXPORT Matrix4x4 toMatrix() const;
#
#             /// <summary>Get string representation of the Pose</summary>
#             /// <returns>Pose as string</returns>
#             ZIVID_CORE_EXPORT std::string toString() const;
#
#         private:
#             Matrix4x4 m_transform;
#         };
#
#         /// <summary>Serialize the value to a stream</summary>
#         ZIVID_CORE_EXPORT std::ostream &operator<<(std::ostream &stream, const Pose &pose);
#     } // namespace Calibration
# } // namespace Zivid
#