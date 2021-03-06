#!/usr/bin/env python
# -*- coding: utf-8 -*-

import curses


MAP = [
    '####  ####',
    '#  ####  #',
    '#        #',
    '##      ##',
    ' #      # ',
    ' #      # ',
    '##      ##',
    '#        #',
    '#  ####  #',
    '####  ####',
]
KEY_QUIT = ord('q')
DIRECTIONS = {
    curses.KEY_UP: (0, -1),
    curses.KEY_RIGHT: (1, 0),
    curses.KEY_DOWN: (0, 1),
    curses.KEY_LEFT: (-1, 0),
}


class BlockedMovement(Exception):
    pass


class Game(object):
    def __init__(self, screen):
        self.screen = screen
        self.x, self.y = 2, 2

    def move_player(self, (dx, dy)):
        x, y = self.x + dx, self.y + dy
        if MAP[y][x] != ' ':
            raise BlockedMovement()
        self.x, self.y = x, y

    def main(self):
        for row in MAP:
            self.screen.addstr(row + '\n')
        key = None
        while key != KEY_QUIT:
            self.screen.addstr(self.y, self.x, '@')
            key = self.screen.getch()
            try:
                direction = DIRECTIONS[key]
            except KeyError:
                pass
            else:
                self.screen.addstr(self.y, self.x, ' ')
                try:
                    self.move_player(direction)
                except BlockedMovement:
                    pass


if __name__ == '__main__':
    curses.wrapper(lambda screen: Game(screen).main())

