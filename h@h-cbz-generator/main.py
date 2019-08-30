import shutil
import os

if __name__ == '__main__':
    # download_path = '/home/hath/hath/download'
    download_path = './test'

    try:
        os.chdir(download_path)
        subfolders = [f.name for f in os.scandir('.') if f.is_dir()]
    except Exception as e:
        print("Failed to find subdirectories in {}".format(download_path))

    for subfolder in subfolders:
        if not os.path.exists('./{}/galleryinfo.txt'.format(subfolder)):
            print('Gallery {} is not complete!'.format(subfolder))
            continue
        shutil.make_archive(subfolder, 'zip', root_dir='./{}'.format(subfolder))
        os.rename('{}.zip'.format(subfolder), '{}.cbz'.format(subfolder))
        shutil.rmtree(subfolder)
