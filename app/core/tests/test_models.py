"""
Models testing
"""
from decimal import Decimal
from django.test import TestCase
from django.contrib.auth import get_user_model
from core import models


class ModelTests(TestCase):
    """testing model create for user"""
    def test_create_user_with_email_success(self):
        """ testing user create successfully"""
        email = "sanjana@example.com"
        password = "Qwerty12"
        user = get_user_model().objects.create_user(   # type: ignore
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalize(self):
        """normalizing email input"""
        sample_emails = [
            ['test1@Example.com', 'test1@example.com'],
            ['Test2@EXAMPLE.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.COM', 'TEST3@example.com'],
            ['test4@example.COM', 'test4@example.com'],
            ['test5@Example.Com', 'test5@example.com'],
        ]

        for emails, expected in sample_emails:
            user = get_user_model().objects.create_user(  # type: ignore
                emails, 'sample123')
            self.assertEqual(user.email, expected)

    def test_new_user_email_req_validation(self):
        """should raise valueerror when email not passed"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(  # type: ignore
                '', 'sample123')

    def test_create_superuser(self):
        "create superuser"
        user = get_user_model().objects.create_superuser(  # type: ignore
            'test@exampler', 'sample123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_create_recipe(self):
        """Test for create a recipe successful"""
        user = get_user_model().objects.create_user(
            'test@example.com',
            'sample123'
        )

        recipe = models.Recipe.objects.create(
            user=user,
            title='Sample recipe name',
            time_minutes=5,
            price=Decimal('5.50'),
            description='Sample recipe description',
        )

        self.assertEqual(str(recipe), recipe.title)
