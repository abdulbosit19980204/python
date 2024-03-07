from django.shortcuts import render, redirect
from .models import Article, Category, Comments, Tag
from django.core.paginator import Paginator

categories = Category.objects.all()


# Create your views here.

def home_view(request):
    data = request.GET
    page = data.get('page', 1)

    categories = Category.objects.all()
    articles = Article.objects.all().order_by('category')
    page_obj = Paginator(articles, 4)
    popular = Article.objects.all().order_by('-view_count')
    tags = Tag.objects.all()
    d = {
        "home": "active",
        "categories": categories,
        "slider_article": articles[1:4],
        "articles": page_obj.get_page(page),
        "popular": popular[:3],
        "tags": tags
    }
    return render(request, 'index.html', context=d)


def about_view(request):
    categories = Category.objects.all()
    tags = Tag.objects.all()
    popular = Article.objects.all().order_by('-view_count')
    d = {
        "about": "active",
        "categories": categories,
        "popular": popular[:3],
        "tags": tags
    }
    return render(request, 'about.html', context=d)


def tag_view(request):
    data = request.GET
    tag = data.get('tag', None)
    categories = Category.objects.all()
    tags = Tag.objects.all()
    popular = Article.objects.all().order_by('-view_count')
    cat_name = Tag.objects.filter(id=int(tag))

    if tag != None:
        articles = Article.objects.filter(tags=int(tag))
        d = {
            "articles": articles,
            "category": "active",
            "categories": categories,
            "cat_name": cat_name[0],
            "popular": popular[:3],
            "tags": tags
        }
        return render(request, 'category.html', context=d)


def categories_view(request, pk):
    data = request.GET
    articles = Article.objects.filter(category=pk)
    page = data.get('page', 1)
    page_obj = Paginator(articles, 6)
    categories = Category.objects.all()
    cat_name = Category.objects.filter(id=pk)
    tags = Tag.objects.all()
    popular = Article.objects.all().order_by('-view_count')

    d = {
        "articles": page_obj.get_page(page),
        "category": "active",
        "categories": categories,
        "cat_name": cat_name[0],
        "popular": popular[:3],
        "tags": tags
    }
    return render(request, 'category.html', context=d)


def article_info(request, pk):
    if request.method == "POST":
        comment = request.POST
        obj = Comments.objects.create(name=comment['name'], email=comment['email'], telegram=comment['telegram'],
                                      comment=comment['comment'], article_id=pk)
        obj.save()
        return redirect(f'/category/{pk}')

    detail = Article.objects.filter(id=pk).first()
    detail.view_count += 1
    comments = Comments.objects.filter(article_id=pk, is_visiable=True)
    detail.save(update_fields=['view_count'])
    popular = Article.objects.all().order_by('-view_count')
    tags = Tag.objects.all()
    reletad_tag = [i for i in detail.tags.all()]
    print(reletad_tag)
    d = {
        "category": "active",
        "categories": categories,
        "comments": comments,
        "detail": detail,
        "len_comment": len(comments),
        "popular": popular[:3],
        "tags": tags
    }
    return render(request, 'blog-single.html', context=d)


def contact_view(request):
    popular = Article.objects.all().order_by('-view_count')
    tags = Tag.objects.all()
    d = {
        "contact": "active",
        "categories": categories,
        "popular": popular[:3],
        "tags": tags
    }
    return render(request, 'contact.html', context=d)
