@app.task
async def sum_squares_slower(a: int, b: int) -> int:
  result1 = await calculate_square(a)
  result2 = await calculate_square(b)
  return result1 + result2

@app.task
def calculate_square(a: int) -> int:
  return a * a
