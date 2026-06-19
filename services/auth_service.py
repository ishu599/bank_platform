import hashlib

from time import time


class AuthService:

    def __init__(

        self,

        repository,

        jwt_manager,

        audit_logger,

        refresh_repository,

        token_manager

    ):

        self.repository = repository

        self.jwt = jwt_manager

        self.audit = audit_logger

        self.refresh_repository = refresh_repository

        self.token_manager = token_manager

    def register(

        self,

        request_id,

        username,

        password,

        role

    ):

        existing_user = self.repository.find_user(

            username

        )

        if existing_user:

            raise Exception(

                "User already exists"

            )

        password_hash = hashlib.sha256(

            password.encode()

        ).hexdigest()

        self.repository.create_user(

            username,

            password_hash,

            role

        )

        self.audit.log(

            request_id,

            username,

            "register",

            "success"

        )

        return True

    def login(

        self,

        request_id,

        username,

        password

    ):

        user = self.repository.find_user(

            username

        )

        if user is None:

            raise Exception(

                "User not found"

            )

        password_hash = hashlib.sha256(

            password.encode()

        ).hexdigest()

        if user["password_hash"] != password_hash:

            raise Exception(

                "Invalid password"

            )

        access_token = self.jwt.generate(

            username,

            user["role"]

        )

        refresh_token = self.token_manager.generate_refresh_token()

        token_hash = self.token_manager.hash_token(

            refresh_token

        )

        expires_at = int(

            time()

        ) + 604800

        self.refresh_repository.create_token(

            username,

            token_hash,

            expires_at

        )

        self.audit.log(

            request_id,

            username,

            "login",

            "success"

        )

        return {

            "access_token": access_token,

            "refresh_token": refresh_token

        }

    def logout(

        self,

        request_id,

        username,

        refresh_token

    ):

        token_hash = self.token_manager.hash_token(

            refresh_token

        )

        self.refresh_repository.delete_token(

            token_hash

        )

        self.audit.log(

            request_id,

            username,

            "logout",

            "success"

        )

        return True

    def refresh_access_token(

        self,

        request_id,

        username,

        refresh_token

    ):

        token_hash = self.token_manager.hash_token(

            refresh_token

        )

        token_row = self.refresh_repository.get_token(

            token_hash

        )

        if token_row is None:

            raise Exception(

                "Invalid refresh token"

            )

        if int(

            time()

        ) > token_row["expires_at"]:

            raise Exception(

                "Refresh token expired"

            )

        user = self.repository.find_user(

            username

        )

        if user is None:

            raise Exception(

                "User not found"

            )

        access_token = self.jwt.generate(

            username,

            user["role"]

        )

        self.audit.log(

            request_id,

            username,

            "refresh_token",

            "success"

        )

        return {

            "access_token": access_token

        }
