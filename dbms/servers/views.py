from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from servers.models import Server

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('server_list')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
	
class ServerForm(ModelForm):
    class Meta:
        model = Server
        fields = ['name', 'ip', 'order']

def server_list(request, template_name='server_list.html'):
    servers = Server.objects.all()
    data = {}
    data['object_list'] = servers
    return render(request, template_name, data)
	
	
def server_create(request, template_name='server_form.html'):
    form = ServerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('server_list')
    return render(request, template_name, {'form':form})
	
	
def server_create1(request, template_name='img.html'):
    form = ServerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('server_list')
    return render(request, template_name, {'form':form})

def server_create2(request, template_name='img1.html'):
    form = ServerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('server_list')
    return render(request, template_name, {'form':form})
	
def server_update(request, pk, template_name='server_form.html'):
    server = get_object_or_404(Server, pk=pk)
    form = ServerForm(request.POST or None, instance=server)
    if form.is_valid():
        form.save()
        return redirect('server_list')
    return render(request, template_name, {'form':form})

def server_delete(request, pk, template_name='server_confirm_delete.html'):
    server = get_object_or_404(Server, pk=pk)    
    if request.method=='POST':
        server.delete()
        return redirect('server_list')
    return render(request, template_name, {'object':server})