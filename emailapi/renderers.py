import json
from rest_framework import renderers

class UserRenderer(renderers.JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        # Set the default charset
        charset = 'utf-8'

        if 'errors' in data:
            # Handle error response
            error_response = {'errors': data['errors']}
            response = json.dumps(error_response)
        else:
            # Handle successful response
            response = json.dumps(data)

        response = response.encode(charset)  # Encode response with specified charset
        return response