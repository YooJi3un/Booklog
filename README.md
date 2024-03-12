Django를 이용하여 책 리뷰 블로그 제작

* 목표
    * Django 프레임워크를 사용하여 실제 웹 애플리케이션을 개발함으로써, 백엔드 개발에 대한 이해를 심화하고 Python 기반의 웹 개발 능력을 향상시키는 것
    * 사용자가 편리하게 책 리뷰를 검색, 읽고, 자신의 리뷰를 작성할 수 있는 직관적이고 사용자 친화적인 웹 인터페이스를 설계하고 구현하는 것
    * 사용자가 리뷰를 통해 의견을 공유하고, 책 추천을 받거나 제공하며, 동일한 관심사를 가진 다른 사용자들과 상호 작용할 수 있는 기능을 제공함으로써, 활발한 참여와 커뮤니티 성장을 도모

* 기능
    * 사용자가 자신이 읽은 책을 업로드하고 그에 대한 감상평을 작성하여 공유할 수 있다.
    * 검색 기능을 통해 자신이 원하는 종류의, 제목의 책을 찾고 추천 받을 수 있다.
    * 댓글 기능을 통해 책에 대한 의견을 공유하고 다른 사용자들과 상호 작용할 수 있다.

  
* WBS
```mermaid
gantt
    dateFormat  YYYY-MM-DD
    title 프로젝트 진행 상황

    section 프로젝트 기획
    프로젝트 아이디어 기획    :done,    des1, 2023-03-07, 1d
    
    section 계획
    WBS 작성   :done,    des2, 2023-03-07, 2d
    
    section 개발 준비
    리포지토리 생성 :active,  des3, 2023-03-09, 1d
    와이어프레임      :active, des4, 2023-03-08, 2d
    
    section 개발
    ERD          :         active, des4, 2023-03-10, 2d
    URL 구현        :       active, des4, 2023-03-12, 2d
    모델 구현       :       active, des4, 2023-03-09, 4d

```



* 와이어프레임
    <table>
        <tr>
            <th>메인화면</th>
            <th>설명</th>
        </tr>
        <tr>
            <td width="70%">
                <img src="img/review.jpg">
            </td>
            <td>
                <ul>
                    <li></li>
                    <li></li>
                    <li></li>
                    <li></li>
                </ul>
            </td>
        </tr>
    </table>
    <table>
        <tr>
            <th></th>
            <th>설명</th>
        </tr>
        <tr width="70%">
            <td width="70%">
                <img src="img/detail.jpg">
            </td>
            <td>
                <ul>
                    <li></li>
                    <li></li>
                    <li></li>
                </ul>
            </td>
        </tr>
    </table>
    
* ERD
    
* 애러와 애러 해결(트러블슈팅 히스토리)
   
    
