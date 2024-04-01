from django.http import HttpResponse
def index(request):
    return HttpResponse(''' 
    Hello <h1>Aarushi Tiwari</h1>  <a href="https://www.youtube.com/watch?v=gnKbAAVUzro&list=PLCC34OHNcOtpalASMlX2HHdsLNipyyhbK&index=1"> 
    Hello Numpy playlist
    </a>''')


def about(request):
    return HttpResponse("About Aarush")