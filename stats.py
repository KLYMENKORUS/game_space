class Stats():
    """Отслеживание статстики"""

    def __init__(self):
        """Игициализация статистики"""
        self.reset_stats()
        self.run_game = True
        with open('high_score.txt', 'r') as f:
            self.high_score = int(f.readline())

    def reset_stats(self):
        """Статистика изменяющаяся в ходе игры"""
        self.guns_left = 2
        self.score = 0
