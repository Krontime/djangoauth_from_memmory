from django.shortcuts import render, get_object_or_404, redirect
from messenger.models import Message
from messenger.forms import ComposeMessageForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
def get_inbox_index(request):
    return render(request, "messenger/inbox.html")

@login_required
def get_sent_index(request):
    return render(request, "messenger/sent.html")

@login_required
def get_mail_index(request, id):
    message = get_object_or_404(Message, pk=id)
    message.read=True
    message.save()
    return render(request, "messenger/mail.html", {'message': message})

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
    
    
    return render(request, "messenger/compose.html", {'form': form})

