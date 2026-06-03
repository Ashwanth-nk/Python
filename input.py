from fastapi import FastAPI,Form,Body,Query,Header,Path,Cookie,HTTPException
from typing import Annotated
#Annotated helps fastapi process username and password with more information.
#For example, if str in username, annotated says fastapi that this str should be obtained from username form.
app = FastAPI()

@app.post("/login")
async def login(
  username: Annotated[str,
    Form(default=...,
         alias=None,
         title="USERNAME",
         description="Username details needed",
         min_length=1,
         max_length=6,
         pattern="^[a-zA-Z]+$",
         examples=["JohnNamo"])],
         #There are many more form methods learn when using them
  password: Annotated[str,Form(...)],
  q: str = Query(),
  price: float = Body(),
  token: str = Header(),
  user_id: int = Path(...),
  session: str = Cookie()
  
  #ALL mentioned functions have same validation features
):
  if price > 5:
    raise HTTPException(
      status_code = 404,
      detail="Price entered > 5",
      headers="Invalid Input"
    )
  return {"username":username,
          "password":password,
          "q":q,
          "price":price,
          "token":token,
          "path":user_id,
          "cookie":session}

