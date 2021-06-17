# FDA  Submission

**Padma Chandramouli**

**Chest Xray Analyzer for detecting Pneumonia**

## Algorithm Description 

### 1. General Information

**Intended to assist Radiologist in identifying if xray imaging indicates Pneumonia condition.It is not intended for use in supporting life or sustaining life.** 

**Indications for Use: Assist Radiologist in screening Pneomonia between the ages 35-65 year old patients**

**Device Limitations: Difficult to detect Pneumonia when the patient has multiple conditions. **

**Clinical Impact of Performance: 
***From clinical prespective,we need to identify as many Postive cases of Pneumonia as possible the more the better. If we misclassify certain negative cases as positives(False Positives are a bit higher) it should be accpetable because we can perform further tests to confirm Pneumonia. However we should not miss Positive cases(least False Negatives) Hence Recall plays a critical role and becomes most important measure of performance in clinical scenario for identifying Pneumonia.*** 


### 2. Algorithm Design and Function

<< Insert Algorithm Flowchart >>

**DICOM Checking Steps: Run inference on only valid Dicom images for Pneumonia i.e. we check if xray images are of chest, the position the image was taken i.e.'AP'or 'PA' and modality being DX**

**Exploratory Data Analysis:**
***1) Data Distribution based on Patient Demography - Age,Gender: We have analysed that data based on Gender and Age these are the only details that have been provided to us. As seen in graphs above majority of Pneumonia cases we found are between 20-75 years. There are more Male count (830) then Female count(550) but the difference is not stark. We do not need to split the training data based on gender or Age inorder to have a balanced training data. However we should mention that intended use of algorithm is restricted to patients of age between 20-75 Yrs.***

***2) The x-ray views taken - AP,PA - We analysed that AP has higher counts(800) then PA(600) however again we do not need to split the training data to create a balance data based on views.***

***3) The number of cases of Pnumonia: There is a stark difference between Pneumonia and non Pneumonia cases.There are 1431 Pneumonia Cases. Where as there are 110689 Non Pneumonia Cases. So we do need to split the training data inorder to have Non Penumonia cases close to Pneumonia cases in order to have a balanced data set for training.***

***4) Distribution of other diseases that are comorbid with pneumonia : The most common disease that co-exists with Pneumonia is Infiltration.We can assume that this will be a challenge if we have to identify Infiltration condition from Pneumonia cases, however thats not our current use case.***

***Conclusion:
Number of Pnumonia vs Non-Pnumonia needs to be taken into account while splitting training data. The need to be equal in order to create a balanced training dataset.
'Infiltration','Edema','Effusion' and 'Atelectasis' are pretty close in intensity level to pneumonia.We can include these dieases that are comorbid as well.***

**Preprocessing Steps for training set: 
All images where Resized to (224,224)  so it could be accepted as input to the VGG model and normalized **

**Preprocessing Steps for validation set: No Image augmentation was done in validation set, the images where however nomlaized and resized to(224,224).

**CNN Architecture:Architecture uses transfer learning to use VGG16 model with last Maxpool layer replaced with 4 Fully connected layers. Each of these 4 layers have a Relu activation function and are followed by Dropout layer to reduce overfitting. The 5th layer has an activation Sigmoid to determine probability of Pneumonia. **


### 3. Algorithm Training

**Parameters:**
* Types of augmentation used during training : Image Augmentation was done on training data set as follows:Normalize the image,random image data sets where horizontally flipped,used a bit of shearing, shifted height and width a bit by 0.01 and rotated the image by an angle of 1.0 . Also zooming by a factor of 0.01.
* Batch size =32
* Optimizer learning rate : 1e-6. the low learning rate provided smoother validation and training loss curves. Batch size of 32 was used for training and a batch size of 100 for validation dataset.
* Layers of pre-existing architecture that were frozen: block1_conv1 to block5_conv3
* Layers of pre-existing architecture that were fine-tuned:block5_pool
* Layers added to pre-existing architecture: 5 fully connected layers. 


<< Insert algorithm training performance visualization >> 

<< Insert P-R curve >>plot_roc_curve() and plot_precision_recall_curve() from Build and Train Model notebook

**Final Threshold and Explanation:**
***the average precision is 0.2 ,high False Positives,this means a huge number of non-Pneumonia pateints are being diagnized as having Pneumonia.The recall being 0.64 could be improved if this needs to be used in clinical scenario.With Recall being 0.64 we know that good number of positive cases are being identified. I will conclude that my algorithm cannot be used in clinical scenario.We need to work on improving Recall to atleast 90%+ and precision to 80% . If patients with no pneumonia are being misdiagnized with Pneumonia because we can still run additional tests to confirm patient's condition.Hence I am not concerned about improving Precision a lot.***

### 4. Databases
 (For the below, include visualizations as they are useful and relevant)

**Description of Training Dataset:Split data to 20% validation set and 80% Training set. We also create balanced training set containing same number of Pneumonia and non Pneumonia cases.** 


**Description of Validation Dataset: Validation dataset should not be augmented. However they need to be resized to match the input dimensions and normalize them. There is no need to create Balanced data set.However we used Non Neumonia cases as 4 times the count of Pneumonia sicne there is huge number of dataset for non Pneumonia cases. ** 


### 5. Ground Truth
"pneumonia_class" can be used as ground truth for the algorithm. However in reality we need to rely on existing device/aglorithm to compare performance with or use silver standard.



### 6. FDA Validation Plan

**Patient Population Description for FDA Validation Dataset:** The training data had majority data from age group of 35-70. So the algorithm can be used for Pneumonia detection int the age group of 35-70.

**Ground Truth Acquisition Methodology: For now its Kaggal, however in reality we need to collaborate with hospitals/clinics to get data and make sure that we have permission to use patient personal information or rather not use data that would identify patient and violiate HIPAA ** 

**Algorithm Performance Standard: It is difficult to get a gold standard We could compare our algorithm with the same xray images that was run through 2-3 radiologists. and then come up with ground truth based on observations of these 3 radiologists.**
