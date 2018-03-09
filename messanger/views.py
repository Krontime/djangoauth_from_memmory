from django.shortcuts import render, get_object_or_404, redirect
from messanger.models import Message
from messanger.forms import ComposeMessageForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def get_inbox_index(request):
    return render(request, "messanger/inbox.html")

@login_required
def get_sent_index(request):
    return render(request, "messanger/sent.html")

@login_required
def get_mail_index(request, id):
    item = get_object_or_404(Message, pk=id)
    
    return render(request, "messanger/mail.html", {'mail': item})

@login_required
def get_compose_index(request):
    if request.method == "POST":
        form = ComposeMessageForm(request.POST)
        message = form.save(commit=False)
        
        message.sender = request.user
        message.save()
        return redirect('inbox')
    else:
        form = ComposeMessageForm()
    
    
    return render(request, "messanger/compose.html", {'form': form})