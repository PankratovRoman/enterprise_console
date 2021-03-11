class Command:
    def __init__(self, name, params, help_text, execute_text):
        self.name = name
        self.params = params
        if len(self.params) != 0:
            self.help_text = help_text + ' Expected parameters: '+', '.join(self.params)
        else:
            self.help_text = help_text
        self.execute_text = execute_text

    def check_param(self, user_input):  # на входе массив из [ключ(команда), все остальное(параметры и знач параметров)]
        if (len(split_command)-1) < len(self.params):
            print('Expected parameters: {}'.format(', '.join(self.params)))
        command_list_item = command_list[user_input]  # получаем экземпляр класса
        # command_param = split_command[1:]  # присваиваем массив в котором все, что после ключа во введенном тексте
        # split_param = [i.split(':') for i in command_param]  # получаем массив [параметр, значение]
        # две строки выше заменил на финкцию, т.к. использую этот способ в нескольких местах
        split_param = split_params(split_command)
        for i in split_param:  # проверяем, есть ли параметр из массива split_param в параметрах команды из справочника
            if len(i[0]) == 0:  # это для команд без параметров, ебучий костыль
                return True
            elif i[0] not in command_list_item.params:
                print('Parameter "{}" is not in parameter list. Type "help {}" for help.'
                      .format(i[0], user_input_command))
                return False
            elif len(i) < 2:
                print('Enter parameter value for {}.'.format(i[0]))
                return False
            elif len(i[1]) == 0:
                print('Expected parameter value for {}.'.format(i[0]))
                return False
        return True

    def execute(self, user_input_command):
        exec_list = split_params(split_command)
        exec_text = [(i[0]+' with value '+i[1]) for i in exec_list]
        if user_input_command == self.name:
            print('Command: ' + user_input_command + '. ' + self.execute_text + ' ' + ', '.join(exec_text))


class Units:
    def __init__(self, name):
        self.name = name


units = {'engine': Units('engine'),
         'injector': Units('injector'),
         'pump': Units('pump')
         }

command_list = {'start': Command('start', [units['engine'].name, units['injector'].name, units['pump'].name],
                                 '"start" gives the command to start one of the modules.', 'Started'),
                'power': Command('power', [units['engine'].name],
                                 '"power" gives the command to increase or decrease engine power.', 'Power on'),
                'velocity': Command('velocity', [],
                                    '"velocity" gives the command to increase or decrease velocity.', 'Velocity now')
                }


def help_command(input_command):
    ''' Функция, которая выводит help к каждой из команд '''
    help_command = input_command.split(' ')
    help_unit = help_command[1]
    if help_unit == 'help':
        print('Help! I need somebody, help! Not just anybody, Help! You know I need someone, help!')
    elif help_unit not in command_list:
        print('Command "{}" is not in command list. Type "help" for help.'.format(help_unit))
    elif help_unit == command_list[help_unit].name:
        print(command_list[help_unit].help_text)


def split_params(split_command):
    split_command = split_command[1:]
    split_param = [i.split(':') for i in split_command]
    return split_param


print('Welcome to Enterprise test console. Type "help" for help.')

while True:
    input_command = input('Enter command: ')  # вводим команду
    split_command = input_command.split()  # разделяем введенный текст на части
    user_input_command = split_command[0]  # нулевой элемент масссива из предыдущейй строки = ключ к справочнику

    if input_command == 'exit':
        print('Terminated.')
        break
    elif user_input_command == 'debug' and (len(split_command) > 1):
        continue
    elif user_input_command == 'help' and (len(split_command) > 1):
        help_command(input_command)
        continue
    elif input_command == 'help':
        com_to_str = ', '.join(command_list)
        print('Expected commands: {}'.format(com_to_str))
        continue
    elif user_input_command not in command_list:  # проверяем есть ли выбранный ранее ключ в словаре
        print('Command "{}" is not in command list. Type "help" for help.'.format(user_input_command))
        continue

    if Command.check_param(command_list[user_input_command], user_input_command) is True:
        Command.execute(command_list[user_input_command], user_input_command)
