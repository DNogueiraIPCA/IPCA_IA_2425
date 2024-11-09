# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 09:08:37 2024

@author: fonte
"""

def minimax(board, is_maximizing):
    winner = check_winner(board)
    if winner is not None:
        return winner  # Retorna 1 se X ganha, -1 se O ganha, 0 se empata

    if is_maximizing:
        best_score = -float("inf")
        for i in range(9):
            if board[i] == "":
                board[i] = "X"  # X joga
                score = minimax(board, False)
                board[i] = ""
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for i in range(9):
            if board[i] == "":
                board[i] = "O"  # O joga
                score = minimax(board, True)
                board[i] = ""
                best_score = min(score, best_score)
        return best_score

def check_winner(board):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Linhas
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Colunas
        [0, 4, 8], [2, 4, 6]  # Diagonais
    ]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != "":
            return 1 if board[combo[0]] == "X" else -1
    return 0 if "" not in board else None

def count_results():
    board = [""] * 9
    results = {1: 0, -1: 0, 0: 0}  # Contadores para vitórias, derrotas e empates
    for i in range(9):
        if board[i] == "":
            results[minimax(board, True)] += 1
    print("Vitórias (1):", results[1])
    print("Empates (0):", results[0])
    print("Derrotas (-1):", results[-1])

count_results()
