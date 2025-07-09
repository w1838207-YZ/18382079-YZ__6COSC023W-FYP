#
import os




#
allowed_extensions = ["jpg","jpeg"]




#
def find_currently_available_models():
    
    #
    paths_for_current_models = []
    project_root_directory = os.path.dirname(os.getcwd())
    parent_subdirectory_for_models = os.path.join(project_root_directory,"II__Deepfake-Detection-Models")

    #
    for folder in os.listdir(parent_subdirectory_for_models):
        folder_path = os.path.join(str(parent_subdirectory_for_models),folder)
        for file in os.listdir(folder_path):
            if (".keras" in file):
                file_path = os.path.join(str(folder_path),file)
                paths_for_current_models.append(file_path)
    
    #
    return paths_for_current_models




#
def is_file_allowed(uploaded_file_name):
    
    #
    return (("." in uploaded_file_name) and \
            (uploaded_file_name.rsplit(".", 1)[1].lower() in allowed_extensions))