class Simulator(object):
    def __init__(self, ttask, umax, new_users_per_tick):
        self.current_tasks = []
        self.servers = []
        self.ttask = ttask
        self.umax = umax
        self.users_per_tick = new_users_per_tick
        self.cost = 1
        self.output_file = open('files/output.txt', 'w')

    def balance(self):
        line = ''
        self.servers = [self.current_tasks[i * self.umax:(i + 1) * self.umax] for i in
                        range((len(self.current_tasks) + self.umax - 1) // self.umax)]
        for server in self.servers:
            line += f'{len(server)},'
            self.cost += 1
        return line

    def tick(self):
        for task in self.current_tasks:
            task['remaining_ttask'] = task.get('remaining_ttask') - 1
        self.current_tasks = [task for task in self.current_tasks if task.get('remaining_ttask') > 0]

    def finish_pending_tasks(self):
        while self.current_tasks:
            self.output_file.write(f'{self.balance()}\n')
            self.tick()
        self.output_file.write('0\n')
        self.output_file.write(str(self.cost))

    def run(self):
        for tick_counter, new_users_for_this_tick in enumerate(self.users_per_tick):
            for new_user_idx in range(new_users_for_this_tick):
                self.current_tasks.append(
                    {'task': f'{tick_counter + 1}/{new_user_idx + 1}', 'remaining_ttask': 4, 'ixd': tick_counter + 1})
            self.output_file.write(f'{self.balance()}\n')
            self.tick()

        self.finish_pending_tasks()
