from math import sqrt, acos, degrees, radians, cos, sin


class Vector:
    def __init__(self, x, y) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(
            self.x + other.x,
            self.y + other.y
        )

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(
            self.x - other.x,
            self.y - other.y
        )

    def __mul__(self, other: float | "Vector") -> float | "Vector":
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

        return Vector(
            self.x * other,
            self.y * other
        )

    @classmethod
    def create_vector_by_two_points(
        cls,
        start_point: tuple,
        end_point: tuple
    ) -> "Vector":
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()

        return Vector(
            self.x / length,
            self.y / length
        )

    def angle_between(self, vector: "Vector") -> int:
        dot_product = self * vector

        cos_a = (
            dot_product /
            (self.get_length() * vector.get_length())
        )

        return round(degrees(acos(cos_a)))

    def get_angle(self) -> int:
        y_axis = Vector(0, 1)
        return self.angle_between(y_axis)

    def rotate(self, degree: int) -> "Vector":
        rad = radians(degree)

        new_x = self.x * cos(rad) - self.y * sin(rad)
        new_y = self.x * sin(rad) + self.y * cos(rad)

        return Vector(new_x, new_y)
