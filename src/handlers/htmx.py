from fastapi import Request
from fastapi.responses import HTMLResponse
import math

counter_i = 0
items = ["a", "b", "c"]

async def counter_button_clicked(request: Request) -> list[HTMLResponse]:
    global counter_i
    global items

    counter_i += 1
    items = [math.factorial(i) for i in range(counter_i)]

    return HTMLResponse(str(counter_i) + "\n" + str(items))