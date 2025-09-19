ifeq ($(OS),Windows_NT)
  SHELL := cmd
  .SHELLFLAGS := /C
  PY := python
  PYBIN := .venv\Scripts\python.exe
else
  SHELL := bash
  .SHELLFLAGS := -eu -o pipefail -c
  PY := python3
  PYBIN := .venv/bin/python
endif

.PHONY: setup be fe dev clean

setup:
	$(PY) -m venv .venv
	"$(PYBIN)" -m pip install -r backend/requirements.txt
	cd frontend && npm i --silent

be:
	"$(PYBIN)" -m uvicorn backend.main:app --host 127.0.0.1 --port 8000

fe:
	cd frontend && npm run dev

dev:
	$(MAKE) -j2 be fe

clean:
ifeq ($(OS),Windows_NT)
	@if exist .venv rmdir /s /q .venv
	@if exist frontend\node_modules rmdir /s /q frontend\node_modules
else
	rm -rf .venv frontend/node_modules
endif