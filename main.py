from data_handler import FileLoader
from simulator import Simulator

if __name__ == '__main__':
    file_loader = FileLoader('files/input.txt')
    file_loader.load_data()
    Simulator(file_loader.ttask, file_loader.umax, file_loader.new_users_per_tick).run()
