# finedust-server
### UOS 소프트웨어 응용 팀 프로젝트
#### 미세먼지 예측 딥러닝 모델의 유저 시나리오를 위한 백엔드 어플리케이션

##### To build and run this project:
1. Install Docker
2. Run this command
``` bash
git clone https://github.com/inourbubble2/finedust-server.git
cd finedust-server
docker build -t finedust-server .
docker run -p 5000:5000 finedust-server
```
3. Visit http://localhost:5000/

Or just...
1. Install Python
2. Run this command

``` bash
git clone https://github.com/inourbubble2/finedust-server.git
cd finedust-server
pip install -r requirements.txt
python app.py
```
3. Visit http://localhost:5000/
