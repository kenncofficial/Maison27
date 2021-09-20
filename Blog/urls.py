from django.urls import path
from .views import HomeView, ContactView, DeleteSupplyView, UpdateSupplyView,  GeneralSuppliesListView, AddSupplyView, GeneralSuppliesDetailView, BlogListView, AboutView, ServiceView, UpdateCommentView, DeletePostView, AddPostView, UpdatePostView, DeleteCommentView, BlogPostDetailView

urlpatterns = [

    path('', HomeView.as_view(), name='home'),
    path('Blog_list/', BlogListView.as_view(), name="blog"),
    path('general_supplies/', GeneralSuppliesListView.as_view(), name='general_supplies'),
    path('supply/<int:pk>', GeneralSuppliesDetailView.as_view(), name='supply_details'),
    path('article/<int:pk>', BlogPostDetailView.as_view(), name='BlogPost-details'),
    path('add_supply/', AddSupplyView.as_view(), name='add_supply'),    
   # path('add_supply_category/', AddSupplyCategoryView.as_view(), name='add_supply_category'),
    #path('supply_category/<str:cats>/', SupplyCategoryDetailView, name='supply_category'),

    path('supply/<int:pk>/update_supply', UpdateSupplyView.as_view(), name='update_supply'),
    path('supply/<int:pk>/delete', DeleteSupplyView.as_view(), name='Delete_supply'),

    #path('category/<str:cats>/', CategoryDetailView, name='category_detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    #path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('article/<int:pk>/delete', DeletePostView.as_view(), name='Delete_post'),
    path('services/', ServiceView.as_view(), name='services'),
    path('about/', AboutView.as_view(), name='about'),
    #path('comment/<id>/update', UpdateCommentView, name='update_comment' ),
    path('article/<int:pk>/update_comment', UpdateCommentView.as_view(), name='Update_comment'),
    path('article/<int:pk>/delete_comment', DeleteCommentView.as_view(), name='Delete_comment'),
    path('contact/', ContactView.as_view(), name="contact_us")
]