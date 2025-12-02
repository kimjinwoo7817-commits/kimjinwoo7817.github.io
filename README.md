# 🧑‍💻 KIM JINWOO's Portfolio
> **"임상의 경험을 데이터의 확신으로, 융합형 AI 엔지니어 김진우입니다."**

<br>

## 🙋‍♂️ Intro
안녕하세요. **간호사 출신의 도메인 지식과 인공지능 기술을 결합**하여 헬스케어와 금융 분야의 비효율을 해결하고자 하는 [이름]입니다.

임상 현장에서 환자의 데이터를 다루며 얻은 꼼꼼함과 책임감을 바탕으로, 현재는 **인공지능학과**에서 데이터 분석 및 딥러닝 모델링 역량을 키우고 있습니다. 단순한 코딩을 넘어, 데이터 뒤에 숨겨진 맥락(Context)을 이해하고 실질적인 가치를 창출하는 개발자가 되는 것이 목표입니다.

* **Background:** 간호사 근무 (15년), 의료 도메인 이해도 보유
* **Focus:** Computer Vision(Image Processing), Quant Trading, Data Modeling
* **Contact:** kimjinwoo7817@gmail.com

<br>

## 🛠 Tech Stack
### Languages
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) ![SQL](https://img.shields.io/badge/SQL-CC2927?style=flat-square&logo=c&logoColor=white)

### AI & Data Analysis
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white) ![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white) ![Matplotlib](https://img.shields.io/badge/Matplotlib-ffffff?style=flat-square&logo=Matplotlib&logoColor=black)

### Tools & Environment
![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white) ![VS Code](https://img.shields.io/badge/VS_Code-007ACC?style=flat-square&logo=visualstudiocode&logoColor=white)

<br>

## 🚀 Projects

### 1. 생성형 AI 기반 이미지 복원 및 스타일 변환

<br>

> **프로젝트 개요**
> 오래되거나 훼손된 저해상도 인물 사진을 최신 생성형 모델을 활용해 고해상도로 복원하고, 특정 시대상(예: 신라시대)에 맞는 화풍으로 변환하는 파이프라인 구축.

**📌 Key Features**
* **Super Resolution:** GFPGAN 등을 활용한 얼굴 디테일 복원 및 업스케일링.
* **Style Transfer:** Stable Diffusion과 ControlNet을 활용하여 인물의 특징(Feature)은 유지하되 의상과 배경 스타일 변환.
* **Data Augmentation:** 학습 데이터 부족 문제를 해결하기 위한 이미지 증강 기법 적용.

**🔧 Tech Stack**
* Python, PyTorch, Stable Diffusion, OpenCV

**💡 Trouble Shooting (문제 해결)**
* **문제:** 이미지 변환 시 얼굴이 뭉개지거나 아이덴티티가 사라지는 현상 발생.
* **해결:** Canny Edge Detection을 통해 윤곽선을 먼저 추출하고, 이를 ControlNet의 입력으로 사용하여 인물 형태 유지력을 30% 이상 향상시킴.

---

### 2. 거시경제 지표 기반 자동 매매 프로그램 (Auto Trader)

<br>

> **프로젝트 개요**
> 단순히 가격 변동만이 아닌, 환율, 금리 등 **최신 매크로 지표**를 실시간으로 수집 및 분석하여 시장 상황에 맞춰 매매를 수행하는 봇 개발.

**📌 Key Features**
* **API 연동:** 증권사 API를 활용한 실시간 호가 수집 및 주문 실행.
* **Macro Analysis:** 한국은행 및 FRED(미 연준) API를 통해 금리, 환율 데이터를 수집하여 매수 가중치 조절 로직 구현.
* **Alert System:** 매매 체결 및 급격한 변동 발생 시 텔레그램 봇으로 알림 전송.

**🔧 Tech Stack**
* Python, Pandas, Requests, Telegram API

**💡 Trouble Shooting (문제 해결)**
* **문제:** 장중 API 요청 횟수 초과로 인한 연결 끊김 현상.
* **해결:** `time.sleep`을 이용한 정적 딜레이 대신, 토큰 버킷 알고리즘을 응용한 요청 속도 제어 모듈을 구현하여 안정성 확보.

---

### 3. 병원 환자 관리 시스템 데이터 모델링 (SQLD 학습)

<br>

> **프로젝트 개요**
> 병원 내 환자 입/퇴원 및 간호 기록 프로세스의 비효율을 개선하기 위한 RDB(관계형 데이터베이스) 설계.

**📌 Key Features**
* **ERD 설계:** 환자, 의료진, 병동, 처방 등 핵심 엔티티 도출 및 관계 정의.
* **정규화(Normalization):** 제3정규형(3NF)까지 적용하여 데이터 중복 최소화 및 무결성 보장.
* **Query Optimization:** 자주 조회되는 환자 이력 검색 쿼리의 효율적인 인덱스 설계.

**🔧 Tech Stack**
* MySQL, ERD Cloud

<br>



<br>

<div align="center">
  Last Updated: 2025. 12. 03 <br>
  Designed by kimjinwoo7817
</div>

