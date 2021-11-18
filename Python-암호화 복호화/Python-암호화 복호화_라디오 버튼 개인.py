# 개인적으로 현재 작성중인 암호화 복호화 GUI 중 라디오 버튼에 해당하는 코드 일부분

# 암호화 복호화 선택 프레임
# 버튼_프레임명 = Frame(클래스_객체명)
버튼_프레임명.pack()

버튼명1 = Radiobutton(프레임 또는 객체명(위치), text="표시할 문자열", value=값)

# 버튼명1을 기본적적으로 선택되게끔 지정, 해당 코드가 없으면 기본값이 전체 선택인 것을 볼 수 있음.
버튼명1.select()

# padx = 라디오 버튼 테두리 및 내용 가로 여백
# pady = 라디오 버튼 테두리 및 내용 세로 여백
버튼명1.pack(padx=5, pady=5)

##############################

# 암호화 복호화 선택 프레임
btn_frame = Frame(root)
btn_frame.pack(fill="x", padx=5, pady=5)
btn1 = Radiobutton(btn_frame, text="암호화", value="암호화")
btn1.select()
btn1.pack(padx=5, pady=5)
btn2 = Radiobutton(btn_frame, text="복호화", value="복호화", variable=btn_var)
btn2.pack(padx=5, pady=5)
