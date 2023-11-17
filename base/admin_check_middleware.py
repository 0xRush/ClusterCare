from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth import logout

class AdminLogoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the user is authenticated and is an admin
        if request.user.is_authenticated and request.user.is_staff:
            # Check if the user is accessing the admin panel
            if request.path.startswith('/admin'):
                response = self.get_response(request)
                return response
            else:
                # Log out the admin user for other routes
                logout(request)
                return redirect(reverse('login'))  # Redirect to the login page or any other desired page

        # For non-admin users or admin accessing admin panel, proceed with the normal flow
        response = self.get_response(request)
        return response
