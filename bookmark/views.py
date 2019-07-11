from django.shortcuts import render

# Create your views here.
from .models import Bookmark
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.urls import  reverse_lazy
from django.views.generic.detail import DetailView
from django import forms

# 뷰에는 함수형 뷰클래스와 클래스형 뷰클스가있다
class BookMarkListView(ListView):
    """
    ListView 디폴트 지정 속성
    1) 컨텍스트 변수 : object_list
    2) 템플릿 파일 : bookmark_list.html (모델명소문자_list.html)
    함수형 뷰에서반복되는 공통 부분을 패턴화하여 사용하기 쉽게 추상화 해두었다.
    아래와 같이 최소한 그 뷰가 어떤 모델을 사용할 것인지만 지정해주면 나머진 모두 상위 클래스(여기서는 List generic view)가 모든 걸 알아서 해준다.
    뷰는 간단 명료해야 한다.
    뷰 코드의 양은 적으면 적을수록 좋다.
    뷰 안에서 같은 코드를 반복적으로 사용하지 않는다.
    뷰는 프레젠테이션 로직에서 관리하고 비즈니스 로직은 모델에서 처리한다. 매우 특별한 경우에만 폼에서 처리한다.
    403, 404, 500 에러 핸들링에는 CBV를 이용하지 않고 FBV를 이용한다.
    믹스인은 간단명료해야 한다.
    https://wikidocs.net/9623
    """

    model = Bookmark

class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name', 'url']
    success_url = reverse_lazy('list')
    # 사용할 템플릿의 접미사만 변경하는 설정값
    template_name_suffix = '_create'

class BookmarkDetailView(DetailView):
    model = Bookmark




