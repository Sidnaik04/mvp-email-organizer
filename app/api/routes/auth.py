from fastapi import APIRouter, Request
from starlette.responses import RedirectResponse

from app.services.gmail.auth import oauth
from app.database.models import User
from app.database.session import SessionLocal

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.get("/login")
async def login(request: Request):

    redirect_uri = request.url_for("auth_callback")

    return await oauth.google.authorize_redirect(request, redirect_uri)


@router.get("/callback", name="auth_callback")
async def auth_callback(request: Request):

    token = await oauth.google.authorize_access_token(request)

    user = token["userinfo"]

    db = SessionLocal()

    existing = db.query(User).filter(User.email == user["email"]).first()

    if existing:
        existing.access_token = token["access_token"]
        existing.refresh_token = token.get("refresh_token")

    else:

        existing = User(
            email=user["email"],
            name=user["name"],
            access_token=token["access_token"],
            refresh_token=token.get("refresh_token"),
        )

        db.add(existing)

    db.commit()

    db.close()

    return RedirectResponse(url="http://localhost:8501/1_Dashboard")
