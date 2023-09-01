from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Todo
import random
# Create your views here.
def home(request):
    tasks = Todo.objects.all()
    image_urls = [
            "https://images.unsplash.com/flagged/photo-1570612861542-284f4c12e75f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60",
            
            "https://images.unsplash.com/photo-1541647376583-8934aaf3448a?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=934&q=80",
            "https://images.unsplash.com/photo-1438761681033-6461ffad8d80?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2100&q=80",
            "https://images.unsplash.com/flagged/photo-1570612861542-284f4c12e75f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60",
            "https://images.unsplash.com/photo-1580489944761-15a19d654956?ixlib=rb-1.2.1&auto=format&fit=crop&w=998&q=80",
            "https://assets.codepen.io/3364143/Screen+Shot+2020-08-01+at+12.24.16.png",
            "https://images.unsplash.com/flagged/photo-1574282893982-ff1675ba4900?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1000&q=80"
            
          ]
    for task in tasks:
        task.random_image_url = random.choice(image_urls)
    return render(request, "index.html", context={"tasks": tasks, "image_urls": image_urls})

def create_task(request):
    
    if request.method == "POST":
        task_text = request.POST.get('task_text')
        Todo.objects.create(name=task_text)
        return JsonResponse({'status': 'success'})
        
    return render(request, "index.html")

def delete_task(request, id):
    if request.method == "POST":
        task = Todo.objects.get(id=id)
        task.delete()
        return JsonResponse({'status': 'success'})
    return render(request, "index.html")
