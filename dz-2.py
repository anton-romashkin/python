seconds = int(input('Сколько секунд вы хотите перевести? '))

hours = str(seconds // 3600)
minutes = str((seconds % 3600) // 60)
seconds = str(seconds % 60)

if len(hours) == 1:
    hours = '0' + hours

if len(minutes) == 1:
    minutes = '0' + minutes

if len(seconds) == 1:
    seconds = '0' + seconds

print(f'{hours}:{minutes}:{seconds}')
