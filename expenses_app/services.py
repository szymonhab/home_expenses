import json

from .models import Bill


class BillService:
    @staticmethod
    def create_bill_from_form_data(data):
        bill = Bill.objects.create(bill_date=data['bill_date'], amount=data['amount'], person=data['person'],
                                   workspace_id=1, shop=data['shop'])

        for row in json.loads(data['rows']):
            bill.billrow_set.create(amount=row['sum'], label=row['label'], category_id=row['category'])

        return bill
