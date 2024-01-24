class zerozeroseven:
    def __init__(self, secret_code, meeting_point, time):
        self.secret_code = secret_code
        self.meeting_point = meeting_point
        self.time = time

secret_code, meeting_point, time = list(map(str, input().split()))
zerozeroseven_object = zerozeroseven(secret_code, meeting_point, time)

print(f'secret code : {zerozeroseven_object.secret_code}')
print(f'meeting point : {zerozeroseven_object.meeting_point}')
print(f'time : {zerozeroseven_object.time}')