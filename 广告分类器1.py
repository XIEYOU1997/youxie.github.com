#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from xgboost import XGBClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA
from sklearn.model_selection import GridSearchCV
import pandas as pd
import numpy as np
from sklearn.metrics import roc_auc_score
import matplotlib.pyplot as plt
import seaborn as sns
import shap
from sklearn.neural_network import MLPClassifier
import eli5
from eli5.sklearn import PermutationImportance
from imblearn.over_sampling import SMOTE

#将features名从所在文件中读取出来放在list中
f=open('/Users/youxie/Downloads/ali-ad-dataset/ad.names.txt','r',encoding='gbk')
results=[]
link=f.readlines()
for fileline in link:
    str=fileline.split(':')[0]
    results.append(str)
f.close()
#读取数据并设置列名
data=pd.read_csv("/Users/youxie/Downloads/ali-ad-dataset/ad.data.txt",sep=',',header=None,names=results)
#将数据中的问号改为空值
data[results[0]]=np.where(data[results[0]]=='   ?',np.nan,data[results[0]])
data[results[1]]=np.where(data[results[1]]=='   ?',np.nan,data[results[1]])
data[results[2]]=np.where(data[results[2]]=='     ?',np.nan,data[results[2]])
data[results[3]]=np.where(data[results[3]]=='?',np.nan,data[results[3]])
#将ad设为0，将nonad设为1
data[results[-1]]=np.where(data[results[-1]]=='nonad.',1,0)
#分别对应找到所有ad和nonad对应数据
data0=data.loc[data[results[-1]]==0]
data1=data.loc[data[results[-1]]==1]
print(data0.shape)
print(data1.shape)
#将所有数据转换成int或者float
data0=data0.apply(pd.to_numeric)
data1=data1.apply(pd.to_numeric)
#分别算出前四列广告和非广告的平均值
fill_value00=data0[results[0]].fillna(0).mean()
fill_value01=data0[results[1]].fillna(0).mean()
fill_value02=data0[results[2]].fillna(0).mean()
fill_value03=data0[results[3]].fillna(0).mean()
fill_value10=data1[results[0]].fillna(0).mean()
fill_value11=data1[results[1]].fillna(0).mean()
fill_value12=data1[results[2]].fillna(0).mean()
fill_value13=data1[results[3]].fillna(0).mean()
#用对应值填充缺失值
data0[results[0]].replace(np.nan,fill_value00,inplace=True)
data0[results[1]].replace(np.nan,fill_value01,inplace=True)
data0[results[2]].replace(np.nan,fill_value02,inplace=True)
data0[results[3]].replace(np.nan,fill_value03,inplace=True)
data1[results[0]].replace(np.nan,fill_value10,inplace=True)
data1[results[1]].replace(np.nan,fill_value11,inplace=True)
data1[results[2]].replace(np.nan,fill_value12,inplace=True)
data1[results[3]].replace(np.nan,fill_value13,inplace=True)
#将两个表格再重新连接
data=data0.append(data1)
#指定x,y
x_cols=[x for x in data.columns if x!='Class']
x=data[x_cols]
y=data[data.columns[-1]]
# 需要使用过抽样的分类器
classifiers1 = [XGBClassifier(),MLPClassifier()]
# 使用SMOTE方法进行过抽样处理
model_smote = SMOTE() # 建立SMOTE模型对象
x_smote_resampled, y_smote_resampled = model_smote.fit_sample(x,y) # 输入数据并作过抽样处理
x_smote_resampled = pd.DataFrame(x_smote_resampled) # 将数据转换为数据框并命名列名
y_smote_resampled = pd.DataFrame(y_smote_resampled) # 将数据转换为数据框并命名列名
smote_resampled = pd.concat([x_smote_resampled, y_smote_resampled],axis=1) # 按列合并数据框
groupby_data_smote = smote_resampled.groupby('Class').count() # 对label做分类汇总
print (groupby_data_smote) # 打印输出经过SMOTE处理后的数据集样本分类分布
# 数据分割
x_train1, x_test1, y_train1, y_test1 = train_test_split(x_smote_resampled, y_smote_resampled, test_size=0.3, random_state=3)
# 分类器名称
classifiers_names1 = ['xgboost',
                      'mlp']

# 分类器参数
classifiers_param_grid1 = [{'xgboost__learning_rate':[0.09],
                            'xgboost__max_depth': [7]},
                           {#     'mlp__hidden_layer_sizes':[(100,20)],
                            'mlp__solver':['adam'],
                            #     'mlp__learning_rate':['constant','invscaling','adaptive'],
                            'mlp__max_iter':[300],
                            'mlp__batch_size':[150],
                            'mlp__activation':['relu']}]


def smote_classifier(classifiers1, classifiers_names1, classifiers_param_grid1, x_train1, y_train1, x_test1):
    for classifier, classifier_name, classifier_param_grid in zip(classifiers1, classifiers_names1,classifiers_param_grid1):
        pipeline = Pipeline([('ss', StandardScaler()),
                             ('mm', MinMaxScaler()),
                             ('pca', PCA(n_components=0.95)),
                             (classifier_name, classifier)])
        gridsearch = GridSearchCV(estimator=pipeline, param_grid=classifier_param_grid, scoring='roc_auc',cv=5, n_jobs=4)
        search = gridsearch.fit(x_train1, y_train1)
        y_predict = gridsearch.predict(x_test1)
        print('GridSearch 最优参数：', search.best_params_)
        print('GridSearch 最优分数：%0.4lf' % search.best_score_)
        print('准确率: %0.4lf' % roc_auc_score(y_test1, y_predict))
        roc_auc_score_list.append(float('%0.4lf' % roc_auc_score(y_test1, y_predict)))


# 不需要使用过抽样的分类器
classifiers2 = [LogisticRegression()]
# 重新分割没有过抽样的数据
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=3)
# 分类器名称
classifiers_names2 = ['lr']

# 分类器参数
classifiers_param_grid2 = [{'lr__class_weight': ['balanced'],
                            'lr__C':[0.7],
                            'lr__solver': ['liblinear']}]


def nsmote_classifier(classifiers2, classifiers_names2, classifiers_param_grid2, x_train, y_train, x_test):
    for classifier, classifier_name, classifier_param_grid in zip(classifiers2, classifiers_names2,classifiers_param_grid2):
        pipeline = Pipeline([('ss', StandardScaler()),
                             ('mm', MinMaxScaler()),
                             ('pca', PCA(n_components=0.95)),
                             (classifier_name, classifier)])
        gridsearch = GridSearchCV(estimator=pipeline, param_grid=classifier_param_grid, scoring='roc_auc',cv=5, n_jobs=4)
        search = gridsearch.fit(x_train, y_train)
        y_predict = gridsearch.predict(x_test)
        print('GridSearch 最优参数：', search.best_params_)
        print('GridSearch 最优分数：%0.4lf' % search.best_score_)
        print('准确率: %0.4lf' % roc_auc_score(y_test, y_predict))
        roc_auc_score_list.append(float('%0.4lf' % roc_auc_score(y_test, y_predict)))


if __name__ == '__main__':
    roc_auc_score_list = []
    smote_classifier(classifiers1, classifiers_names1, classifiers_param_grid1, x_train1, y_train1, x_test1)
    nsmote_classifier(classifiers2, classifiers_names2, classifiers_param_grid2, x_train, y_train, x_test)
    classifiers_names = ['XGB','MLP','LR']
    df = pd.DataFrame({'Classifier': classifiers_names, 'AUC': roc_auc_score_list})
    sns.lineplot(x='Classifier', y='AUC', data=df)
    plt.title("Comparision between different classifiers ")
    print(df)
    plt.savefig('/Users/youxie/Desktop/阿里实习/comparision.png')
    plt.show()
#XGBoost特征贡献度
xgb = XGBClassifier(learning_rate=0.09, max_depth=7)
xgb = xgb.fit(x_train, y_train)
mybooster = xgb.get_booster()
model_bytearray = mybooster.save_raw()[4:]
def myfun(self=None):
    return model_bytearray
mybooster.save_raw = myfun
explainer = shap.TreeExplainer(xgb, feature_perturbation="tree_path_dependent")
shap_values = explainer.shap_values(x_test)
print(shap_values.shape)
shap.summary_plot(shap_values, x_test)
shap.summary_plot(shap_values, x_test, plot_type="bar")
#神经网络特征贡献度
mlp=MLPClassifier(solver='adam',max_iter=300,activation='relu',batch_size=150)
mlp=mlp.fit(x_train,y_train)
perm=PermutationImportance(mlp).fit(x_test,y_test)
explanation = eli5.formatters.as_dataframe.explain_weights_df(perm, 
feature_names=x_test.columns.tolist())
explanation.head(10).plot(x='feature',y='weight',kind='bar')
#逻辑回归特征贡献度
lr = LogisticRegression(C=2, class_weight='balanced', solver='liblinear')
lr = lr.fit(x_train, y_train)
importances = lr.coef_
features = list(x_test.columns)
importances_frame = pd.DataFrame({
    'Importance': list(abs(importances)[0]),
    'Feature': list(features)
})
importances_frame.sort_values(by='Importance', inplace=True,ascending=False)
importances_frame.head(10).plot(kind='bar', x='Feature', figsize=(8, 8))
plt.show()

