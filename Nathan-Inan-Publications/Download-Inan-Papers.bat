@echo off
REM Double-click this file to download Nathan (Nader A.) Inan's publications.
REM It runs download_inan_papers.ps1, which must sit in the same folder.
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0download_inan_papers.ps1"
