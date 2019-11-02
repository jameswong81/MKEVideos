from django.shortcuts import render


# Create your views here.
def test_view(request):
    return render(request, template_name='Home/test.html')


def upload_file(request):
    if request.method == 'POST':
        pass
    else: # get
        return render(request, template_name='Home/upload.html')
