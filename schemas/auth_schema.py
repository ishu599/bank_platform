from pydantic import BaseModel


class RegisterRequest(

    BaseModel

):

    username: str

    password: str

    role: str


class LoginRequest(

    BaseModel

):

    username: str

    password: str


class RefreshRequest(

    BaseModel

):

    username: str

    refresh_token: str


class LogoutRequest(

    BaseModel

):

    username: str

    refresh_token: str