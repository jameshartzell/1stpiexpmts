from fastapi import FastAPI,Request,Header,Form
from fastapi.responses import HTMLResponse,FileResponse,JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse,StreamingResponse
from pydantic import BaseModel
from typing import List
from typing_extensions import Annotated #type: ignore
from datetime import datetime,timedelta
import pytz,sys,os,random,requests,uuid,time,asyncio,base64,io,time
import RPi.GPIO as GPIO

#==========================================================================
#localex                                        uvicorn server:app --reload
#--------------------------------------------------------------------------
#nodebuglocalex                                        gunicorn server:app
#==========================================================================

#==========================================================================
#init----------------------------------------------------------------------
#==========================================================================
app = FastAPI()
app.mount('/static',StaticFiles(directory='static'),'static')
templates = Jinja2Templates('Templates')
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, 50)
GPIO.setup(12, 50)
x = GPIO.PWM(11, 50)
y = GPIO.PWM(12, 50)

#==========================================================================
#internal------------------------------------------------------------------
#==========================================================================
@app.get(path='/robots.txt',response_class=FileResponse,include_in_schema=False)
async def robots():
    return FileResponse(path='./static/robots.txt',status_code=200)

#==========================================================================
#pages---------------------------------------------------------------------
#==========================================================================

@app.get("/", response_class=HTMLResponse)
async def root(request:Request):
    try:
        resp = templates.TemplateResponse(request=request,name='index.html',status_code=200,headers=request.headers)
        return resp
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print('root',f"{exc_type} - {str(e)}\n{fname} - ln {exc_tb.tb_lineno}")


class Input(BaseModel):
    x:float
    y:float

@app.post("/control")
async def control(request:Request,input:Input):
    try:
        resp = {"cool":"thanks"}

        print(input.x,input.y)
        #DO THING HERE HEEEHEEEEHAAAWW
        return resp

    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print('root',f"{exc_type} - {str(e)}\n{fname} - ln {exc_tb.tb_lineno}")

@app.get("/healthcheck")
async def health():
    return {200}
