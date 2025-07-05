# Django Todo 시스템


## 학습 추천 : <a href="https://codam.kr/" target="_blank">코담</a>

### 파이썬·장고 웹개발 | 코담 - 코드에 세상을 담다.

<a href="https://codam.kr/" target="_blank">
<img src="https://codam.kr/assets/images/og-image.jpg">
</a>


## 화면 구성

##### 1.메인화면
<img src="https://blogger.googleusercontent.com/img/a/AVvXsEg-2QR0MM2r9tHzCWkieOwgGIhP3vOJihO3bCIlXN6YNSbF1n1iMuoQ8sQnt4_VvxQ8TNQOm5lSIdg9RUkS3XfN88CCd6gbOu5ruKosftWo0crtbLwMoIO83tcLvgW9-tBxK6gGcXNkbttZpndvhj6aogsPPWIHQAW0Pf_DTMc7-NQf2lPjpvLi5zYIR6BO=w640-h364" >

##### 2.회원가입
<img src="https://blogger.googleusercontent.com/img/a/AVvXsEgPBcBn2OFh3ErQrx_MBzkRQcrzH5VMya7xwWujCFsSRnGYseGiA_CkBGU12XcWW4E5RSJBRWGcGL4yDsuP3Fr5vprdFyxspvwo7XG-A_GCgD2gYD6H3Bb6kxd-VzBz-500-IeMdQpDAAbgRLeim_HzbXmS4NqPdLgmxzuNVMWNYVpWaZtegiX8MdJ5AQLZ=w640-h514" >


##### 3.로그인
<img src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgtmgL8cvRWFUIKioF1mPvtvJ3EbI9USNjxRwGkWIquq_ZF4TMSqgTRvElzmytQmbAWQWRPOSE_nIGQg_ghuQ2iJ26Bk_-gAGGkTo2_GpWYadd-tgwllvbX5wd27X3Lv_pkd54xxV3nTi6ATVCKRMeCpokAtNsirhQp71mAjKVYCmMAB1laH6DcgldHDRMM/w636-h640/2025-06-12%2017%2010%2002.png">


##### 4.Todo 목록
<img src="https://blogger.googleusercontent.com/img/a/AVvXsEi_n2DUxEBj2EECanJBVPS0JsV6-_TNXdwMXouG57pZZEpTRrlgL0i79Ch587CqaKvnRhIFG5df1vilTc0LkYc2xU5cEqDOOsVoYI_hFJuhoEl1B-U7-HvfFL98sqat-rzqocl0Q3zvvQJ_HSGTVWdT2vsLvXrLbcTW8RArkcYVv3xeMvGZ-vvhRJj53bW_=w528-h640" >


##### 5.Todo 등록
<img src="https://blogger.googleusercontent.com/img/a/AVvXsEg3xuH3QGebLBkMs7Ov3A7QDFOA-3xr_pX0H7jyG_sbIAK9u8NIxEMHANMM_fiOIDtY6iA9pYbt7LNkOYQSGcmh085luMPZSIoglILDXd2EntalHbSLPv9vs5HHNGyyOvwLGjoCU91E5POzcQRz_-1oNX31UbZexmXuhG7Sw92QJ61hQ1HDyR16oD_l0DRt=w525-h640" >


##### 6.Todo 수정
<img src="https://blogger.googleusercontent.com/img/a/AVvXsEhWAaAPHFxwJnuK90jyO7RwNw_Z0n_gHZHmPOCyHY9ivBK-PcXw7fHJ_fBjYcjsylolVfjcB2lMmnE-uy9mrnWiRgWZq7FB7awC9Ws9wumH4lVWZbBTRxP5C9EYHUuwAU7dK8uYcbja50pGccVz2sj4r4UQ3qAQL7T32FoiFC98ZwhiO-RruADhwH7Dq4lU=w536-h640" >






## 📁 프로젝트 구조

```
todoList_django2/
│
├── accounts/            # 사용자 인증 및 관련 기능 앱
├── config/              # Django 설정 파일 (settings.py, urls.py 등)
├── node_modules/        # npm 패키지 저장소 (Tailwind 등 프론트엔드용)
├── static/              # 정적 파일(css, js 등)
├── templates/           # HTML 템플릿 폴더
├── todo/                # ToDo 기능 관련 앱
│
├── .gitignore           # Git에서 제외할 파일 정의
├── db.sqlite3           # SQLite 데이터베이스 파일
├── manage.py            # Django 명령어 실행용 스크립트
├── package.json         # 프론트엔드 패키지 정의 (Tailwind 포함 예상)
├── pnpm-lock.yaml       # pnpm 패키지 잠금 파일
├── README.md            # 프로젝트 설명 문서
├── requirements.txt     # Python 패키지 목록
├── tailwind.config.js   # Tailwind CSS 설정 파일
└── venv/                # 가상환경 폴더 (Python 패키지 독립 환경)

```

<img src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjY8ES0MwWoQZAP-3Zi3qpvJ_VZNZ453B1lJbT9eHcsl2tomqpy2BOqyaDaeAoYGKLgDwGy3o91NrY7AFqG-SHXC5-aeNqh4zpuwDZD0rnGZxPkE7HA7ywFgOzobCH2e-YdR7Xy1V9Pk6kvsOGBmF2a05swU-qO8x_tzOXsrrhyjfARisplNledScO8-u4o/w628-h640/2025-06-12%2017%2013%2030.png">


### 📁  todo 앱 디렉토리 구조
```
todo/
│
├── __pycache__/               # 파이썬 캐시 파일
├── migrations/                # 마이그레이션 파일 (DB 스키마 관리)
│
├── templates/
│   └── todo/
│       ├── include/           # 공통 include 템플릿 폴더
│       ├── base.html          # 기본 레이아웃 템플릿
│       ├── head.html          # <head> 태그 관련 HTML 분리
│       ├── header.html        # 일반 헤더
│       ├── header-account.html # 로그인/계정 관련 헤더
│       ├── footer.html        # 공통 푸터
│       ├── todo_create.html   # 할 일 생성 페이지
│       ├── todo_detail.html   # 할 일 상세 페이지
│       ├── todo_list.html     # 할 일 목록 페이지
│       └── todo_update.html   # 할 일 수정 페이지
│
├── __init__.py                # 패키지 초기화
├── admin.py                   # Django 관리자 페이지 설정
├── apps.py                    # 앱 구성 정보
├── form.py                    # 폼 클래스 정의 (Form, ModelForm 등)
├── models.py                  # DB 모델 정의 (ToDo 모델 등)
├── tests.py                   # 테스트 코드
├── urls.py                    # URL 라우팅 정의
└── views.py                   # 뷰 함수/클래스 정의
```



## ⚙️ 개발 환경
- Python 3.12.3
- Django 5.2.1
- 가상환경: venv 사용
- tailwindcss v4.1 사용
- 

## ▶️ 실행 방법
1. 가상환경 활성화:
```bash
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

2. 패키지 설치: 
```bash
pip install -r requirements.txt
```

3. 수정


## 📦 Commit 메시지 컨벤션 (Conventional Commits)

본 프로젝트는 [Conventional Commits](https://www.conventionalcommits.org/) 표준을 따릅니다.

## ✅ 기본 형식



### ✍️ 커밋 타입 예시

| 타입        | 설명                                |
|-------------|-------------------------------------|
| `feat`      | 새로운 기능 추가                    |
| `fix`       | 버그 수정                           |
| `docs`      | 문서 변경 (README 등)              |
| `style`     | 코드 포맷팅, 세미콜론 누락 등       |
| `refactor`  | 코드 리팩토링 (기능 변화 없음)       |
| `test`      | 테스트 코드 추가 또는 수정          |
| `chore`     | 빌드, 패키지 설정 등 기타 변경사항   |

### 💡 예시

```bash
git commit -m "feat: 사용자 로그인 기능 추가"
git commit -m "fix: 게시글 생성 시 오류 수정"
git commit -m "docs: README에 커밋 규칙 추가"
git commit -m "style: 코드 들여쓰기 수정"
git commit -m "refactor: DB 모델 구조 개선"
git commit -m "test: 유저 모델 테스트 추가"
git commit -m "chore: 패키지 의존성 업데이트"
```







## ✅ DB 마이그레이션

##### 1. 모델 변경 사항 탐지 (마이그레이션 파일 생성)
python manage.py makemigrations

##### 2. 실제 DB에 테이블 생성
python manage.py migrate

##### 3. 확인: 모델이 정상적으로 DB에 반영되었는지
python manage.py showmigrations



## ✅ Tailwindcss 4.1 설정

####  1.루트 경로에서 다음 명령 실행:
```
npm init -y
npm install -D tailwindcss
npx tailwindcss init

```
    생성되는 파일들:
    package.json
    tailwind.config.js

#### 2. Tailwind 설정 파일 수
```
module.exports = {
  content: [
    "./templates/**/*.html", // Django 템플릿들
    "./**/templates/**/*.html", // 앱별 템플릿 폴더까지 포함
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

#### 3. Tailwind CSS 입력 파일 생성
 static/css/input.css

```
@import "tailwindcss";

```

#### 5. Tailwind CSS 빌드 설정 (output.css 생성)
예: static/css/output.css로 빌드하려면 아래 명령 실행:

```
npx tailwindcss -i ./static/css/input.css -o ./static/css/output.css --watch

```





## 👨‍💻 Author

**코담([Codam](https://codam.kr/))**  :  Jun Ho Choi : braverokmc79@gmail.com








