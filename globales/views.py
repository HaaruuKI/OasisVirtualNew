from django.shortcuts import redirect
from django.contrib.auth import logout

def close_sesion(request):
    logout(request)
    return redirect('/')