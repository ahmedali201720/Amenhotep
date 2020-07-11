from django.urls import path
# from django.conf.urls import url
from . import views
app_name = 'news-api'
urlpatterns = [
    # News Section
    path('news/new/', views.NewsCreateAPIView.as_view(), name='create_news'),
    path('news/<int:pk>/edit/', views.NewsUpdateAPIView.as_view(), name='edit_news'),
    path('news/', views.NewsListAPIView.as_view(), name='list_news'),
    path('news/<int:pk>/', views.NewsDetailAPIView.as_view(), name='news_details'),

    # Offers Section
    path('offers/new/', views.OffersCreateAPIView.as_view(), name='create_offer'),
    path('offers/<int:pk>/edit/',
         views.OffersUpdateAPIView.as_view(), name='edit_offer'),
    path('offers/', views.OffersListAPIView.as_view(), name='list_offers'),
    path('offers/<int:pk>/', views.OffersDetailAPIView.as_view(),
         name='offer_details'),
    # path('<int:pk>/delete/', views.BookDeleteAPIView.as_view(), name='delete_offer'),

    # Request Section
    path('requests/new/', views.RequestCreateAPIView.as_view(),
         name='create_request'),
    path('requests/', views.RequestListAPIView.as_view(), name='list_requests'),
    path('requests/<int:pk>/', views.RequestDetailAPIView.as_view(),
         name='requests_details'),
    path('requests/delete/<int:pk>/', views.DeleteRequestView,
         name='request_delet'),

    # Employee Section
    path('employee/new/', views.EmployeeCreateAPIView.as_view(),
         name='create_employee'),
    path('employees/<int:pk>/edit/',
         views.EmployeeUpdateAPIView.as_view(), name='edit_employee'),
    path('employees/', views.EmployeesListAPIView.as_view(), name='list_employees'),
    path('employees/<int:pk>/', views.EmployeeDetailAPIView.as_view(),
         name='employee_details'),
    # path('<int:pk>/delete/', views.BookDeleteAPIView.as_view(), name='delete_employee'),

    # Existance Section
    path('existence/new/', views.ExistenceCreateAPIView.as_view(),
         name='create_existence'),
    path('existence/<int:pk>/edit/',
         views.ExistenceUpdateAPIView.as_view(), name='edit_existence'),
    path('existence/', views.ExistenceListAPIView.as_view(), name='list_existence'),
    path('existence/<int:pk>/', views.ExistenceDetailAPIView.as_view(),
         name='existence_details'),
    # path('<int:pk>/delete/', views.BookDeleteAPIView.as_view(), name='delete_existence')

    # Compound Section
    path('compound/new/', views.CompoundCreateAPIView.as_view(),
         name='create_compound'),
    path('compound/edit/<int:pk>/',
         views.CompoundUpdateAPIView.as_view(), name='edit_compound'),
    path('compound/', views.CompoundListAPIView.as_view(), name='list_compounds'),
    path('compound/<int:pk>/', views.CompoundDetailAPIView.as_view(),
         name='compound_details'),
    path('compound/delete/<int:pk>/',
         views.DeleteCompoundView, name='delete_compound'),

    # Block Section
    path('block/new/', views.BlockCreateAPIView.as_view(), name='create_block'),
    path('block/edit/<int:pk>/',
         views.BlockUpdateAPIView.as_view(), name='edit_block'),
    path('block/', views.BlockListAPIView.as_view(), name='list_blocks'),
    path('block/<int:pk>/', views.BlockDetailAPIView.as_view(), name='block_details'),
    path('block/delete/<int:pk>/',
         views.DeleteBlockView, name='delete'),
    # Tower Section
    path('tower/new/', views.TowerCreateAPIView.as_view(), name='create_tower'),
    path('tower/edit/<int:pk>/',
         views.TowerUpdateAPIView.as_view(), name='edit_tower'),
    path('tower/', views.TowerListAPIView.as_view(), name='list_towers'),
    path('tower/<int:pk>/', views.TowerDetailAPIView.as_view(), name='tower_details'),
    path('tower/delete/<int:pk>/',
         views.DeleteTowerView, name='delete_tower'),

    # Flat Section
    path('flat/new/', views.FlatCreateAPIView.as_view(), name='create_flat'),
    path('flat/edit/<int:pk>/', views.FlatUpdateAPIView.as_view(), name='edit_flat'),
    path('flat/', views.FlatListAPIView.as_view(), name='list_flats'),
    path('flat/<int:pk>/', views.FlatDetailAPIView.as_view(), name='flat_details'),
    path('flat/delete/<int:pk>/',
         views.DeleteFlatView, name='delete_flat'),

    # Store Section
    path('store/new/', views.StoreCreateAPIView.as_view(), name='create_store'),
    path('store/edit/<int:pk>/',
         views.StoreUpdateAPIView.as_view(), name='edit_store'),
    path('store/', views.StoreListAPIView.as_view(), name='list_stores'),
    path('store/<int:pk>/', views.StoreDetailAPIView.as_view(), name='store_details'),
    path('store/delete/<int:pk>/',
         views.DeleteShopView, name='delete_store'),

    # owner section
    path('owner/new/', views.OwnerCreateAPIView.as_view(), name='create_owner'),
    path('owner/edit/<int:pk>/',
         views.OwnerUpdateAPIView.as_view(), name='edit_owner'),
    path('owner/', views.OwnerListAPIView.as_view(), name='list_owner'),
    path('owner/<int:pk>/', views.OwnerDetailAPIView.as_view(), name='owner_details'),
    path('owner/delete/<int:pk>/', views.DeleteOwnerView, name='owner_delete'),

    # Ownership Store Section
    path('ownershipstore/new/', views.ownershipStoreCreateAPIView.as_view(),
         name='create_ownership_store'),
    path('ownershipstore/edit/<int:pk>/',
         views.ownershipStoreUpdateAPIView.as_view(), name='edit_ownership_store'),
    path('ownershipstore/', views.ownershipStoreListAPIView.as_view(),
         name='list_ownership_stores'),
    path('ownershipstore/delete/<int:pk>/',
         views.DeleteOwnershipStoreView, name='delete_ownership_store'),

    # Family Section
    path('family/new/', views.FamilyCreateAPIView.as_view(), name='create_family'),
    path('family/edit/<int:pk>/',
         views.FamilyUpdateAPIView.as_view(), name='edit_family'),
    path('family/', views.FamilyListAPIView.as_view(), name='list_familys'),
    path('family/<int:pk>/', views.FamilyDetailAPIView.as_view(),
         name='family_details'),
    path('family/<int:pk>/delete', views.DeleteFamilyView,
         name='family_delete'),
]
