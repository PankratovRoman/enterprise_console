class Command:
    def __init__(self, name, params):
        self.name = name
        self.params = params

    def check_key_param(self, user_input): # на входе у нас массив из [ключ(команда), все остальное(параметры и значения параметров)]
        split_command = user_input.split()  # разделяем введенный текст на части
        user_input_command = split_command[0]  # закидываем в переменную command_key нулевой элемент масссива из предыдущейй строки, который есть ключ к справочнику
        if user_input_command not in command_list:  # проверяем есть ли выбранный ранее ключ в словаре, если нет, то пишем об этом
            print('Command "{}" is not in command list. Type "help" for help.'.format(user_input_command))
            return True


        """Участок кода в котором я сомневаюсь, но как по-другому я не придумал. Сначала я смотрю есть ли вообще параметры в словаре для данной команды, если нет, то пасс.
        Далее, если "длина введенного списка параметров меньше длины списка параметров в словаре - (длина списка параметров в словаре - 1)", тогда говорим, что параметров недостаточно."""
        len_param = len(command_list[user_input_command].params) - (len(command_list[user_input_command].params)-1)
        if len(split_command[1:]) == len(command_list[user_input_command].params):
            pass
        elif len(split_command[1:]) < len_param:
            print('Expected parameters: {}'.format(command_list[user_input_command].params)) # к тому же вот тут возвращается список, а пробежать по нему циклом корректно чет не получается
        """Конец участка в котором я сомневаюсь"""

        command_list_item = command_list[user_input_command]  # получаем экземпляр класса
        command_param = split_command[1:]  # присваиваем в command_param массив в котором все, что после ключа во введенном тексте
        split_param = (i.split(':') for i in command_param)  # получаем массив [параметр, значение]
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

while True:
    input_command = input('Enter command: ') # вводим команду

    if input_command == 'exit':  # сразу проверяем не хочет ли пользователь выйти
        print('Terminal broke')
        break

    Command.check_key_param(command_list, input_command)
