# 组合数学笔记

使用markdown与latex进行排版

使用mdconverter.py来将markdown转为按模板格式的tex文档并导出

## Markdown语法

参见<http://www.appinn.com/markdown/>

## Latex语法

参见<http://blog.csdn.net/zdk930519/article/details/54137476>

行内公式  $formula$

行间公式

$$formula$$

公式编号

$$foo$$(0)

上角标

$$A^{n}$$

下角标

$$A_{n}$$

分式

$$\frac{a}{b}$$

根式

$$\sqrt{2000}$$

$$\sqrt[3]{2000}$$

求和

$$\sum$$

ps:求和号配合上下角标语法使用

$$\sum_{i=0}^n i^2$$

同理，有：

积分

$$\int$$

上下划线

$$\overline{foo}^{illu}\underline{foo}$$

上下括弧

$$\overbrace{foo}^{illustrate}$$

数学重音

$$
\hat{a}
\check{a}
\breve{a}
\tilde{a}
\bar{a}
\vec{a}
\acute{a}
\grave{a}
\dot{a}
\ddot{a}
$$

atop 公式叠加

$${def \atop =}$$

组合

$${m\choose n}$$

空心字体mathbb

$${\mathbb{R},\mathbb{Q}}$$

空格

$$a \quad b \  c$$

集合相关

$$ \in \subset \subsetneqq \not \in \cap \cup \setminus \emptyset$$

希腊字母

<http://blog.163.com/goldman2000@126/blog/static/167296895201223104411122/>

$$\omega \lambda \alpha \beta \gamma \phi \delta$$

大于小于大于等于

$$ \le \leq \ge \geq < > $$

## 导出

$pandoc -N -s --toc --smart --latex-engine=xelatex -V CJKmainfont='PingFang SC' -V mainfont='Monaco' -V geometry:margin=1in note.md -o output.pdf
