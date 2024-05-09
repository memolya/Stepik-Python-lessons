day = int(input())
weight = float(input())
goal_loss_daily = 0.2 * day
goal_weight_daily = 100 - goal_loss_daily
result = f'#{day} ДЕНЬ: ТЕКУЩИЙ ВЕС = {weight} кг, ЦЕЛЬ по ВЕСУ = {goal_weight_daily} кг'

if weight <= goal_weight_daily:
    print('Все идет по плану', result, sep = '\n')
else:
    print('Что-то пошло не так', result, sep = '\n')
