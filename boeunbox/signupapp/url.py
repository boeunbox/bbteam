import account.views

urlpatterns = [
    path('login/', account.views.login, name='login'),
    path('signup/', account.views.signup, name='signup'),
    path('logout/', account.views.logout, name='logout'),
]