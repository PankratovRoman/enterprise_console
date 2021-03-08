class Command:
    def __init__(self, name, params):
        self.name = name
        self.params = params

    def check_params(self, user_input):
        if len(user_input) < len(self.params):
            print('Параметров мало')
            return False
        else:
            for i in user_input[1:]:
                split_param = i.split(':')
                param = split_param[0]
                if param not in command.params:
                    print('Параметра нет')
                    return False
        return True


class Units:
    def __init__(self, name):
        self.name = name




units = {'engine': Units('engine'),
         'injector': Units('injector'),
         'pump': Units('pump')
         }


command_list = {'start': Command('start', [units['engine'].name, units['injector'].name, units['pump'].name]),
                'power': Command('power', []),
                'velocity': Command('velocity', [])
                }

while True:
    input_text = input("Введите команду (на английском, а то Сергей заругает!): ")
    split_command = input_text.split() # делим введенный текст на массив из команды и парамеров
    command_text = split_command[0] # выделяем команду - нулевой элемент массива

    if command_text not in command_list: # проверяем наличие команды в словаре command_list
        print('Такой команды нет')
        continue

    command = command_list[command_text]  # получаем экземпляр класса
    command_list = {}
    for i in split_command[1:]:
        split_i = i.split(':')
        if len(split_i) != 2:
            print('Ошибка')



    if not command.check_params(command_text_param):
        continue
