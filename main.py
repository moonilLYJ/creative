pip install streamlit
def recommend_soccer_exercises():
    # 유소년 축구 맞춤형 운동 데이터베이스 (전체 단점 확장)
    exercise_database = {
        "순발력": {
            "맨몸 운동": [
                "1. 사이드 스텝 (Side Step) - 방향 전환 능력 향상",
                "2. 스쿼트 점프 (Squat Jump) - 폭발적인 하체 탄력 강화",
                "3. 마운틴 클라이머 (Mountain Climber) - 민첩한 발놀림과 심폐 지구력"
            ],
            "기구 운동": [
                "1. 스피드 래더 (Agility Ladder) 드릴 - 발 스텝의 세밀함",
                "2. 콘 위빙 (Cone Weaving) - 드리블 및 방향 전환 스피드",
                "3. 저항 밴드 사이드 워크 (Resistance Band Side Walk) - 고관절 외전근 단련"
            ],
            "웨이트 운동": [
                "1. 덤벨 스쿼트 (Dumbbell Squat) - 하체 기본 근력 및 가속력",
                "2. 바벨 런지 (Barbell Lunge) - 한쪽 다리 지지력 및 밸런스",
                "3. 케틀벨 스윙 (Kettlebell Swing) - 후면 사슬 및 폭발적인 파워"
            ]
        },
        "슈팅력": {
            "맨몸 운동": [
                "1. 워킹 런지 (Walking Lunge) - 킥을 할 때 디딤발의 안정성 강화",
                "2. 싱글 레그 브릿지 (Single Leg Bridge) - 엉덩이 및 햄스트링 강화",
                "3. 카프 레이즈 (Calf Raise) - 발목 힘과 슈팅 임팩트 순간 고정력"
            ],
            "기구 운동": [
                "1. 메디신볼 스로우 (Medicine Ball Throw) - 코어와 상체의 슈팅 협응력",
                "2. 저항 밴드 레그 익스텐션 (Band Leg Extension) - 대퇴사두근 강화",
                "3. 짐볼 레그 컬 (Stability Ball Leg Curl) - 슈팅 후 다리 회수력 강화"
            ],
            "웨이트 운동": [
                "1. 바벨 스쿼트 (Barbell Squat) - 전반적인 하체 파워 증대",
                "2. 레그 컬 (Leg Curl) - 킥 모션 후반부 근력 유지",
                "3. 루마니안 데드리프트 (Romanian Deadlift) - 킥 중심이 되는 후면 근육"
            ]
        },
        "코어": {
            "맨몸 운동": [
                "1. 플랭크 (Plank) - 기본 코어 안정화 및 자세 유지",
                "2. 사이드 플랭크 (Side Plank) - 몸싸움 시 버티는 측면 코어 강화",
                "3. 버드 독 (Bird Dog) - 허리 안정성과 신체 균형 감각 향상"
            ],
            "기구 운동": [
                "1. 짐볼 플랭크 (Gymball Plank) - 불안정한 상태에서의 미세 코어 자극",
                "2. 보수볼 밸런스 (BOSU Ball Balance) - 발목 및 코어 밸런스 트레이닝",
                "3. 메디신볼 트위스트 (Medicine Ball Twist) - 상체 회전 운동 및 킥 회전력"
            ],
            "웨이트 운동": [
                "1. 케이블 크런치 (Cable Crunch) - 복부 근력 및 굴곡력 강화",
                "2. 랫 풀다운 (Lat Pulldown) - 상체 프레임 유지 및 코어 안정화",
                "3. 덤벨 파머스 워크 (Farmer's Walk) - 전신 근력 및 악력, 코어 유지력"
            ]
        },
        "지구력": {
            "맨몸 운동": [
                "1. 버피 테스트 (Burpee) - 심폐 지구력 극한 강화",
                "2. 하이 니즈 (High Knees) - 빠른 페이스 유지",
                "3. 점핑잭 (Jumping Jack) - 전신 유산소 및 근지구력"
            ],
            "기구 운동": [
                "1. 로잉 머신 (Rowing Machine) - 전신 유산소 및 근지구력",
                "2. 스텝박스 오르내리기 (Step-box) - 하체 근지구력",
                "3. 실내 자전거 (Stationary Bike) - 하체 유산소 지구력"
            ],
            "웨이트 운동": [
                "1. 저중량 고반복 바벨 스쿼트 - 하체 근지구력 유지",
                "2. 케틀벨 스윙 (Kettlebell Swing) - 전신 후면 사슬 지구력",
                "3. 워킹 런지 (Walking Lunge) - 활동량 대비 피로도 감소"
            ]
        },
        "헤딩": {
            "맨몸 운동": [
                "1. 카프 레이즈 (Calf Raise) - 점프력을 위한 발목 힘 강화",
                "2. 수퍼맨 익스텐션 (Superman) - 헤딩 시 필요한 상체 후면 및 기립근",
                "3. 브릿지 (Bridge) - 엉덩이 및 허리 후면 안정화"
            ],
            "기구 운동": [
                "1. 짐볼 백 익스텐션 (Gymball Back Extension) - 허리와 등 근육 강화",
                "2. 저항 밴드 풀다운 (Resistance Band Pulldown) - 상체 후면 단련",
                "3. 메디신볼 캐치 (Medicine Ball Catch) - 공중 경합 시 상체 버팀목"
            ],
            "웨이트 운동": [
                "1. 루마니안 데드리프트 (Romanian Deadlift) - 후면 근육 전체 강화",
                "2. 랫 풀다운 (Lat Pulldown) - 점프 직전 팔과 등의 협응력",
                "3. 바벨 굿모닝 (Barbell Good Morning - 저중량) - 기립근 및 엉덩이"
            ]
        },
        "드리블": {
            "맨몸 운동": [
                "1. 토우 탭 (Toe Tap) - 발바닥 볼 감각 및 민첩한 발놀림",
                "2. 싱글 레그 밸런스 (Single Leg Balance) - 디딤발의 균형 감각",
                "3. 사이드 플랭크 (Side Plank) - 수비수와의 몸싸움 중 드리블 유지"
            ],
            "기구 운동": [
                "1. 스피드 래더 (Agility Ladder) - 현란한 발 스텝과 리듬감",
                "2. 콘 위빙 (Cone Weaving) - 지그재그 돌파 및 방향 전환",
                "3. 저항 밴드 레그 리프트 - 하체 제어력 향상"
            ],
            "웨이트 운동": [
                "1. 덤벨 런지 (Dumbbell Lunge) - 돌파 시 급가속 및 밸런스",
                "2. 케이블 우드초퍼 (Cable Woodchopper) - 회전 시 중심 잡기",
                "3. 덤벨 카프 레이즈 (Dumbbell Calf Raise) - 세밀한 발목 컨트롤"
            ]
        },
        "민첩성": {
            "맨몸 운동": [
                "1. 사이드 스텝 (Side Step) - 좌우 방향 전환 능력",
                "2. 스쿼트 점프 (Squat Jump) - 폭발적인 반응 탄력",
                "3. 마운틴 클라이머 (Mountain Climber) - 빠르고 민첩한 발놀림"
            ],
            "기구 운동": [
                "1. 허들 점프 (Hurdle Jump) - 순간 반응 및 장애물 회피",
                "2. 스피드 래더 다각도 드릴 - 복합 스텝 능력",
                "3. 리액션 볼 캐치 (Reaction Ball) - 시각 반응 및 민첩성"
            ],
            "웨이트 운동": [
                "1. 바벨 런지 (Barbell Lunge) - 방향 전환 시 하체 지지력",
                "2. 케틀벨 스윙 (Kettlebell Swing) - 신체 중심 이동 능력",
                "3. 덤벨 스쿼트 (Dumbbell Squat) - 하체 반응 속도"
            ]
        },
        "속도": {
            "맨몸 운동": [
                "1. 숏 스프린트 (Short Sprint) - 순간 가속 및 최대 속도 도달",
                "2. A-마치 (A-March) - 주법 교정 및 무릎 올리기",
                "3. 하이 니즈 스프린트 (High Knees Sprint) - 피치 속도 향상"
            ],
            "기구 운동": [
                "1. 저항 밴드 스프린트 (Resistance Band Sprint) - 가속 구간 파워 강화",
                "2. 스피드 래더 패스트 스텝 - 발 구름 속도 극대화",
                "3. 슬레드 푸시 (Sled Push - 가벼운 무게) - 폭발적인 전방 밀기 속도"
            ],
            "웨이트 운동": [
                "1. 덤벨 스쿼트 점프 (Dumbbell Squat Jump) - 폭발적인 추진력 증대",
                "2. 파워 클린 (Power Clean - 유소년용 저중량) - 전신 폭발력",
                "3. 바벨 런지 (Barbell Lunge) - 스트라이드(보폭) 확장"
            ]
        }
    }

    print("⚽ 유소년 축구 선수 단점 극복 트레이닝 추천 프로그램 ⚽\n")
    print("선택 가능한 단점 키워드:")
    print(list(exercise_database.keys()))
    print("-" * 50)
    
    # 사용자 입력 받기
    user_input = input("\n개선하고 싶은 선수의 단점을 입력해주세요: ").strip()

    if user_input in exercise_database:
        print(f"\n[분석 결과] '{user_input}' 개선을 위한 맞춤형 운동 루틴입니다!\n")
        
        # 맨몸, 기구, 웨이트 운동 3가지씩 출력
        for category, exercises in exercise_database[user_input].items():
            print(f"--- {category} (3가지) ---")
            for ex in exercises:
                print(f"  • {ex}")
            print()
    else:
        print(f"\n❌ 등록되지 않은 단점입니다. 위 목록에 있는 단점 중 하나를 정확히 입력해주세요.")

# 프로그램 실행
if __name__ == "__main__":
    recommend_soccer_exercises()
