from flask import Flask, render_template, jsonify, request
from tic_tac_toe import TicTacToe

app = Flask(__name__)
game = TicTacToe()


@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def home():
    return render_template('homepage.html')

@app.route('/projects', methods=['GET'])
def projects():
    projects = [
        {
            'name': 'Tic Tac Toe with MinMax Algorithm',
            'description': 'Description of project 1',
            'link': '/game',
            'repo': '#',
            'image': 'static/images/education.png'
        },
        {
            'name': 'Wheelchair Control using BCI',
            'description': 'Description of project 2',
            'link': '#',
            'repo': '#',
            'image': 'path/to/image2.jpg'
        },
        {
            'name': 'Budget Tracking Android App',
            'description': 'Description of project 3',
            'link': '#',
            'repo': '#',
            'image': 'path/to/image3.jpg'
        }
        ,
        {
            'name': 'E-commerce Website',
            'description': 'Description of project 3',
            'link': '#',
            'repo': '#',
            'image': 'static/images/education.png'
        }
    ]
    return render_template('projects.html', projects=projects)

@app.route('/resume', methods=['GET'])
def resume():
    return render_template('resume.html')

@app.route('/game')
def index():
    return render_template('tic_tac_toe.html')

@app.route('/move', methods=['POST'])
def move():
    try:
        data = request.get_json()
        if data is None:
            raise ValueError('Invalid JSON data')
    except Exception as e:
        return jsonify({'error': str(e)}), 400

    row, col = int(data.get('row')), int(data.get('col'))
    if game.board[row][col] == ' ':
        game.board[row][col] = game.player
        winner = game.check_winner()
        if winner != 0:
            return jsonify({'winner': game.current_winner, 'board': game.board})

        if not game.is_move_left():
            return jsonify({'winner': 'Draw', 'board': game.board})

        game.player, game.opponent = game.opponent, game.player  # Switch players

        ai_move = game.play_game()
        game.board[ai_move[0]][ai_move[1]] = game.player
        winner = game.check_winner()
        if winner != 0:
            return jsonify({'winner': game.current_winner, 'board': game.board})

        if not game.is_move_left():
            return jsonify({'winner': 'Draw', 'board': game.board})

        game.player, game.opponent = game.opponent, game.player  # Switch players back

        return jsonify({'board': game.board, 'current_player': game.player})
    return jsonify({'error': 'Invalid move'})

@app.route('/reset', methods=['POST'])
def reset():
    global game
    game = TicTacToe()
    return jsonify({'board': game.board, 'current_player': game.player})

if __name__ == '__main__':
    app.run(debug=True)
