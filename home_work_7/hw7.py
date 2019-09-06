import random
import sys
import time


class Caskets:
    def f(self):
        lst = [x for x in range(1, self.amount + 1)]
        random.shuffle(lst)
        for i, y in enumerate(lst):
            print('{:*^30}'.format('*'))
            print('Новый бочонок: {} (осталось {})'.format(y, self.amount - (i + 1)))
            yield y

    def __init__(self, amount):
        self.amount = amount
        self.gen = self.f()


class Loto:
    def __set_card(self):
        num = set()
        while len(num) < self.all_row * 5:
            num.add(random.randint(1, 91))
        cards = list(num)
        random.shuffle(cards)

        while len(cards) % self.all_row != 0:
            cards.append('None')
        self.all_row = int(len(cards) / self.all_row)
        cards = [cards[i: i + self.all_row] for i in range(0, len(cards), self.all_row)]

        for i in range(len(cards)):
            cards[i].sort()
        self.card_user = cards[:3]
        self.card_comp = cards[3:]

    def __init__(self, amount_card):
        row = 3
        self.all_row = row * amount_card
        self.__set_card()

    def get_card(self, card_player):
        print('{:-^25}'.format(self.name))
        print('{0[0]:>2} {0[1]:<10} {0[2]:<5} {0[3]} {0[4]} '.format(card_player[0]))
        print('{0[0]:>4} {0[1]:<6} {0[2]:<4} {0[3]:<4} {0[4]} '.format(card_player[1]))
        print('{0[0]} {0[1]:<5} {0[2]:<5} {0[3]:<5} {0[4]} '.format(card_player[2]))
        print('{:-^25}'.format('-'))

    def search(self, card_player, num_cask):
        for i, n in enumerate(card_player):
            if num_cask in n:
                card_player[i][n.index(num_cask)] = '-'
                self.score += 1
                if self.score == 15:
                    print('{} Победила!'.format(self.name))
                    sys.exit(1)
                return True
        return False


class Player(Loto):

    def __init__(self, name):
        self.name = name
        self.score = 0


def main():
    game = Loto(2)
    cask = Caskets(90)
    player1 = Player('Ваша карточка')
    player2 = Player('Карточка компьютера')

    while True:
        num_cask = next(cask.gen)
        player1.get_card(game.card_user)
        player2.get_card(game.card_comp)

        inp_user = input('Зачеркнуть цифру? (y/n)')
        if inp_user == 'y':
            if player1.search(game.card_user, num_cask):
                continue
            else:
                print('Game Over')
                sys.exit(1)
        if inp_user == 'n':
            if player1.search(game.card_user, num_cask):
                print('Game Over')
                sys.exit(1)
            elif player2.search(game.card_comp, num_cask):
                continue
        if inp_user != 'n' and inp_user != 'y':
            print('Введите y or n')
            time.sleep(1)
            continue


if __name__ == '__main__':
    main()
