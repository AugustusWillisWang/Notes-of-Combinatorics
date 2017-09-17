#read file in lines

paper=""
insection=0
inalign=0

def add(addon):
    global paper
    paper=paper+addon

def convertline(line):
    global paper
    global insection

    if "##" in line:
        paper=paper+r'''    
    \section{'''

        paper=paper+line[3:]
    
        paper=paper+r'''}

'''
        return 0

    if "#" in line:
        return 0

    if "***" in line:
        paper=paper+r'''    
    \newpage
'''
        return 0


    if "@" in line:

        #定义
        if insection==0 and "定义" in line:
            insection="定义"
            name=line[4:]
            add(r'''
    \begin{concept}{'''+name+r'''}
 ''')
            return 0

        if insection=="定义":
            add(r'''
    \end{concept}
 ''')
            insection = 0
            return 0

        #例
        if (insection == 0 and "例" in line):
            insection="例"
            add(r'''
    \begin{example}
    ''')
            return 0


        if (insection=="例"):
            add(r'''    
    \end{example}
''')
            insection = 0
            return 0

        #定理
        if(insection == 0 and "定理" in line):
            insection = "定理"
            add(r'''
    \begin{theorem}
''')
            return 0
        
        if(insection=="定理"):
            insection=0
            add(r'''
    \end{theorem}
''')
            return 0

        #证明
        if(insection==0 and "证明" in line):
            insection="证明"
            add(r'''
    \begin{proof}
''')
            return 0

        if(insection=="证明"):
            insection=0
            add(r'''
    \end{proof}
''')
            return 0

        #解
        if(insection ==0 and "解" in line):
            insection="解"
            add(r'''
    \begin{solution}
''')
            return 0

        if(insection=="解"):
            add(r''' \end{solution}
''')
            return 0


    #若不属于任何特殊情况(没有@)
    add(line)
            
            


#写文件头
file=open("note.md",encoding='utf-8')

lesson=input("lesson:")
time=input("time:")
name=input("recoder:")

head=open('filehead.dat','r',encoding='utf-8').read()
paper=paper+head

paper=paper+r'''\begin{document}
    
    \pagestyle{fancy}
    \lhead{\kaishu 中国科学院大学}
    \chead{}
    \rhead{\kaishu 2017年秋季学期组合数学}
    
    \begin{center}
        {\LARGE \bf 组合数学第'''

paper=paper+lesson

paper=paper+r'''讲}\\
    \end{center}
        \begin{kaishu}
            授课时间: '''

paper=paper+time

paper=paper+r'''\quad
            授课教师: 孙晓明
            \hfill 记录人: '''
paper=paper+name

paper=paper+r'''        \end{kaishu}'''

#逐行处理
while True:
    line =file.readline()
    if not line:
        break
    convertline(line)

#写文件尾
paper=paper+r'''
\end{document}

'''


output=open('output.tex','w',encoding='gb2312')
output.write(paper)

output.close()
file.close()

