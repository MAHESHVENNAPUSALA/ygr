from django.core.management.base import BaseCommand
from main.models import Ticket  # import Ticket from main app
from django.utils import timezone
from datetime import timedelta

class Command(BaseCommand):
    help = "Mark tickets as Review if client didn't reply in 3 days after admin reply"

    def handle(self, *args, **kwargs):
        tickets = Ticket.objects.filter(status='Pending')
        for ticket in tickets:
            if ticket.last_admin_reply and timezone.now() > ticket.last_admin_reply + timedelta(days=3):
                ticket.status = 'Review'
                ticket.save()
                self.stdout.write(f"{ticket.ticket_id} marked as Review")
