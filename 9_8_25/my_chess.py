import chess

def print_board_with_coords(board):
    board_str = str(board).split('\n')
    files = '  a b c d e f g h'
    print(files)  # Top files labels

    for rank in range(8):
        print(8 - rank, board_str[rank], 8 - rank)

    print(files)  # Bottom files labels


def main():
    board = chess.Board()
    print("Welcome to the text-based Chess game!")
    print_board_with_coords(board)

    while not board.is_game_over():
        move_input = input("Enter your move in algebraic notation (e.g., d4, Nf3, O-O): ")
        try:
            move = board.parse_san(move_input)
            board.push(move)
            print_board_with_coords(board)
        except ValueError:
            print("Invalid move! Please enter a valid algebraic notation move.")

    print("Game over!")
    print(f"Result: {board.result()}")


if __name__ == "__main__":
    main()
