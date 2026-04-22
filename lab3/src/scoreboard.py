import json
import os

class Scoreboard:
    def __init__(self, path='data/leaderboard.json'):
        self.path = path
        self.scores = []
        self._load()

    def _load(self):
        if os.path.exists(self.path):
            with open(self.path, 'r', encoding='utf-8') as f:
                self.scores = json.load(f)
        else:
            self.scores = []

    def _save(self):
        with open(self.path, 'w', encoding='utf-8') as f:
            json.dump(self.scores, f, indent=4)

    def add_score(self, name, score):
        self.scores.append({'name': name, 'score': score})
        self.scores.sort(key=lambda x: x['score'], reverse=True)
        self.scores = self.scores[:10]
        self._save()

    def is_high_score(self, score):
        if not self.scores: 
            return True
        return score > self.scores[0]['score']

    def get_top(self):
        return self.scores