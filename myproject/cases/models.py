from django.db import models

# Create your models here.
class CaseStore(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    # class Meta:
    #     table_name = "tb_case_store"

class CaseParam(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    casestore = models.ForeignKey(CaseStore, on_delete=models.CASCADE)

    # class Meta:
    #     table_name = "tb_case_param"