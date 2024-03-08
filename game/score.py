class PlayerRecord:
    def __init__(self, name, mode, score):
        self.name = name
        self.mode = mode
        self.score = score

    def __gt__(self, other):
        return self.score > other.score

    def __str__(self):
        return f"Name: {self.name}, Mode: {self.mode}, Score: {self.score}"


class GameRecord:
    def __init__(self):
        self.records = []

    def add_record(self, record):
        for existing_record in self.records:
            if existing_record.name == record.name and existing_record.mode == record.mode:
                if record.score > existing_record.score:
                    existing_record.score = record.score
                return
        self.records.append(record)

    def prepare_records(self, max_records):
        self.records.sort(reverse=True)
        self.records = self.records[:max_records]


class ScoreHandler:
    def __init__(self, file_name):
        self.game_record = GameRecord()
        self.file_name = file_name
        self.read()

    def read(self):
        try:
            with open(self.file_name, 'r') as file:
                for line in file:
                    name, mode, score = line.strip().split(',')
                    player_record = PlayerRecord(name, mode, int(score))
                    self.game_record.add_record(player_record)
        except FileNotFoundError:
            pass

    def save(self):
        with open(self.file_name, 'w') as file:
            for record in self.game_record.records:
                file.write(f"{record.name},{record.mode},{record.score}\n")

    def display(self):
        for record in self.game_record.records:
            print(record)


