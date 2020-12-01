from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.clickjacking import xframe_options_exempt

from datetime import datetime as dt
import datetime

from .models import Winx, Arkle, Denman, Enable, Frankel, Kauto
from .forms import WinxForm, ArkleForm, DenmanForm, EnableForm, FrankelForm, KautoForm


today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)


# Individual OCM Pages
@xframe_options_exempt
@login_required
def winx_page(request):
    winxes_missing = Winx.objects.filter(date_added = today, status = 'MISSING').order_by('-date_added', 'number')
    winxes_stick = Winx.objects.filter(date_added = today, status = 'STICK').order_by('-date_added', 'number')
    context = {'winxes_missing' : winxes_missing, 'winxes_stick': winxes_stick}
    return render(request, 'unit_logs/winx.html', context)

@xframe_options_exempt
@login_required
def arkle_page(request):
    arkles_missing = Arkle.objects.filter(date_added = today, status = 'MISSING').order_by('-date_added', 'number')
    arkles_stick = Arkle.objects.filter(date_added = today, status = 'STICK').order_by('-date_added', 'number')
    context = {'arkles_missing' : arkles_missing, 'arkles_stick': arkles_stick}
    return render(request, 'unit_logs/arkle.html', context)

@xframe_options_exempt
@login_required
def denman_page(request):
    denmans_missing = Denman.objects.filter(date_added = today, status = 'MISSING').order_by('-date_added', 'number')
    denmans_stick = Denman.objects.filter(date_added = today, status = 'STICK').order_by('-date_added', 'number')
    context = {'denmans_missing' : denmans_missing, 'denmans_stick': denmans_stick}
    return render(request, 'unit_logs/denman.html', context)

@xframe_options_exempt
@login_required
def enable_page(request):
    enables_missing = Enable.objects.filter(date_added = today, status = 'MISSING').order_by('-date_added', 'number')
    enables_stick = Enable.objects.filter(date_added = today, status = 'STICK').order_by('-date_added', 'number')
    context = {'enables_missing' : enables_missing, 'enables_stick': enables_stick}
    return render(request, 'unit_logs/enable.html', context)

@xframe_options_exempt
@login_required
def frankel_page(request):
    frankels_missing = Frankel.objects.filter(date_added = today, status = 'MISSING').order_by('-date_added', 'number')
    frankels_stick = Frankel.objects.filter(date_added = today, status = 'STICK').order_by('-date_added', 'number')
    context = {'frankels_missing' : frankels_missing, 'frankels_stick': frankels_stick}
    return render(request, 'unit_logs/frankel.html', context)

@xframe_options_exempt
@login_required
def kauto_page(request):
    kautos_missing = Kauto.objects.filter(date_added = today, status = 'MISSING').order_by('-date_added', 'number')
    kautos_stick = Kauto.objects.filter(date_added = today, status = 'STICK').order_by('-date_added', 'number')
    context = {'kautos_missing' : kautos_missing, 'kautos_stick': kautos_stick}
    return render(request, 'unit_logs/kauto.html', context)



# Main index page
@xframe_options_exempt
@login_required
def index(request):
    winxes = Winx.objects.order_by('number')
    arkles = Arkle.objects.order_by('number')
    denmans = Denman.objects.order_by('number')
    enables = Enable.objects.order_by('number')
    frankels = Frankel.objects.order_by('number')
    kautos = Kauto.objects.order_by('number')
    context = {'winxes' : winxes, 'arkles' : arkles, 'denmans' : denmans, 'enables' : enables, 'frankels' : frankels, 'kautos' : kautos}
    return render(request, 'unit_logs/index.html', context)



# Individual Pages
@xframe_options_exempt
@login_required
def winxes(request):
    winxes = Winx.objects.order_by('-date_added', '-status', 'number')
    
    context = {'winxes' : winxes}
    return render(request, 'unit_logs/winxes.html', context)

@xframe_options_exempt
@login_required
def winx(request, winx_id):
    winx = Winx.objects.get(id=winx_id)
    entries = winx.entry_set.order_by('-date_added')
    
    if request.method == 'GET':
        form = WinxForm(instance=winx)
        context = {'winx': winx, 'form':form, 'entries':entries}
        return render(request, 'unit_logs/winx_unit.html', context)
    else:
        form = WinxForm(request.POST, instance=winx)
        form.save()
        return redirect('unit_logs:winxes')
    


@xframe_options_exempt
@login_required
def arkles(request):
    arkles = Arkle.objects.order_by('-date_added', '-status', 'number')
    context = {'arkles' : arkles}
    return render(request, 'unit_logs/arkles.html', context)

@xframe_options_exempt
@login_required
def arkle(request, arkle_id):
    arkle = Arkle.objects.get(id=arkle_id)
    if request.method == 'GET':
        form = ArkleForm(instance=arkle)
        context = {'arkle': arkle, 'form':form}
        return render(request, 'unit_logs/arkle_unit.html', context)
    else:
        form = ArkleForm(request.POST, instance=arkle)
        form.save()
        return redirect('unit_logs:arkles')


@xframe_options_exempt
@login_required
def denmans(request):
    denmans = Denman.objects.order_by('-date_added', '-status', 'number')
    context = {'denmans' : denmans}
    return render(request, 'unit_logs/denmans.html', context)


@xframe_options_exempt
@login_required
def denman(request, denman_id):
    denman = Denman.objects.get(id=denman_id)
    if request.method == 'GET':
        form = DenmanForm(instance=denman)
        context = {'denman': denman, 'form':form}
        return render(request, 'unit_logs/denman_unit.html', context)
    else:
        form = DenmanForm(request.POST, instance=denman)
        form.save()
        return redirect('unit_logs:denmans')


@xframe_options_exempt
@login_required
def enables(request):
    enables = Enable.objects.order_by('-date_added', '-status', 'number')
    context = {'enables' : enables}
    return render(request, 'unit_logs/enables.html', context)


@xframe_options_exempt
@login_required
def enable(request, enable_id):
    enable = Enable.objects.get(id=enable_id)
    if request.method == 'GET':
        form = EnableForm(instance=enable)
        context = {'enable': enable, 'form':form}
        return render(request, 'unit_logs/enable_unit.html', context)
    else:
        form = EnableForm(request.POST, instance=enable)
        form.save()
        return redirect('unit_logs:enables')


@xframe_options_exempt
@login_required
def frankels(request):
    frankels = Frankel.objects.order_by('-date_added', '-status', 'number')
    context = {'frankels' : frankels}
    return render(request, 'unit_logs/frankels.html', context)


@xframe_options_exempt
@login_required
def frankel(request, frankel_id):
    frankel = Frankel.objects.get(id=frankel_id)
    if request.method == 'GET':
        form = FrankelForm(instance=frankel)
        context = {'frankel': frankel, 'form':form}
        return render(request, 'unit_logs/frankel_unit.html', context)
    else:
        form = FrankelForm(request.POST, instance=frankel)
        form.save()
        return redirect('unit_logs:frankels')


@xframe_options_exempt
@login_required
def kautos(request):
    kautos = Kauto.objects.order_by('-date_added', '-status', 'number')
    context = {'kautos' : kautos}
    return render(request, 'unit_logs/kautos.html', context)


@xframe_options_exempt
@login_required
def kauto(request, kauto_id):
    kauto = Kauto.objects.get(id=kauto_id)
    if request.method == 'GET':
        form = KautoForm(instance=kauto)
        context = {'kauto': kauto, 'form':form}
        return render(request, 'unit_logs/kauto_unit.html', context)
    else:
        form = KautoForm(request.POST, instance=kauto)
        form.save()
        return redirect('unit_logs:kautos')


@xframe_options_exempt
@login_required
def new_winx(request):
    """Add a new winx"""
    if request.method != 'POST':
        # No data submitted, create a blank form
        form = WinxForm()
    else:
        # POST data submitted; process data
        form = WinxForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('unit_logs:winxes')

    # Display a blank or invalid form
    context = {'form': form}
    return render(request, 'unit_logs/new_winx.html', context)


@xframe_options_exempt
@login_required
def new_arkle(request):
    """Add a new arkle"""
    if request.method != 'POST':
        # No data submitted, create a blank form
        form = ArkleForm()
    else:
        # POST data submitted; process data
        form = ArkleForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('unit_logs:arkles')

    # Display a blank or invalid form
    context = {'form': form}
    return render(request, 'unit_logs/new_arkle.html', context)


@xframe_options_exempt
@login_required
def new_denman(request):
    """Add a new denman"""
    if request.method != 'POST':
        # No data submitted, create a blank form
        form = DenmanForm()
    else:
        # POST data submitted; process data
        form = DenmanForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('unit_logs:denmans')

    # Display a blank or invalid form
    context = {'form': form}
    return render(request, 'unit_logs/new_denman.html', context)


@xframe_options_exempt
@login_required
def new_enable(request):
    """Add a new enable"""
    if request.method != 'POST':
        # No data submitted, create a blank form
        form = EnableForm()
    else:
        # POST data submitted; process data
        form = EnableForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('unit_logs:enables')

    # Display a blank or invalid form
    context = {'form': form}
    return render(request, 'unit_logs/new_enable.html', context)


@xframe_options_exempt
@login_required
def new_frankel(request):
    """Add a new frankel"""
    if request.method != 'POST':
        # No data submitted, create a blank form
        form = FrankelForm()
    else:
        # POST data submitted; process data
        form = FrankelForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('unit_logs:frankels')

    # Display a blank or invalid form
    context = {'form': form}
    return render(request, 'unit_logs/new_frankel.html', context)


@xframe_options_exempt
@login_required
def new_kauto(request):
    """Add a new kauto"""
    if request.method != 'POST':
        # No data submitted, create a blank form
        form = KautoForm()
    else:
        # POST data submitted; process data
        form = KautoForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('unit_logs:kautos')

    # Display a blank or invalid form
    context = {'form': form}
    return render(request, 'unit_logs/new_kauto.html', context)


@xframe_options_exempt
@login_required
def deletewinx(request, winx_id):
    winx = Winx.objects.get(id=winx_id)
    if request.method == 'POST':
        winx.delete()
        return redirect('unit_logs:winxes')


@xframe_options_exempt
@login_required
def deletearkle(request, arkle_id):
    arkle = Arkle.objects.get(id=arkle_id)
    if request.method == 'POST':
        arkle.delete()
        return redirect('unit_logs:arkles')


@xframe_options_exempt
@login_required
def deletedenman(request, denman_id):
    denman = Denman.objects.get(id=denman_id)
    if request.method == 'POST':
        denman.delete()
        return redirect('unit_logs:denmans')


@xframe_options_exempt
@login_required
def deleteenable(request, enable_id):
    enable = Enable.objects.get(id=enable_id)
    if request.method == 'POST':
        enable.delete()
        return redirect('unit_logs:enables')


@xframe_options_exempt
@login_required
def deletefrankel(request, frankel_id):
    frankel = Frankel.objects.get(id=frankel_id)
    if request.method == 'POST':
        frankel.delete()
        return redirect('unit_logs:frankels')


@xframe_options_exempt
@login_required
def deletekauto(request, kauto_id):
    kauto = Kauto.objects.get(id=kauto_id)
    if request.method == 'POST':
        kauto.delete()
        return redirect('unit_logs:kautos')