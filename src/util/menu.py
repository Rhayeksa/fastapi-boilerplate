from sqlalchemy import text

from src.configs import POSTGRES_SCHEMA, session
from src.util.verify_token import f as verify_token


async def f(token: str):
    payload = verify_token(token=token)
    if isinstance(payload, str):
        return []
    user = payload["user_id"]
    user = session.execute(
        text(
            f"""
            SELECT role
            FROM {POSTGRES_SCHEMA}.tb_users
            WHERE deleted_at IS NULL
            AND user_id = :user_id
            """
        ), {"user_id": user}
    ).mappings().fetchone()

    result = [
        {
            "icon": "<i class='fa-regular fa-house me-2'></i>",
            "text": "Home",
            "link": "/"
        },
        {
            "icon": "<i class='fa-solid fa-diagram-project me-2'></i>",
            "text": "Cabang",
            "link": f"/cabang"
        },
        {
            "icon": "<i class='fa-regular fa-user me-2'></i>",
            "text": "User",
            "link": f"/user"
        },
        {
            "icon": "<i class='fa-solid fa-arrow-right-from-bracket me-2'></i>",
            "text": "Logout",
            "link": "/logout"
        },
    ]
    if user["role"] == "user_cabang":
        result = [i for i in result if i["text"] not in ["Cabang", "User"]]

    return result
