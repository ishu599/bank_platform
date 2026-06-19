import time

import jwt


class JWTManager:

    def __init__(

        self

    ):
        self.secret = (
    "bank_platform_secret_key_2026_"
    "production_grade_demo_secret"
)
        self.algorithm = "HS256"

        self.expiration = 900

    def generate(

        self,

        username,

        role

    ):

        payload = {

            "username": username,

            "role": role,

            "exp": int(

                time.time()

            ) + self.expiration

        }

        token = jwt.encode(

            payload,

            self.secret,

            algorithm=self.algorithm

        )

        return token

    def verify(

        self,

        token

    ):

        try:

            payload = jwt.decode(

                token,

                self.secret,

                algorithms=[

                    self.algorithm

                ]

            )

            return payload

        except jwt.ExpiredSignatureError:

            raise Exception(

                "Token expired"

            )

        except jwt.InvalidTokenError:

            raise Exception(

                "Invalid token"

            )
