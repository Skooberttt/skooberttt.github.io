@echo off
REM ───────── Activate venv ─────────
call "%~dp0venv\Scripts\activate"

REM ───────── Generate post ──────────
python "%~dp0generate_post.py"

REM ───────── Git operations ─────────
cd "%~dp0"

REM Stage any new posts or runner changes
git add posts generate_post.py run_daily.bat

REM If there are staged changes, commit & push
git diff --cached --quiet || (
  git commit -m "📝 Auto-post %date%"
  git push
) 

REM Done
exit /b 0
