import os


class ProjectSettings:
    API_VERSION = '1.0.0'
    API_VERSION_PATH = '/api/v1'
    SERVER_HOST = 'https://localhost:8081/api/v1/'
    BACKEND_CORS_ORIGINS = {
        "http://localhost",
        "http://localhost:8080",
    }


class TokenSettings:
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
    REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7
    ALGORITHM = "HS256"
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'gfsdfasddsfdsfsafefads')
    JWT_REFRESH_SECRET_KEY = os.getenv('JWT_REFRESH_SECRET_KEY', 'gggggygfdsuyafiue')
