from rest_framework import serializers
from emailapi.utils import Util



class EmailSerializer(serializers.Serializer):
    
    email = serializers.EmailField()
    subject = serializers.CharField(max_length=255)
    body_text = serializers.CharField()

    class Meta:
        fields = ['email', 'subject', 'body_text']

    def validate(self, attrs):
        to_email = attrs.get('email')
        subject = attrs.get('subject')
        body_text = attrs.get('body_text')

        data = {
            'to_email' : to_email,
            'subject' : subject,
            'body': body_text
        }
        try:
            Util.send_email(data)
        except Exception as e:
            raise serializers.ValidationError("Error sending email: " + str(e))
        return attrs
