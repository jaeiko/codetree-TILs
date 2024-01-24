# WeatherData 클래스
class WeatherData:
    def __init__(self, day, date, weather):
        self.date = date        # 날짜
        self.day = day          # 요일
        self.weather = weather  # 날씨

# 날씨 데이터 입력 횟수
n = int(input())

# 년도, 월, 일, 날짜,데이터 설정 함수
def set_data(year, month, day, week, weather):
    return (int(year), int(month), int(day), week, weather)

key = 'off'

for i in range(n):
    date, week, weather = list(map(str, input().split()))    # 날짜, 요일, 날씨 데이터 입력
    if weather != 'Rain':   # 들어온 날씨 데이터가 Rain이 아니면 패스
        continue
    year, month, day = date.split('-')  # 년도, 월, 일을 '-' 기준으로 분리 : 날짜 비교를 위해서
    if key == 'off':    # 날씨가 Rain으로 들어온 데이터가 처음이라면 해당 데이터를 pre_year, pre_month, pre_day, pre_week, pre_weather에 저장하며 초기값 설정
        pre_year, pre_month, pre_day, pre_week, pre_weather = set_data(year, month, day, week, weather)
        key = 'on'  # on으로 바꾸어 두번째 Rain으로 들어오는 데이터는 아래 조건식으로
    else:
        if pre_year > int(year):    # 현 반복문의 year이 이전에 저장된 pre_year보다 작으면 데이터 새로 갱신
            pre_year, pre_month, pre_day, pre_week, pre_weather = set_data(year, month, day, week, weather)
        elif pre_year == int(year):
            if pre_month > month:   # 현 반복문의 year이 이전에 저장된 pre_year과 같고, month가 pre_month보다 작으면 데이터 새로 갱신
                pre_year, pre_month, pre_day, pre_week, pre_weather = set_data(year, month, day, week, weather)
            elif pre_month == int(month) and pre_day >= int(day):   # 현 반복문의 year, month가 이전에 저장된 pre_year, pre_month과 같고, day가 pre_day보다 작으면 데이터 새로 갱신
                pre_year, pre_month, pre_day, pre_week, pre_weather = set_data(year, month, day, week, weather)

if len(str(pre_month)) == 1:    # 만약 월이 1~9라면 앞에 0을 붙여서 형식대로 출력하도록 조건문 설정
    pre_month = '0' + str(pre_month)

# 출력
print(f'{pre_year}-{pre_month}-{pre_day} {pre_week} {pre_weather}')