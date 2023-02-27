from django.shortcuts import render
from django.http import HttpResponse 
from .models import Domain, Section, Article, Contributor
from django.db.models import Count


# Create your views here.
def statistics(request):
    articles_count = Article.objects.all().count()
    domains_count = Domain.objects.all().count()   
    content = {'articles_count': articles_count, 'domains_count':domains_count} 
    return render(request, "statistics.html", content)

def how_to_publish(request):
    return render(request, "how_to_publish.html")


def home(request):
    domains = Domain.objects.all()
    latest_articles = Article.objects.all()[:3]
    return render(request, "home.html", {'domains': domains, 'latest_articles':latest_articles})

def domain(request, domain_id):
    domain = Domain.objects.filter(id=domain_id)[0]
    articles = Article.objects.filter(domain=domain)
    # print(articles[0].publisher)
    return render(request, "domain.html", {'domain': domain, 'articles':articles})

def top_contributors(request):
    contributors = Contributor.objects.all()
    contributor_article_count = (Article.objects
    .values('contributor')
    .annotate(article_count=Count('contributor'))
    .order_by('-article_count')
    )[:8]
    contributors_info = []
    for contributor_id in contributor_article_count:
        c  = Contributor.objects.filter(id=contributor_id['contributor'])[0]
        contributors_info.append({'name':c.name, 'section':c.section,'phone':c.phone, 'photo':c.photo,
        'email':c.email, 'contributor_article_count':contributor_id['article_count']})

    return render(request, "top_contributors.html", {'contributors_info':contributors_info})


def top_viewed(request):
    articles = Article.objects.all().order_by('-views')

    return render(request, "top_viewed.html", {'articles':articles})

from django.http import JsonResponse


def add_view(request, article_id): 
    article = Article.objects.filter(id=article_id)[0]
    article.views = article.views + 1        
    article.save()
    return Jsonresponse(status=200)
