from math import *


class Vector3:
    count = 0

    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        try:
            sumx = self.x + other.x
            sumy = self.y + other.y
            sumz = self.z + other.z
        except AttributeError:
            sumx = self.x + other
            sumy = self.y + other
            sumz = self.z + other
        return Vector3(sumx, sumy, sumz)

    def __sub__(self, other):
        try:
            subx = self.x - other.x
            suby = self.y - other.y
            subz = self.z - other.z
        except AttributeError:
            subx = self.x - other
            suby = self.y - other
            subz = self.z - other
        return Vector3(subx, suby, subz)

    def __neg__(self):
        subx = -self.x
        suby = -self.y
        subz = -self.z
        return Vector3(subx, suby, subz)

    def __mul__(self, other):
        try:
            mulx = self.x * other.x
            muly = self.y * other.y
            mulz = self.z * other.z
        except AttributeError:
            mulx = self.x * other
            muly = self.y * other
            mulz = self.z * other
        return Vector3(mulx, muly, mulz)

    def __truediv__(self, other):
        try:
            divx = self.x / other.x
            divy = self.y / other.y
            divz = self.z / other.z
        except AttributeError:
            divx = self.x / other
            divy = self.y / other
            divz = self.z / other
        return Vector3(divx, divy, divz)

    def __floordiv__(self, other):
        try:
            divx = self.x // other.x
            divy = self.y // other.y
            divz = self.z // other.z
        except AttributeError:
            divx = self.x // other
            divy = self.y // other
            divz = self.z // other
        return Vector3(divx, divy, divz)

    def __mod__(self, other):
        try:
            modx = self.x % other.x
            mody = self.y % other.y
            modz = self.z % other.z
        except AttributeError:
            modx = self.x % other
            mody = self.y % other
            modz = self.z % other
        return Vector3(modx, mody, modz)

    def __pow__(self, power, modulo=None):
        try:
            powx = self.x ** power.x
            powy = self.y ** power.y
            powz = self.z ** power.z
        except AttributeError:
            powx = self.x ** power
            powy = self.y ** power
            powz = self.z ** power
        return Vector3(powx, powy, powz)

    def dot(self, other):
        mulx = self.x * other.x
        muly = self.y * other.y
        mulz = self.z * other.z
        return mulx + muly + mulz

    def cross(self, other):
        mulx = self.y * other.z - self.z * other.y
        muly = self.z * other.x - self.x * other.z
        mulz = self.x * other.y - self.y * other.x
        return Vector3(mulx, muly, mulz)

    def mang(self):
        mang = sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
        return mang

    def identity(self):
        x, y, z = self
        mang = self.mang()
        if mang != 0:
            cos_a = x / mang
            cos_b = y / mang
            cos_c = z / mang
            return Vector3(cos_a, cos_b, cos_c)
        else:
            return Vector3(0, 0, 0)

    def normalize(self):
        x, y, z = self
        mang = self.mang()
        if mang != 0:
            cos_a = x / mang
            cos_b = y / mang
            cos_c = z / mang
            self.x, self.y, self.z = Vector3(cos_a, cos_b, cos_c)

    # noinspection PyTypeChecker
    def rotate_deg(self, axis, angle):
        angle = radians(angle)
        q = Quaternion(cos(angle / 2), *(axis * sin(angle / 2)))
        qi = Quaternion(cos(-angle / 2), *(axis * sin(-angle / 2)))
        prod1 = q * Quaternion(0, *self)
        prod2 = prod1 * qi
        self.x, self.y, self.z = Vector3(prod2.x, prod2.y, prod2.z)
        return Vector3(prod2.x, prod2.y, prod2.z)

    def angle_bet(self, other):
        dot = self.dot(other)
        mang_prod = self.mang() * other.mang()
        if mang_prod == 0:
            return 0
        else:
            cosine = dot / mang_prod
            if cosine > 1:
                cosine = 1
            elif cosine < -1:
                cosine = -1
            return degrees(acos(cosine))

    def __iter__(self):
        return self

    def __next__(self):
        if self.count == 0:
            self.count += 1
            return self.x
        elif self.count == 1:
            self.count += 1
            return self.y
        elif self.count == 2:
            self.count += 1
            return self.z
        else:
            self.count = 0
            raise StopIteration

    def __round__(self, n=None):
        x = round(self.x, n)
        y = round(self.y, n)
        z = round(self.z, n)
        return Vector3(x, y, z)

    def __repr__(self):
        return f'Vector3{self.x, self.y, self.z}'


class Vector2:
    count = 0

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        try:
            sumx = self.x + other.x
            sumy = self.y + other.y
        except AttributeError:
            sumx = self.x + other
            sumy = self.y + other
        return Vector2(sumx, sumy)

    def __sub__(self, other):
        try:
            subx = self.x - other.x
            suby = self.y - other.y
        except AttributeError:
            subx = self.x - other
            suby = self.y - other
        return Vector2(subx, suby)

    def __neg__(self):
        subx = -self.x
        suby = -self.y
        return Vector2(subx, suby)

    def __mul__(self, other):
        try:
            mulx = self.x * other.x
            muly = self.y * other.y
        except AttributeError:
            mulx = self.x * other
            muly = self.y * other
        return Vector2(mulx, muly)

    def __truediv__(self, other):
        try:
            divx = self.x / other.x
            divy = self.y / other.y
        except AttributeError:
            divx = self.x / other
            divy = self.y / other
        return Vector2(divx, divy)

    def __floordiv__(self, other):
        try:
            divx = self.x // other.x
            divy = self.y // other.y
        except AttributeError:
            divx = self.x // other
            divy = self.y // other
        return Vector2(divx, divy)

    def __mod__(self, other):
        try:
            modx = self.x % other.x
            mody = self.y % other.y
        except AttributeError:
            modx = self.x % other
            mody = self.y % other
        return Vector2(modx, mody)

    def __pow__(self, power, modulo=None):
        try:
            powx = self.x ** power.x
            powy = self.y ** power.y
        except AttributeError:
            powx = self.x ** power
            powy = self.y ** power
        return Vector2(powx, powy)

    def dot(self, other):
        mulx = self.x * other.x
        muly = self.y * other.y
        return mulx + muly

    def cross(self, other):
        mulz = self.x * other.y - self.y * other.x
        return Vector3(0, 0, mulz)

    def mang(self):
        mang = sqrt(self.x ** 2 + self.y ** 2)
        return mang

    def identity(self):
        x, y = self
        mang = self.mang()
        if mang != 0:
            cos_a = x / mang
            cos_b = y / mang
            return Vector2(cos_a, cos_b)
        else:
            return Vector2(0, 0)

    # noinspection PyTypeChecker
    def rotate_deg(self, axis, angle):
        vector3 = Vector3(*self, 0)
        vector3.rotate_deg(Vector3(0, 0, 1), angle)
        x, y, z = vector3.rotate_deg(Vector3(0, 0, 1), angle)
        self.x, self.y = x, y
        return Vector2(x, y)

    def angle_bet(self, other):
        dot = self.dot(other)
        mang_prod = self.mang() * other.mang()
        if mang_prod == 0:
            return 0
        else:
            cosine = dot / mang_prod
            if cosine > 1:
                cosine = 1
            elif cosine < -1:
                cosine = -1
            return degrees(acos(cosine))

    def __iter__(self):
        return self

    def __next__(self):
        if self.count == 0:
            self.count += 1
            return self.x
        elif self.count == 1:
            self.count += 1
            return self.y
        else:
            self.count = 0
            raise StopIteration

    def __round__(self, n=None):
        x = round(self.x, n)
        y = round(self.y, n)
        return Vector2(x, y)

    def __repr__(self):
        return f'Vector2{self.x, self.y}'


class Quaternion:
    def __init__(self, w=0, x=0, y=0, z=0):
        self.w = w
        self.x = x
        self.y = y
        self.z = z

    def __mul__(self, other):
        w = self.w * other.w - self.x * other.x - self.y * other.y - self.z * other.z
        x = self.w * other.x + self.x * other.w + self.y * other.z - self.z * other.y
        y = self.w * other.y - self.x * other.z + self.y * other.w + self.z * other.x
        z = self.w * other.z + self.x * other.y - self.y * other.x + self.z * other.w
        return Quaternion(w, x, y, z)

    def __repr__(self):
        return f'{self.w} {self.x}i {self.y}j {self.z}k'
