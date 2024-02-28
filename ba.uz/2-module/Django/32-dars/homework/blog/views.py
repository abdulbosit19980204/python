from django.shortcuts import render

from .models import Articles, ContactUs, Comments, Subscribers


# Create your views here.

def home_view(request):
    articles = Articles.objects.filter(main_page=True)
    d = {
        "articles": articles[::-1]
    }
    return render(request, 'index.html', context=d)


def blog_view(request):
    articles = Articles.objects.all()
    d = {
        "articles": articles[::-1],
        "message": "Articles are loading...",
    }
    return render(request, "blog.html", context=d)


def blog_info(request, pk):
    if request.method == "POST":
        comment = request.POST
        obj = Comments.objects.create(commentor_name=comment['name'], comment_message=comment['message'],
                                      commentor_email=comment['email'], commentor_website=comment['website'],
                                      article_id=pk)
        obj.save()
    article = Articles.objects.get(id=pk)
    comments = Comments.objects.filter(article_id=pk, is_Visable=True)
    d = {
        'article': article,
        'comments': comments
    }
    print(d)
    return render(request, 'blog-single.html', context=d)


def about_view(request):
    return render(request, 'about.html')


def contact_view(request):
    if request.method == "POST":
        data = request.POST
        obj = ContactUs.objects.create(fullName=data['name'], email=data['email'], subject=data['subject'],
                                       message=data['message'])
        obj.save()
    return render(request, 'contact.html')


def subscribes(request):
    if request.method == "POST":
        print("==" * 50)
        print(request)
        print('==' * 50)
    # subEmail = request.POST
    # obj = Subscribers.objects.create(subscriber_email=subEmail['email'])
    # obj.save()

    return render(request, 'index.html')
