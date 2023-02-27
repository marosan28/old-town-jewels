from django.shortcuts import render


def handler404(request, exception=None, template_name="errors/404.html"):
    print("error 404 is here")
    return render(request, template_name, status=404)
