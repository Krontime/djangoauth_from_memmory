from django.test import TestCase
from .views import *

class MessageViewTests(TestCase):
    def test_inbox_template(self):
        response = self.client.get('/messenger/inbox/')
        self.assertTemplateUsed(response, "messenger/inbox.html")
        
    def test_post_message(self):
        sender = User.objects.create_user('sender', 'sender@example.com', 'sender')
        recipient = User.objects.create_user('recipient', 'recipient@example.com', 'recipient')
        self.client.login(username="sender", password="sender")
        
        message = {
            "subject": "Test Subject",
            "body": "Test Body",
            "recipient": recipient.id
        }

        response = self.client.post('/messenger/inbox/compose_message/', message)
        self.assertEqual(response.status_code, 302)
    
    def test_view_message_that_exists(self):
        sender = User(username="sender")
        sender.save()
    
        recipient = User(username="receiver")
        recipient.save()
    
        message = Message(
            subject = "Test Subject",
            body = "Test Body",
            sender = sender,
            recipient = recipient)
        message.save()
    
        response = self.client.get('/messenger/message/1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "messenger/mail.html")
    
    # def test_viewing_a_message_marks_it_as_read(self):
    #     sender = User.objects.create_user('sender', 'sender@example.com', 'sender')
    #     recipient = User.objects.create_user('recipient', 'recipient@example.com', 'recipient')

    #     message = Message(
    #         subject = "Test Subject",
    #         body = "Test Body",
    #         sender = sender,
    #         recipient = recipient)
    #     message.save()
        
        
    #     self.assertEqual(message.read, False)
        
    #     response = self.client.get('/messenger/message/1')
    #     self.assertEqual(response.status_code, 200)
        # message = get_object_or_404(Message, pk=1)
        
        # self.assertEqual(message.read, True)
    
    