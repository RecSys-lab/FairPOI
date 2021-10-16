import os


def dataset_path(dir_path: str, dataset: str, split: str, format: str) -> str:
    """
    This function returns the path to the current dataset

    :param dataset: the name of the dataset
    :param split: the portsion of the split (i.e., train, test, tune)
    :param format: the format of the dataset
    :return: a full path to the existing dataset
    """
    return dir_path + dataset + "/" + dataset + "_" + split + format


def mk_dir(dataset, type="binary"):
    full_path = dir_path + dataset + "_" + type
    if not os.path.exists(full_path):
        os.makedirs(full_path)
    else:
        print("\nDirectory %s already exists. \n" % full_path)

    return dataset + "_" + type


def to_binary(sample, new_path):
    new_data = open(new_path, 'w')
    sample_data = open(sample, 'r').readlines()
    for eachline in sample_data:
        uid, lid, _ = eachline.split('\t')
        new_data.write(uid + '\t' + lid + '\t' + str(1) + '\n')

    new_data.close()


if __name__ == '__main__':
    dir_path = "../datasets/"
    format = ".txt"
    datasets = ["Gowalla", "Yelp"]
    splits = ["train", "test", "tune"]

    # iterate over datasets
    for dataset in datasets:
        # create a new directory for the new generated dataset
        new_dataset = mk_dir(dataset=dataset)
        # iterate over different split of dataset
        for split in splits:
            data_path = dataset_path(dir_path=dir_path, dataset=dataset, split=split, format=format)
            #
            new_dataset_path = dataset_path(dir_path=dir_path, dataset=new_dataset, split=split, format=format)
            #
            to_binary(sample=data_path, new_path=new_dataset_path)