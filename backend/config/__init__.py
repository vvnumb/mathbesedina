from config.settings import (UvicornSettings, ApplicationSettings, CORSSettings,
                             DatabaseSettings, AlembicSettings, JWTSettings)

uvicorn_config = UvicornSettings()
application_config = ApplicationSettings()
cors_config = CORSSettings()
database_config = DatabaseSettings()
alembic_config = AlembicSettings.generate()
jwt_config = JWTSettings()
