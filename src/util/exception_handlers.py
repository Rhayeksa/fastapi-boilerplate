from fastapi import Request
from slowapi.errors import RateLimitExceeded

from src.configs import templates
# from src.util.menu import f as menu
from src.util.response import f as response


async def http_code_429(request: Request, exc: RateLimitExceeded):
    print(f"\nError {exc}\n")
    accept = request.headers.get("accept", "")
    if "text/html" in accept:
        # token = request.cookies.get("x-access-token")
        return templates.TemplateResponse(
            name="pages/error.html",
            context={
                "request": request,
                # "token": token,
                "err": {"code": 429, "msg": "Too Many Requests"},
                # "menu": await menu(token=token),
            },
            status_code=429
        )
    return response(code=429, message="Too many requests, please try again later.")


async def http_code_500(request: Request, exc: Exception):
    print(f"\nError 500: {exc}\n")
    return templates.TemplateResponse(
        name="pages/error.html",
        context={
            "request": request,
            "err": {"code": 500, "msg": "Internal Server Error"}
        },
        status_code=500
    )


async def http_code_404(request: Request, exc: Exception = None):
    print(f"\nError {exc}\n")
    return templates.TemplateResponse(
        name="pages/error.html",
        context={
            "request": request,
            "err": {"code": 404, "msg": "Page Not Found"},
        },
        status_code=404
    )
