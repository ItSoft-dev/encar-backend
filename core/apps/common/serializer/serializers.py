from rest_framework import serializers



from core.apps.common.models import AboutProject, Contact, Disclaimer, FAQ, FeedBack, OfferAgreement, OrderCarImport, Partner, PrivacyPolicy, SecureTransaction, ReturnPolicy



class ReturnPolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = ReturnPolicy
        fields = '__all__'


class SecureTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecureTransaction
        fields = '__all__'


class PrivacyPolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = PrivacyPolicy
        fields = '__all__'


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = '__all__'


class OrderCarImportSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderCarImport
        fields = '__all__'


class OfferAgreementSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfferAgreement
        fields = '__all__'



class FeedBackSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedBack
        fields = '__all__'


class AboutProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutProject
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'



class DisclaimerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disclaimer
        fields = '__all__'
    

class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = '__all__'
    