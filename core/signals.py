from core.models import Profile
import string, hashlib, json, random
from django.contrib.auth.models import User
from django.db.models.signals import post_save


def create_token():
	return ''.join(random.choices(string.ascii_letters + string.digits, k=30))


def create_profile(sender, instance, created, **kwargs):
	if created:
		
		token = create_token()
		unique_key = f"{token}_{instance.pk}"
		
		hash_str = json.dumps(unique_key, sort_keys=True).encode()
		hashed_unique_key = hashlib.sha256(hash_str).hexdigest()

		Profile.objects.create(
			user=instance, 
			api_key=unique_key, 
			hashed_api_key=hashed_unique_key
		)

		print(f"""
			Profile of '{instance.username}' created successfully !!!!
			User sex: {instance.profile.sex}
			API key: {instance.profile.api_key}
			Hashed API key: {instance.profile.hashed_api_key}
		""")
        
		
post_save.connect(create_profile, sender=User)
