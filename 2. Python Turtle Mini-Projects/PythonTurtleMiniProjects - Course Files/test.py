import random

def losowy_kolor_rgb():
  """Generuje losowy kolor w formacie RGB (tuple)."""
  red = random.randint(0, 255)
  green = random.randint(0, 255)
  blue = random.randint(0, 255)
  return (red, green, blue)

losowy_kolor = losowy_kolor_rgb()
print(f"Losowy kolor RGB: {losowy_kolor}")