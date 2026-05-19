from fastapi import APIRouter, Depends, UploadFile
import os
from helpers.config import get_settings, Settings
from controllers import DataController, ProjectController



data_router = APIRouter(
    prefix="/api/v1/data",
    tags=["api_v1", "data"],
)

@data_router.post("/upload/{project_id}")
async def upload_data(
    project_id: str,
    file: UploadFile,
    app_settings: Settings = Depends(get_settings)
):
    data_controller = DataController()

    is_valid, result_signal = data_controller.validate_uploaded_file(file=file)

    if not is_valid:
        return {
            "status": "failed",
            "message": result_signal
        }

    return {
        "status": "success",
        "message": result_signal,
        "project_id": project_id,
        "filename": file.filename,
        "content_type": file.content_type,
        "size": file.size
    }