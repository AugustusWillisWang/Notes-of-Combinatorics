# 组合数学 1.2 (2017.9.12)

by: 王华强

## 组合数作为多项式的基

上一节结尾, 我们讨论了$1^2+2^2+3^3\cdots +n^2$的求法, 其可由${n\choose 2}=n^2/2-n/2$求出

由${n\choose 3}, 以及朱世杰恒等式:

$${k\choose k}+{k+1\choose k}+\cdots +{n\choose k}={n+1\choose k}$$

可求得$1^3+2^3+3^3+\cdots+n^3$

考虑对于$X^k$, 是否有$X^k=?{x\choose k}+?{x\choose k-1}+\cdots+{x\choose 1}$

例如:$X^3=6{x\choose 3}+6{x\choose 2}+\cdots+{x\choose 1}$

可以发现:$X^k=k!{x\choose k}$

***

定理: 存在$C_k,C_{k-1},\cdots$ st.

$$x^k=\sum_{j=0}^k C_j{x\choose j}$$

其中$C_k,C_{k-1},\cdots$与2nd pluse stirling number 相关

$S_2(k,j)=C(k,j)/k!$ , $S_2$为2nd plus stirling number

## 整系数多项式

定义: P(x)称为整值多项式, 若对于所有的整数x, P(x)为整数

讨论: 求deg<=5的行列式的刻画?

设$C_d,C_d-1,\cdots C_0$是整数

$$P(x)=C_d{x\choose d}+C_{d-1}{x\choose d-1}+\cdots+C_0$$

显然, ${x\choose d},\cdots,{x\choose 0}$与$x^d,\cdots,1$是P(x)的一组基

于是存在 martix A, such that $A(1,x^1,\cdots,x^d)^T=({x\choose 0},{x\choose 1},\cdots,{X\choose d}^T$ 然而显然A中元素不一定取整, 例如: 

${x\choose 2}$ 用 $1,x^1,x^2$ 的刻画

问题是: ${x\choose d},\cdots,{x\choose 0}$是否刻画了所有这样的多项式?


***

定理: P(x)是整系数多项式 iff 存在整系数$C_d,C_d-1,\cdots,C_0$使得$P(x)=C_d{x\choose d}+C_{d-1}{x\choose d-1}+\cdots+C_0$

证明: 取基${x\choose d},\cdots,{x\choose 0}$

P(0)=$C_0$ 整数

P(1)=$C_0+C_1$ 整数

$\cdots$

P(i)=$1*C_i+kC_{i-1}\cdots$

故P(0)......P(d)为整数 定理成立

因此, 定理可加强为:

***

定理+: P(x)是整系数多项式 iff 存在整系数$C_d,C_d-1,\cdots,C_0$使得$P(x)=C_dP(d)_+C_{d-1}P(d-1)+\cdots+C_0P(0)$

思考: 此定理是否可推广到任意(d+1)个点?

***

解答: 必须是(d+1)个连续点

证明: 反例易得

对于(d+1)个连续点