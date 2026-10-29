from rest_framework import serializers
from clinic.models import DoctorDb,AppointmentDb

class doctor_serializer(serializers.ModelSerializer):
    class Meta:
        model=DoctorDb
        fields="__all__"                                                               #field=["id","name"]
        read_only_field=["id"]
                                                                        #automaric field generation
class appointment_serializer(serializers.ModelSerializer):
    class Meta:
        model=AppointmentDb
        fields="__all__"
        read_only_field=["id","appointment_time"]                                                              #default validation
                                                                        #conversion between model instance and serialized data
                                                                        #classs meta:
                                                                        #defines the serializers configuration