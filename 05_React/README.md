# React

[← 루트로 이동](../README.md)


React 기반 웹 화면을 만들면서 **라우팅, 상태관리, API 연동, 인증 상태, CRUD UI**를 실습한 내용을 정리했습니다.

기존 프로젝트에서 학습 과정 중 남아 있던 중복 게시판(`Board` / `Board1`), Vite·React 기본 로고, 메모 파일, 오타가 포함된 파일명 등을 정리하고 대표 구현만 남겼습니다.

## 학습 내용

- React 컴포넌트와 상태 관리
- React Router 기반 페이지 이동과 중첩 라우팅
- Axios를 이용한 REST API 연동
- Redux Toolkit을 이용한 로그인 상태 관리
- 세션 스토리지 기반 토큰 관리
- 게시판 목록/검색/페이지네이션
- 회원가입/로그인/회원정보 변경 UI
- 상품 등록/목록 UI
- MQTT 기반 채팅 실습
- Ant Design 컴포넌트 활용

## 주요 구조

```text
src/
├─ components/      # 공통 UI
├─ pages/           # 화면 단위 컴포넌트
│  └─ mypage/       # 마이페이지 하위 화면
├─ store/           # Redux 상태관리
├─ css/             # 공통/화면별 스타일
├─ assets/          # 실습 이미지
├─ App.jsx          # 라우팅 및 공통 레이아웃
└─ main.jsx         # React 진입점
```

> 이 폴더는 완성 서비스 배포용 저장소가 아니라, React에서 여러 기능을 구현하고 백엔드 API와 연결하는 방법을 학습한 기록입니다.
