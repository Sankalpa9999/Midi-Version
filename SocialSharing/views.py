from django.shortcuts import render, redirect
from .models import SharedContent
from .forms import SharedContentForm
from django.contrib.auth.decorators import login_required

@login_required
def share_content(request):
    if request.method == 'POST':
        form = SharedContentForm(request.POST, request.FILES)
        if form.is_valid():
            shared_content = form.save(commit=False)
            shared_content.user = request.user
            shared_content.save()
            return redirect('view_shared_content')
    else:
        form = SharedContentForm()
    return render(request, 'SocialSharing/share_content.html', {'form': form})

@login_required
def view_shared_content(request):
    shared_contents = SharedContent.objects.all().order_by('-created_at')
    return render(request, 'SocialSharing/view_shared_content.html', {'shared_contents': shared_contents})
