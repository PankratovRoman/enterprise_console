class Command:
    def __init__(self, name, params, help_text, execute_text):
        self.name = name
        self.params = params
        if len(self.params) != 0:
            self.help_text = help_text + ' Expected parameters: '+', '.join(self.params)
        else:
            self.help_text = help_text
        self.execute_text = execute_text

    def execute(self, params):
        if len(params) < len(self.params):
            raise Exception('Expected parameters: {}'.format(', '.join(self.params)))
        split_param = split_params(params)
        for i in split_param:  # проверяем, есть ли параметр из массива split_param в параметрах команды из справочника
            if i[0] not in self.params:
                raise Exception('Parameter "{}" is not in parameter list. Type "help {}" for help.'
                      .format(i[0], self.name))
            elif len(i) < 2:
                raise Exception('Enter parameter value for {}.'.format(i[0]))
            elif len(i[1]) == 0:
                raise Exception('Expected parameter value for {}.'.format(i[0]))
        exec_text = [(i[0]+' with value '+i[1]) for i in split_param]
        print('Command: ' + self.name + '. ' + self.execute_text + ' ' + ', '.join(exec_text))


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


def help_command(inp_for_help):
    ''' Функция, которая выводит help к каждой из команд '''
    help_command = inp_for_help.split(' ')
    help_unit = help_command[1]
    if help_unit == 'help':
        print('Help! I need somebody, help! Not just anybody, Help! You know I need someone, help!')
    elif help_unit not in command_list:
        print('Command "{}" is not in command list. Type "help" for help.'.format(help_unit))
    elif help_unit == command_list[help_unit].name:
        print(command_list[help_unit].help_text)


def split_params(command_for_split):
    return [i.split(':') for i in command_for_split]


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
    elif user_input_command == 'help':
        if len(split_command) > 1:
            help_command(input_command)
        elif input_command == 'help':
            com_to_str = ', '.join(command_list)
            print('Expected commands: {}'.format(com_to_str))
        continue
    elif user_input_command not in command_list:  # проверяем есть ли выбранный ранее ключ в словаре
        print('Command "{}" is not in command list. Type "help" for help.'.format(user_input_command))
        continue

    command = command_list[user_input_command]
    try:
        command.execute(split_command[1:])
    except Exception as ex:
        print(str(ex))
