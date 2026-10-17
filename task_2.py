import cmath
import math
import matplotlib.pyplot as plt


def koch_curve(z1, z2, level):
  """Рекурсивно будує криву Коха між двома комплексними точками z1 та z2
     згідно з правилом поділу на 3 частини та побудови трикутного піка.
  """
  if level == 0:
    return [z1, z2]

  v = z2 - z1
  pA = z1 + v / 3.0
  pB = z1 + 2.0 * v / 3.0

  # Поворот на +60 градусів (pi / 3)
  rot = cmath.exp(1j * math.pi / 3.0)
  pC = pA + (v / 3.0) * rot

  # Рекурсивний виклик для 4 ланок
  seg1 = koch_curve(z1, pA, level - 1)
  seg2 = koch_curve(pA, pC, level - 1)
  seg3 = koch_curve(pC, pB, level - 1)
  seg4 = koch_curve(pB, z2, level - 1)

  return seg1[:-1] + seg2[:-1] + seg3[:-1] + seg4


if __name__ == "__main__":
  try:
    user_input = input("Введіть рівень рекурсії n : ")
    level = int(user_input)

    if level < 0:
      print("Рівень рекурсії не може бути від'ємним.")
    else:
      print(f"Генерація кривої Коха для рівня n = {level}...")

      # Початковий горизонтальний відрізок від (0, 0) до (1, 0)
      z1 = complex(0.0, 0.0)
      z2 = complex(1.0, 0.0)

      # Отримуємо точки виключно для введеного рівня
      points = koch_curve(z1, z2, level)
      x = [p.real for p in points]
      y = [p.imag for p in points]

      # Відображаємо тільки єдиний графік для заданого рівня
      plt.figure(figsize=(10, 5))
      plt.plot(x, y, color="black", linewidth=1.2)
      plt.title(f"Крива Коха (n = {level})", fontsize=14)
      plt.axis("equal")
      plt.axis("off")
      plt.show()

  except ValueError:
    print("Помилка: будь ласка, введіть ціле число.")