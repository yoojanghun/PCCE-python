# join: 문자 합치기
text = ["Monday", "Friday", "Saturday"]
print("".join(text))
print("    ".join(text))
print("::::".join(text))

# strip: 공백 문자 자르기 strip, lstrip, rstrip
text = "          안녕하세요?  만나서 반갑     습니다.       "
print(text.strip())
print(text.rstrip())
print(text.lstrip())