from django.shortcuts import render


def list_info(request):
    return render(request, 'info.html')
