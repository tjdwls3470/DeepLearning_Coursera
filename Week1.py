Coursera. Deep Learning Specialization

Lecture1. Neural Networks and Deep Learning

Week.1
#1
DeepLearning : 신경망의 트레이닝
ex) size of house를 input으로 해서 price를 예측해서 output하는 ReLU함수(Rectified Linear Unit Function)
Neural Network : Input(size of house) -> node('Neuron') -> Output(price)
Input의 종류 증가 : Stack (ex. size, #rooms, zip code wealth -> family size, walkability, school quaility... -> price)

#2
Supervised Learning
Example
Input(x)			Output(y)					Application
-Home features		-Price						-Real Estate			#Standard NN
-Ad, user info		-Click on ad? (0/1)			-Online Advertising		#Standard NN
-Image				-Object (1,...,1000)		-Photo tagging			#CNN
-Audio				-Text transcript			-Speech recognition		#RNN
-English			-Korean						-Machine translation	#RNN
-Image, Radar info	-Position of other cars		-Autonomous driving		#Custom/hybrid NN

Structured Data		Data의 Database
Unstructured Data	Audio or Image와 같이 Image나 Text 내부에 있는 내용을 인식하고자 하는 Data

#3
Digitize가 되면서 Computer,Internet,Smartphone소비가 증가하여 App,Web등의 접속시간이 늘어나면서 Data가 방대해졌고 새로 만들어지는 Data의 양도 늘어남
이전의 알고리즘(ex.로지스틱 회귀 등)은  Data가 증가하면 성능이 초기에는 증가하다가 어느순간 안정화되는 경향을 보임
트레이닝을 시키다보면 성능이 증가하는 것을 볼 수 있음

고성능의 프로그램
1. 큰 신경망을 트레이닝 할 수 있어야함
2. 많은 양의 데이터가 필요함

* variable m : Number of training examples
* Sigmoid Funcion : +-inf로 가면 함수의 gradient가 0에 수렴해서 Learning speed가 매우 느려짐
* ReLU Function : x>0에서 gradient가 1이어서 gradient descent(기울기 강화)라는 알고리즘을 생성, Learning speed 향상