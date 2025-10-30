import random

def play(board: list[str]) -> int:
    """
    Implements a simple rule-based Tic-Tac-Toe AI.
    Strategy hierarchy: Win, Block, Center, Corner, Side.

    Args:
        board: A list of 9 strings ('', 'x', or 'o') representing the state.

    Returns:
        The index (0-8) of the calculated optimal move.
    """
    x_count = board.count('x')
    o_count = board.count('o')

    if x_count == o_count:
        # X always starts, so if counts are equal, it's X's turn
        marker = 'x'
        opponent_marker = 'o'
    else:
        marker = 'o'
        opponent_marker = 'x'

    WINNING_LINES = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    def check_for_move(player_marker: str) -> int | None:
        """Returns the index if the specified player can complete a line."""
        for line in WINNING_LINES:
            line_values = [board[i] for i in line]
            player_spots = line_values.count(player_marker)
            empty_spots = line_values.count('')

            if player_spots == 2 and empty_spots == 1:
                for index in line:
                    if board[index] == '':
                        return index
        return None

    # 1. Win
    winning_move = check_for_move(marker)
    if winning_move is not None:
        return winning_move

    # 2. Block
    blocking_move = check_for_move(opponent_marker)
    if blocking_move is not None:
        return blocking_move

    # 3. Center
    CENTER = 4
    if board[CENTER] == '':
        return CENTER

    # 4. Corner
    CORNERS = [0, 2, 6, 8]
    available_corners = [i for i in CORNERS if board[i] == '']

    if available_corners:
        return random.choice(available_corners)

    # 5. Side
    SIDES = [1, 3, 5, 7]
    available_sides = [i for i in SIDES if board[i] == '']

    if available_sides:
        return random.choice(available_sides)

    return -1
