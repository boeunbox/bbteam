# BBTeam - 보은박스 프로젝트
이 프로젝트는 멋쟁이 사자처럼 부산 3기의 BB Team에서 진행한 팀 프로젝트입니다.

## 보은박스란?
<div>
  <img src="https://user-images.githubusercontent.com/66506477/103867713-290add00-510b-11eb-83de-a47ca7cb61d0.jpg" width="500px" />
  <img src="https://user-images.githubusercontent.com/66506477/103867718-2ad4a080-510b-11eb-8fd2-ebe1a67d2969.jpg" width="500px" />
</div>
보은박스는 40대 이상 연세의 부모님을 둔 20-40대의 자녀를 타겟 소비자층으로 하는 정기구독 배송서비스입니다.
MD가 직접 엄선한 물품으로 가득 채운 상자를 타겟 소비자층의 부모님들께 매달 배송하는 것을 콘셉트로 하였습니다.

## 보은박스 웹사이트 구성
<div>
  <img src="https://user-images.githubusercontent.com/66506477/103867720-2ad4a080-510b-11eb-95f9-857c2b7fc579.jpg" width="500px" />
  <img src="https://user-images.githubusercontent.com/66506477/103867721-2b6d3700-510b-11eb-9245-5dea6b438476.jpg" width="500px" />
</div>
보은박스 웹사이트는 크게 메인페이지, 서비스 소개 페이지, MD상품 페이지, 고객센터 페이지, 회원정보관리 페이지, 로그인/회원가입 페이지로 구성되어 있습니다.
각 대표 페이지는 부속 페이지들과 함께 application에 속해 있습니다.

### 1. mainapp by. minami-cs
- base.html: 
글로벌 네비게이션바를 구현한 html문서입니다.
JavaScript로 스크롤에 따른 부드러운 색상 전환 효과를 주었으며, 미디어쿼리를 적용하여 작은 화면에서는 modal창처럼 왼쪽에서 화면 위로 네비게이션바가 나오도록 하였습니다.
나의보은 submenu 펼침/접힘 동작도 JavaScript 동작 효과를 주었습니다.
- index.html: 
index.html은 이미지를 통해 보은박스의 브랜드를 나타내고자 하였기 때문에 텍스트 사용을 최소화하였습니다.
사이드 네비게이션바로 각 이미지를 페이지 넘기듯 이동할 수 있으며, 각 이미지별로 다른 페이지로 이동할 수 있는 버튼이 다르게 적용되어 있습니다.
- terms-of-use.html, privacy-policy.html: 
웹서비스 개발 시 자칫 빠뜨릴 수 있는 사이트 이용약관과 개인정보처리방침 페이지를 빠뜨리지 않고 제작하였습니다.

### 2. subscrapp by. jungbin hong
- subscrapp.html:
보은박스 이용방법과 비용 등을 안내하는 페이지입니다.
페이지의 내용들은 모두 반응형으로 만들었습니다.
비용안내 부분은 wrap을 이용해 가격표를 배치했습니다.

### 3. productapp by. geonhnam
- product.html

### 4. cscenterapp by. minami-cs
- cscenter.html:
고객센터 메뉴를 클릭하면 나타나는 고객센터의 메인페이지입니다.
FAQ 게시판은 input과 label만을 이용해서 내용을 접었다 펼칠 수 있는 간단한 기능으로 구현하였습니다.
FAQ 게시판 아래의 1:1문의 페이지로 이동하는 버튼을 누르면 login_required 기능에 따라 로그인 여부를 즉시 판별하여 로그인하지 않았다면 로그인 또는 회원가입을 하도록 합니다.
- enquiry.html, create.html, modify.html: 
회원 로그인 후에만 이동할 수 있는 1:1문의 게시판 페이지로, Django의 modelform을 사용했습니다.
게시글 작성과 수정에 쓰이는 editor는 summernote를 사용하여 디자인을 css로 수정하였습니다.
- detail.html: 
게시글 상세보기 페이지는 css로 디자인하였고, 역시 Django의 modelform을 사용합니다.

### 5. myboeunapp by. jungbin hong
- myboeun.html


### 6. signupapp by. seongyeol park
- signup.html
- login.html
