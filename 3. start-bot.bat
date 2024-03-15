@echo off

REM Definir la ruta del script actual
set "script_path=%~dp0"

REM Activar el entorno virtual (Windows)
call "%script_path%venv\Scripts\activate"

REM Cambiar al directorio del bot
cd "%script_path%REST_API_BOT"

REM Iniciar el bot de Discord
python "rest-api-bot.py" run

REM Desactivar el entorno virtual
deactivate
