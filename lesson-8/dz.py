import random
import time
from itertools import chain


class LotoCard:
    def __init__(self):
        self.loto_range = list(range(1, 91))

    def create_card(self):
        loto_card = []
        rand_list = random.sample([i for i in range(1, 90)], 15)
        rand_list = [sorted([i for i in rand_list[:5]]), sorted([i for i in rand_list[5:10]]),
                     sorted([i for i in rand_list[10:15]])]
        for line in rand_list:
            while len(line) < 9:
                line.insert(random.randint(0, 5), ' ')
            loto_card.append(line)
        return loto_card


class PlayLoto(LotoCard):
    def __init__(self):
        super().__init__()
        self.player = LotoCard.create_card(self)
        self.computer = LotoCard.create_card(self)
        # self.pop_number = PlayLoto.get_number(self)

    def __str__(self):
        player_card = '\n'.join([''.join(['%s\t' % i for i in line]) for line in self.player])
        computer_card = '\n'.join([''.join(['%s\t' % i for i in line]) for line in self.computer])
        return f'Ваша карта\n' \
               f'------------------------------------\n{player_card}\n------------------------------------\n' \
               f'\nКарта компьютера\n' \
               f'------------------------------------\n{computer_card}\n------------------------------------\n'

    def _get_number(self):
        random.shuffle(self.loto_range)
        self.pop_number = self.loto_range.pop()
        # return pop_number

    def _cross_number(self):
        for num, line in enumerate(self.player):
            try:
                num_match = line.index(self.pop_number)
                self.player[num][num_match] = '--'
            except Exception:
                pass

    def _computer_move(self):
        for num, line in enumerate(self.computer):
            try:
                num_match = line.index(self.pop_number)
                self.computer[num][num_match] = '--'
            except Exception:
                pass

    def play_game(self):
        while len(self.loto_range) > 0:
            print(self)
            print('Достаём бочонок из мешка:')
            time.sleep(1)
            PlayLoto._get_number(self)
            print(f'({self.pop_number})')
            player_move = input('Вы хотите зачеркнуть этот номер? y/n ')
            if player_move == 'y':
                if (self.pop_number in list(chain(*self.player))) == True:
                    PlayLoto._cross_number(self)
                else:
                    print('Вы проиграли. Такого номера в вашей карточке нет.')
                    break
            else:
                if (self.pop_number in list(chain(*self.player))) == True:
                    print('Вы проиграли. Этот номер есть в вашей карточке. Теперь заполнить её не получится.')
                    break
            PlayLoto._computer_move(self)

            if list(chain(*self.player)).count('--') == 15:
                print('Вы победили!')
                break
            elif list(chain(*self.computer)).count('--') == 15:
                print('Вы проиграли.')
                break
            print(f'\nВ мешке осталось {len(self.loto_range)} бочонков\n')
            # time.sleep(1)


loto = PlayLoto()
loto.play_game()
