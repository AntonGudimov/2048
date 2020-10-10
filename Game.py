import random as rnd
from GameState import GameState
from GameCell import GameCell


class Game:
    def __init__(self):
        self.__row_count = 4
        self.__col_count = 4
        self.__limit = 2048
        self.__state = GameState.NOT_PLAYING
        self.__score = 0
        self.__the_best_score = 0
        self.__field = list(list())
        self.__flag = False
        self.__is_won = False

    @property
    def row_count(self):
        return self.__row_count

    @property
    def col_count(self):
        return self.__col_count

    @property
    def state(self):
        return self.__state

    @property
    def field(self):
        return self.__field

    @property
    def score(self):
        return self.__score

    @property
    def the_best_score(self):
        return self.__the_best_score

    @state.setter
    def state(self, state):
        self.__state = state

    def new_game(self, row_count, col_count, limit, the_best_score):
        self.__row_count = row_count
        self.__col_count = col_count
        self.__limit = limit
        self.__the_best_score = the_best_score
        self.__state = GameState.PLAYING
        self.__is_won = False
        self.__field.clear()
        self.__score = 0
        self.__field = [[GameCell(0) for col in range(self.__col_count)]
                        for row in range(self.__row_count)]
        self.new_elements(2)

    def new_elements(self, limit):
        xy = list(list())
        if limit == 2:
            xy = [[row, col] for row in range(self.__row_count) for col in range(self.__col_count)]
        elif limit == 1:
            xy = self.checking()
        for i in range(limit):
            index = rnd.randrange(len(xy))
            array = list(range(11))
            if rnd.choice(array) <= 9:
                self.__field[xy[index][0]][xy[index][1]].value = 2
            else:
                self.__field[xy[index][0]][xy[index][1]].value = 4
            del xy[index]
        if (len(xy) == 0) and (not self.__is_won):
            self.is_failed()

    def checking(self):
        zero_cells = list()
        for row in range(self.__row_count):
            for col in range(self.__col_count):
                if (self.__field[row][col].value == self.__limit) and (not self.__is_won):
                    self.__state = GameState.WIN
                    self.__is_won = True
                elif self.__field[row][col].value == 0:
                    zero_cells.append([row, col])
        return zero_cells

    def moving(self, reverse_parameter, transposition_parameter):
        if transposition_parameter:
            self.__field = list(zip(*self.__field))
        if reverse_parameter:
            self.__field.reverse()
        for col in range(self.__col_count):
            pivot, row = 0, 1
            while row < self.__row_count:
                if self.__field[row][col].value == 0:
                    row += 1
                elif self.__field[pivot][col].value == 0:
                    self.__field[pivot][col].value = self.__field[row][col].value
                    self.__field[row][col].value = 0
                    row += 1
                    self.__flag = True
                elif self.__field[pivot][col].value == self.__field[row][col].value:
                    self.__field[pivot][col].value += self.__field[row][col].value
                    if self.__the_best_score == self.__score:
                        self.__the_best_score += self.__field[pivot][col].value
                    self.__score += self.__field[pivot][col].value
                    pivot += 1
                    self.__field[row][col].value = 0
                    row += 1
                    self.__flag = True
                    if self.__the_best_score < self.__score:
                        self.__the_best_score = self.__score
                else:
                    pivot += 1
                    if pivot == row:
                        row += 1
        if self.__flag:
            self.new_elements(1)
            self.__flag = False
        if reverse_parameter:
            self.__field.reverse()
        if transposition_parameter:
            self.__field = list(zip(*self.__field))

    def is_failed(self):
        local_flag = False
        for row in range(self.__row_count - 1):
            for col in range(self.__col_count):
                if self.__field[row][col].value == self.__field[row + 1][col].value:
                    local_flag = True
                    break
            if local_flag:
                break

        if not local_flag:
            for row in range(self.__row_count):
                for col in range(self.__col_count - 1):
                    if self.__field[row][col].value == self.__field[row][col + 1].value:
                        local_flag = True
                        break
                if local_flag:
                    break

            if not local_flag:
                self.__state = GameState.FAIL
