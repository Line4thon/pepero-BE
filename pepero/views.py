from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Pepero
import json

# 첫 시작 화면 렌더
def pepero_make_home_view(request):
    if request.method == 'GET':
        return render(request, 'peperos/pepero.html')
    return render(request, 'peperos/pepero.html')

# 그..홈 화면에서 빼빼로 1단계 넘어가기 전 효과 뷰 렌더
def pepero_make_start_view(request):
    if request.method == 'GET':
        return render(request, 'peperos/loading-start.html')
    elif request.method == 'POST':
        return render(request, 'peperos/loading-start.html')
    return render(request, 'peperos/loading-start.html')

# 빼빼로 1단계 만들기
def pepero_make_choco_view(request):
    if request.method == 'GET':
        print("빼빼로 1단계 시작")
        return render(request, 'peperos/pepero_make1.html')
    elif request.method == 'POST':
        try:
            post_data = json.loads(request.body.decode('utf-8'))
            selected_choco = post_data.get("selected_choco")
            if selected_choco:
                print("사용자 선택 초코 값 : "+selected_choco)
                request.session['selected_choco'] = selected_choco
                return JsonResponse({'message': 'Success'})
        except json.JSONDecodeError as e:
            return JsonResponse({'message': 'Error', 'error': str(e)})
    return render(request, 'peperos/pepero_make1.html')

# 빼빼로 2단계
def pepero_make_sauce_view(request):
    if request.method == 'GET':
        print("1단계에서 선택한 값 체크 :" + request.session['selected_choco'])
        print("빼빼로 2단계 시작")
        return render(request, 'peperos/pepero_make2.html')
    elif request.method == 'POST':
        try:
            post_data = json.loads(request.body.decode('utf-8'))
            selected_sauce = post_data.get('selected_sauce')
            if selected_sauce:
                print("사용자 선택 소스 값 : "+selected_sauce)
                request.session['selected_sauce'] = selected_sauce
                return JsonResponse({'message': 'Success'})
        except json.JSONDecodeError as e:
            return JsonResponse({'message': 'Error', 'error': str(e)})
        return render(request, 'peperos/pepero_make3.html')
    
# 빼빼로 3단계
def pepero_make_deco_view(request):
    if request.method == 'GET':
        print("1단계에서 선택한 값 체크 :" + request.session['selected_choco'])
        print("2단계에서 선택한 값 체크 :" + request.session['selected_sauce'])
        print("빼빼로 3단계 시작")
        return render(request, 'peperos/pepero_make3.html')
    elif request.method == 'POST':
        return render(request, 'peperos/pepero_letter.html')

    
    
def pepero_make_letter_view(request):
    if request.method == 'GET':
        print("1단계에서 선택한 값 체크 :" + request.session['selected_choco'])
        print("2단계에서 선택한 값 체크 :" + request.session['selected_sauce'])
        print("빼빼로 편지 쓰기 시작")
        return render(request, 'peperos/pepero_letter.html')
    elif request.method == 'POST':
        selected_choco = request.session.get('selected_choco', '기본')
        selected_sauce = request.session.get('selected_sauce', '기본')
        selected_deco = request.session.get('selected_deco', '기본')
        content = request.POST.get('content', '')
        pepero = Pepero(choco=selected_choco, sauce=selected_sauce, deco=selected_deco, content=content)
        pepero.save()
        print("빼빼로 편지 완성 확인")
        return render(request, 'peperos/loading-ing.html')

    
    
# 빼빼로 전송하기 뷰 ( 효과 )
def pepero_make_ing_view(request):
    if request.method == 'GET':
        return render(request, 'peperos/loading-ing.html')
    return render(request, 'peperos/loading-ing.html')
# 빼빼로 전송완료 뷰 ( 효과 )
def pepero_make_end_view(request):
    if request.method == 'GET':
        return render(request, 'peperos/loading-end.html')
    return render(request, 'peperos/loading-end.html')

