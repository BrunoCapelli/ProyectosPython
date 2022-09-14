from turtle import title
from django.shortcuts import redirect, render, HttpResponse
from firstApp.models import Article, Categoria


lenguajes = ['C#', 'Javascript', 'Python', 'PHP', 'Ruby']
# lenguajes = []

def inicio(request):
    return render(request, 'index.html', {
        'title' : 'Kaya',
        'argumento': 'Letra peculiar',
        'lenguajes': lenguajes

    })

def pruebas(request):
    return render(request, 'index.html')



def create_articles(request):

    return render(request, 'create-articles.html')

def save_article(request):
    
    if request.method == 'POST':

        title = request.POST['title']
        description = request.POST['description']
        public = request.POST['public']
        
        article = Article(
            title = title,
            description = description,
            public = public
        )
        article.save() 
        return render(request, 'save-articles.html')
    else:

        return HttpResponse(f"<h2>El articulo no fue publicado</h2>")




def show_articles(request):
    articles = Article.objects.all()

    return render(request, 'show-articles.html', {
       'articles': articles})
#    return HttpResponse(articles)    

def delete_article(request, id):
    article = Article.objects.get(pk=id)
    article.delete()

    return redirect('show-articles')
