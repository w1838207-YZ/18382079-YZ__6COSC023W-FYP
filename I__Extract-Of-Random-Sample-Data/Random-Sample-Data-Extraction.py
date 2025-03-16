# The Python library 'OS' gets imported.
# The OS functions used by this script allow for the construction and management of file/folder paths.
import os

# The Python library 'Shutil' gets imported.
# The Shutil functions used by this script allow for the deletion of folders and the copying of files.
import shutil

# The Python library 'Random' gets imported.
# A function used by this script, '.randint()', allows for the generation of a random number.
import random

# The class 'Path', from the Python library 'Pathlib', gets imported.
# A function usable by this class, '.home()', allows for a flexible way to reach a user's given home folder.
from pathlib import Path




# This variable stores a folder path, to a given user's downloads.
# An unzipped folder of the used Kaggle dataset is presumed to also be found here.
original_dataset_files_path = os.path.join(Path.home(),"Downloads","Dataset")

# This variable stores a folder path, pointing to where this script exists.
# The location will be where extracted sample data gets saved to.
directory_for_sample_data = os.path.join(os.path.dirname(__file__),"Data-Sample")

# These variables store folder paths, made using the data sample's parent folder.
# The folders will be used to group files into train, validation, and test data.
data_sample_general_subdir1 = os.path.join(directory_for_sample_data,"Test-Data")
data_sample_general_subdir2 = os.path.join(directory_for_sample_data,"Train-Data")
data_sample_general_subdir3 = os.path.join(directory_for_sample_data,"Validation-Data")

# These variables store folder paths, made using data sample general sub-folders.
# The folders will be used to group files into real and fake data.
data_sample_specific_subdir1 = os.path.join(data_sample_general_subdir1,"Fake")
data_sample_specific_subdir2 = os.path.join(data_sample_general_subdir1,"Real")
data_sample_specific_subdir3 = os.path.join(data_sample_general_subdir2,"Fake")
data_sample_specific_subdir4 = os.path.join(data_sample_general_subdir2,"Real")
data_sample_specific_subdir5 = os.path.join(data_sample_general_subdir3,"Fake")
data_sample_specific_subdir6 = os.path.join(data_sample_general_subdir3,"Real")




# This function is for copying files between folders.
# Here is where the actual extraction of original dataset files eventually occurs.
def copy_sample_data_from_original_dataset(path_slice_for_dataset_images,dataset_extract_subdir_flag,random_index_list):
    
    # This for loop iterates over all random indices in the corresponding list. Initially each index value gets combined with path slices, to eventually make a full path to a source file from the original dataset.
    for existing_index in random_index_list:
        path_slice_extended = path_slice_for_dataset_images + str(existing_index) + ".jpg"
        full_source_file_path = os.path.join(original_dataset_files_path,path_slice_extended)
        
        # This match case statement checks the value of a given flag variable. The currently iterated index is used in another combination to make a full destination path. The flag value determines the subfolder of sample data that said destination path will exist under.
        match (dataset_extract_subdir_flag):
            case 1:
                path_slice_for_copy_destination = "fake_" + str(existing_index) + ".jpg"
                full_path_for_copy_destination = os.path.join(data_sample_specific_subdir1,path_slice_for_copy_destination)
            case 2:
                path_slice_for_copy_destination = "real_" + str(existing_index) + ".jpg"
                full_path_for_copy_destination = os.path.join(data_sample_specific_subdir2,path_slice_for_copy_destination)
            case 3:
                path_slice_for_copy_destination = "fake_" + str(existing_index) + ".jpg"
                full_path_for_copy_destination = os.path.join(data_sample_specific_subdir3,path_slice_for_copy_destination)
            case 4:
                path_slice_for_copy_destination = "real_" + str(existing_index) + ".jpg"
                full_path_for_copy_destination = os.path.join(data_sample_specific_subdir4,path_slice_for_copy_destination)
            case 5:
                path_slice_for_copy_destination = "fake_" + str(existing_index) + ".jpg"
                full_path_for_copy_destination = os.path.join(data_sample_specific_subdir5,path_slice_for_copy_destination)
            case 6:
                path_slice_for_copy_destination = "real_" + str(existing_index) + ".jpg"
                full_path_for_copy_destination = os.path.join(data_sample_specific_subdir6,path_slice_for_copy_destination)
                
        # The Shutil function '.copyfile()' uses both source and destination paths, in order to take an original dataset file and copy it into the folders for sample data.
        shutil.copyfile(full_source_file_path,full_path_for_copy_destination)




# This function is for generating a random list of indices.
# Said list aids in identifying which files to extract from the original dataset.
def get_image_index_list(dataset_image_subcount_approx,data_sample_copy_amount,path_slice_for_dataset_images,dataset_extract_subdir_flag):

    # A variable stores the index list, which starts off as being empty.
    random_index_list = []

    # This for loop uses the Random function '.randint()' to iteratively populate the above list. By the end, said list will have a given number of random numbers representing files within the original dataset (e.g. test fake files) to extract.
    for i in range(data_sample_copy_amount):
        while (True):
            newly_generated_index = random.randint(1,dataset_image_subcount_approx)
            if (not(newly_generated_index in random_index_list)):
                break
        random_index_list.append(newly_generated_index)

    # A call is made for the function which copies files between folders.
    copy_sample_data_from_original_dataset(path_slice_for_dataset_images,dataset_extract_subdir_flag,random_index_list)




# This function is for extracting specifically the test fake data.
# It is called by the function which groups all extraction functions in order.
def test_fake_image_extraction():

    # These variables store: the approximate subcount of files in a subfolder of the original dataset, the amount of test fake data needed to be copied, a necessary slice of a path to the original dataset, and a flag value.
    dataset_image_subcount_approx = 5400
    data_sample_copy_amount = 30
    path_slice_for_dataset_images = "Test/Fake/fake_"
    dataset_extract_subdir_flag = 1

    # A call is made for the function which generates a random index list.
    get_image_index_list(dataset_image_subcount_approx,data_sample_copy_amount,path_slice_for_dataset_images,dataset_extract_subdir_flag)




# This function is for extracting specifically the test real data.
# It is called by the function which groups all extraction functions in order.
def test_real_image_extraction():

    # These variables store: the approximate subcount of files in a subfolder of the original dataset, the amount of test real data needed to be copied, a necessary slice of a path to the original dataset, and a flag value.
    dataset_image_subcount_approx = 5400
    data_sample_copy_amount = 30
    path_slice_for_dataset_images = "Test/Real/real_"
    dataset_extract_subdir_flag = 2
    
    # A call is made for the function which generates a random index list.
    get_image_index_list(dataset_image_subcount_approx,data_sample_copy_amount,path_slice_for_dataset_images,dataset_extract_subdir_flag)




# This function is for extracting specifically the train fake data.
# It is called by the function which groups all extraction functions in order.
def train_fake_image_extraction():
    
    # These variables store: the approximate subcount of files in a subfolder of the original dataset, the amount of train fake data needed to be copied, a necessary slice of a path to the original dataset, and a flag value.
    dataset_image_subcount_approx = 70000
    data_sample_copy_amount = 240
    path_slice_for_dataset_images = "Train/Fake/fake_"
    dataset_extract_subdir_flag = 3

    # A call is made for the function which generates a random index list.
    get_image_index_list(dataset_image_subcount_approx,data_sample_copy_amount,path_slice_for_dataset_images,dataset_extract_subdir_flag)




# This function is for extracting specifically the train real data.
# It is called by the function which groups all extraction functions in order.
def train_real_image_extraction():

    # These variables store: the approximate subcount of files in a subfolder of the original dataset, the amount of train real data needed to be copied, a necessary slice of a path to the original dataset, and a flag value.
    dataset_image_subcount_approx = 70000
    data_sample_copy_amount = 240
    path_slice_for_dataset_images = "Train/Real/real_"
    dataset_extract_subdir_flag = 4

    # A call is made for the function which generates a random index list.
    get_image_index_list(dataset_image_subcount_approx,data_sample_copy_amount,path_slice_for_dataset_images,dataset_extract_subdir_flag)




# This function is for extracting specifically the validation fake data.
# It is called by the function which groups all extraction functions in order.
def validation_fake_image_extraction():

    # These variables store: the approximate subcount of files in a subfolder of the original dataset, the amount of validation fake data needed to be copied, a necessary slice of a path to the original dataset, and a flag value.
    dataset_image_subcount_approx = 19600
    data_sample_copy_amount = 30
    path_slice_for_dataset_images = "Validation/Fake/fake_"
    dataset_extract_subdir_flag = 5

    # A call is made for the function which generates a random index list.
    get_image_index_list(dataset_image_subcount_approx,data_sample_copy_amount,path_slice_for_dataset_images,dataset_extract_subdir_flag)




# This function is for extracting specifically the validation real data.
# It is called by the function which groups all extraction functions in order.
def validation_real_image_extraction():

    # These variables store: the approximate subcount of files in a subfolder of the original dataset, the amount of validation real data needed to be copied, a necessary slice of a path to the original dataset, and a flag value.
    dataset_image_subcount_approx = 19600
    data_sample_copy_amount = 30
    path_slice_for_dataset_images = "Validation/Real/real_"
    dataset_extract_subdir_flag = 6

    # A call is made for the function which generates a random index list.
    get_image_index_list(dataset_image_subcount_approx,data_sample_copy_amount,path_slice_for_dataset_images,dataset_extract_subdir_flag)




# This function is for the organisation of sample data extracts.
# The extractions for all subgroups of sample data files are included in this function, and ordered in a specific sequence.
def ordered_sample_extractions():

    # This try block attempts to extract the test fake files.
    # In case any exception is thrown, this except block catches the exception, prints it, and raises one more with a less technical message.
    try:
        test_fake_image_extraction()
        print("> The sample data for test fake images have been successfully extracted!")
    except Exception as e:
        print("|\n>",e)
        raise Exception("|\n> Exception! Something went wrong with extracting test fake images from the original dataset.")

    # This try block attempts to extract the test real files.
    # In case any exception is thrown, this except block catches the exception, prints it, and raises one more with a less technical message.
    try:
        test_real_image_extraction()
        print("> The sample data for test real images have been successfully extracted!")
    except Exception as e:
        print("|\n>",e)
        raise Exception("|\n> Exception! Something went wrong with extracting test real images from the original dataset.")

    # This try block attempts to extract the train fake files.
    # In case any exception is thrown, this except block catches the exception, prints it, and raises one more with a less technical message.
    try:
        train_fake_image_extraction()
        print("> The sample data for train fake images have been successfully extracted!")
    except Exception as e:
        print("|\n>",e)
        raise Exception("|\n> Exception! Something went wrong with extracting train fake images from the original dataset.")

    # This try block attempts to extract the train real files.
    # In case any exception is thrown, this except block catches the exception, prints it, and raises one more with a less technical message.
    try:
        train_real_image_extraction()
        print("> The sample data for train real images have been successfully extracted!")
    except Exception as e:
        print("|\n>",e)
        raise Exception("|\n> Exception! Something went wrong with extracting train real images from the original dataset.")

    # This try block attempts to extract the validation fake files.
    # In case any exception is thrown, this except block catches the exception, prints it, and raises one more with a less technical message.
    try:
        validation_fake_image_extraction()
        print("> The sample data for validation fake images have been successfully extracted!")
    except Exception as e:
        print("|\n>",e)
        raise Exception("|\n> Exception! Something went wrong with extracting validation fake images from the original dataset.")

    # This try block attempts to extract the validation real files.
    # In case any exception is thrown, this except block catches the exception, prints it, and raises one more with a less technical message.
    try:
        validation_real_image_extraction()
        print("> The sample data for validation real images have been successfully extracted!")
    except Exception as e:
        print("|\n>",e)
        raise Exception("|\n> Exception! Something went wrong with extracting validation real images from the original dataset.")




# This function is for making folders, ready for newly extracted sample data.
# It can also serve to remove previously extracted data, if this script file manages to locate said data and a user confirms said action.
def make_data_sample_directories():

    # This try block attempts to make the new data sample's folders, using folder paths kept in above variables.
    try:

        # This if statement uses the OS function '.path.isdir()' and the Shutil function '.rmtree()'. If a parent folder of pre-existing sample data can be found, then it gets deleted.
        if (os.path.isdir(directory_for_sample_data)):
            shutil.rmtree(directory_for_sample_data)
            print("|\n> The pre-existing sample data has deleted.")

        # The OS function '.mkdir()' is used one time, to create a parent folder for new sample data with the relevant folder path.
        os.mkdir(directory_for_sample_data)

        # The OS function '.mkdir()' is called three more times, to make the new data sample's general sub-folders with relevant folder paths.
        os.mkdir(data_sample_general_subdir1)
        os.mkdir(data_sample_general_subdir2)
        os.mkdir(data_sample_general_subdir3)

        # The OS function '.mkdir()' is called six more times, to make the new data sample's specific sub-folders using relevant folder paths.
        os.mkdir(data_sample_specific_subdir1)
        os.mkdir(data_sample_specific_subdir2)
        os.mkdir(data_sample_specific_subdir3)
        os.mkdir(data_sample_specific_subdir4)
        os.mkdir(data_sample_specific_subdir5)
        os.mkdir(data_sample_specific_subdir6)
    
    # In case any exception is thrown, this except block catches the exception, prints it, and raises one more with a less technical message.
    except Exception as e:
        print("|\n>",e)
        raise Exception("> Exception! Something went wrong with making directories for the sample data.")




# This function is for checking whether sample data extracted in the past currently exists in the same parent folder as this script file.
# It serves to initiate a new process of sample data extraction, bearing in mind some conditions indicated by user input.
def existing_sample_directories_check():

    # This if statement uses the OS function '.path.isdir()'. If it can locate previous sample data, it asks the user if they want to overwrite it or not.
    if (os.path.isdir(directory_for_sample_data)):
        print(">",str(directory_for_sample_data))
        print("> Previously extracted sample data was found at the above path.")
        overwrite_data_decision = input("> Please enter 'Y' *only* if you wish to overwrite this pre-existing data.\n> Alternatively, enter any other value or no value if you wish not to overwrite.\n> ")

        # This if statement checks for user confirmation in the prior question, about a new extraction bearing in mind removal of previous sample data.
        if (overwrite_data_decision.upper()=="Y"):

            # This try block attempts to perform extraction with overwriting.
            # In case any exception is thrown, this except block catches the exception, prints it, and concludes the script's runtime.
            try:
                make_data_sample_directories()
                print("> The directories for the sample data have successfully been made!")
                ordered_sample_extractions()
                print("|\n> This script's execution has finished.")
            except Exception as e:
                print(e,"|\n> This script's execution has finished.")

        # In the event that the user doesn't confirm, this else clause doesn't perform extraction and concludes the script's runtime.
        else:
            print("|\n> The pre-existing sample data has not been overwritten.")
            print("|\n> This script's execution has finished.")

    # In the event that previous sample data is not found, this else clause begins a new extraction without removal of data.
    else:
        
        # This try block attempts to perform extraction without overwriting.
        # In case any exception is thrown, this except block catches the exception, prints it, and concludes the script's runtime.
        try:
            print("> A creation of new sample data from nothing will begin now.\n|")
            make_data_sample_directories()
            print("> The directories for the sample data have successfully been made!")
            ordered_sample_extractions()
            print("|\n> This script's execution has finished.")
        except Exception as e:
            print(e,"|\n> This script's execution has finished.")




# This is the main function of this script file.
# It serves as the main entry point, once the script's runtime begins.
def main():

    # This if statement uses the 'not' operator and OS function '.path.isdir()'. It checks whether the original Kaggle dataset is downloaded, unzipped, and exists in a given user's downloads folder.
    if (not(os.path.isdir(original_dataset_files_path))):

        # In the event that the original dataset files cannot be found, they are informed of this and the script's runtime also concludes here.
        print("> This script could not find the images of the original dataset during its runtime.")
        print("> Please ensure that the dataset images are unzipped and stored in the downloads folder, before running this script again.")
        print("|\n> This script's execution has finished.")

    # When the original dataset files *are* locatable, this else clause calls the function which checks for previously extracted sample data.
    else:
        existing_sample_directories_check()




# This if statement checks a special Python variable '__name__'. It calls a main function, whenever it receives a 'True' value.
# The check is what lets this script be runnable in the first place.
if (__name__=="__main__"):
    main()