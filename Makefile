# ─────────────────────────────────────────────────────────────────────────────
# Makefile — Curso de Ciencia de Datos · Tecmilenio
# Uso: make <comando> [N=<número>] [PKG=<paquete>] [SEMANA=<semanaX>]
# ─────────────────────────────────────────────────────────────────────────────

.DEFAULT_GOAL := help

SEMANAS_DIR  := semanas
PACKAGES_DIR := packages
UV           := uv

# ─── Colores ANSI ────────────────────────────────────────────────────────────
BLUE   := \033[0;34m
GREEN  := \033[0;32m
YELLOW := \033[1;33m
CYAN   := \033[0;36m
RESET  := \033[0m

# ─── Ayuda ───────────────────────────────────────────────────────────────────
.PHONY: help
help: ## Muestra todos los comandos disponibles
	@printf "\n  $(CYAN)Curso de Ciencia de Datos$(RESET) — Comandos disponibles\n\n"
	@grep -E '^[a-zA-Z%_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "  $(GREEN)%-28s$(RESET) %s\n", $$1, $$2}'
	@printf "\n"

# ─── Workspace ───────────────────────────────────────────────────────────────
.PHONY: install
install: ## Instala todas las dependencias del workspace
	$(UV) sync --all-packages

.PHONY: sync
sync: ## Sincroniza el entorno virtual con el lock file actual
	$(UV) sync

.PHONY: lock
lock: ## Actualiza uv.lock sin instalar paquetes
	$(UV) lock

# ─── Semanas (reglas de patrón) ───────────────────────────────────────────────
.PHONY: jupyter-%
jupyter-%: ## Abre Jupyter Notebook para una semana  (ej: make jupyter-semana1)
	$(UV) run --package $* jupyter notebook $(SEMANAS_DIR)/$*/

.PHONY: run-%
run-%: ## Ejecuta el script principal de una semana  (ej: make run-semana1)
	$(UV) run --package $* python $(SEMANAS_DIR)/$*/main.py

# ─── Nueva semana ────────────────────────────────────────────────────────────
.PHONY: new-semana
new-semana: ## Crea la estructura de una nueva semana  (ej: make new-semana N=2)
	@[ -n "$(N)" ] || { printf "$(YELLOW)Error:$(RESET) Especifica el número de semana: make new-semana N=2\n"; exit 1; }
	@[ ! -d "$(SEMANAS_DIR)/semana$(N)" ] || { printf "$(YELLOW)Aviso:$(RESET) semana$(N) ya existe, omitiendo.\n"; exit 0; }
	@mkdir -p $(SEMANAS_DIR)/semana$(N)/actividad \
	           $(SEMANAS_DIR)/semana$(N)/complementarios/actividades
	@printf '[project]\nname = "semana$(N)"\nversion = "0.1.0"\ndescription = "Semana $(N)"\nrequires-python = ">=3.11"\ndependencies = []\n' \
		> $(SEMANAS_DIR)/semana$(N)/pyproject.toml
	@printf '# Semana $(N)\n\n## Actividades Completadas\n\n- [ ] Actividad $(N).1\n\n## Aprendido\n\n## Commits Realizados\n' \
		> $(SEMANAS_DIR)/semana$(N)/CONSOLIDADO.md
	$(UV) sync
	@printf "$(GREEN)✓$(RESET) Semana $(N) creada en $(SEMANAS_DIR)/semana$(N)/\n"
	@printf "  Agrega dependencias con: $(CYAN)make add-dep SEMANA=semana$(N) PKG=<paquete>$(RESET)\n\n"

# ─── Gestión de dependencias ─────────────────────────────────────────────────
.PHONY: add-dep
add-dep: ## Agrega una dependencia a una semana  (ej: make add-dep SEMANA=semana2 PKG=pymongo)
	@[ -n "$(PKG)" ]    || { printf "$(YELLOW)Error:$(RESET) Especifica el paquete:  make add-dep SEMANA=<semanaX> PKG=<paquete>\n"; exit 1; }
	@[ -n "$(SEMANA)" ] || { printf "$(YELLOW)Error:$(RESET) Especifica la semana:   make add-dep SEMANA=<semanaX> PKG=<paquete>\n"; exit 1; }
	$(UV) add --package $(SEMANA) $(PKG)

.PHONY: add-ws-dep
add-ws-dep: ## Agrega un paquete interno a una semana  (ej: make add-ws-dep SEMANA=semana2 PKG=ds-mongo)
	@[ -n "$(PKG)" ]    || { printf "$(YELLOW)Error:$(RESET) Especifica el paquete interno:  PKG=ds-mongo | PKG=ds-postgres\n"; exit 1; }
	@[ -n "$(SEMANA)" ] || { printf "$(YELLOW)Error:$(RESET) Especifica la semana:           SEMANA=<semanaX>\n"; exit 1; }
	$(UV) add --package $(SEMANA) $(PKG) --editable ./$(PACKAGES_DIR)/$(PKG)

.PHONY: list
list: ## Lista todas las semanas disponibles en el workspace
	@printf "\n  $(CYAN)Semanas disponibles:$(RESET)\n"
	@ls -d $(SEMANAS_DIR)/semana* 2>/dev/null \
		| xargs -I{} basename {} \
		| while IFS= read -r s; do printf "  $(GREEN)•$(RESET) $$s\n"; done || printf "  (ninguna)\n"
	@printf "\n"

# ─── Limpieza ────────────────────────────────────────────────────────────────
.PHONY: clean
clean: ## Elimina archivos de caché (.pyc, __pycache__, .ipynb_checkpoints)
	@find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	@find . -type d -name .ipynb_checkpoints -exec rm -rf {} + 2>/dev/null || true
	@find . -name "*.pyc" -delete 2>/dev/null || true
	@printf "$(GREEN)✓$(RESET) Caché eliminado\n"

.PHONY: clean-venv
clean-venv: clean ## Elimina caché Y el entorno virtual (.venv) — requiere 'make install' después
	@rm -rf .venv
	@printf "$(GREEN)✓$(RESET) Entorno virtual eliminado. Ejecuta '$(CYAN)make install$(RESET)' para reconstruirlo.\n"
