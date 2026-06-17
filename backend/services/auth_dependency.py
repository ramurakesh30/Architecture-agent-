from fastapi import Depends
from fastapi import HTTPException
from fastapi.security import HTTPBearer

from jose import jwt

from backend.app.config.settings import Settings

from backend.services.auth_service import (
    ALGORITHM
)

security = HTTPBearer()

def get_current_user_id(
    credentials=Depends(security)
):

    try:

        payload = jwt.decode(

            credentials.credentials,

            Settings.SECRET_KEY,

            algorithms=[ALGORITHM]

        )

        return payload["sub"]

    except Exception:

        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )