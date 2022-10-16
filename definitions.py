def replacer(df):
    for i in df.columns:
        if df[i].dtypes == "object":
            x = df[i].mode()[0]
            df[i]=df[i].fillna(x)
        else:
            x = df[i].mean()
            df[i] = df[i].fillna(x)
    print('Missing Values replaced in DataFrame')
    
def catcon(df):
    cat = []
    con = []
    for i in df.columns:
        if df[i].dtypes=="object":
            cat.append(i)
        else:
            con.append(i)
    print('Categorical and Continuous variables appended')
    return cat, con

def ANOVA(df,cat,con):
    from statsmodels.formula.api import ols
    eqn = str(con) + " ~ " + str(cat)
    model = ols(eqn,df).fit()
    from statsmodels.stats.anova import anova_lm
    Q = anova_lm(model)
    return round(Q.iloc[0:1,4:5].values[0][0],5)          

def chisquare(df,cat1,cat2):
    import pandas as pd
    from scipy.stats import chi2_contingency
    a,b,c,d = chi2_contingency(pd.crosstab(df[cat1],df[cat2]))
    return b