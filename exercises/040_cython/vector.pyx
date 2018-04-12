def object is_normalized(object vector):
    return vector.magnitude2() == 1


class Vector3:
    cdef public double x, y, z

    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z

    def __add__(self, other):
        if isinstance(self, Vector3) and isinstance(other, Vector3):
            return Vector3(_self.x + _other.x, _self.y + _other.y, _self.z + _other.z)
        else:
            return NotImplemented

    def double magnitude2(self):
        return self.x ** 2 + self.y ** 2 + self.z ** 2
