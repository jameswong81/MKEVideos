from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Videos


# Create your views here.
def test_view(request):
    return render(request, template_name='Home/test.html')


def upload_file(request):
    if request.method == 'POST':
        user_obj = User.objects.all()[:1].get()
        upload = request.POST.get('upload')
        if upload is None:
            return redirect('home:upload_video')
        v = Videos.objects.create(user=user_obj, video_filename=upload)
        v.save()
        return redirect('home:upload_video')
    else:  # get
        return render(request, template_name='Home/upload.html')
