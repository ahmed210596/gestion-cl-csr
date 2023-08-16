from django.core.management.base import BaseCommand
from elasticsearch_dsl.connections import connections
from log_management.models import LogEntry

class Command(BaseCommand):
    help = 'Send logs to Elasticsearch'

    def handle(self, *args, **options):
        es = connections.get_connection()

        for log_entry in LogEntry.objects.all():
            es.index(index='logs', body={
                'timestamp': log_entry.timestamp,
                'message': log_entry.message
            })

        self.stdout.write(self.style.SUCCESS('Logs sent to Elasticsearch.'))
