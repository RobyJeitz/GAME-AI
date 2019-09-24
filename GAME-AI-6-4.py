#!/usr/bin/env python
# coding: utf-8

# In[146]:


import math
from IPython.core.debugger import set_trace


# In[271]:


def DT_LEARNING(examples, labels, attributes, parent_examples, parent_labels):
    if len(examples) == 0:
        if PLURALITY_VAL(parent_labels) == 0:
            return '-'
        else:
            return '+'
    elif all(las == labels[0] for las in labels):
        if labels[0] == 0:
            return '-'
        else:
            return '+' #todo
    elif len(attributes) == 0:
        if PLURALITY_VAL(labels) == 0:
            return '-'
        else:
            return '+'
    else:
        at = IMPORTANCE(attributes, examples, labels)
        pvalues = prominent_value(at, examples)
        x = ''
        y = ''
        if len(pvalues) > 1:
            x = str(pvalues[0])
            y = str(pvalues[1])
        else:
            x = str(pvalues[0])
            
        att = attributes[at]
        if y == '':
            tree = {'attribute': att,
                    x: {}}
        else:
            tree = {'attribute': att,
                    x: {},
                    y: {}}
        vk = [x, y]
        for cv in vk:
            if cv != '':
                exs = []
                ls = []
                exm = examples.copy()
                for exp in exm:
                    if exp[at] == cv:
                        #set_trace()
                        ls.append(labels[examples.index(exp)])
                        exp.pop(at)
                        exs.append(exp)
                atts = attributes.copy()
                atts.pop(at)
                #set_trace()
                tree[cv] = DT_LEARNING(exs, ls, atts, examples, labels)
    return tree


# In[272]:


def IMPORTANCE(attributes, examples, labels):
    qv = labels.count(1) / len(labels)
    if qv != 0:
        results = []
        def entropie (qv):
            if qv != 0 and qv != 1:
                return -(qv * math.log2(qv) + (1 - qv) * math.log2(1 - qv))
            return 0
        bv = entropie(qv)
        for att in attributes:
            pvalues = prominent_value(attributes.index(att), examples)
            x = ''
            y = ''
            if len(pvalues) > 1:
                x = str(pvalues[0])
                y = str(pvalues[1])
            else:
                x = str(pvalues[0])
            v = []
            xc = 0
            yc = 0
            xv = 0
            yv = 0
            for e in examples:
                if labels[examples.index(e)] == 1 and str(e[attributes.index(att)]) == str(x):
                    xc += 1
                    xv += 1
                elif str(e[attributes.index(att)]) == str(x):
                    xv += 1
                elif labels[examples.index(e)] == 1 and str(e[attributes.index(att)]) == str(y) and str(y) != '':
                    yc += 1
                    yv += 1
                elif str(e[attributes.index(att)]) == str(y) and str(y) != '':
                    yv += 1
                v.append(str(e[attributes.index(att)]))
            if yv == 0:
                yv = 1
                
            remainder = (v.count(x) / len(v)) * entropie(xc / xv) + (v.count(y) / len(v)) * entropie(yc / yv)
            results.append(bv - remainder)
            
        atti = 0
        atti = results.index(max(results))
        #set_trace()
        return atti
    return 0


# In[273]:


def PLURALITY_VAL(labels):
    x0 = labels.count(0)
    x1 = labels.count(1)
    if max(x0, x1) == x0:
        return 0 
    else:
        return 1


# In[274]:


def prominent_value (attribute, examples):
    v = []
    for e in examples:
        v.append(str(e[attribute]))
        
    def unique(list1): 
        # insert the list to the set 
        list_set = set(list1) 
        # convert the set to the list 
        unique_list = (list(list_set))
        return unique_list
    return unique(v)


# In[275]:


examples = [['sunny', 'warm', 'normal', 'strong', 'warm', 'same'],
            ['sunny', 'warm', 'high', 'strong', 'warm', 'same'],
            ['rainy', 'cold', 'high', 'strong', 'warm', 'change'],
            ['sunny', 'warm', 'high', 'strong', 'cool', 'change'],
            ['sunny', 'warm', 'normal', 'weak', 'warm', 'same']]
labels = [1, 1, 0, 1, 0]
attributes = ['sky', 'air', 'humid', 'wind', 'water', 'forecast']

DT_LEARNING(examples, labels, attributes, examples, labels)


# In[ ]:




