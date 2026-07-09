from fastapi import APIRouter, Request
from starlette.responses import RedirectResponse

from app.services.gmail.auth import oauth

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.get("/login")
async def login(request: Request):

    redirect_uri = request.url_for("auth_callback")

    return await oauth.google.authorize_redirect(request, redirect_uri)


@router.get("/callback", name="auth_callback")
async def auth_callback(request: Request):

    token = await oauth.google.authorize_access_token(request)

    user = token.get("userinfo")

    return {
        "message": "Authentication Successful",
        "email": user["email"],
        "name": user["name"],
    }
