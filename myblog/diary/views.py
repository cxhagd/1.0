# diary/views.py
from django.shortcuts import render
from .models import DiaryEntry
from django.contrib.auth.decorators import login_required

def home(request):
    if not request.user.is_authenticated:
        return redirect('login')  # 如果用户未登录，重定向到登录页面
    else:
        return redirect('diary_list')  # 如果用户已登录，重定向到日记列表或个人主页视图
# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')  # 或者重定向到用户的个人主页
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

# diary/views.py
from django.shortcuts import render
from .models import DiaryEntry
@login_required  # 确保只有登录用户可以访问此视图
def diary_list(request):
    entries = DiaryEntry.objects.filter(user=request.user)  # 获取当前用户的日记条目
    return render(request, 'diary/diary_list.html', {'entries': entries})

# diary/views.py
from django.shortcuts import render, get_object_or_404
from .models import DiaryEntry

def diary_detail(request, pk):
    entry = get_object_or_404(DiaryEntry, pk=pk, user=request.user)  # 获取指定的日记条目
    return render(request, 'diary/diary_detail.html', {'entry': entry})


# diary/views.py
from django.shortcuts import render, redirect
from .forms import DiaryEntryForm
from django.contrib.auth.decorators import login_required

@login_required  # 确保只有登录用户可以创建日记条目
def diary_create(request):
    if request.method == 'POST':
        form = DiaryEntryForm(request.POST, request.FILES)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.user = request.user  # 设置日记条目的作者为当前用户
            new_entry.save()
            return redirect('diary_detail', pk=new_entry.pk)  # 重定向到日记的详细视图
    else:
        form = DiaryEntryForm()
    return render(request, 'diary/diary_form.html', {'form': form})


from django.contrib.auth.decorators import login_required

@login_required
def diary_create(request):
    if request.method == 'POST':
        form = DiaryEntryForm(request.POST, request.FILES)
        if form.is_valid():
            diary_entry = form.save(commit=False)
            diary_entry.user = request.user
            diary_entry.save()
            return redirect('diary_detail', pk=diary_entry.pk)
    else:
        form = DiaryEntryForm()
    return render(request, 'diary/diary_create.html', {'form': form})

def diary_detail(request, pk):
    diary_entry = get_object_or_404(DiaryEntry, pk=pk, user=request.user)
    return render(request, 'diary/diary_detail.html', {'diary_entry': diary_entry})

import calendar
from datetime import datetime
from django.shortcuts import render
from .models import DiaryEntry
from django.utils.timezone import now
def get_calendar(request, year=datetime.now().year, month=datetime.now().month):
    # 使用 Python calendar 模块生成当前月份的日历
    cal = calendar.Calendar()
    month_days = cal.itermonthdays(year, month)

    # 检查每天是否有日记条目
    days_with_entries = {entry.date.day for entry in DiaryEntry.objects.filter(date__year=year, date__month=month, user=request.user)}

    # 准备传递给模板的上下文
    context = {
        'month_days': month_days,
        'days_with_entries': days_with_entries,
        'month': month,
        'year': year,
    }

    return render(request, 'diary/calendar.html', context)


from django.shortcuts import render
# 导入日历生成函数


def user_home(request):
    today = datetime.now()
    year, month = today.year, today.month

    month_days, days_with_entries = get_calendar(year, month, request.user)

    context = {
        'month_days': month_days,
        'days_with_entries': days_with_entries,
        'year': year,
        'month': month,
        # 其他上下文数据...
    }
    return render(request, 'diary/user_home.html', context)

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def my_view(request):
    # 视图逻辑，这里简单地渲染一个名为 'my_template.html' 的模板
    return render(request, 'diary/templates/registration/register.html')
