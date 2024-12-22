import streamlit as st
from game import Game
from human_player import HumanPlayer
from min_max_player import Min_max_Player
from Goal_player import GoalPlayer
from utility_player import UtilityPlayer

# Initialize session state variables
if 'game' not in st.session_state:
    st.session_state.game = None
if 'current_player' not in st.session_state:
    st.session_state.current_player = None
if 'board_state' not in st.session_state:
    st.session_state.board_state = ['-'] * 9
if 'message' not in st.session_state:
    st.session_state.message = "Welcome to Tic-Tac-Toe!"
if 'player1_type' not in st.session_state:
    st.session_state.player1_type = 'Human'
if 'player2_type' not in st.session_state:
    st.session_state.player2_type = 'AI'
if 'player1_difficulty' not in st.session_state:
    st.session_state.player1_difficulty = 'Easy'
if 'player2_difficulty' not in st.session_state:
    st.session_state.player2_difficulty = 'Easy'
if 'game_over' not in st.session_state:
    st.session_state.game_over = False

# Function to map difficulty level to AI player class
def get_ai_player(player_number, difficulty):
    if difficulty == 'Easy':
        return GoalPlayer(player_number)
    elif difficulty == 'Medium':
        return UtilityPlayer(player_number)
    elif difficulty == 'Hard':
        return Min_max_Player(player_number)
    else:
        raise ValueError("Invalid difficulty level")

# Function to start a new game
def start_game():
    player1_type = st.session_state.player1_type
    player2_type = st.session_state.player2_type
    player1_difficulty = st.session_state.player1_difficulty
    player2_difficulty = st.session_state.player2_difficulty

    player1 = HumanPlayer(1) if player1_type == 'Human' else get_ai_player(1, player1_difficulty)
    player2 = HumanPlayer(2) if player2_type == 'Human' else get_ai_player(2, player2_difficulty)
    st.session_state.game = Game(player1, player2)
    st.session_state.current_player = player1
    st.session_state.board_state = ['-'] * 9
    st.session_state.message = f"Player {st.session_state.current_player.number}'s turn."
    st.session_state.game_over = False

    # If the starting player is AI, make its move
    if isinstance(st.session_state.current_player, (GoalPlayer, UtilityPlayer, Min_max_Player)):
        ai_move()

# Function to handle a player's move
def make_move(position):
    if (
        st.session_state.board_state[position] == '-' 
        and st.session_state.game 
        and not st.session_state.game_over
    ):
        current_player = st.session_state.current_player
        st.session_state.game.board.mark_space(position, current_player.mark)
        st.session_state.board_state[position] = current_player.mark

        if st.session_state.game.board.has_win(current_player.mark):
            st.session_state.message = f"🎉 Congratulations! Player {current_player.number} ({current_player.mark}) wins! 🎉"
            st.session_state.game_over = True
        elif st.session_state.game.board.is_full():
            st.session_state.message = "🤝 It's a draw! 🤝"
            st.session_state.game_over = True
        else:
            # Switch players
            st.session_state.current_player = (
                st.session_state.game.player2
                if st.session_state.current_player == st.session_state.game.player1
                else st.session_state.game.player1
            )
            st.session_state.message = f"Player {st.session_state.current_player.number}'s turn."

            # If the next player is AI, make its move
            if isinstance(st.session_state.current_player, (GoalPlayer, UtilityPlayer, Min_max_Player)):
                ai_move()

# Function to handle AI moves
def ai_move():
    if (
        st.session_state.game 
        and isinstance(st.session_state.current_player, (GoalPlayer, UtilityPlayer, Min_max_Player)) 
        and not st.session_state.game_over
    ):
        move = st.session_state.current_player.get_next_move(st.session_state.game.board)
        make_move(move)

# Streamlit UI
st.title("Tic-Tac-Toe")

# Determine which UI to display based on the game state
if st.session_state.game is None and not st.session_state.game_over:
    # Game setup UI
    st.subheader("Start a New Game")
    st.session_state.player1_type = st.selectbox(
        "Select Player 1 Type", 
        ['Human', 'AI'], 
        index=['Human', 'AI'].index(st.session_state.player1_type)
    )
    if st.session_state.player1_type == 'AI':
        st.session_state.player1_difficulty = st.selectbox(
            "Select Player 1 Difficulty", 
            ['Easy', 'Medium', 'Hard'], 
            index=['Easy', 'Medium', 'Hard'].index(st.session_state.player1_difficulty)
        )

    st.session_state.player2_type = st.selectbox(
        "Select Player 2 Type", 
        ['Human', 'AI'], 
        index=['Human', 'AI'].index(st.session_state.player2_type)
    )
    if st.session_state.player2_type == 'AI':
        st.session_state.player2_difficulty = st.selectbox(
            "Select Player 2 Difficulty", 
            ['Easy', 'Medium', 'Hard'], 
            index=['Easy', 'Medium', 'Hard'].index(st.session_state.player2_difficulty)
        )

    if st.button("Start Game"):
        start_game()

elif st.session_state.game_over:
    # Game over UI
    st.subheader(st.session_state.message)
    if st.button("Play Again"):
        st.session_state.game = None
        st.session_state.game_over = False
        st.session_state.message = "Welcome to Tic-Tac-Toe!"
        st.session_state.board_state = ['-'] * 9

else:
    # Active game UI
    st.subheader(st.session_state.message)
    cols = st.columns(3)
    for i in range(3):
        for j in range(3):
            position = 3 * i + j
            if st.session_state.board_state[position] == '-':
                cols[j].button(" ", key=position, on_click=make_move, args=(position,))
            else:
                cols[j].button(st.session_state.board_state[position], key=position, disabled=True)

    # Optionally, provide a reset button during an active game
    if st.button("Reset Game"):
        st.session_state.game = None
        st.session_state.game_over = False
        st.session_state.message = "Welcome to Tic-Tac-Toe!"
        st.session_state.board_state = ['-'] * 9

