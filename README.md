# Paper-for-ML-DL

ML/DL 관련 논문을 주제별로 정리한 저장소입니다. 각 최상위 폴더와 그 안의 주요 하위 분류는 다음과 같습니다.

## 폴더 구조

- `RAG`: Retrieval-Augmented Generation 관련 자료
  - `00_Surveys_Overviews`: RAG 개요·survey 논문
  - `01_Graph_RAG`: 그래프 기반 RAG 및 관련 기법
  - `02_MultiHop_Path`: 멀티홉 검색과 reasoning path 연구
  - `03_Efficient_RAG`: 경량/고효율 RAG 기법
  - `04_Specialized_Methods`: 하이브리드·특수 구조 RAG
  - `99_Misc`: 상위 규칙에 맞지 않는 기타 자료
- `딥러닝전반`: 범용 딥러닝 이론 및 기법
  - `00_Optimization`: 최적화·공격 관련 기법
  - `01_Normalization`: 정규화 관련 논문
  - `02_ModelArchitectures`: 대표 모델 구조 정리
  - `03_Data_Quality`: 데이터 품질·평가 관련 자료
  - `04_Foundation_Models`: 범용 대모델 및 기타 주제
  - `99_Misc`와 기존 폴더(`ModelEvaluation...`, `Outlier-detection`, `Tidy_Data`)는 세부 주제별 참고 자료
- `연구`: 지식 그래프/연구 관련 논문
  - `00_Surveys_Textbooks`: 서베이 및 교재성 자료
  - `01_KG_Construction`: 지식 그래프 구축·추출 연구
  - `02_RAG_for_KG`: KG 기반 RAG·QA 응용
  - `03_Diffusion_Generative`: 확산 기반 접근
  - `04_Temporal_Multimodal`: 시계열·멀티모달 KG 연구
  - `99_Misc`: 기타 관련 논문
- `자연어처리`: NLP 전반
  - `00_Attention_Architecture`: 어텐션/기본 구조 논문
  - `01_Foundation_Models`: 대형 언어모델 및 파생 연구
  - `02_Training_Optimization`: 학습 최적화·압축 기법
  - `03_Prompting_Agentic`: 프롬프트·에이전트 기법
  - `04_Evaluation_Detection`: 평가·검출 관련 연구
  - `05_RLHF_Alignment`: 보상학습·선호 정렬
  - `06_Embeddings`: 임베딩 및 표현 학습
  - 하위 기존 폴더(`Attention is all you need`, `Model`, `자연어기초논문` 등)는 원문 분류 유지
- `종설1논문관련`: 종설1 주제 (시계열·언러닝 등)
  - `00_TimeSeries`, `01_Unlearning`, `02_Representation`, `03_Normalization`, `04_KoreanResources`, `99_Misc`
- `종설2논문관련`: 종설2 주제 (적대적 공격·딥페이크 등)
  - `00_Adversarial_Attacks`, `01_Deepfake_Detection`, `02_Defense_Strategies`, `03_Metrics_Quality`, `99_Misc`

각 분류 규칙은 `organize_papers.py`에서 관리합니다. 필요에 따라 정규식을 수정해 재정렬할 수 있습니다.
