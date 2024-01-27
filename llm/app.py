from main import get_summarisation
import uvicorn
from fastapi import FastAPI
app=FastAPI()

@app.post("/summaries")
async def get_summary(message):
    response=get_summarisation(message)
    print(response)
    return response
   
if __name__=="__main__":
    uvicorn.run(app,host="0.0.0.0",port=8001)