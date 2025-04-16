class Vector:
    def __init__(self, *coordinates):
        self.coordinates = coordinates

    def __repr__(self):
        return f"Vector{self.coordinates}"
    
    def __neg__(self):
        return Vector(*[-coord for coord in self.coordinates])
    
    def __pos__(self):
        return Vector(*self.coordinates)
    
    def __abs__(self):
        return pow(sum(coord ** 2 for coord in self.coordinates), 0.5)
    
    def __invert__(self):
        """Compute a vector that is orthogonal to this one"""
        if len(self.coordinates) <= 1:
            raise TypeError(
                f"Cannot invert vector of length {len(self.coordinates)}"
            )
        
        # Look for two non-zero coordinates to swap
        to_flip = [0, 1]
        for idx, coord in enumerate(self.coordinates):
            if coord:
                to_flip.append(idx)

        # Zero out all coordinates
        coordinates = [0] * len(self.coordinates)

        # except the two we are swapping out
        coordinates[to_flip[-1]] = self.coordinates[to_flip[-2]]
        coordinates[to_flip[-2]] = -self.coordinates[to_flip[-1]]
        return Vector(*coordinates)
    
if __name__ == "__main__":
    pass