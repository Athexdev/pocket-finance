@echo off
echo.
echo ============================================
echo   🚀 Pushing Pocket Finance to GitHub...
echo ============================================
echo.

:: Initialize Git if not already done
if not exist .git (
    echo [1/6] Initializing local repository...
    git init
) else (
    echo [1/6] Git repository already initialized.
)

:: Add files
echo [2/6] Staging project files...
git add .

:: Commit
echo [3/6] Committing changes...
git commit -m "feat: initial commit for Pocket Finance via Antigravity"

:: Set branch
echo [4/6] Setting branch to main...
git branch -M main

:: Add remote
echo [5/6] Adding remote origin...
git remote add origin https://github.com/Athexdev/pocket-finance.git 2>nul
if %errorlevel% neq 0 (
    echo [!] Remote origin already exists. Updating it...
    git remote set-url origin https://github.com/Athexdev/pocket-finance.git
)

:: Push
echo [6/6] Pushing to GitHub (this may open a login window)...
git push -u origin main

echo.
echo ============================================
echo   ✅ SUCCESS! Your project should be live.
echo ============================================
echo.
pause
