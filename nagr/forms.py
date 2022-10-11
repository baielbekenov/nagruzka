from django.forms import ModelForm, forms, Textarea
from django.utils.translation import gettext_lazy as _
from nagr.models import Groupp, Discipline, Teacher
from django import forms


class GrouppForm(ModelForm):

    class Meta:
        model = Groupp
        fields = ('name', 'kol_stud_budget', 'kol_stud_contract', 'semester', 'lekcii_po_ucheb_planu', 'lekcii_zachityvaetsa_v_nagruzku',
                  'praktZan_po_ucheb_planu', 'praktZan_zachityvaetsa_v_nagruzku', 'labRab_po_ucheb_planu', 'labRab_zachityvaetsa_v_nagruzku',
                  )


class DisciplineForm(ModelForm):
    # name = forms.CharField(label='name', max_length=100)
    # group_id = forms.ChoiceField(label='group_id')
    # teacher = forms.ChoiceField(label='teacher')

    class Meta:
        model = Discipline
        fields = ('name', 'group_id', 'teacher')


class TeacherForm(ModelForm):

    class Meta:
        model = Teacher
        fields = '__all__'

