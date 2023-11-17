from os import listdir


def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames
    of the image files. These pet image labels are used to check the accuracy
    of the labels that are returned by the classifier function, since the
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    in_files = listdir(image_dir)
    results_dic = dict()

    for idx in range(0, len(in_files), 1):
        if in_files[idx][0] != ".":
            pet_label = (in_files[idx][:in_files[idx].rindex("_")]).replace("_", " ").lower()
            if in_files[idx] not in results_dic:
                results_dic[in_files[idx]] = [pet_label]

    return results_dic
