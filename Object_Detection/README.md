# ReadMe

首先我們使用DataAugmentationForObjectDetection

所以第一步是想使用git clone https://github.com/Paperspace/DataAugmentationForObjectDetection 將這個資料下載下來
接著在data_process中使用data_aug()這個function裡面使用
我們為了方便把code寫得有點醜，我們是直接把他寫死然後一個一個換aug的效果
最後把產生出來的txt和img利用下面的merge整合在一個資料夾裡面

而aug&split_train_val.ipynb檔案是我們當初拿來做測試的，裡面主要只用train_val這個功能
evaluate.py是老師給的檔案

當img和txt都整合在一起之後就可以在kaggle02_report裡面的model進行training