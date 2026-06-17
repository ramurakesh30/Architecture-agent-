from datetime import datetime
from datetime import timedelta

from jose import jwt
from jose import JWTError

from passlib.context import CryptContext
from app.config.settings import Settings



ALGORITHM = (
    "HS256"
)

ACCESS_TOKEN_EXPIRE_DAYS = 7


pwd_context = CryptContext(

    schemes=["bcrypt"],

    deprecated="auto"
)


class AuthService:

    def hash_password(

        self,

        password: str

    ) -> str:

        return pwd_context.hash(
            password
        )

    def verify_password(

        self,

        plain_password: str,

        hashed_password: str

    ) -> bool:

        return pwd_context.verify(

            plain_password,

            hashed_password
        )

    def create_token(

        self,

        user_id: str

    ) -> str:

        expire = (

            datetime.utcnow()

            +

            timedelta(
                days=
                ACCESS_TOKEN_EXPIRE_DAYS
            )
        )

        payload = {

            "sub":
            user_id,

            "exp":
            expire
        }

        return jwt.encode(

            payload,

            Settings.SECRET_KEY,

            algorithm=
            ALGORITHM
        )

    def decode_token(

        self,

        token: str

    ):

        try:

            payload = jwt.decode(

                token,

                Settings.SECRET_KEY,

                algorithms=[
                    ALGORITHM
                ]
            )

            return payload

        except JWTError:

            return None