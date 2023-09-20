puzzle = [[1,0,3,4,5,6,7,8,9],
          [1,2,3,4,5,6,7,8,9],
          [1,2,3,4,5,6,7,8,9],
          [1,2,3,4,5,6,7,8,9],
          [1,2,3,4,5,6,7,8,9],
          [1,2,3,4,5,6,7,8,9],
          [1,2,3,4,5,6,7,8,9],
          [1,2,3,4,5,6,7,8,9],
          [1,2,3,4,5,6,7,8,9]]


def display_sudoku(puzzle: list) -> None:
    for row_break, row in enumerate(puzzle):
        if row_break in [0, 3, 6]:
            print('-'*25)
        print(f'| {row[0]} {row[1]} {row[2]} | {row[3]} {row[4]} {row[5]} | {row[6]} {row[7]} {row[8]} |')
    print('-'*25)

display_sudoku(puzzle)