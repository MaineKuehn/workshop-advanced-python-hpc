cpdef bint is_normalized(Vector3 vector):
    return vector.magnitude2() == 1


cdef class Vector3:
    cdef public double x, y, z

    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z

    def __add__(self, other):
        cdef Vector3 _self, _other
        try:
            _self = self
            _other = other
            return Vector3(_self.x + _other.x, _self.y + _other.y, _self.z + _other.z)
        except TypeError:
            return NotImplemented

    cpdef double magnitude2(self):
        return self.x ** 2 + self.y ** 2 + self.z ** 2
