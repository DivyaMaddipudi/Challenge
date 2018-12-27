import numpy as np 
import pandas as pd 
import matplotlib as mpl
import matplotlib.pyplot as plt
from os import path
from PIL import Image
from matplotlib import style
import csv
from subprocess import check_output
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

'''
def grey_color_func(word, font_size, position,orientation,random_state=None, **kwargs):
	return("hsl(0,0%%, %d%%)" % np.random.randint(5,5))
'''


text=open('/tact/youtube/comments.txt').read()

stopwords = set(STOPWORDS)

mask = np.array(Image.open('/tact/youtube/pictures/twitter_mask.png'))

wc = WordCloud(background_color="white", 
			   max_words=100, 
			   mask=mask,
               stopwords=stopwords, 
               contour_width=3, 
               contour_color='green'
               )

# generate word cloud
wc.generate(text)

image_colors = ImageColorGenerator(mask)

#show
plt.figure(figsize=(3,3))
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.show()