import re
import yaml
import os
import random
import time

vars_file = os.path.join(os.path.dirname(__file__), 'vars.yml')
commands_file = os.path.join(os.path.dirname(__file__), 'commands.yml')


class PlushPlant:
    dict_cmd = {}
    dict_vars = {}

    def __init__(self):
        with open(commands_file, 'r') as c:
            self.dict_cmd = yaml.safe_load(c)
        with open(vars_file, 'r') as c:
            self.dict_vars = yaml.safe_load(c)

    def send_cmd(self, cmd):
        main_cmd = cmd.split(' -l ')[0]
        try:
            option = cmd.split(' -l ')[1]
        except:
            option = ""
        try:
            update = cmd.split(' -u ')[1]
            main_cmd = cmd.split(' -u ')[0]
        except:
            update = ""
        response_time = random.randint(0, 4)
        try:
            for command in self.dict_cmd['commands']:
                if main_cmd in command['command']:
                    index_cmd = self.dict_cmd['commands'].index(command)
                    # print(dict['commands'])
                    stdout_cmd = self.dict_cmd['commands'][index_cmd]['stdout']
                    if option != "":
                        i = 0
                        opt_found = False
                        for opt in self.dict_cmd['commands'][index_cmd]['options']:
                            if option in opt:
                                stdout_cmd = stdout_cmd + "\n" + self.dict_cmd['commands'][index_cmd]['options'][i][option]
                                opt_found = True
                            i = i + 1
                        if not opt_found:
                            stdout_cmd = "No valid option -l"
                    if update != "":
                        self.dict_vars['vars'][update] = self.dict_cmd['commands'][index_cmd]['update']
                    if re.findall(r'\{\{.*\}\}', stdout_cmd):
                        var_to_replace = re.findall(r'\{\{vars\((.*)\)\}\}', stdout_cmd)[0]
                        stdout_cmd = re.sub(r'(\{\{vars\(\w+\)\}\})', self.dict_vars['vars'][var_to_replace], stdout_cmd)
                    time.sleep(response_time)
                    return stdout_cmd
            stdout_cmd = "could not resolve your command"
            time.sleep(response_time)
            return stdout_cmd
        except:
            stdout_cmd = "could not resolve your command"
            time.sleep(response_time)
            return stdout_cmd

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
