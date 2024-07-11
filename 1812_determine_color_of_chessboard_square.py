# white square if coordinate values are in different parity groups
class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        z = "1357aceg"
        x, y = coordinates
        return (x in z and y not in z) or (x not in z and y in z)