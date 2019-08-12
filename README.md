## Offline Writer Independent Forge signature verification



### Models used
Used a Convolutional Siamese network along with the Constrastive loss function.



### Preprocessing [Preprocessing.py]
Images were converted to grayscale, inverted and scaled down to 0 or up to 255 depending on whether the pixel value was below or above 50(this was done to remove any background specks and proved to simple yet effective technique for this task).



#### Image Cropping [getSignature1.py]
Image copping is done to get only signed part of the image.


### Dataset


Here We created the dataset which consists of 24 genuine and forged signatures each from 10 different signers. The naming convention is as below.
base_path_org = 'Datasets1/full_org/original_%d_%d.jpg'
		Datasets1/full_org/original_1_1.jpg
		Datasets1/full_org/original_1_2.jpg

                .
                .

		Datasets1/full_org/original_1_24.jpg
base_path_forg = 'Datasets1/full_forg/forgeries_%d_%d.jpg'

		Datasets1/full_forg/forgeries_1_1.jpg
		Datasets1/full_org/forgeries_1_2.jpg

                .
                .

		Datasets1/full_org/forgeries_1_24.jpg


you can use the CEDAR signature dataset is one of the benchmark datasets for signature verification. It consists of 24 genuine and forged signatures each from 55 different signers.

[Dataset link](http://www.cedar.buffalo.edu/NIJ/data/signatures.rar)

### Create Pickle File [Dataloaders.py]
Images were grouped in pairs of genuine and forged images, where the label was 0 if both were genuine and of the same writer and 1 otherwise.
5000 image pairs of each label where chosen.
# Offline-Writer-Independent-Forge-signature-verification
# Offline-Writer-Independent-Forge-signature-verification
