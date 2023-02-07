from django.shortcuts import render, redirect
from .models import Server
from .forms import ServerForm
# Create your views here.
def servers(request):
    server = Server.objects.all()
    context = {'servers':server}
    return render(request, 'servers/index.html',context)

def createServer(request):
    if request.method == 'POST':
        form = ServerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('servers')
    else:
        form = ServerForm()
        context = {'form':form}
        return render(request, 'servers/create_server.html', context)

def updateServer(request, pk):
    server = Server.objects.get(id = pk)
    form = ServerForm(instance = server)
    if request.method == 'POST':
        form = ServerForm(request.POST, instance = server)
        if form.is_valid():
            form.save()
            return redirect('servers')
    else:
        context = {'form':form}
        return render(request, 'servers/update_server.html', context)

def deleteServer(request, pk):
    server = Server.objects.get(id = pk)
    if request.method == 'POST':
        server.delete()
        return redirect('servers')
    else:
        context = {'form':server}
        return render(request, 'servers/delete_server.html', context)