from django.urls import path
from .views import *



urlpatterns = [
    # path('', home, name = 'home'),
    # path('login-user/', login_user, name = 'login'),
    path('register-user/', register_user, name = 'register'),
    path('logout/', logout, name = 'logout'),
    # path('active-account/<uidb64>/<token>/', activate_account, name='activate_account'), 
    # path('desactivate-account/', desactivate_account, name = 'desactivate_account'),
    # path('change-pass/', change_pass, name = 'change_pass'),
    # # path('forget-my-pass/', forget_my_pass, name = 'forget_my_pass'),

    # path('my-notifications/', my_notifications, name = 'my_notifications'),

    # path('profile/', profile_user, name = 'profile_user'),
    # path('new-profile/', new_profile, name = 'new_profile'),
    # path('edit-profile/', edit_profile, name="edit_profile"),
    # path('projects-save/', projects_save, name = 'projects_save'),
    # path('save-project/<int:job_id>/', save_project, name = 'save_project'),
    # path('remove-project/<int:job_id>/', remove_save_project, name = 'remove_save_project'),

    # path('my-projects-in-progress/', my_jobs_in_progress, name = 'my_jobs_in_progress'),
    # path('done-job-in-progress/<int:job_id>/', done_job_in_progress, name = 'done_job_in_progress'),
    # path('giv-up-job-in-progress/<int:job_id>/', giv_up_job_in_progress, name = 'giv_up_job_in_progress'),

    # path('chats/', my_chats, name='my_chats'),
    # path('chats/room-details/<int:id_user>/', chat_details_room, name='chat_details_room'),
    # path('export-docs-chat/<path:path_doc>/', export_docs_chat, name='export_docs_chat'),

    # path('settings/', settings_user, name='settings_user'),
    # path('my-finances/', my_finances, name='my_finances'),
    # path('plans/', plans_user, name ='plans_user'),
    # path('add-plan/<int:id_plan>/', add_plan, name= 'add_plan'),
    # path('success-checkout-plan/', success_buy_plan, name='success_buy_plan'),

]
