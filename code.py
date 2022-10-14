!pip install docx2txt
import docx2txt

job_description = docx2txt.process('/content/sample_description.docx')

resume = docx2txt.process('/content/sample_resume1.docx')
print(job_description)

content = [job_description, resume]

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer()
count_matrix = cv.fit_transform(content) #to convert all testxs into vectories

from sklearn.metrics.pairwise import cosine_similarity
mat = cosine_similarity(count_matrix)
print(mat)

print('Resume Matches by: '+  str(mat[1][0]*100) + '%') #1 , 0 index of the value in the matrix 
