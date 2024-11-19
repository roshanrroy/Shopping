from django.shortcuts import redirect

class RedirectOrderMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path == "/order" and not request.user.is_authenticated:
            return redirect('/login')
        if request.path == "/cart" and not request.user.is_authenticated:
            return redirect('/login')
        if request.path == "/checkout" and not request.user.is_authenticated:
            return redirect('/login')
        
        response = self.get_response(request)
        return response
