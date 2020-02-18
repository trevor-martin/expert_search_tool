from django.shortcuts import render

from django.db.models import Q
from django.db.models import Count

from .forms import ExpertForm
from .models import Expert, Friendships

class ExpertInfo:
    def __init__(self, pk=0, name='', short_url='', num_of_friends=0):
        pk = pk
        name = name
        short_url = short_url
        num_of_friends = num_of_friends


def home(request):

    form = ExpertForm()
    if request.method == 'POST':
        form = ExpertForm(request.POST)
        if form.is_valid():
            expert = Expert(
                name = form.cleaned_data['name'],
                personal_website_url = form.cleaned_data['personal_website_url']
            )
            expert.save()
            form = ExpertForm()

    experts_list = Expert.objects.all()
    friends_count = Friendships.objects.values('expert_id_001').annotate(total=Count('expert_id_001'))

    num_of_friends = {}
    for f in friends_count:
        num_of_friends[f['expert_id_001']] = f['total']

    experts = []
    for expert in experts_list:
        cur_expert = {'pk': expert.pk, 'name': expert.name, 'short_url': expert.personal_website_url, 'num_of_friends': 0}

        if expert.pk in num_of_friends:
            cur_expert['num_of_friends'] = num_of_friends[expert.pk]

        experts.append(cur_expert)

    context = {
        'experts': experts,
        'form': form,
    }

    return render(request, 'expert_search/home.html', context)

def expert_detail(request, pk):
    expert = Expert.objects.get(pk=pk)

    if request.method == 'POST':       
        new_friends = []

        for key in request.POST:
            if key.startswith('pf'):
                new_friends.append(key.split('pf')[1])      

        for new_friend in new_friends:
            friendship = Friendships()
            friendship.expert_id_001 = expert.pk
            friendship.expert_id_002 = new_friend
            friendship.save()

            friendship = Friendships()
            friendship.expert_id_001 = new_friend
            friendship.expert_id_002 = expert.pk
            friendship.save()
            
    friendships = Friendships.objects.filter(expert_id_001=expert.pk)

    friends = []
    friends_id_list = [expert.pk]
    for friendship in friendships:
        info = Expert.objects.get(pk=friendship.expert_id_002)
        friends.append({'pk': info.pk, 'name': info.name})
        friends_id_list.append(friendship.expert_id_002)

    potential_friends = Expert.objects.all().exclude(id__in=friends_id_list)

    context = {
        'expert': expert,
        'friends': friends,
        'potential_friends': potential_friends
    }

    return render(request, 'expert_search/expert_detail.html', context)
