class UsaPackage:
    def detail(self):
        print("[미국 패키지 3박 5일] LA 관광 여행 400만원")
    __name__ : str
        
if __name__ == "__main__":
    print("usa 모듈을 직접 실행") #usa.py 파일 자체를 실행할 경우 출력됨
    print("이 문장은 모듈을 직접 작성할 경우에만 실행됩니다.") #usa.py 파일 자체를 실행할 경우 출력됨
    trip_to = UsaPackage()
    trip_to.detail()
else:
    print("usa 외부에서 모듈을 호출") #외부에서 해당 모듈을 import를 진행하여 사용할 경우 출력됨