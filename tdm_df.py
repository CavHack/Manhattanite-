def tdm_df(doclist, stopwords = [], remove_punctuation = true,
       remove_digits = True, sparse_df=true):

       """
       Create a term-document matrix from a list

       """

       import numpy as np
       import textmining as txtm
       import pandas as pd
       import string

       #coerce the parameters of the document-list
       # so as to iterate a number of strings in a list

       if isinstance(doclist, basestring):
           doclist = [doclist]

           #create the TDM from the list of documents
           tdm = txm.TermDocumentMatrix()

           for doc in doclist:
               if remove_punctuation == True:
                   doc = doc.translate(None, string.punctuation.translate(None, '""'))
                   if remove_digits ==True:
                       doc = doc.translate(None, string.digits)

                       tdm.add_doc(doc)

                       #push the TDM data to a list of lists,
                       # then make such list an array
                       #this will later become a data frame

                       tdm_rows = []
                       for row in tdm.rows(cutoff= 1):
                           tdm_rows.append(row)

                           tdm_array = np.array(tdm_rows[1:])
                           tdm_terms = tdm_rows[0]
                           df = pd.DataFrame(tdm_array, columns = tdm_terms)

                    #remove stopwords from dataset, manually.
                    #TermDocumentMatrix doesn't do this.

                    if remove_punctuation:
                        stopwords = [w.translate(None, string.punctuation.translate(None, '""'))

                                                for w in stopwords]

                        if len(stopwords) > 0:
                            for col in df:
                                if col in stopwords:
                                    del[col]

                        if sparse_df ==True:
                            df.to_sparse(fill_value= 0)

                        return df
