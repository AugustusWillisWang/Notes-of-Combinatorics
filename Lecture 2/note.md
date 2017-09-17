# 组合数学 1.2 (2017.9.12)

by: 王华强 段江飞

## 组合数作为多项式的基

上一节结尾, 我们讨论了$1^2+2^2+3^2\cdots +n^2$的求法, 其可由${n\choose 2}=n^2/2-n/2$求出

由${n\choose 3}$, 以及朱世杰恒等式:

$${k\choose k}+{k+1\choose k}+\cdots +{n\choose k}={n+1\choose k}$$

可求得$1^3+2^3+3^3+\cdots+n^3$

考虑对于$x^k$, 是否有$x^k=?{x\choose k}+?{x\choose k-1}+\cdots+{x\choose 1}$

例如:$x^3=6{x\choose 3}+6{x\choose 2}+\cdots+{x \choose 1}$

可以发现:$x^k=k!{x\choose k}+\cdots$

***

定理: 存在$C_k,C_{k-1},\cdots$ s.t.

$$x^k=\sum_{j=0}^k C_j{x\choose j}$$

其中$C_k,C_{k-1},\cdots$与Stirling numbers of the second kind相关

$S_2(k,j)=\frac{C(k,j)}{k!}$ , $S_2$为Stirling numbers of the second kind

## 整系数多项式

定义: P(x)称为整值多项式, 若对于所有的整数x, P(x)为整数  

思考：如何刻画P(x)的形式？

讨论:  求 $deg(P(x)) \le d$ 的整值多项式的刻画?  

${x \choose i}$是关于$x$的$i$次多项式，且是整数  

猜想: 设$C_d,C_{d-1},\cdots, C_0$是整数

$$P(x)=C_d{x\choose d}+C_{d-1}{x\choose d-1}+\cdots+C_0{x \choose 0}$$

显然, P(x) 是 {${x\choose d},\cdots,{x\choose 0}$}与{$x^d,\cdots,1$} 张成的空间中的的多项式，但其张成空间是整数环吗？

存在 martix A

$$A(1,x^1,\cdots,x^d)^T=({x \choose 0},{x\choose 1},\cdots,{x\choose d})^T$$   
显然A中元素不一定取整, 例如: 

${x\choose 2}$ 用 $1,x^1,x^2$ 的刻画  

即整数没有覆盖刻画张成空间的系数

问题: ${x\choose d},\cdots,{x\choose 0}$ 是否刻画了所有这样的多项式?


***

定理: $P(x)$是整系数多项式$\iff$存在整系数$C_d,C_{d-1},\cdots,C_0$使得$P(x)=C_d{x\choose d}+C_{d-1}{x\choose d-1}+\cdots+C_0{x \choose 0}$

证明 $\quad$ $1^{\circ}$ 取一组基${x\choose d},\cdots,{x\choose 0}$

P(0)=$C_0$ 整数

P(1)=$C_0+C_1$ 整数

$\cdots$

P(i)=$1\cdot C_i+k\cdot C_{i-1}+\cdots$

可推出P(0)......P(d)为整数 

$2^\circ \quad {x \choose i}$显然是整数，$P(x)$的系数也是整数，则 $P(x)$是整系数多式 $\quad \quad \blacksquare$


证明此定理的时候只用到了 $d+1$ 个整点 $P(0), P(1), \cdots, P(d)$

猜想: 此定理是否可推广到 $P(x)$ 在任意 $(d+1)$ 个整点的值为整数?



反例： $P(x) = \frac{x}{2}$ 在偶数点处均为整数，但不是整数多项式

解答: $(d+1)$ 不是随意取得，必须是$(d+1)$个连续点

***
定理: 若$deg(P(x)) = d$,则$P(x)$是整系数多项式$\iff$$p(x)$ 在$d+1$ 个连续整点处取值为整数

***

证明：$1^{\circ}$  $P(x)$是整系数多项式，显然，$p(x)$ 在$d+1$ 个连续整点处取值为整数

$2^\circ$ $P(x)$在连续$d+1$个整点处取值为整数 $P(n), P(n+1), \cdots, P(n+d) \in \mathbb{Z}$  

对$P(x)$进行平移，$Q(x) \triangleq P(x+n)$

则 $Q(0), Q(1), \cdots, Q(d) \in \mathbb{Z}$


$\exists \tilde{C_0}, \tilde{C_1}, \cdots, \tilde{C_d} \quad s.t.$

$$Q(x) = \sum_{i=0}^{d}\tilde{C_i}{x \choose i} \Rightarrow P(x) = Q(x-n) = \sum_{i=0}^{d}\tilde{C_i}{x-n \choose i} \quad \quad \quad \blacksquare$$

将${x-n \choose i}$化为${x \choose i}$的形式

$${x-n \choose i} = \tilde{\tilde{C_i}}{x \choose i}+\tilde{\tilde{C_{i-1}}}{x \choose i-1}+\cdots+\tilde{\tilde{C_{0}}}{x \choose 0}$$

1. 考虑 $R(x) = {x-n \choose i} \quad  R(0), R(1), \cdots, R(i) \in \mathbb{Z}$ 由定理可证

2. $Vandermonde \quad formula$

$${m+n \choose i} = {m \choose 0}{n \choose i} + {m \choose 1}{n\choose i-1}+\cdots+{n\choose i}{m\choose 0}$$

对任意 $m,n\in \mathbb{R}$ 总是成立的

$${x-n \choose i} = {-n \choose 0}{x \choose i} + {-n \choose 1}{x\choose i-1}+\cdots+{-n\choose i}{x\choose 0}$$

## 抛硬币

抛 $n$ 次硬币，其中 $m$ 次正面向上的概率为

$$P=\frac{n \choose m}{2^n}$$

${n \choose 0}, {n \choose 1}, \cdots, {n \choose n}$ 呈现先增后减的趋势，随着 $m$ 的增大，$P$ 先增大后减小

估算抛 $2n$ 次硬币，恰好 $n$ 次正面向上的概率

$$\frac{2n \choose n}{2^{2n}} = \frac{(2n)!}{n!\cdot n!}\cdot\frac{1}{2^{2n}}\backsim \frac{1}{\sqrt{n}}$$

这用到了$stirling \quad formula$

$$n! \backsim \sqrt{2\pi n}(\frac{n}{e})^n$$

$$ln(n!) \backsim (n+\frac{1}{2})lnn-n+O(1)$$

我们估算 $n!$ 量级

$$\int_{1}^{n}lnx dx \le \sum_{i=1}^{n}lni \le \int_{1}^{n+1}lnxdx$$




$$\Rightarrow nlnn-n+1 \le \sum_{i=1}^{n}lni \le (n+1)ln(n+1)-n$$

估算$lnk$时，右多算了一部分面积，右估算值多算的面积为

$\int_{k}^{k+1}lnxdx-lnk = (k+1)ln(1+\frac{1}{k})-1=(k+1)(\frac{1}{k}-\frac{1}{2k^2}+\frac{1}{3k^3}-\cdots)-1 = \frac{1}{2k}-\frac{1}{6k^2}+\cdots$

$\sum_{k=1}^{n}(\int_{k}^{k+1}lnxdx-lnk)= \frac{1}{2}\cdot(1+\frac{1}{2}+\cdots+\frac{1}{n})+O(1)=\frac{1}{2}lnn+O(1)$


$ln(n!)= (n+1)ln(n+1)-n-\frac{1}{2}lnn+O(1) \simeq(n+1)lnn-n-\frac{1}{2}lnn+O(1)= (n+\frac{1}{2})lnn-n+O(1)$
