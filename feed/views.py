from django.views.generic import TemplateView,DetailView,FormView
from .models import Post
from django.contrib import messages


from .forms import PostForm
class HomePageView(TemplateView):
    template_name='home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.all()
        return context
    
class PostDetailView(DetailView):
    template_name="detail.html"
    model=Post


class PostFormView(FormView):
    template_name='new_post.html'
    form_class=PostForm
    success_url='/'
    
    def get(self, request, *args, **kwargs):
        self.request=request
        return super().get(self, request, *args, **kwargs)
    
    def form_valid(self, form):
        new_object=Post.objects.create(text=form.cleaned_data['text'],image=form.cleaned_data['image'])
        messages.add_message(self.request,messages.SUCCESS,'You successfully posted')
        return super().form_valid(form)
    