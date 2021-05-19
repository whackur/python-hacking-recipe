import uvicorn
from typing import Optional
from fastapi import FastAPI

app = FastAPI()
animals = {"cat": "meow", "dog": "bark", "duck": "quack"}


@app.get("/")
async def home():
    return {"Hello": "World"}


@app.get("/animals/{animal}")
async def animal_cry(animal: str, cry: Optional[int]):
    """
    동물의 울음소리를 cry 횟수만큼 출력
    """
    sound = ""
    for time in range(cry):
        sound = sound + animals[animal] + " "
    return {"animal": animal, "sound": sound.strip()}


if __name__ == "__main__":
    uvicorn.run("7-1:app", host="0.0.0.0", port=80, reload=True)
