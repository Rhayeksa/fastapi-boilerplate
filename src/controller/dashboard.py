from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, RedirectResponse

from src.configs import session, templates
from src.util.exception_handlers import http_code_500
from src.util.menu import f as menu
from src.util.rate_limiter import limiter
from src.util.verify_token import f as verify_token

router = APIRouter()


@router.get(
    path="/",
    response_class=HTMLResponse,
    include_in_schema=False,
)
# @limiter.limit("30/minute")  # limit requests | second, minute, hour, day
async def f(request: Request):
    # token = request.cookies.get("x-access-token")
    # payload = verify_token(token=token)
    # if not token or isinstance(payload, str):
    #     return RedirectResponse(url="/login")
    try:
        return templates.TemplateResponse(
            request=request,
            context={
                # "role": user["role"],
                # "pasien": pasien,
                # "menu": await menu(token=token),
            },
            name="pages/dashboard.html",
        )
    except Exception as e:
        return await http_code_500(request=request, exc=e, module="dashboard GET")
    finally:
        session.close()
