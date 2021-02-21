from django.http import HttpResponse


def editor_index(request):
    return HttpResponse('<html><body><h1>Hello! You are in app "EDITOR"</h1></body></html>')
