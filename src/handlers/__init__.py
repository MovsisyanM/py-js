from fastapi import Request
from fastapi.responses import Response
from fastapi.templating import Jinja2Templates

from .htmx import counter_button_clicked  # noqa: F401

templates = Jinja2Templates(directory="templates")


async def root(request: Request) -> Response:

    return templates.TemplateResponse(
        "home.html",
        {
            "request": request,
            "counter_i": 0,
            "items": ["a", "b", "c"],
            "title": "wow"
        }
    )
