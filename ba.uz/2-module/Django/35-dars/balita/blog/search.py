from .models import Article, Category, Comments, Tag

result_articles = []


def search(key):
    articles = Article.objects.all()
    for article in articles:
        if key in article.title or article.description or article.tags or article.category:
            print('*==*' * 80)
            print(article)
            print('*==*' * 80)
            result_articles.append(article)
    return result_articles
