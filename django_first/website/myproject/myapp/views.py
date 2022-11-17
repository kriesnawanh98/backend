from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature


# Create your views here.
def index(request):
    # name_1 = 'Kriesnawan'
    # name_1 = user.name
    # context = {'name': 'Handy', 'age': 24, 'nationality': 'indonesian'}
    # return HttpResponse('<h1>Hey, Welcome </h1>')

    feature1 = Feature()
    feature1.id = 0
    feature1.name = "fast"
    feature1.details = 'Our services is very quick'

    feature2 = Feature()
    feature2.id = 1
    feature2.name = "reliable"
    feature2.details = 'Our services is very reliable'

    feature3 = Feature()
    feature3.id = 2
    feature3.name = "easy to use"
    feature3.details = 'Our services is very easy to use'

    feature4 = Feature()
    feature4.id = 3
    feature4.name = "affordable"
    feature4.details = 'Our services is very affordable'

    features = [feature1, feature2, feature3, feature4]
    return render(request, 'templates/index.html', {'features': features})


def counter(request):
    words = request.POST['text_input']
    count_words = len(words.split())
    context = {'data_type': str(type(words)), 'count_words': count_words}
    return render(request, 'templates/counter.html', context)
