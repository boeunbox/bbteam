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
1. mainapp
- base.html: 글로벌 네비게이션바
- index.html: 인덱스 페이지
- terms-of-use.html: 사이트 이용약관 페이지
- privacy-policy.html: 사이트 개인정보처리방침 안내 페이지

2. subscrapp

3. productapp

4. cscenterapp
- cscenter.html: 고객센터 faq게시판 페이지
- enquiry.html: 고객센터 1:1문의 게시판 페이지
- detail.html: 고객센터 1:1문의 게시글 확인 페이지
- update.html: 고객센터 1:1문의 게시글 수정 페이지

5. myboeunapp

6. signupapp
- signup.html: 회원가입 페이지
- login.html: 로그인 페이지

### 1. mainapp
index.html은 이미지를 통해 보은박스의 브랜드를 나타내고자 하였기 때문에 텍스트 사용을 최소화하였습니다.
사이드 네비게이션바로 각 이미지를 페이지 넘기듯 이동할 수 있으며, 각 이미지별로 다른 페이지로 이동할 수 있는 버튼이 다르게 적용되어 있습니다.
글로벌 네비게이션바에는 JavaScript로 동적인 효과를 주었습니다.
