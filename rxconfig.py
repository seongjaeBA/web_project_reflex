import reflex as rx

class UploadConfig(rx.Config):
    pass

config = rx.Config(
    app_name="web_proejct",
    # db_url="postgresql://user:password@localhost:5432/my_db",
    # Change the frontend port.
    # frontend_port=3001,
    # Backend default = 8000,
    db_url="sqlite:///./reflex.db",
    env = rx.Env.DEV,
    # api_url = "http://192.:3000"
)