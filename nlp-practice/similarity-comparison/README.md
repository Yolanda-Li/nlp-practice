## 基于连体深度神经网络的文本相似度测试模型


暹罗神经网络是一类**神经网络架构，包含两个或多个** **相同的** **子网**。 *相同*这里表示它们具有相同参数的相同配置和重量。 参数更新跨两个子网进行镜像。

它是基于keras的深暹罗双向LSTM网络实现，使用字嵌入来捕获短语/句子相似性。

以下是相同的架构描述。

![rch_imag](images/arch_image.png)

## 用法

###训练数据准备

1. 从网站下载所需数据

      [日本学习者的书面作文语料库](http://sakubun.jpn.org/)
 
2. 解压数据，将文件夹命名为thedata


###Mecab分词系统安装


1. 无法使用pip安装Mecab时，从网站下载安装包
 
    [Mecab Japanese word segmentation system](http://taku910.github.io/mecab/)

2. 根据安装教程安装Mecab

    [windows10+py36+MeCab安装总结](https://blog.csdn.net/ZYXpaidaxing/article/details/81913708)


### 配置环境

1. 安装python3.6.6
2. 安装pycharm
3. 安装virtualenv10.0.1

       pip install virtualenv

4. 构造项目目录，为项目安装虚拟环境

       virtualenv venv --no-site-packages

5. 启动虚拟环境，安装所需类库
    * Linux或Mac启用虚拟环境
    
          source venv/bin/activate
    
    * Windows启用虚拟环境
    
          venv\Scripts\activate
    
6. 安装所需类库
    
       pip install -r requirements.txt

7. 在虚拟环境中训练模型测试模型

       python controller.py 
  
8. 离开虚拟环境

       deactivate


###预测文本相似度

1. 运行app.py

       python app.py

2. 使用postman打开http://172.29.226.176:5500/eval

3. 设置请求为Post，在Headers里设置KEY为Content-Type，VALUE为application/form-data

4. 设置Body的KEY依次为article_content、record_content、content_type、record_id，类型均为txt

5. 在article_content与record_content中输入待识别文本的base64编码，在content_type中输入txt，设置record_id，然后点击Send发送数据

6. 获得返回结果，同时结果会被发送到 http://172.29.226.64:8080/api/score/receive


### 参考:

1. [Siamese Recurrent Architectures for Learning Sentence Similarity (2016)](https://www.aaai.org/ocs/index.php/AAAI/AAAI16/paper/view/12195)
2. Inspired from Tensorflow Implementation of  https://github.com/dhwajraj/deep-siamese-text-similarity
3. [Lstm Siamese Text Similarity from Github](https://github.com/amansrivastava17/lstm-siamese-text-similarity)