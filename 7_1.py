import os

project = ['HEAD', 'settings', 'mainapp', 'adminapp', 'authapp']

main_dir = project[0]
if not os.path.exists(main_dir):
    os.mkdir(main_dir)
    os.chdir(main_dir)
    tree = [os.mkdir(i) for i in project[1:] if os.path.exists('.')]
else:
    print(f'Папка с таким именем существует - "{main_dir}"')