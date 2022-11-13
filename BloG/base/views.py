from django.shortcuts import render,redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView
from django.views.generic.edit import DeleteView,FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.db.models.aggregates import Count
from django.db.models import Q
from django.urls import reverse_lazy
from .models import *

#Authentication
class customLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('bloglist')
class registerView(FormView):
    template_name='base/register.html'
    form_class=UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('bloglist')

    def form_valid(self, form):
        user=form.save()
        if user is not None:
            login(self.request,user)
        return super(registerView,self).form_valid(form)


# Blogs
class blogList(ListView):
    model=Blog
    fields='__all__'
    context_object_name = 'blogList'

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        search_key=self.request.GET.get('search-area') or ''
        context['blogList']=context['blogList'].filter(
            Q(title__icontains=search_key) | Q(description__icontains=search_key)
        )
        return context

class blogDetails(LoginRequiredMixin,DetailView):
    model=Blog
    fields='__all__'
    context_object_name = 'blogDetails'


class blogCreate(LoginRequiredMixin,CreateView):
    model=Blog
    fields = ['title','category','description']
    context_object_name = 'blogCreate'
    success_url = reverse_lazy('bloglist')

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super(blogCreate,self).form_valid(form)

class blogUpdate(LoginRequiredMixin,UpdateView):
    model=Blog
    fields = '__all__'
    success_url = reverse_lazy('bloglist')

class blogDelete(LoginRequiredMixin,DeleteView):
    model = Blog
    context_object_name = 'blog'
    success_url = reverse_lazy('bloglist')

class myBlogs(LoginRequiredMixin,ListView):
    model=Blog
    template_name = 'base/myblogs.html'
    fields='__all__'
    context_object_name = 'blogList'

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['blogList']=context['blogList'].filter(user=self.request.user)
        context['count']=context['blogList'].aggregate(count=Count('id'))
        return context

#Category
def getCategoryDetails(request,pk):
    query_set=Blog.objects.filter(category=pk).all()
    category=Category.objects.get(id=pk)
    context={
        "title":category,
        "objects":query_set
    }
    return render(request,'base/category_list.html',context)

#Comments
def getComments(request,pk):
    query_set=Comment.objects.filter(blog=pk).all()
    count=query_set.aggregate(count=Count('id'))
    title=Blog.objects.get(id=pk)
    context={
        "title":title,
        "number_of_comments":count,
        "comments":query_set
    }
    return render(request,'base/comments.html',context)




