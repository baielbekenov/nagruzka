from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.db.models import Sum, Subquery, OuterRef

from nagr.forms import GrouppForm, DisciplineForm, TeacherForm
from nagr.models import Teacher, Discipline, Groupp


# Create your views here.

def teacher(request):
    if request.method == 'GET':
        teacher = Teacher.objects.all().annotate(total=Sum('disciplene__group_id__vsego_uchebnyh_chasov')).order_by('-id')

        context = {'teachers': teacher}
        return render(request, 'teacher.html', context)
    return HttpResponse('Error')

def create(request):
    if request.method == 'POST':
        form = GrouppForm(request.POST)
        if form.is_valid():
            group = form.save(commit=False)
            group.obshee_kol_stud = group.kol_stud_budget + group.kol_stud_contract
            group.priem_SRS = (group.amount_of_credit * 30 - group.lekcii_po_ucheb_planu - group.praktZan_po_ucheb_planu - group.labRab_po_ucheb_planu) / 30 * 0.2 * group.obshee_kol_stud
            group.kontrol_tekuchiy1 = group.obshee_kol_stud * 0.3
            group.kontrol_tekuchiy2 = group.obshee_kol_stud * 0.3
            group.kontrol_itogovyi = group.kontrol_tekuchiy1 + group.kontrol_tekuchiy2 + group.kontrol_tekuchiy3
            group.vsego_uchebnyh_chasov = (group.lekcii_po_ucheb_planu + group.lekcii_zachityvaetsa_v_nagruzku
                                           + group.praktZan_po_ucheb_planu + group.praktZan_zachityvaetsa_v_nagruzku + group.labRab_po_ucheb_planu
                                           + group.labRab_zachityvaetsa_v_nagruzku + group.rukovod_KRIKP + group.recenzirov_KR + group.priem_SRS
                                           + group.praktika_uchebnay + group.praktika_proizvod + group.praktika_predkval + group.praktika_pedagog
                                           + group.praktika_nauchno + group.kontrol_tekuchiy1 + group.kontrol_tekuchiy2 + group.kontrol_tekuchiy3
                                           + group.kontrol_itogovyi + group.zachita_rukovod_VKR + group.zachita_konsult + group.zachita_recencirovanie
                                           + group.zachita_uchastie_v_GAK + group.normokontr + group.magistratura + group.aspirantura_doctorontura
                                           + group.online + group.offline + group.academ_sov + group.rukovodstvo_kafedroi + group.rukovodstvo_dekanatom
                                           + group.prochie) - group.lekcii_po_ucheb_planu - group.praktZan_po_ucheb_planu - group.labRab_po_ucheb_planu - group.kontrol_tekuchiy1 - group.kontrol_tekuchiy2 - group.kontrol_tekuchiy3
            # group.vsego_uchebnyh_chasov = (sum(group[])) - group.lekcii_po_ucheb_planu - group.praktZan_po_ucheb_planu - group.labRab_po_ucheb_planu - group.kontrol_tekuchiy1 - group.kontrol_tekuchiy2 - group.kontrol_tekuchiy3

            form.save()
    else:
        form = GrouppForm()
    content = {'form': form}
    return render(request, 'create.html', content)


def creatediscipline(request):
    if request.method == 'POST':
        form = DisciplineForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/thanks/')
    else:
        form = DisciplineForm()

    context = {'form': form}
    return render(request, 'creatediscipline.html', context)


def thanks(request):
    return render(request, 'thanks.html',)

def createteacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/thanks/')
    else:
        form = TeacherForm()
    context = {'form': form}
    return render(request, 'createteacher.html', context)


def showgroupp(request):
    if request.method == 'GET':
        groupp = Groupp.objects.all()

        context = {'groupp': groupp}
        return render(request, 'showgroupp.html', context)

