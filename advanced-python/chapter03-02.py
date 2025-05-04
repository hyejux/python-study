# 벡터 (x,y) (5,2)
# (5,2) + (5,3) = (9,5)


class Vector(object):
      def __init__(self, *arg): #패킹
            '''
            Create a vector, example : v = Vector(5,10)
            '''
            if len(arg) == 0:
                 self._x, self._y = 0, 0
            else:
                 self._x, self._y = arg

      def __repr__(self):
            '''Retrun the vector informations'''
            return 'Vector(%r, %r)' % (self._x, self._y)
      
      def __add__(self, other):
            '''Return the vector addtion of self and other'''
            return Vector(self._x + other._x, self._y + other._y)
      
      def __mul__(self, y):
            '''Return the vector addtion of self and other'''
            return Vector(self._x * y, self._y * y)

      def __bool__(self):
            print('warging!!! 0,0')
            return bool(max(self._x, self._y)) 


# Vector 인스턴스 생성

v1 = Vector(5,7)
v2 = Vector(23,35)
v3 = Vector()

print(Vector.__init__.__doc__)
print(Vector.__repr__.__doc__)
print(Vector.__add__.__doc__)

print(v1,v2,v3)
print(v1 + v2)
print(v1 * 3)
print(v2 * 3)
print(bool(v1), bool(v2), bool(v3))




        