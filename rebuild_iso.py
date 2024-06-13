import os
import shutil
# Создание папки и распаковка iso
PATH_TO_ISO = '/home/tv/Загрузки/installer-py/load.iso'
ISO_FOLDER_PATH = 'unpack'
os.makedirs(ISO_FOLDER_PATH, exist_ok=True)
os.system(f'xorriso -osirrox on -indev {PATH_TO_ISO} -extract / {ISO_FOLDER_PATH}')

# Копирование файла ФС
os.system(f'cp /home/tv/Загрузки/installer-py/{ISO_FOLDER_PATH}/live/filesystem.squashfs /home/tv/Загрузки/installer-py/') #Заменить конечный путь на тот, где лежит rebuild_iso.py
# Распаковка ФС
os.system('unsquashfs filesystem.squashfs')
# Удаление файла ФС
os.system('rm filesystem.squashfs')
# Создание папки intel SSD и выдача прав
os.makedirs('squashfs-root/root/LOADFWDR/Intel_ssd', exist_ok=True)
os.system('chmod 0777 -R squashfs-root/root/LOADFWDR/Intel_ssd')
# Копирование файлов из папки files в папку Intel_ssd
for file in os.listdir('files'):
    shutil.copy(f'files/{file}', f'squashfs-root/root/LOADFWDR/Intel_ssd/{file}')
# Сборка и замена ФС
os.system('mksquashfs squashfs-root filesystem.squashfs')
os.system(f'cp filesystem.squashfs /home/tv/Загрузки/installer-py/{ISO_FOLDER_PATH}/live/')
os.system('rm filesystem.squashfs')
# Сборка iso
os.system(f'xorrisofs -v -J -r -V "LABEL" -o result.iso {ISO_FOLDER_PATH}/')