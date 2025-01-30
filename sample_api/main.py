from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()
app.add_middleware( CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])
@app.get('/')
async def root():
    return JSONResponse(content={"message": "Server is Listening","status": "success"}, status_code=200)

@app.get("/api/get/events")
async def get_events() :
    events = [
        {"name": "Event A,", "hostedby" : "SRM", "date" : "2025-01-24"},
        {"name": "Event B,", "hostedby" : "BIT", "date" : "2025-01-16"},
        {"name": "Event C,", "hostedby" : "IIT", "date" : "2025-01-30"},
        {"name": "Event D,", "hostedby" : "NIT", "date" : "2025-01-29"}
    ]
    
    return JSONResponse(content={"message": "Events fetched successfully", "content" : events ,"status": "success"}, status_code=200)

@app.post("/api/add/contibutor")
async def add_contributor(email) :
    # email --> searches user in db --> add x points to that user
    return True

# Run the FastAPI application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8000)
    