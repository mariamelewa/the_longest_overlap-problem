def longest_overlap_brute_force(s1, s2):
    max_length = 0
    longest_overlap = ""

    len1, len2 = len(s1), len(s2)

    # Check suffixes of s1
    for i in range(len1):  
        suffix = s1[i:] 
        length = len(suffix) #length of the whole word
        if length <= len2 and suffix == s2[:length]: #human  #man  
            if length > max_length:
                max_length = length
                longest_overlap = suffix 

    # Check suffixes of s2
    for i in range(len2):    #erase  #paper
        suffix = s2[i:]
        length = len(suffix)
        if length <= len1 and suffix == s1[:length]:   
            if length > max_length:
                max_length = length
                longest_overlap = suffix

    return f"The longest overlapping substring is: \"{longest_overlap}\" of length {max_length}"


# Example 
s1 = "human"
s2 = "woman"
longest_overlap = longest_overlap_brute_force(s1, s2)
print(longest_overlap)

#"human"
#"woman"
#no overlap


#human
#  man  
#man


#   erase  
#paper
#er

#hulkman
#    manhulk 
#hulk


















































# from textblob import TextBlob
# import pandas as pd
# import streamlit as st
# import cleantext


# st.header('Sentiment Analysis')
# with st.expander('Analyze Text'):
#     text = st.text_input('Text here: ')
#     if text:
#         blob = TextBlob(text)
#         st.write('Polarity: ', round(blob.sentiment.polarity,2))
#         st.write('Subjectivity: ', round(blob.sentiment.subjectivity,2))


#     pre = st.text_input('Clean Text: ')
#     if pre:
#         st.write(cleantext.clean(pre, clean_all= False, extra_spaces=True ,
#                                  stopwords=True ,lowercase=True ,numbers=True , punct=True))

# with st.expander('Analyze CSV'):
#     upl = st.file_uploader('Upload file')

#     def score(x):
#         blob1 = TextBlob(x)
#         return blob1.sentiment.polarity


#     def analyze(x):
#         if x >= 0.5:
#             return 'Positive'
#         elif x <= -0.5:
#             return 'Negative'
#         else:
#             return 'Neutral'


#     if upl:
#         df = pd.read_excel(upl)
#         del df['Unnamed: 0']
#         df['score'] = df['tweets'].apply(score)
#         df['analysis'] = df['score'].apply(analyze)
#         st.write(df.head(10))

#         @st.cache
#         def convert_df(df):
#             # IMPORTANT: Cache the conversion to prevent computation on every rerun
#             return df.to_csv().encode('utf-8')

#         csv = convert_df(df)

#         st.download_button(
#             label="Download data as CSV",
#             data=csv,
#             file_name='sentiment.csv',
#             mime='text/csv',
#         )