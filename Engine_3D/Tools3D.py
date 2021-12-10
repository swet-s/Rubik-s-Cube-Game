from Engine_3D.Vector import Quaternion as Q4, Vector3 as V3, Vector2 as V2


def Displace_z(point, cam=800):
    dx, dy, dz = point
    pix = V2(dx, dy)
    if dz < cam:
        pix = (pix * cam) / (cam - dz)
    else:
        pix = V2(800, 600)
    return round(pix)


def Rotate_axis(coor, axis, angle):
    angle = np.radians(angle)
    q = Q4(np.cos(angle / 2), *(axis * np.sin(angle / 2)))
    qi = Q4(np.cos(-angle / 2), *(axis * np.sin(-angle / 2)))
    prod1 = q * Q4(0, *coor)
    prod2 = prod1 * qi
    coor.x, coor.y, coor.z = V3(prod2.x, prod2.y, prod2.z)


def RotateX(angle, vector3):
    rotmatx = np.array([[1, 0, 0],
                        [0, np.cos(angle), -np.sin(angle)],
                        [0, np.sin(angle), np.cos(angle)]])
    return rotmatx.dot(np.array([*vector3]))


def RotateY(angle, point3):
    rotmaty = np.array([[np.cos(angle), 0, np.sin(angle)],
                        [0, 1, 0],
                        [-np.sin(angle), 0, np.cos(angle)]])
    return rotmaty.dot(np.array([*point3]))


def RotateZ(angle, point3):
    rotmatz = np.array([[np.cos(angle), -np.sin(angle), 0],
                        [np.sin(angle), np.cos(angle), 0],
                        [0, 0, 1]])
    return rotmatz.dot(np.array([*point3]))
