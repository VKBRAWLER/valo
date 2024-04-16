from rest_framework import serializers
from api.models import Company
class CompanySerializer(serializers.HyperlinkedModelSerializer):
  comapny_id = serializers.ReadOnlyField() # to get the primary key as Read Only
  class Meta:
    model = Company
    fields = "__all__"

