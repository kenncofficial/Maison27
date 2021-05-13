from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import BlogPost, BlogComment, Category, Supply_Category, General_Supplies, About, Main_Service, Contact, Home_Layout
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from .forms import EditCommentForm, EditSupplyForm, CommentForm, PostForm, EditForm, AddSupplyForm
from django.contrib.messages.views import SuccessMessageMixin

#####--------------------- home view
class HomeView(ListView):
    context_object_name = 'home'
    template_name = 'index.html'
    queryset = Home_Layout.objects.all()

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        context["Abouts"] = About.objects.all()[:1]
        context["Main_Services"] = Main_Service.objects.all()
        context["BlogPosts"] =  BlogPost.objects.all().order_by('-date_posted')[:4]
        context["Home_Layouts"] = self.queryset
        return context
###################################################################################################



###------------------- Redirect to previous page Mixin
class RedirectToProviousMixin:
    default_redirect = '/'

    def get(self, request, *args, **kwargs):
        request.session['previous_page'] = request.META.get('HTTP_REFERER', self.default_redirect)
        return super().get(request, *args, **kwargs)

    def get_success_url(self):
        return self.request.session['previous_page']
###################################################################################################



#####------------------- General supplies list view 
class GeneralSuppliesListView(ListView):
    context_object_name = 'Supplies'
    template_name = 'general_supplies.html'
    queryset = General_Supplies.objects.all()
    paginate_by = 8

    def get_context_data(self, *args, **kwargs):
        cat_menu = Supply_Category.objects.all()
        context = super(GeneralSuppliesListView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        context["General_Supplies"] = self.queryset 
        return context
###################################################################################################



######----------------- General Supplies Detail View
class GeneralSuppliesDetailView(DetailView):
    model = General_Supplies
    template_name = 'general_supplies_details.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Supply_Category.objects.all()
        context = super(GeneralSuppliesDetailView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        context["General_Supply"] = General_Supplies.objects.all()
        return context
###################################################################################################



#######----------------- General Supplies Category Detail View
def SupplyCategoryDetailView(request, cats):
    category_posts = General_Supplies.objects.filter(supply_category=cats.replace('-', ' '))
    return render(request, 'supply_category.html',
                  {'cats': cats.title().replace('-', ' '), 'category_posts': category_posts})
###################################################################################################



#####------------------ Add General Supply
class AddSupplyView(CreateView):
    model = General_Supplies
    form_class = AddSupplyForm
    template_name = 'add_supply.html'
    success_url = reverse_lazy('general_supplies')
###################################################################################################


#####------------------ update General Supply View
class UpdateSupplyView( RedirectToProviousMixin, UpdateView):
    model = General_Supplies
    form_class = EditSupplyForm
    template_name = 'update_supply.html'
    # fields = ['title', 'title_tag', 'body']
###################################################################################################


#####------------------ Add Category View
class AddSupplyCategoryView(CreateView):
    model = Supply_Category
    # form_class = PostForm
    template_name = 'add_Supply_category.html'
    fields = '__all__'
    success_url = reverse_lazy('home')
###################################################################################################



#####---------------- Delete Post View
class DeleteSupplyView(DeleteView):
    model = General_Supplies
    template_name = 'delete_supply.html'
    success_url = reverse_lazy('home')

###################################################################################################



#####------------------ Blog list view 
class BlogListView(ListView):
    context_object_name = 'Blog'
    template_name = 'blog_list.html'
    ordering = ['-date_posted']
    queryset = BlogPost.objects.all()
    paginate_by = 6

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(BlogListView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        context["Main_Services"] = Main_Service.objects.all()
        context["Blog_lists"] = self.queryset 
        return context
###################################################################################################


#####-------------------- Blog Post Detail View
class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'BlogPost_detail.html'


    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(BlogPostDetailView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        context["BlogPosts"] =  BlogPost.objects.all().order_by('-date_posted')[:3]
        #context["related_items"] = self.object.tags.similar_objects()[:5]
        comments_connected = BlogComment.objects.filter(blogpost_connected=self.get_object()).order_by('-date_posted')
        context['comments'] = comments_connected
        if self.request.user.is_authenticated:
            context['form_comment'] = CommentForm(instance=self.request.user)

        return context
    
    def post(self, request, *args, **kwargs):
        new_comment = BlogComment(content=request.POST.get('content'),
                                  author=self.request.user,
                                  blogpost_connected=self.get_object())
        new_comment.save()
        return self.get(self, request, *args, **kwargs)
###################################################################################################




#######----------------- Category Detail View
def CategoryDetailView(request, cats):
    category_posts = BlogPost.objects.filter(category=cats.replace('-', ' '))
    return render(request, 'category_detail.html',
                  {'cats': cats.title().replace('-', ' '), 'category_posts': category_posts})
###################################################################################################




#####------------------ Add post view
class AddPostView(CreateView):
    model = BlogPost
    form_class = PostForm
    template_name = 'add_post.html'

 
###################################################################################################



#####------------------ Add Category View
class AddCategoryView(CreateView):
    model = Category
    # form_class = PostForm
    template_name = 'add_category.html'
    fields = '__all__'
    success_url = reverse_lazy('home')
###################################################################################################




#####------------------ update Post View
class UpdatePostView( RedirectToProviousMixin, UpdateView):
    model = BlogPost
    form_class = EditForm
    template_name = 'update_post.html'
    # fields = ['title', 'title_tag', 'body']
###################################################################################################



#####---------------- Delete Post View
class DeletePostView(DeleteView):
    model = BlogPost
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

###################################################################################################



#######--------------- service View
class ServiceView(ListView):
    model = BlogPost
    template_name = 'services.html'
###################################################################################################


######----------------- About View   
class AboutView(ListView):
    model = About
    template_name = 'about.html'
###################################################################################################


#########---------------- Delete Comment View    
class DeleteCommentView(RedirectToProviousMixin, DeleteView):
    model = BlogComment
    template_name = 'delete_comment.html'
###################################################################################################

   

#####-------------------- Update comment View
class UpdateCommentView(RedirectToProviousMixin, UpdateView):
    model = BlogComment
    template_name = 'update_comment.html'
    form_class = EditCommentForm
###################################################################################################


######-------------------- Contact View
class ContactView(ListView):
    model = Contact
    template_name  = 'contact.html'
###################################################################################################

