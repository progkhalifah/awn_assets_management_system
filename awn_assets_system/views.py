from django.shortcuts import render

# Create your views here.


def home(request):

    context = {

    }
    return render(request, 'awn_assets_system/main/home.html', context)


def custom_404(request, exception):
    return render(request, 'awn_assets_system/page_not_found/404.html', status=404)


def custom_500(request):
    return render(request, 'awn_assets_system/page_not_found/500.html', status=500)

