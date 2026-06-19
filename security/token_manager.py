import secrets
import hashlib


class TokenManager:

    def generate_refresh_token(

        self

    ):

        return secrets.token_hex(16)

    def hash_token(

        self,

        token

    ):

        return hashlib.sha256(

            token.encode(

                "utf-8"

            )

        ).hexdigest()

    def verify_token(

        self,

        plain_token,

        stored_token

    ):

        hashed = hashlib.sha256(

            plain_token.encode(

                "utf-8"

            )

        ).hexdigest()

        return hashed == stored_token
