from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseNotFound
from django.shortcuts import redirect
from django.contrib import messages

class DoesNotExistMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        if isinstance(exception, ObjectDoesNotExist):
            messages.error(request, 'somthing went wrong')
            return redirect('home')
