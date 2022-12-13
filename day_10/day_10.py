
FILE_NAME = 'input.txt'


def _cycle_cathode(ticks):
    def actual_decorator(func):
        def wrapper(self, *args, **kw):
            result = None
            for i in range(ticks):
                self.circuit_ticks += 1
                # ^ pass on self here

                if self.check_state():
                    self.update_state()
                    result = self.state
            func(self, *args, **kw)
            if self.check_state():
                self.update_state()
                result = self.state
            return result
        return wrapper
    return actual_decorator


class CathodeRay:

    def __init__(self):
        self.circuit_ticks = 0
        self.register = 1
        self.output_times = 20
        self.output_time_increments = 40
        self.state = 0

    def update_state(self):
        self.state = self.register * self.circuit_ticks
        # After first cycle this resets to 40
        self.output_times += self.output_time_increments

    def check_state(self):
        return self.circuit_ticks > 0 and self.circuit_ticks % self.output_times == 0

    @_cycle_cathode(1)
    def noop(self):
        pass

    @_cycle_cathode(2)
    def addx(self, num):
        self.register += num


def main():

    cathode = CathodeRay()

    outputs = []

    with open(FILE_NAME) as file:
        for rec in file.readlines():
            rec = rec.strip()
            if rec == 'noop':
                result = cathode.noop()
            elif rec.startswith('addx'):
                num = int(rec.split()[-1])
                result = cathode.addx(num)

            if result is not None:
                outputs.append(result)

            print(f"{rec}: reg: {cathode.register}, count: {cathode.circuit_ticks}, result: {result}, {cathode.output_times }")
    print(f'Outputs : {outputs}')
    print(f'Total: {sum(outputs)}')


if __name__ == '__main__':
    main()
