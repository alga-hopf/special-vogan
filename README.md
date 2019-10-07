
  


In this project we want to present a combinatorial property of Vogan
diagrams which may be studied directly and by deep learning techniques.
Let $\mathfrak{g}$ be a real semisimple Lie algebra of rank $\ell$ with
Vogan diagram having indices of painted nodes $$P$$ and set of positive
roots $\Delta^+$. Let $\{\gamma_1,\ldots,\gamma_{\ell}\}$ be the set of
simple roots and $\{\varphi_1,\ldots,\varphi_{\ell}\}$ be the set of
fundamental dominant weights. We assign to each root $\alpha$ a
coefficient $\varepsilon_{\alpha}$ which is $-1$ if $\alpha$ is compact
and $1$ otherwise. Define the vector
\[
\eta=\sum_{\alpha\in\Delta^+}\varepsilon_{\alpha}\alpha
\]
and consider the vector
\[
\eta-4\sum_{\alpha\in\mathrm{span}\{\gamma_i\vert i\in S^c\}},
\]
which
may be expressed in the basis of fundamental dominant weights as
$\sum_{i\in P}a_i\varphi_i$, with $a_i\in \mathbb{Z}$. We say that a
Vogan diagram is *special* if the $a_i$'s are all positive, negative or
zero. Thus, the problem is the following: given a (connected) Vogan
diagram, to determine whether it is special or not. This issue turns out
to be purely combinatorial in terms of root data. In particular, it may
be studied directly through to the algorithm specialOrbits.sage.
The
speciality of Vogan diagrams is relevant in the almost-Kähler geometry
of adjoint orbits of semisimple Lie groups, as it allows to determine
when an orbit admits a canonical metric. For more details, see [arXiv:1811.06958 [math-DG]](https://arxiv.org/abs/1811.06958).

On the other hand, the problem may be studied also with deep learning
techniques, especially to make predictions on higher ranks Vogan
diagrams. We use the algorithm in specialOrbits.sage to prepare data, in
particular we run the algoritm for each Vogan diagram up to rank ?? and
we pair each diagram with a label (0 if it is special, 1 otherwise).
Then we build a simple fully connected deep neural network and we train
it with the prepared data. After many temptatives, one may see that the
neural network gives quite precise prediction for Vogan diagrams up to
rank ??, but it seems that it is not precise in extrapolating
predictions for higher rank Vogan diagrams. We tried also with a
convolutional neural network, but the results are the same as for the
fully connected neural network.
