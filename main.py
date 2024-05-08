from fastapi import FastAPI

app = FastAPI()

def round(
    num: float,
    decimal: int = 0,
):
    if decimal == 0:
        return int(num + 0.5)
    else:
        digit_value = 10 ** decimal
        return int(num * digit_value + 0.5) / digit_value