import random

class ColorHax():
    RED = 0xf74b20
    BLUE = 0x5833ff
    PERPLE = 0x9900ff
    PINK = 0xff0080
    GRAY = 0x2f3136

    def randomColor():
        return random.choice([ColorHax.RED, ColorHax.BLUE, ColorHax.PERPLE, ColorHax.PINK, ColorHax.GRAY])
    
color = ColorHax
