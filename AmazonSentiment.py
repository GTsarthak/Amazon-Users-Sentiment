import pandas as pd
import numpy as np
import seaborn as sns
df=pd.read_csv(r'C:\Users\Sarthak Gupta\NLP Real World Projects\Amazon User Sentiment\Dataset/Reviews.csv')
df['Helpful%']=np.where(df['HelpfulnessDenominator']>0,df['HelpfulnessNumerator']/df['HelpfulnessDenominator'],-1)
df['%upvote']=pd.cut(df['Helpful%'],bins=[-1,0,0.2,0.4,0.6,0.8,1],labels=['Empty','0-20%','20-40%','40-60%','60-80%','80-100%'])
df_s=df.groupby(['Score','%upvote']).agg({'Id':'count'}).reset_index()


pivot=df_s.pivot(index='%upvote',columns='Score')
df2=df[df['Score']!=3]
X=df2['Text']
y_dict={1:0,2:0,4:1,5:1}
y=df2['Score'].map(y_dict)


from sklearn.feature_extraction.text import CountVectorizer
c=CountVectorizer(stop_words="english")
X_c=c.fit_transform(X)


from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X_c,y)


from sklearn.linear_model import LogisticRegression
log=LogisticRegression()
ml=log.fit(X_train,y_train)
w=c.get_feature_names()


coef=ml.coef_.tolist()[0]
coef_df=pd.DataFrame({'Word':w,'Coefficient':coef})
coef_df=coef_df.sort_values(['Coefficient','Word'],ascending=False)


def text_fit(X,y,nlp_model,ml_model):
    X_c=nlp.fit_transform(X)
    print('features:{}'.format(X_c.shape[1]))
    X_train,X_test,y_train,y_test=train_test_split(X_c,y)
    ml=ml_model.fit(X_test,y_test)
    acc=ml.score(X_test,y_test)
    print(acc)
    
    w=c.get_feature_names()
