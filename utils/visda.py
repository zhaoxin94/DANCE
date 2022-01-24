import os.path as osp
import os

if __name__ == '__main__':
    # mode: univ or obda
    mode = 'obda'

    source_path = "data/visda/train"
    target_path = "data/visda/validation"

    dir_list = os.listdir(source_path)
    dir_list = [x.lower() for x in dir_list]
    dir_list.sort()
    print(dir_list)

    n_total = 12

    if mode == 'univ':
        n_share = 6
        n_source_private = 3
    elif mode == 'obda':
        n_share = 6
        n_source_private = 0
    else:
        raise NotImplementedError

    n_source = n_share + n_source_private
    source_list = dir_list[:n_source]
    target_list = dir_list[:n_share] + dir_list[n_source:]

    print(source_list)
    print(target_list)

    source_txt = f"txt/source_visda_{mode}.txt"
    target_txt = f"txt/target_visda_{mode}.txt"

    with open(source_txt, "w") as f:
        for direc in source_list:
            if not '.txt' in direc:
                files = os.listdir(os.path.join(source_path, direc))
                files.sort()
                for i, file in enumerate(files):
                    file_name = os.path.join(source_path, direc, file)
                    class_name = direc
                    f.write('%s %s\n' %
                            (file_name, source_list.index(class_name)))

    with open(target_txt, "w") as f:
        for direc in target_list:
            if not '.txt' in direc:
                files = os.listdir(os.path.join(target_path, direc))
                files.sort()
                for i, file in enumerate(files):
                    file_name = os.path.join(target_path, direc, file)
                    if direc in source_list:
                        class_name = direc
                        f.write('%s %s\n' %
                                (file_name, source_list.index(class_name)))
                    elif direc in target_list:
                        f.write('%s %s\n' % (file_name, len(source_list)))
