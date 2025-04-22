document.addEventListener('DOMContentLoaded', () => {
    const cells = document.querySelectorAll('.cell');
    const resetButton = document.getElementById('reset-btn');

    cells.forEach(cell => {
        cell.addEventListener('click', () => {
            const row = cell.getAttribute('data-row');
            const col = cell.getAttribute('data-col');
            fetch('/move', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ row: row, col: col })
            })
            .then(response => response.json())
            .then(data => {
                if (data.error) {
                    alert(data.error);
                } else {
                    updateBoard(data.board);
                    if (data.winner) {
                        alert(data.winner === 'Draw' ? 'It\'s a draw!' : `${data.winner} wins!`);
                    }
                }
            });
        });
    });

    resetButton.addEventListener('click', () => {
        fetch('/reset', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(response => response.json())
        .then(data => {
            updateBoard(data.board);
        });
    });

    function updateBoard(board) {
        cells.forEach(cell => {
            const row = cell.getAttribute('data-row');
            const col = cell.getAttribute('data-col');
            cell.textContent = board[row][col];
        });
    }
});
