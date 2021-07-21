# Partial implementation of Cesium's northEastDownToFixedFrame method from Javascript to Python
import numpy as np
import numpy.linalg as LA

def northEastDownToFixedFrame(origin):
#
#         if (CesiumMath.equalsEpsilon(origin.x, 0.0, CesiumMath.EPSILON14) &&
#             CesiumMath.equalsEpsilon(origin.y, 0.0, CesiumMath.EPSILON14)) {
#             // The poles are special cases.  If x and y are zero, assume origin is at a pole.
#             var sign = CesiumMath.sign(origin.z);
#             if (!defined(result)) {
#                 return new Matrix4(
#                   -sign, 0.0,   0.0, origin.x,
#                     0.0, 1.0,   0.0, origin.y,
#                     0.0, 0.0, -sign, origin.z,
#                     0.0, 0.0,   0.0, 1.0);
#             }
#             result[0] = -sign;
#             result[1] = 0.0;
#             result[2] = 0.0;
#             result[3] = 0.0;
#             result[4] = 0.0;
#             result[5] = 1.0;
#             result[6] = 0.0;
#             result[7] = 0.0;
#             result[8] = 0.0;
#             result[9] = 0.0;
#             result[10] = -sign;
#             result[11] = 0.0;
#             result[12] = origin.x;
#             result[13] = origin.y;
#             result[14] = origin.z;
#             result[15] = 1.0;
#             return result;
#         }
#
    ellipsoid = np.array([6378137.0, 6378137.0, 6356752.3142451793])
    tangent = np.array([0,0,0])

    tangent[0] = -origin[1]
    tangent[1] = origin[0]
    tangent[2] = 0.0

    nnorm = np.array([(1/ellipsoid[0]**2),  (1/ellipsoid[1]**2), (1/ellipsoid[2]**2)])
    nnorm = np.mat(nnorm)
    normal = np.multiply(origin, nnorm)
    normal = normal/LA.norm(normal)
    tangent = tangent/LA.norm(tangent, 3)
    bitangent = np.cross(normal, tangent)
    normal = np.asarray(normal[0])
    normal = np.asarray(normal[0])
    bitangent = np.asarray(bitangent[0])

#         if (!defined(result)) {
#             return new Matrix4(
#                     bitangent.x, tangent.x, -normal.x, origin.x,
#                     bitangent.y, tangent.y, -normal.y, origin.y,
#                     bitangent.z, tangent.z, -normal.z, origin.z,
#                     0.0,       0.0,         0.0,      1.0);
#         }

    return np.array([[bitangent[0], tangent[0], -normal[0], origin[0]],
                    [bitangent[1], tangent[1], -normal[1], origin[1]],
                    [bitangent[2], tangent[2], -normal[2], origin[2]],
                    [0, 0, 0, 1]])
