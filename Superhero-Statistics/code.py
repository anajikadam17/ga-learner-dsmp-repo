# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#path of the data file- path

#Code starts here 
data = pd.read_csv(path)
data['Gender'].replace('-','Agender')
gender_count = data['Gender'].value_counts()
gender_count.plot(kind='bar')
plt.show()


# --------------
#Code starts here

alignment = data['Alignment'].value_counts()

plt.pie(alignment,labels=alignment.index)
plt.show()



# --------------
#Code starts here

sc_df = data[['Strength','Combat']]


# sc_covariance = (((sc_df['Strength'] - sc_df['Strength'].mean()) *(sc_df['Combat'] - sc_df['Combat'].mean())).sum() / (sc_df.shape[0])).round(2)
sc_covariance = sc_df.Strength.cov(sc_df.Combat)
print(sc_covariance)

sc_strength = sc_df.Strength.std()
print(sc_strength)

sc_combat = sc_df.Combat.std()
print(sc_combat)
sc_pearson = (sc_covariance / (sc_strength * sc_combat))
print(sc_pearson)
ic_df = data[['Intelligence','Combat']]

ic_covariance = ic_df.Intelligence.cov(ic_df.Combat)
print(ic_covariance)
ic_intelligence = ic_df.Intelligence.std()
print(ic_intelligence)
ic_combat = ic_df.Combat.std()
print(ic_combat)

ic_pearson = (ic_covariance / (ic_intelligence * ic_combat)).round(2)
print(ic_pearson)




# --------------
#Code starts here

total_high = data['Total'].quantile(.99)

super_best = data[data['Total'] > total_high]
 
super_best_names = list(super_best['Name'])

print(super_best_names)


# --------------
#Code starts here

fig, (ax_1, ax_2, ax_3) = plt.subplots(3,1)
plt.subplot(3,1,1)
ax_1.boxplot(data['Intelligence'])
plt.subplot(3,1,2)
ax_2.boxplot(data['Speed'])
plt.subplot(3,1,3)
ax_3.boxplot(data['Power'])

plt.show()


