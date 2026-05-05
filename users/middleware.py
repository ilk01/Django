from django.contrib.auth import logout
from django.shortcuts import redirect

class BanMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            if hasattr(request.user, 'profile') and request.user.profile.is_banned:
                if request.path != '/users/banned/': 
                    logout(request)
                    return redirect('banned')
        
        response = self.get_response(request)
        return response
