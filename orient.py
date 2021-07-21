import math
import numpy as np

# [w, x, y, z].
from transformations import rotation_matrix, quaternion_from_matrix, quaternion_multiply, quaternion_conjugate
from pymap3d.ecef import geodetic2ecef

from cesiumNEDtoFixedFrame import northEastDownToFixedFrame


def hpr2Quaternion(lat, lon, alt, heading, pitch, roll):

    rotZ = rotation_matrix(math.radians(heading), [0,0,1])
    rotY = rotation_matrix(math.radians(180 + pitch), [0,1,0])
    rotX = rotation_matrix(math.radians(roll), [1,0,0])
    # print("rotX:",rotX)
    tmp = np.dot(rotZ, rotY)
    rotM = np.dot(tmp, rotX)
    # 4x4 print("rotM:",rotM)

    origin = geodetic2ecef(lat, lon, alt,  deg=True)
    # print("origin:",origin)
    # origin = np.multiply(origin, 1000)
    locTransform = northEastDownToFixedFrame(origin)
    # print("locTransform:",locTransform)

    transMatrix = np.dot(locTransform, rotM)
    tempQ = quaternion_from_matrix(transMatrix)
    return [tempQ[1], tempQ[2], tempQ[3], tempQ[0]]


def corrQuaternion(lat, lon, alt, conj):

    origin = geodetic2ecef(lat, lon, alt,  deg=True)
    # print("origin:",origin)
    # origin = np.multiply(origin, 1000)
    locTransform = northEastDownToFixedFrame(origin)
    # print("locTransform:",locTransform)

    #transMatrix = np.dot(locTransform, rotM)
    x = quaternion_from_matrix(locTransform)
    tempQ = quaternion_multiply(x, conj)

    return [tempQ[1], tempQ[2], tempQ[3], tempQ[0]]





if __name__ == "__main__":
    print(hpr2Quaternion(47, 15, 500, 180, 0, 0))
    print(hpr2Quaternion(47, 15, 500, 0, 180, 0))
    print(hpr2Quaternion(47, 15, 500, 0, 0, 0))
