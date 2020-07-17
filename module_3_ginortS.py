#실패 잘못되었다는 건 알겠으면서도 어떻게 고쳐야할지 잘 모르겠어요ㅠㅠ

print(*sorted(x for x if x.islower()) + sorted(x for x if x.isupper()) + sorted(x for x if x.isdigit() and x%2!=0) + sorted(x for x if x.isdignt() and x%2==0))