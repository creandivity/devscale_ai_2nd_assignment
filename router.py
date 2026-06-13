from fastapi import APIRouter

from app.schema import MessageInput

from app.schema import CompletionResponse
from app.services import generate_response

router = APIRouter()

@router.post("/completions", response_model=CompletionResponse)
def start_completions(body: MessageInput):
    response = generate_response(body.message)
    return CompletionResponse(response=response)
