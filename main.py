from render_sdk import Workflows

app = Workflows()

@app.task
def calculate_square(a: int) -> int:
  import os
  os.system('lscpu')
  return a * a

if __name__ == "__main__":
  app.start()
