from tree import *
import random
import sys
from hashmap import HashMap
import os
import time
import datetime
os.system("cls")

positive_inifnity = float("infinity")
negative_infinity = float("-infinity")


def introduction():
    print()
    print("          OTHELLO / REVERSI")
    print()
    print("Discs can be placed only on the fields labeled as '$'\n")
    print("If you want to quit the game, just type in 'q'\n")


class GameTable:

    def __init__(self):
        self._game_table = [["*", "*", "*", "*", "*", "*", "*", "*"], ["*", "*", "*", "*", "*", "*", "*", "*"],
                            ["*", "*", "*", "*", "*", "*", "*", "*"], ["*", "*", "*", "W", "B", "*", "*", "*"],
                            ["*", "*", "*", "B", "W", "*", "*", "*"], ["*", "*", "*", "*", "*", "*", "*", "*"],
                            ["*", "*", "*", "*", "*", "*", "*", "*"], ["*", "*", "*", "*", "*", "*", "*", "*"]]

        self._row_length = 8
        self._column_length = 8
        self._pieces = []
        self._table_characters = []
        self._number_of_black_discs = 2
        self._number_of_white_discs = 2
        self._allowed_input_values = ['1', '2', '3', '4', '5', '6', '7', '8', 'q']
        self._white_pieces_coordinates = []
        self._black_pieces_coordinates = []
        self._white_blocked_pieces = []
        self._black_blocked_pieces = []
        self._number_of_player_mills = 7
        self._number_of_opponent_mills = 0
        self._map = HashMap(self._row_length * self._column_length)


    def fill_hashmap(self):
        self.fill_table_characters()
        map_key = 1
        for i in range(self._row_length * self._column_length):
            self._map.add(map_key, self._table_characters[i])
            map_key += 1

    def print_hashmap(self):
        for i in range(self._row_length * self._column_length):
            print(self._map[i])

    def fill_table_characters(self):
        for i in range(self._row_length):
            for j in range(self._column_length):
                self._table_characters.append(self._game_table[i][j])

    def get_field(self, x, y):
        if x not in range(0, self._row_length) or y not in range(0, self._column_length):
            print("Date koordinate ne postoje!")

        elif self._game_table[x][y] not in ("B", "W", "O"):
            print("Na ovim koordinatama se ne nalazi nikakvo polje!")

        else:
            return self._game_table[x][y]

    def set_field(self, x, y, value):
        if x not in range(0, self._row_length) or y not in range(0, self._column_length):
            print("Date koordinate ne postoje!")

        elif value not in ("B", "W", "O"):
            print("Uneli ste lose karakter. Unesite W, B ili O")

        elif self._game_table[x][y] not in ("B", "W", "O"):
            print("Na ovim koordinatama se ne nalazi nikakvo polje!")

        else:
            if value == "W":
                white_coordinate = "(" + str(x) + "," + " " + str(y) + ")"
                self._white_pieces_coordinates.append(white_coordinate)
            elif value == "B":
                black_coordinate = "(" + str(x) + "," + " " + str(y) + ")"
                self._black_pieces_coordinates.append(black_coordinate)
            self._game_table[x][y] = value

    def get_white_pieces_coordinates(self):
        return self._white_pieces_coordinates

    def get_black_pieces_coordinates(self):
        return self._black_pieces_coordinates

    def get_white_blocked_pieces(self):
        return self._white_blocked_pieces

    def get_black_blocked_pieces(self):
        return self._black_blocked_pieces

    def get_number_of_player_mills(self):
        return self._number_of_player_mills

    def set_number_of_player_mills(self, value):
        self._number_of_player_mills = value

    def get_number_of_opponent_mills(self):
        return self._number_of_opponent_mills

    def set_number_of_opponent_mills(self, value):
        self._number_of_opponent_mills = value

    def get_x_coordinate(self):
        return self._x_coordinate

    def get_y_coordinate(self):
        return self._y_coordinate

    def set_x_coordinate(self, value):
        self._x_coordinate = value

    def set_y_coordinate(self, value):
        self._y_coordinate = value

    def set_new_table(self, x_coordinate, y_coordinate, new_value):
        self._game_table[int(x_coordinate) - 1][int(y_coordinate) - 1] = new_value
        self.fill_hashmap()

    def iterate(self):
        for row in self._game_table:
            for element in row:
                if element in ("W", "B"):
                    self._pieces.append(element)
        return self._pieces

    def print_table(self):
        self.display_score()
        LINE = '  \u001b[32m +---+---+---+---+---+---+---+---+'
        print('    \u001b[34m 1   2   3   4   5   6   7   8')
        print(LINE)
        for i in range(self._row_length):
            print("\u001b[34m", i+1, end=' ')
            for j in range(self._column_length):
                if self._game_table[i][j] == 'W':
                    print('\u001b[32m| %s' % ("\u001b[37m" + self._game_table[i][j]), end=' ')
                elif self._game_table[i][j] == 'B':
                    print('\u001b[32m| %s' % ("\u001b[30;1m" + self._game_table[i][j]), end=' ')
                elif self._game_table[i][j] == '$':
                    print('\u001b[32m| %s' % ("\u001b[31;1m" + self._game_table[i][j]), end=' ')
                elif self._game_table[i][j] == 'x':
                    print('\u001b[32m| %s' % ("\u001b[35;1m" + self._game_table[i][j]), end=' ')
                else:
                    print('\u001b[32m| %s' % ("\u001b[32m" + self._game_table[i][j]), end=' ')
            print('|')
            print(LINE)

    def display_score(self):
        print("\n\u001b[30;1m BLACK: " + "\u001b[30;1m" + str(self._number_of_black_discs) + "                   " +
              "\u001b[37mWHITE: " + str(self._number_of_white_discs) +"\n")

    def get_input(self):
        return self._x_coordinate, self._y_coordinate

    def maximizing_player(self):
        return True

    def is_game_over(self):
        if self._number_of_black_discs == 0:
            print("\n\nGAME OVER! WHITE WINS!\n\n")
            sys.exit()
        if self._number_of_white_discs == 0:
            print("\n\nGAME OVER! BLACK WINS!\n\n")
            sys.exit()
        if self._number_of_black_discs + self._number_of_white_discs == 64:
            if self._number_of_black_discs > self._number_of_white_discs:
                print("\n\nGAME OVER! BLACK WINS!\n\n")
                sys.exit()
            elif self._number_of_white_discs > self._number_of_black_discs:
                print("\n\nGAME OVER! WHITE WINS!\n\n")
                sys.exit()
            else:
                print("\n\nGAME OVER! IT'S A DRAW!\n\n")
                sys.exit()

    def import_input_coordinations(self):

        x_coord = input("\nType in row number: ")
        if x_coord == 'q':
            sys.exit()

        while x_coord not in self._allowed_input_values:
            print("Invalid input. Type in 1-8.")
            x_coord = input("\nType in row number: ")
            if x_coord == 'q':
                sys.exit()

        y_coord = input("\nType in column number: ")
        if y_coord == 'q':
            sys.exit()

        while y_coord not in self._allowed_input_values:
            print("Invalid input. Type in 1-8.")
            y_coord = input("\nType in column number: ")
            if y_coord == 'q':
                sys.exit()

        return x_coord, y_coord

    def check_input_coordinations(self, player_color):

        x_coord, y_coord = self.import_input_coordinations()

        while self._game_table[int(x_coord) - 1][int(y_coord) - 1] != '*' and self._game_table[int(x_coord) - 1][int(y_coord) - 1] != '$' and self._game_table[int(x_coord) - 1][int(y_coord) - 1] != 'x':
            print("There already exist a disc. Try with other positions.\n")
            x_coord, y_coord = self.import_input_coordinations()

        while player_color == 'black' and self._game_table[int(x_coord) - 1][int(y_coord) - 1] != '$':
            print("Not a valid move. You can only move to '$' positions.\n")
            x_coord, y_coord = self.import_input_coordinations()

        if player_color == 'black':
            self.set_new_table(x_coord, y_coord, 'B')

        #elif player_color == 'white':
            #self.set_new_table(x_coord, y_coord, 'W')

        # if player_color == 'white':
        #     allowed_white_moves = self.mark_allowed_fields_white()
        #     [result_x_coord, result_y_coord, max_changed_discs] = self.minimax(allowed_white_moves)
        #     self.set_new_table(result_x_coord, result_y_coord, 'W')
        self.mark_allowed_fields(True)

    def minimax(self, allowed_white_moves):
        max_changed_discs_move = [0, 0, -1]                      #potez koji bi doneo maksimalni broj "pojedenih" diskova (x, y, max_changed_discs)
        for move in allowed_white_moves:
            x_coord = move[0]
            y_coord = move[1]
            num_of_changed_discs = move[2]
            if num_of_changed_discs > max_changed_discs_move[2]:
                max_changed_discs_move[0] = x_coord
                max_changed_discs_move[1] = y_coord
                max_changed_discs_move[2] = num_of_changed_discs

        return max_changed_discs_move


    def player_turn(self):
        print("\nBlack turn.\n")
        self.check_input_coordinations('black')
        self.refresh_score()
        self.print_table()

    def bot_turn(self):
        print("\nWhite turn.\n")
        allowed_white_moves = self.mark_allowed_fields_white()
        [result_x_coord, result_y_coord, max_changed_discs] = self.minimax(allowed_white_moves)
        self.set_new_table(result_x_coord, result_y_coord, 'W')
        self.change_discs_white()
        self.mark_allowed_fields(False)
        self.refresh_score()
        self.print_table()

    def refresh_score(self):
        self._number_of_white_discs, self._number_of_black_discs = 0, 0

        for i in range(self._row_length):
            for j in range(self._column_length):
                if self._game_table[i][j] == 'B':
                    self._number_of_black_discs += 1
                elif self._game_table[i][j] == 'W':
                    self._number_of_white_discs += 1

    def change_disc_color(self, x_to_be_changed, y_to_be_changed):
        for i in range(self._row_length):
            for j in range(self._column_length):
                for k in range(len(x_to_be_changed)):
                    if i == x_to_be_changed[k] and j == y_to_be_changed[k]:
                        if self._game_table[i][j] == 'B':
                            self._game_table[i][j] = 'W'
                        else:
                            self._game_table[i][j] = 'B'
                        if self._game_table[i+1][j] == '$':
                            self._game_table[i+1][j] = '*'
                        if self._game_table[i][j+1] == '$':
                            self._game_table[i][j+1] = '*'
                        if self._game_table[i-1][j] == '$':
                            self._game_table[i-1][j] = '*'
                        if self._game_table[i][j-1] == '$':
                            self._game_table[i][j-1] = '*'
                        if self._game_table[i+1][j+1] == '$':
                            self._game_table[i+1][j+1] = '*'
                        if self._game_table[i-1][j-1] == '$':
                            self._game_table[i-1][j-1] = '*'
                        if self._game_table[i+1][j-1] == '$':
                            self._game_table[i+1][j-1] = '*'
                        if self._game_table[i-1][j+1] == '$':
                            self._game_table[i-1][j+1] = '*'

    def change_discs_white(self):
        for i in range(self._row_length):
            for j in range(self._column_length):
                if self._game_table[i][j] == 'W':
                    north_x, north_y, num_of_changed_discs = self.iterate_north_white(i, j, True)             #prvo pokusava da iterira u jednom smeru, pa ako ne nadje
                                                                                                                # disk za promenu ide dalje sve dok ne prodje kroz sve pravce

                    south_x, south_y, num_of_changed_discs = self.iterate_south_white(i, j, True)

                    east_x, east_y, num_of_changed_discs = self.iterate_east_white(i, j, True)

                    west_x, west_y, num_of_changed_discs = self.iterate_west_white(i, j, True)

                    south_east_x, south_east_y, num_of_changed_discs = self.iterate_south_east_white(i, j, True)

                    south_west_x, south_west_y, num_of_changed_discs = self.iterate_south_west_white(i, j, True)

                    north_west_x, north_west_y, num_of_changed_discs = self.iterate_north_west_white(i, j, True)

                    north_east_x, north_east_y, num_of_changed_discs = self.iterate_north_east_white(i, j, True)

    def mark_allowed_fields(self, is_disc_changing):      #strane sveta sam izabrao kako bih napravio jednostavnu
                                                                    # analogiju za iteraciju u 8 pravaca
                                                                    #svaka crna figura moze da se krece samo u tim osama,
                                                                    #i cilj nam je da iteriramo
                                                                    #kroz te ose da bi videli ima li usput nekih belih figura

        for i in range(self._row_length):
            for j in range(self._column_length):
                if self._game_table[i][j] == 'B':
                    north_x, north_y = self.iterate_north(i, j, is_disc_changing)

                    if north_x != None and north_y != None and self._game_table[north_x][north_y] != 'B':

                        self._game_table[north_x][north_y] = '$'

                    south_x, south_y = self.iterate_south(i, j, is_disc_changing)

                    if south_x != None and south_y != None and self._game_table[south_x][south_y] != 'B':

                        self._game_table[south_x][south_y] = '$'

                    east_x, east_y = self.iterate_east(i, j, is_disc_changing)

                    if east_x != None and east_y != None and self._game_table[east_x][east_y] != 'B':
                        self._game_table[east_x][east_y] = '$'

                    west_x, west_y = self.iterate_west(i, j, is_disc_changing)

                    if west_x != None and west_y != None and self._game_table[west_x][west_y] != 'B':
                        self._game_table[west_x][west_y] = '$'

                    south_east_x, south_east_y = self.iterate_south_east(i, j, is_disc_changing)

                    if south_east_x != None and south_east_y != None and self._game_table[south_east_x][south_east_y] != 'B':
                        self._game_table[south_east_x][south_east_y] = '$'

                    south_west_x, south_west_y = self.iterate_south_west(i, j, is_disc_changing)

                    if south_west_x != None and south_west_y != None and self._game_table[south_west_x][
                        south_west_y] != 'B':
                        self._game_table[south_west_x][south_west_y] = '$'

                    north_west_x, north_west_y = self.iterate_north_west(i, j, is_disc_changing)

                    if north_west_x != None and north_west_y != None and self._game_table[north_west_x][
                        north_west_y] != 'B':
                        self._game_table[north_west_x][north_west_y] = '$'

                    north_east_x, north_east_y = self.iterate_north_east(i, j, is_disc_changing)

                    if north_east_x != None and north_east_y != None and self._game_table[north_east_x][
                        north_east_y] != 'B':
                        self._game_table[north_east_x][north_east_y] = '$'

    def mark_allowed_fields_white(self):

        allowed_white_moves = []        # sluzi za cuvanje mogucih poteza od strane bota

        for i in range(self._row_length):
            for j in range(self._column_length):
                if self._game_table[i][j] == 'W':
                    north_x, north_y, num_of_changed_discs = self.iterate_north_white(i, j, False)

                    if north_x != None and north_y != None and self._game_table[north_x][north_y] != 'W':
                        allowed_white_moves.append([north_x + 1, north_y + 1, num_of_changed_discs])

                    south_x, south_y, num_of_changed_discs = self.iterate_south_white(i, j, False)

                    if south_x != None and south_y != None and self._game_table[south_x][south_y] != 'W':
                        allowed_white_moves.append([south_x + 1, south_y + 1, num_of_changed_discs])

                    east_x, east_y, num_of_changed_discs = self.iterate_east_white(i, j, False)

                    if east_x != None and east_y != None and self._game_table[east_x][east_y] != 'W':
                        allowed_white_moves.append([east_x + 1, east_y + 1, num_of_changed_discs])    #staviti kao povratnu vrednost i broj figura koje ce promeniti boju

                    west_x, west_y, num_of_changed_discs = self.iterate_west_white(i, j, False)

                    if west_x != None and west_y != None and self._game_table[west_x][west_y] != 'W':
                        allowed_white_moves.append([west_x + 1, west_y + 1, num_of_changed_discs])

                    south_east_x, south_east_y, num_of_changed_discs = self.iterate_south_east_white(i, j, False)

                    if south_east_x != None and south_east_y != None and self._game_table[south_east_x][south_east_y] != 'W':
                        allowed_white_moves.append([south_east_x + 1, south_east_y + 1, num_of_changed_discs])

                    south_west_x, south_west_y, num_of_changed_discs = self.iterate_south_west_white(i, j, False)

                    if south_west_x != None and south_west_y != None and self._game_table[south_west_x][south_west_y] != 'W':
                        allowed_white_moves.append([south_west_x + 1, south_west_y + 1, num_of_changed_discs])

                    north_west_x, north_west_y, num_of_changed_discs = self.iterate_north_west_white(i, j, False)

                    if north_west_x != None and north_west_y != None and self._game_table[north_west_x][north_west_y] != 'W':
                        allowed_white_moves.append([north_west_x + 1, north_west_y + 1, num_of_changed_discs])

                    north_east_x, north_east_y, num_of_changed_discs = self.iterate_north_east_white(i, j, False)

                    if north_east_x != None and north_east_y != None and self._game_table[north_east_x][north_east_y] != 'W':
                        allowed_white_moves.append([north_east_x + 1, north_east_y + 1, num_of_changed_discs])

        return allowed_white_moves

    def iterate_north(self, disc_x_coord, disc_y_coord, is_disc_changing):
        x_to_be_changed = []            # lista mogucih x koordinata za promenu boja diska (kada crni okruze beli disk, on menja boju)
        y_to_be_changed = []            # lista mogucih y koordinata za promenu boja diska
        target_x_coord = None
        if disc_x_coord != 0:
            if self._game_table[disc_x_coord - 1][disc_y_coord] == 'W':
                for i in reversed(range(disc_x_coord)):
                    if self._game_table[i][disc_y_coord] == 'W':

                        while self._game_table[i][disc_y_coord] == 'W':
                            x_to_be_changed.append(i)
                            y_to_be_changed.append(disc_y_coord)
                            if i > 0:
                                i -= 1
                            else:
                                break
                        if i < 0:
                            target_x_coord = None
                        else:
                            target_x_coord = i

                        if self._game_table[i][disc_y_coord] == 'B':
                            if is_disc_changing:
                                self.change_disc_color(x_to_be_changed, y_to_be_changed)

        return target_x_coord, disc_y_coord

    def iterate_north_white(self, disc_x_coord, disc_y_coord, is_disc_changing):
        num_of_changed_discs = 0
        x_to_be_changed = []  # lista mogucih x koordinata za promenu boja diska (kada crni okruze beli disk, on menja boju)
        y_to_be_changed = []  # lista mogucih y koordinata za promenu boja diska
        target_x_coord = None
        if disc_x_coord != 0:
            if self._game_table[disc_x_coord - 1][disc_y_coord] == 'B':
                for i in reversed(range(disc_x_coord)):
                    if self._game_table[i][disc_y_coord] == 'B':

                        while self._game_table[i][disc_y_coord] == 'B':
                            x_to_be_changed.append(i)
                            y_to_be_changed.append(disc_y_coord)
                            if i > 0:
                                i -= 1
                            else:
                                break
                        if i < 0:
                            target_x_coord = None
                        else:
                            target_x_coord = i

                        if self._game_table[i][disc_y_coord] == 'W':
                            if not is_disc_changing:
                                num_of_changed_discs += 1
                            else:
                                self.change_disc_color(x_to_be_changed, y_to_be_changed)

        return target_x_coord, disc_y_coord, num_of_changed_discs

    def iterate_south(self, disc_x_coord, disc_y_coord, is_disc_changing):
        target_x_coord = None
        x_to_be_changed = []        #lista mogucih x koordinata za promenu boja diska (kada crni okruze beli disk, on menja boju)
        y_to_be_changed = []        #lista mogucih y koordinata za promenu boja diska
        if disc_x_coord != 7:
            if self._game_table[disc_x_coord + 1][disc_y_coord] == 'W':
                for i in range(disc_x_coord, self._row_length):
                    if self._game_table[i][disc_y_coord] == 'W':
                        while self._game_table[i][disc_y_coord] == 'W':
                            x_to_be_changed.append(i)
                            y_to_be_changed.append(disc_y_coord)
                            if i < 7:
                                i += 1
                            else:
                                break
                        if i > 7:
                            target_x_coord = None
                        else:
                            target_x_coord = i

                        if self._game_table[i][disc_y_coord] == 'B':
                            if is_disc_changing:
                                self.change_disc_color(x_to_be_changed, y_to_be_changed)

        return target_x_coord, disc_y_coord

    def iterate_south_white(self, disc_x_coord, disc_y_coord, is_disc_changing):
        num_of_changed_discs = 0
        target_x_coord = None
        x_to_be_changed = []        #lista mogucih x koordinata za promenu boja diska (kada crni okruze beli disk, on menja boju)
        y_to_be_changed = []        #lista mogucih y koordinata za promenu boja diska
        if disc_x_coord != 7:
            if self._game_table[disc_x_coord + 1][disc_y_coord] == 'B':
                for i in range(disc_x_coord, self._row_length):
                    if self._game_table[i][disc_y_coord] == 'B':
                        while self._game_table[i][disc_y_coord] == 'B':
                            x_to_be_changed.append(i)
                            y_to_be_changed.append(disc_y_coord)
                            if i < 7:
                                i += 1
                            else:
                                break
                        if i > 7:
                            target_x_coord = None
                        else:
                            target_x_coord = i

                        if self._game_table[i][disc_y_coord] == 'W':
                            if not is_disc_changing:
                                num_of_changed_discs += 1
                            else:
                                self.change_disc_color(x_to_be_changed, y_to_be_changed)

        return target_x_coord, disc_y_coord, num_of_changed_discs

    def iterate_east(self, disc_x_coord, disc_y_coord, is_disc_changing):
        target_y_coord = None
        x_to_be_changed = []
        y_to_be_changed = []
        if disc_y_coord != 7:
            if self._game_table[disc_x_coord][disc_y_coord + 1] == 'W':
                for j in range(disc_y_coord, self._column_length):
                    if self._game_table[disc_x_coord][j] == 'W':
                        while self._game_table[disc_x_coord][j] == 'W':
                            x_to_be_changed.append(disc_x_coord)
                            y_to_be_changed.append(j)
                            if j < 7:
                                j += 1
                            else:
                                break
                            if j > 7:
                                target_y_coord = None
                                return disc_x_coord, target_y_coord
                            else:
                                target_y_coord = j

                        if self._game_table[disc_x_coord][j] == 'B':
                            if is_disc_changing:
                                self.change_disc_color(x_to_be_changed, y_to_be_changed)

        return disc_x_coord, target_y_coord

    def iterate_east_white(self, disc_x_coord, disc_y_coord, is_disc_changing):
        num_of_changed_discs = 0
        target_y_coord = None
        x_to_be_changed = []
        y_to_be_changed = []
        if disc_y_coord != 7:
            if self._game_table[disc_x_coord][disc_y_coord + 1] == 'B':
                for j in range(disc_y_coord, self._column_length):
                    if self._game_table[disc_x_coord][j] == 'B':
                        while self._game_table[disc_x_coord][j] == 'B':
                            x_to_be_changed.append(disc_x_coord)
                            y_to_be_changed.append(j)
                            if j < 7:
                                j += 1
                            else:
                                break
                            if j > 7:
                                target_y_coord = None
                                return disc_x_coord, target_y_coord
                            else:
                                target_y_coord = j

                        if self._game_table[disc_x_coord][j] == 'W':
                            if not is_disc_changing:
                                num_of_changed_discs += 1
                            else:
                                self.change_disc_color(x_to_be_changed, y_to_be_changed)

        return disc_x_coord, target_y_coord, num_of_changed_discs

    def iterate_west(self, disc_x_coord, disc_y_coord, is_disc_changing):
        target_y_coord = None
        x_to_be_changed = []
        y_to_be_changed = []
        if disc_y_coord != 0:
            if self._game_table[disc_x_coord][disc_y_coord - 1] == 'W':
                for j in reversed(range(disc_y_coord)):
                    if self._game_table[disc_x_coord][j] == 'W':
                        while self._game_table[disc_x_coord][j] == 'W':
                            x_to_be_changed.append(disc_x_coord)
                            y_to_be_changed.append(j)
                            if j > 0:
                                j -= 1
                            else:
                                break
                        if j < 0:
                            target_y_coord = None
                        else:
                            target_y_coord = j

                        if self._game_table[disc_x_coord][j] == 'B':
                            if is_disc_changing:
                                self.change_disc_color(x_to_be_changed, y_to_be_changed)

        return disc_x_coord, target_y_coord

    def iterate_west_white(self, disc_x_coord, disc_y_coord, is_disc_changing):
        num_of_changed_discs = 0
        target_y_coord = None
        x_to_be_changed = []
        y_to_be_changed = []
        if disc_y_coord != 0:
            if self._game_table[disc_x_coord][disc_y_coord - 1] == 'B':
                for j in reversed(range(disc_y_coord)):
                    if self._game_table[disc_x_coord][j] == 'B':
                        while self._game_table[disc_x_coord][j] == 'B':
                            x_to_be_changed.append(disc_x_coord)
                            y_to_be_changed.append(j)
                            if j > 0:
                                j -= 1
                            else:
                                break
                        if j < 0:
                            target_y_coord = None
                        else:
                            target_y_coord = j

                        if self._game_table[disc_x_coord][j] == 'W':
                            if not is_disc_changing:
                                num_of_changed_discs += 1
                            else:
                                self.change_disc_color(x_to_be_changed, y_to_be_changed)

        return disc_x_coord, target_y_coord, num_of_changed_discs

    def iterate_south_east(self, disc_x_coord, disc_y_coord, is_disc_changing):
        x_to_be_changed = []
        y_to_be_changed = []
        target_x_coord = None
        target_y_coord = None
        if disc_x_coord != 7 and disc_y_coord != 7:
            if self._game_table[disc_x_coord + 1][disc_y_coord + 1] == 'W':
                if disc_x_coord < 7 and disc_y_coord < 7:
                    disc_x_coord += 1
                    disc_y_coord += 1
                while self._game_table[disc_x_coord][disc_y_coord] == 'W':
                    x_to_be_changed.append(disc_x_coord)
                    y_to_be_changed.append(disc_y_coord)
                    if disc_x_coord < 7 and disc_y_coord < 7:
                        disc_x_coord += 1
                        disc_y_coord += 1
                    else:
                        break
                if disc_x_coord > 7 or disc_y_coord > 7:
                    target_x_coord = None
                    target_y_coord = None
                else:
                    target_x_coord = disc_x_coord
                    target_y_coord = disc_y_coord
                if self._game_table[disc_x_coord][disc_y_coord] == 'B':
                    if is_disc_changing:
                        self.change_disc_color(x_to_be_changed, y_to_be_changed)

        return target_x_coord, target_y_coord

    def iterate_south_east_white(self, disc_x_coord, disc_y_coord, is_disc_changing):
        num_of_changed_discs = 0
        x_to_be_changed = []
        y_to_be_changed = []
        target_x_coord = None
        target_y_coord = None
        if disc_x_coord != 7 and disc_y_coord != 7:
            if self._game_table[disc_x_coord + 1][disc_y_coord + 1] == 'B':
                if disc_x_coord < 7 and disc_y_coord < 7:
                    disc_x_coord += 1
                    disc_y_coord += 1
                while self._game_table[disc_x_coord][disc_y_coord] == 'B':
                    x_to_be_changed.append(disc_x_coord)
                    y_to_be_changed.append(disc_y_coord)
                    if disc_x_coord < 7 and disc_y_coord < 7:
                        disc_x_coord += 1
                        disc_y_coord += 1
                    else:
                        break
                if disc_x_coord > 7 or disc_y_coord > 7:
                    target_x_coord = None
                    target_y_coord = None
                else:
                    target_x_coord = disc_x_coord
                    target_y_coord = disc_y_coord
                if self._game_table[disc_x_coord][disc_y_coord] == 'W':
                    if not is_disc_changing:
                        num_of_changed_discs += 1
                    else:
                        self.change_disc_color(x_to_be_changed, y_to_be_changed)

        return target_x_coord, target_y_coord, num_of_changed_discs

    def iterate_north_east(self, disc_x_coord, disc_y_coord, is_disc_changing):
        x_to_be_changed = []
        y_to_be_changed = []
        target_x_coord = None
        target_y_coord = None
        if disc_x_coord != 0 and disc_y_coord != 7:
            if self._game_table[disc_x_coord - 1][disc_y_coord + 1] == 'W':
                if disc_x_coord > 0 and disc_y_coord < 7:
                    disc_x_coord -= 1
                    disc_y_coord += 1
                while self._game_table[disc_x_coord][disc_y_coord] == 'W':
                    x_to_be_changed.append(disc_x_coord)
                    y_to_be_changed.append(disc_y_coord)
                    if disc_x_coord > 0 and disc_y_coord < 7:
                        disc_x_coord -= 1
                        disc_y_coord += 1
                    else:
                        break
                if disc_x_coord < 0 or disc_y_coord > 7:
                    target_x_coord = None
                    target_y_coord = None
                else:
                    target_x_coord = disc_x_coord
                    target_y_coord = disc_y_coord
                if self._game_table[disc_x_coord][disc_y_coord] == 'B':
                    if is_disc_changing:
                        self.change_disc_color(x_to_be_changed, y_to_be_changed)

        return target_x_coord, target_y_coord

    def iterate_north_east_white(self, disc_x_coord, disc_y_coord, is_disc_changing):
        num_of_changed_discs = 0
        x_to_be_changed = []
        y_to_be_changed = []
        target_x_coord = None
        target_y_coord = None
        if disc_x_coord != 0 and disc_y_coord != 7:
            if self._game_table[disc_x_coord - 1][disc_y_coord + 1] == 'B':
                if disc_x_coord > 0 and disc_y_coord < 7:
                    disc_x_coord -= 1
                    disc_y_coord += 1
                while self._game_table[disc_x_coord][disc_y_coord] == 'B':
                    x_to_be_changed.append(disc_x_coord)
                    y_to_be_changed.append(disc_y_coord)
                    if disc_x_coord > 0 and disc_y_coord < 7:
                        disc_x_coord -= 1
                        disc_y_coord += 1
                    else:
                        break
                if disc_x_coord < 0 or disc_y_coord > 7:
                    target_x_coord = None
                    target_y_coord = None
                else:
                    target_x_coord = disc_x_coord
                    target_y_coord = disc_y_coord
                if self._game_table[disc_x_coord][disc_y_coord] == 'W':
                    if not is_disc_changing:
                        num_of_changed_discs += 1
                    else:
                        self.change_disc_color(x_to_be_changed, y_to_be_changed)

        return target_x_coord, target_y_coord, num_of_changed_discs

    def iterate_north_west(self, disc_x_coord, disc_y_coord, is_disc_changing):
        x_to_be_changed = []
        y_to_be_changed = []
        target_x_coord = None
        target_y_coord = None
        if disc_x_coord != 0 and disc_y_coord != 0:
            if self._game_table[disc_x_coord - 1][disc_y_coord - 1] == 'W':
                if disc_x_coord > 0 and disc_y_coord > 0:
                    disc_x_coord -= 1
                    disc_y_coord -= 1
                while self._game_table[disc_x_coord][disc_y_coord] == 'W':
                    x_to_be_changed.append(disc_x_coord)
                    y_to_be_changed.append(disc_y_coord)
                    if disc_x_coord > 0 and disc_y_coord > 0:
                        disc_x_coord -= 1
                        disc_y_coord -= 1
                    else:
                        break
                if disc_x_coord < 0 or disc_y_coord < 0:
                    target_x_coord = None
                    target_y_coord = None
                else:
                    target_x_coord = disc_x_coord
                    target_y_coord = disc_y_coord
                if self._game_table[disc_x_coord][disc_y_coord] == 'B':
                    if is_disc_changing:
                        self.change_disc_color(x_to_be_changed, y_to_be_changed)

        return target_x_coord, target_y_coord

    def iterate_north_west_white(self, disc_x_coord, disc_y_coord, is_disc_changing):
        num_of_changed_discs = 0
        x_to_be_changed = []
        y_to_be_changed = []
        target_x_coord = None
        target_y_coord = None
        if disc_x_coord != 0 and disc_y_coord != 0:
            if self._game_table[disc_x_coord - 1][disc_y_coord - 1] == 'B':
                if disc_x_coord > 0 and disc_y_coord > 0:
                    disc_x_coord -= 1
                    disc_y_coord -= 1
                while self._game_table[disc_x_coord][disc_y_coord] == 'B':
                    x_to_be_changed.append(disc_x_coord)
                    y_to_be_changed.append(disc_y_coord)
                    if disc_x_coord > 0 and disc_y_coord > 0:
                        disc_x_coord -= 1
                        disc_y_coord -= 1
                    else:
                        break
                if disc_x_coord < 0 or disc_y_coord < 0:
                    target_x_coord = None
                    target_y_coord = None
                else:
                    target_x_coord = disc_x_coord
                    target_y_coord = disc_y_coord
                if self._game_table[disc_x_coord][disc_y_coord] == 'W':
                    if not is_disc_changing:
                        num_of_changed_discs += 1
                    else:
                        self.change_disc_color(x_to_be_changed, y_to_be_changed)

        return target_x_coord, target_y_coord, num_of_changed_discs

    def iterate_south_west(self, disc_x_coord, disc_y_coord, is_disc_changing):
        x_to_be_changed = []
        y_to_be_changed = []
        target_x_coord = None
        target_y_coord = None
        if disc_x_coord != 7 and disc_y_coord != 0:
            if self._game_table[disc_x_coord + 1][disc_y_coord - 1] == 'W':
                if disc_x_coord < 7 and disc_y_coord > 0:
                    disc_x_coord += 1
                    disc_y_coord -= 1
                while self._game_table[disc_x_coord][disc_y_coord] == 'W':
                    x_to_be_changed.append(disc_x_coord)
                    y_to_be_changed.append(disc_y_coord)
                    if disc_x_coord < 7 and disc_y_coord > 0:
                        disc_x_coord += 1
                        disc_y_coord -= 1
                    else:
                        break
                if disc_x_coord > 7 or disc_y_coord < 0:
                    target_x_coord = None
                    target_y_coord = None
                else:
                    target_x_coord = disc_x_coord
                    target_y_coord = disc_y_coord
                if self._game_table[disc_x_coord][disc_y_coord] == 'B':
                    if is_disc_changing:
                        self.change_disc_color(x_to_be_changed, y_to_be_changed)

        return target_x_coord, target_y_coord

    def iterate_south_west_white(self, disc_x_coord, disc_y_coord, is_disc_changing):
        num_of_changed_discs = 0
        x_to_be_changed = []
        y_to_be_changed = []
        target_x_coord = None
        target_y_coord = None
        if disc_x_coord != 7 and disc_y_coord != 0:
            if self._game_table[disc_x_coord + 1][disc_y_coord - 1] == 'B':
                if disc_x_coord < 7 and disc_y_coord > 0:
                    disc_x_coord += 1
                    disc_y_coord -= 1
                while self._game_table[disc_x_coord][disc_y_coord] == 'B':
                    x_to_be_changed.append(disc_x_coord)
                    y_to_be_changed.append(disc_y_coord)
                    if disc_x_coord < 7 and disc_y_coord > 0:
                        disc_x_coord += 1
                        disc_y_coord -= 1
                    else:
                        break
                if disc_x_coord > 7 or disc_y_coord < 0:
                    target_x_coord = None
                    target_y_coord = None
                else:
                    target_x_coord = disc_x_coord
                    target_y_coord = disc_y_coord
                if self._game_table[disc_x_coord][disc_y_coord] == 'W':
                    if not is_disc_changing:
                        num_of_changed_discs += 1
                    else:
                        self.change_disc_color(x_to_be_changed, y_to_be_changed)

        return target_x_coord, target_y_coord, num_of_changed_discs

    def delete_allowed_fields(self):
        for i in range(self._row_length):
            for j in range (self._column_length):
                if self._game_table[i][j] == '$':
                    self._game_table[i][j] = '*'

    def delete_allowed_fields_white(self):
        for i in range(self._row_length):
            for j in range (self._column_length):
                if self._game_table[i][j] == '$':
                    self._game_table[i][j] = 'x'


if __name__ == '__main__':
    introduction()
    g = GameTable()
    g.fill_hashmap()
    g.mark_allowed_fields(True)
    allowed_white_moves = g.mark_allowed_fields_white()
    g.print_table()

    while True:
        g.is_game_over()
        g.player_turn()
        g.delete_allowed_fields()
        g.is_game_over()
        time.sleep(1.5)
        start = datetime.datetime.now()
        g.bot_turn()
        end = datetime.datetime.now()
        print("Bot playing time: " + str(end - start))