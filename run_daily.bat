@echo off
REM — activate your venv
call "%~dp0venv\Scripts\activate"

REM — generate a new post
python "%~dp0generate_post.py"

REM — commit & push to GitHub (so your Pages site stays up-to-date)
cd "%~dp0"
git add posts/
git commit -m "📝 Auto-post %date%"
git push

REM — done
exit /b 0
