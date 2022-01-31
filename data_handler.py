class FileLoader(object):
    def __init__(self, filename):
        self.filename = filename
        self.ttask = None
        self.umax = None
        self.new_users_per_tick = None

    def validate_data(self):
        if not (1 <= self.ttask <= 10):
            raise Exception("ttask number not allowed")
        if not (1 <= self.umax <= 10):
            raise Exception("umax number not allowed")

    def load_data(self):
        try:
            with open(self.filename) as input_file:
                data = [int(line.strip()) for line in input_file.readlines()]
                self.ttask = data[0]
                self.umax = int(data[1])
                self.new_users_per_tick = data[2:]
                self.validate_data()
        except FileNotFoundError:
            print(f'File with name {self.filename} not found! Check if it exists')
        except IndexError:
            print(f'File with name {self.filename} is empty')

