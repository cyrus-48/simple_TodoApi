import uvicorn


port = 8000
host = "0.0.0.0"
app_name = "app.main:app"
if __name__ == "__main__":
    uvicorn.run(app_name, host=host, port=port, reload=True)