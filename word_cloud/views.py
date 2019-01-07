from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from .scrape import get_words_from_website


def index(request):
    return HttpResponse("I am at the index()")

def result(request):
    context = dict(website = request.POST['website']) 
    
    total_words = get_words_from_website(context['website'], ['p', 'div'])

    context.update(top_100 = total_words.most_common(100))
    print(context)

    return render(request, "word_cloud/result.html", context)

@csrf_protect
def submit(request):
    return render(request, "word_cloud/submit.html", {})
