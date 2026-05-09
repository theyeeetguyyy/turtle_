from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Any
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

# -----------------------------
# Request Body Schema
# -----------------------------
class ProjectRequest(BaseModel):
    clientId: str
    projectId: str

# -----------------------------
# Sample Hardcoded JSON Response
# -----------------------------
SAMPLE_PROJECT_DATA = {
    "client_id": "client_2",
    "provider": "openai",
    "model": "gpt-4.1",
    "extracted_at": "2026-04-25T21:40:37.500553",
    "duration_seconds": 245.94,
    "total_fields": 174,
    "fields": {
        "1": {
            "value": "client_2",
            "confidence": 1.0,
            "confidence_level": "exact_quote",
            "source": "System",
            "agent": "SystemResolver",
            "attribute": "T_id",
            "touch_point": "Turtle ID"
        },
        "4": {
            "value": 27,
            "confidence": 0.8,
            "confidence_level": "clearly_inferable",
            "source": "Age inferred from DOB",
            "agent": "DemographicsAgent",
            "attribute": "Lead/ Client's Age",
            "touch_point": "Demographics & Family"
        },
        "5": {
            "value": "Single",
            "confidence": 0.95,
            "confidence_level": "exact_quote",
            "source": "Transcript",
            "agent": "DemographicsAgent",
            "attribute": "Marital Status",
            "touch_point": "Demographics & Family"
        },
        "12": {
            "value": {
                "city": "Bangalore",
                "state": "Karnataka"
            },
            "confidence": 0.95,
            "confidence_level": "exact_quote",
            "source": "Transcript",
            "agent": "DemographicsAgent",
            "attribute": "Current Residence",
            "touch_point": "Demographics & Family"
        },
        "44": {
            "value": "66,05,000",
            "confidence": 0.8,
            "confidence_level": "clearly_inferable",
            "source": "Calculated from assets",
            "agent": "FinanceAgent",
            "attribute": "Assets Worth (Rs.)",
            "touch_point": "Finances"
        },
        "82": {
            "value": "Retire at 45 with target corpus ~11 crore INR",
            "confidence": 0.95,
            "confidence_level": "exact_quote",
            "source": "Transcript",
            "agent": "GoalsAgent",
            "attribute": "Retirement Planning",
            "touch_point": "Life Goals"
        }
    }
}


# -----------------------------
# Route
# -----------------------------
@router.post("/project", status_code=200)
async def fetch_project(body: ProjectRequest):

    logger.info(
        "project_fetch_requested",
        extra={
            "client_id": body.clientId,
            "project_id": body.projectId
        }
    )

    try:
        # hardcoded validation
        if body.clientId != "client_2":
            raise HTTPException(
                status_code=404,
                detail="Client not found"
            )

        response = {
            "success": True,
            "message": "Project data fetched successfully",
            "projectId": body.projectId,
            "data": SAMPLE_PROJECT_DATA
        }

        logger.info(
            "project_fetch_success",
            extra={
                "client_id": body.clientId,
                "project_id": body.projectId
            }
        )

        return response

    except HTTPException:
        raise

    except Exception as exc:

        logger.error(
            "project_fetch_failed",
            extra={"error": str(exc)}
        )

        raise HTTPException(
            status_code=500,
            detail="Something went wrong while fetching project"
        )