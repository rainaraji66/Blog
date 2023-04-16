from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from . models import User_credential

data = [
     {
         'author' : 'Raji',
         'title' : 'My post 1',
         'content' : 'First content',
         'date' : 'Dec 05,2022'
     },

     {
         'author' : 'Raina',
         'title' : 'My post 2',
         'content' : 'Second content',
         'date' : 'Dec 06,2022'
     }
 ]

def home(request):
    context={
        'datas' : 'data'
    }
    return render(request,'muruga/home.html',context)

class PostListView(ListView):
    model = User_credential
    template_name = 'muruga/home.html'
    context_object_name = 'datas'
    ordering = ['-date']

class PostDetailView(DetailView):
    model = User_credential
    template_name = 'muruga/data_detail.html'


class PostCreateView(LoginRequiredMixin,CreateView):
    model = User_credential
    template_name = 'muruga/data_form.html'
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = User_credential
    template_name = 'muruga/data_form.html'
    fields = ['title','content']
    

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = User_credential
    template_name = 'muruga/data_delete.html'
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    
    return render(request,'muruga/about.html',{'title':'About'})