from src.views.http_types.http_response import HttpResponse
from .types.http_bad_request import HttpBadRequestError
from .types.http_not_found import HttpNotFoundError
from .types.http_unauthorized import HttpUnauthorizedError

def handle_errors(error: Exception) -> HttpResponse:
    if isinstance(error, (HttpBadRequestError, HttpUnauthorizedError, HttpNotFoundError)):
        return HttpResponse(
            body={
                'error': [{
                    "title": error.name,
                    'detail': error.message
                }]
            },
            status_code=error.status_code
        )
    
    return HttpResponse(
        body={
            'error': [{
                'title': 'Internal Server Error',
                'detail': str(error)
            }]
        },
        status_code=500
    )