class Command:
    def __init__(self, name, params):
        self.name = name
        self.params = params

    def check_param(self, user_input):  # на входе у нас массив из [ключ(команда), все остальное(параметры и значения параметров)]
        params = ', '.join(self.params)
        if (len(split_command)-1) < len(self.params):
            print('Expected parameters: {}'.format(params))  # к тому же вот тут возвращается список, а пробежать по нему циклом корректно чет не получается
        command_list_item = command_list[user_input]  # получаем экземпляр класса
        command_param = split_command[1:]  # присваиваем в command_param массив в котором все, что после ключа во введенном тексте
        split_param = [i.split(':') for i in command_param]  # получаем массив [параметр, значение]
        for i in split_param:  # проверяем, есть ли параметр из массива splited_param в параметрах команды из справочника
            if i[0] not in command_list_item.params:
                print('Parameter "{}" is not in parameter list. Type "help {}" for help.'.format(i[0], user_input_command))


class Units:
    def __init__(self, name):
        self.name = name


units = {'engine': Units('engine'),
         'injector': Units('injector'),
         'pump': Units('pump')
         }

command_list = {'start': Command('start', [units['engine'].name, units['injector'].name, units['pump'].name]),
                'power': Command('power', [units['engine'].name]),
                'velocity': Command('velocity', [])
                }


def help_command(input_command):
    '''Функция, которая выводит help к каждой из команд'''
    help_command = input_command.split(' ')
    help_unit = help_command[1]
    if help_unit == 'help':
        print('Help! I need somebody, help! Not just anybody, Help! You know I need someone, help!')
        return True
    elif help_unit not in command_list:
        print('Command "{}" is not in command list. Type "help" for help.'.format(help_unit))
        return True

    list_to_str = ', '.join(command_list[help_unit].params)
    if help_unit == 'start':
        print('"start" gives the command to start one of the modules. Expected parameters: {}'.format(', '.join(command_list[help_unit].params)))
    elif help_unit == 'power':
        print('"power" gives the command to increase or decrease engine power. Expected parameters: {}'.format(list_to_str))
    elif help_unit == 'velocity':
        print('"velocity" gives the command to increase or decrease velocity. Expected parameters: {}'.format(list_to_str))


print('Welcome to Enterprise test console. Type "help" for help.')

while True:
    input_command = input('Enter command: ') # вводим команду
    split_command = input_command.split()  # разделяем введенный текст на части
    user_input_command = split_command[0]  # закидываем в переменную command_key нулевой элемент масссива из предыдущейй строки, который есть ключ к справочнику

    if input_command == 'exit':  # сразу проверяем не хочет ли пользователь выйти
        print('Terminal broke')
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
    elif user_input_command not in command_list:  # проверяем есть ли выбранный ранее ключ в словаре, если нет, то пишем об этом
        print('Command "{}" is not in command list. Type "help" for help.'.format(user_input_command))
        continue

    Command.check_param(command_list[user_input_command], user_input_command)
