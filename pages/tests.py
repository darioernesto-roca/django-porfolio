from django.test import TestCase
from django.urls import reverse

from pages.models import ContactMessage


class ContactMessageViewTests(TestCase):
    def setUp(self):
        self.url = reverse("pages:contact_message")
        self.valid_data = {
            "name": "Ada Lovelace",
            "email": "ada@example.com",
            "subject": "Project enquiry",
            "message": "I would like to discuss a Django project.",
        }

    def test_homepage_contains_django_contact_form(self):
        response = self.client.get(reverse("pages:index"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, f'action="{self.url}"')
        self.assertContains(response, "hx-post=")

    def test_htmx_submission_stores_message_and_returns_success_fragment(self):
        response = self.client.post(
            self.url,
            self.valid_data,
            headers={"HX-Request": "true"},
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Your message was received successfully")
        self.assertEqual(ContactMessage.objects.count(), 1)

    def test_invalid_htmx_submission_returns_errors_without_saving(self):
        response = self.client.post(
            self.url,
            {**self.valid_data, "email": "not-an-email"},
            headers={"HX-Request": "true"},
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Enter a valid email address")
        self.assertFalse(ContactMessage.objects.exists())

    def test_standard_submission_redirects_after_saving(self):
        response = self.client.post(self.url, self.valid_data)

        self.assertRedirects(response, reverse("pages:index"))
        self.assertEqual(ContactMessage.objects.count(), 1)

    def test_contact_service_rejects_get_requests(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 405)
