from rest_framework import serializers
from.models import Profile
import datetime  # Import the datetime module

class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.first_name')
    is_owner = serializers.SerializerMethodField()
    date_of_birth = serializers.DateField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def validate_date_of_birth(self, obj):
        # Check if the date is not in the future
        if obj > datetime.date.today():
            print("Cannot be in the future")
            raise serializers.ValidationError("Date cannot be in the future.")
            
        # Calculate age based on today's date
        today = datetime.date.today()
        age = today.year - obj.year - ((today.month, today.day) < (obj.month, obj.day))
        
        # Add a custom message and flag to the context if the user is under 18
        if age < 18:
            self.context['can_create_training_plan'] = False
            # Print the custom message to the console
            print("Under 18. Cannot create a training plan.")
        return obj

    class Meta:
        model = Profile
        fields = ['id', 'owner', 'created_at', 'updated_at', 'first_name', 'last_name',
                  'email', 'gender', 'fitness_level', 'image', 'content', 'is_owner','date_of_birth',]
