from django.test import TestCase
from restapi import models


class TestModels(TestCase):
    def test_expense(self):
        expense = models.Expense.objects.create(
            amount=12.99, merchant="DMart", description="Chocolate", category="Grocery"
        )
        inserted_expense = models.Expense.objects.get(pk=expense.id)

        self.assertEqual(inserted_expense.amount, 12.99)
        self.assertEqual(inserted_expense.merchant, "DMart")
        self.assertEqual(inserted_expense.description, "Chocolate")
        self.assertEqual(inserted_expense.category, "Grocery")
