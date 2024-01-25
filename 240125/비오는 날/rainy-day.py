# WeatherData 클래스
class WeatherData:
    def __init__(self, date, week, weather):
        self.date = date        # 날짜
        self.week = week          # 요일
        self.weather = weather  # 날씨

# 날씨 데이터 입력 횟수
n = int(input())

# WeatherData 객체를 담을 data_list
data_list = []

for i in range(n):
    date, week, weather = list(map(str, input().split(' ')))    # 날짜, 요일, 날씨 데이터 입력
    if weather != 'Rain':   # 들어온 날씨 데이터가 Rain이 아니면 패스
        continue
    data_list.append(WeatherData(date, week, weather))  # 입력받은 date, week, weather를 담은 Weather 객체를 data_list에 추가

# 우선 순위 1. 년도 빠른 순 / 2. 월 빠른 순 / 3. 일 빠른 순 으로 정렬
sorted_data_list = sorted(data_list, key=lambda x : (int(x.date[0:4]), int(x.date[5:7]), int(x.date[8:10])))

# 출력
print(f'{data_list[0].date[0:4]}-{data_list[0].date[5:7]}-{data_list[0].date[8:10]} {data_list[0].week} {data_list[0].weather}')