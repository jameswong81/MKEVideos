from django.shortcuts import render


# Create your views here.
def test_view(request):
    return render(request, template_name='Home/test.html')

