IP_ADDR := recalbox.local
USER := root
TARGET_DIR := /recalbox/share/system
ROMS_DIR := /recalbox/share/roms

.PHONY: deploy deploy-roms logs restart

deploy:
	@echo "Syncing config to $(IP_ADDR)..."
	rsync -avz --progress ./config/recalbox.conf $(USER)@$(IP_ADDR):$(TARGET_DIR)/recalbox.conf
	@echo "Config synced."

deploy-roms:
	@echo "Syncing favorites to $(IP_ADDR)..."
	rsync -avz --progress ./roms/favorites/ $(USER)@$(IP_ADDR):$(ROMS_DIR)/favorites/

restart:
	ssh $(USER)@$(IP_ADDR) "/etc/init.d/S31emulationstation restart"

logs:
	ssh $(USER)@$(IP_ADDR) "tail -f /recalbox/share/system/logs/es_system.log"
