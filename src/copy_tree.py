import shutil
import os
private_dir = "/home/tomma/workspace/github.com/Tomma-pwd/static_siteogen/private"
public_dir = "/home/tomma/workspace/github.com/Tomma-pwd/static_siteogen/public"
def copy_tree(source_dir, destination_dir):

    def copy_tree_r(current_path):
        for path in os.listdir(current_path):
            path_r = os.path.join(current_path, path)
            if os.path.isdir(path_r):
                os.mkdir(os.path.join(destination_dir, path_r[split_index:]))
                copy_tree_r(path_r)
            else:
                shutil.copy(path_r, os.path.join(destination_dir, path_r[split_index:]))
            
    if not os.path.isdir(source_dir):
        raise Exception("source_dir is not a directory")
    split_index = len(source_dir) + 1
    shutil.rmtree(destination_dir)
    os.mkdir(destination_dir)
    copy_tree_r(source_dir)

copy_tree(private_dir, public_dir)