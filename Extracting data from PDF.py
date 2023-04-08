#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd
import pdfquery

pdf = PDFQuery('kt/SSRN-id3668857.pdf')
pdf.load()

#convert the pdf to XML
pdf.tree.write('kt/SSRN-id3668857.pdf.xml', pretty_print = True)
pdf


# In[14]:


# Use CSS-like selectors to locate the elements
text_elements = pdf.pq('LTTextLineHorizontal').text()


print(text_elements)


# In[ ]:




