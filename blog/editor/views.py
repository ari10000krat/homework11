from django.http import HttpResponse
from django.template import loader


def editor_index(request):
    app_name = 'editor'
    template = loader.get_template('templates/base.html')
    context = {
        'app_name': app_name,
    }
    return HttpResponse(template.render(context, request))
    # return HttpResponse('<html><body><h1>Hello! You are in app "EDITOR"</h1></body></html>') TODO

