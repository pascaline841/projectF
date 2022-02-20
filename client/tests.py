from django.test import TestCase

import asyncio

from .models import Client
from .views import get_client


class TestIndex(TestCase):
    def setUp(self):
        """Create a client test."""
        Client.objects.create(
            first_name="test",
            last_name="test_name",
            email="test@test.com",
        )  
    
    
    def test_profile_correct_template(self):
        """Test display the client's  datas."""
        user_test = Client.objects.first()
        first_name = user_test.first_name
        last_name = user_test.last_name
        email = user_test.email
        loop = asyncio.get_running_loop()
        clients_default = get_client("default",first_name, last_name, email)
        clients_db1 = get_client("db_1", first_name, last_name, email)
        loop.close()
        self.assertTrue(clients_default)
        self.assertTrue(clients_db1)
