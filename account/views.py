from django.shortcuts import render

# Create your views here.

def reg(request):
    if request.method == "GET":
        return render(request, 'account/reg.html')
    elif request.method == "POST":
        return render(request, 'account/reg_result.html')

def entry(request):
    return render(request, 'account/entry.html')

def exit(request):
    return render(request, 'account/exit.html')

def reset(request):
    return render(request, 'account/reset.html')

