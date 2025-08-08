from rest_framework import generics

from core.apps.common.models import AboutProject, Contact, Disclaimer, FAQ, FeedBack, OfferAgreement, OrderCarImport, Partner, PrivacyPolicy, SecureTransaction, ReturnPolicy

from core.apps.common.serializer import serializers



class ReturnPolicyListApiView(generics.ListAPIView):
    queryset = ReturnPolicy.objects.all()
    serializer_class = serializers.ReturnPolicySerializer


class SecureTransactionListApiView(generics.ListAPIView):
    queryset = SecureTransaction.objects.all()
    serializer_class = serializers.SecureTransactionSerializer


class PrivacyPolicyListApiView(generics.ListAPIView):
    queryset = PrivacyPolicy.objects.all()
    serializer_class = serializers.PrivacyPolicySerializer


class PartnerListApiView(generics.ListAPIView):
    queryset = Partner.objects.all()
    serializer_class = serializers.PartnerSerializer


class OrderCarImportListApiView(generics.ListAPIView):
    queryset = OrderCarImport.objects.all()
    serializer_class = serializers.OrderCarImportSerializer


class OfferAgreementListApiView(generics.ListAPIView):
    queryset = OfferAgreement.objects.all()
    serializer_class = serializers.OfferAgreementSerializer


class FeedBackListApiView(generics.ListAPIView):
    queryset = FeedBack.objects.all()
    serializer_class = serializers.FeedBackSerializer


class FAQListApiView(generics.ListAPIView):
    queryset = FAQ.objects.all()
    serializer_class = serializers.FAQSerializer


class DisclaimerListApiView(generics.ListAPIView):
    queryset = Disclaimer.objects.all()
    serializer_class = serializers.DisclaimerSerializer


class ContactListApiView(generics.ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = serializers.ContactSerializer


class AboutProjectListApiView(generics.ListAPIView):
    queryset = AboutProject.objects.all()
    serializer_class = serializers.AboutProjectSerializer
