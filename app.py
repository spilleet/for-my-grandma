from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# 하드코딩된 사용자 정보 예시
auth_users = {
    'admin': {'pw': 'password', 'phone': '010-1234-5678'}
}

# 경기 매치, 경기장 정보를 담을 리스트
matches = []    # {'name','date','location','team1','team2'}
stadiums = []   # {'name','location','capacity'}

# --- 로그인 페이지 (GET) ---
@app.route('/', methods=['GET'])
def login_page():
    return render_template('login.html')

# --- 로그인 처리 (POST) ---
@app.route('/login', methods=['POST'])
def do_login():
    user_id = request.form.get('login-id')
    pw      = request.form.get('login-pw')
    user = auth_users.get(user_id)
    if user and user['pw'] == pw:
        session['user'] = user_id
        return redirect(url_for('dashboard'))
    flash('아이디 또는 비밀번호가 올바르지 않습니다.')
    return redirect(url_for('login_page'))

# --- 대시보드 페이지 (GET) ---
@app.route('/dashboard', methods=['GET'])
def dashboard():
    if 'user' not in session:
        flash('로그인 후 접근 가능합니다.')
        return redirect(url_for('login_page'))
    return render_template('dashboard.html', user=session['user'], matches=matches)

# --- 경기 매치 신청 페이지 (GET+POST) ---
@app.route('/match', methods=['GET', 'POST'])
def match_register():
    if 'user' not in session:
        flash('로그인 후 접근 가능합니다.')
        return redirect(url_for('login_page'))

    if request.method == 'POST':
        name     = request.form.get('match-name')
        date     = request.form.get('match-date')
        location = request.form.get('match-location')
        team1    = request.form.get('match-team1')
        team2    = request.form.get('match-team2')

        if not all([name, date, location, team1, team2]):
            flash('모든 항목을 입력해주세요.')
            return redirect(url_for('match_register'))

        matches.append({
            'name': name,
            'date': date,
            'location': location,
            'team1': team1,
            'team2': team2
        })
        flash(f'경기 "{name}" 등록 완료.')
        return redirect(url_for('dashboard'))

    return render_template('match.html')

# --- 경기장 등록 페이지 (GET+POST) ---
@app.route('/stadium/register', methods=['GET', 'POST'])
def stadium_register():
    if 'user' not in session:
        flash('로그인 후 접근 가능합니다.')
        return redirect(url_for('login_page'))

    if request.method == 'POST':
        name     = request.form.get('stadium-name')
        location = request.form.get('stadium-location')
        capacity = request.form.get('stadium-capacity')

        if not all([name, location, capacity]):
            flash('모든 항목을 입력해주세요.')
            return redirect(url_for('stadium_register'))

        stadiums.append({
            'name': name,
            'location': location,
            'capacity': capacity
        })
        flash(f'경기장 "{name}" 등록 완료.')
        return redirect(url_for('dashboard'))

    return render_template('stadium.html')

# --- 경기 목록 보기 페이지 (GET) ---
@app.route('/matches', methods=['GET'])
def view_matches():
    if 'user' not in session:
        flash('로그인 후 접근 가능합니다.')
        return redirect(url_for('login_page'))

    return render_template('matches.html', matches=matches)

# --- 로그아웃 ---
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login_page'))

# --- 서버 실행 진입점 ---
if __name__ == '__main__':
    # 개발 중 debug=True, 배포 시 False로 변경하세요
    app.run(debug=True, host='0.0.0.0', port=5000)


