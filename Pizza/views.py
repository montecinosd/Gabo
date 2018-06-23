from django.shortcuts import render

# Create your views here.

def index(request):
    data = {}

    data['saludar'] = 'Hola dsfs'

    # SELECT * FROM player
    data['object_list'] = Player.objects.all()

    template_name = 'index.html'
    return render(request, template_name, data)
