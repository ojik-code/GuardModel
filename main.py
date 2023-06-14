#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import Flask 
from flask import Flask
#create an instance of Flask
app = Flask(__name__)
@app.route('/')
def home():
    return "Hello World"
if __name__ == '__main__':
    app.run(debug=True)


# In[ ]:




