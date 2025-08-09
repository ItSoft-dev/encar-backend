from django.urls import path

from core.apps.common.views.main import AboutProjectListApiView, ContactListApiView, PartnerListApiView, FeedBackListApiView, DisclaimerListApiView, ReturnPolicyListApiView, PrivacyPolicyListApiView, OfferAgreementListApiView, OrderCarImportListApiView, SecureTransactionListApiView, FAQListApiView

urlpatterns = [
    path('about_projects/', AboutProjectListApiView.as_view()),
    path('contracts/', ContactListApiView.as_view()),
    path('partners/', PartnerListApiView.as_view()),
    path('feedbacks/', FeedBackListApiView.as_view()),
    path('disclaimer/', DisclaimerListApiView.as_view()),
    path('return_policy/', ReturnPolicyListApiView.as_view()),
    path('privacy_policy/', PrivacyPolicyListApiView.as_view()),
    path('offer_agreement/', OfferAgreementListApiView.as_view()),
    path('order_car_import/', OrderCarImportListApiView.as_view()),
    path('secure_transaction/', SecureTransactionListApiView.as_view()),
    path('faq/', FAQListApiView.as_view()),
]