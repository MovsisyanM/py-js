from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from handlers import root, counter_button_clicked


app = FastAPI()


app.mount("/static", StaticFiles(directory="static"), name="static")
app.add_route("/", root, ["GET"])
app.add_route("/clicked", counter_button_clicked, ["POST"])

