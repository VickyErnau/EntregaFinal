* Se mencionan debajo las URLs que pueden ser utilizadas. 
  Hay dos aplicaciones: 
	- AppBlog que contiene el sitio principal.
	- AppAccount que contiene lo referido al comportamiento de usuarios.

* Accediendo al inicio hay una barra de navegación con todos los links necesarios
  por lo que no debería ser necesario tener que ingresar a las distintas urls de manera directa.

URLs AppBlog

    path("", inicio, name="inicio"),
    path("inicio/", inicio, name="inicio"),
    path("about/", about, name="about"),
    path("create-page/", post_create, name="post_create"),
    path("update-page/<int:id>/", post_update, name="post_update"),
    path("update-page/", post_update, name="post_update"),
    path('pages/', PosteoListView.as_view(), name='posts'),
    path("page_detail/<int:pk>/", PosteoDetailView.as_view(), name="post_detail"),
    path("delete_page/<int:pk>/", PosteoDeleteView.as_view(), name="post_delete"),

URLs AppAccount

    path('registration/', register_user, name='register_user'),
    path('update_user/', update_user, name='update_user'),
    path('perfil/', ProfileView.as_view(), name='profile_user'),
    path('logout/', logout_user, name='logout'),
    path('password_changed/', password_changed, name='password_changed'),
    path('update_password/', PassChangeView.as_view(template_name='registration/update_password.html'), name='update_password'),
    path('error/', error, name='error'),
    path('admin/', modulo_admin, name='modulo_admin'),


