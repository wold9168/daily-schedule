# 定义变量
SCRIPT_NAME=daily-schedule.py
INSTALLED_NAME=daily-schedule
INSTALL_DIR=$(HOME)/.local/bin

.PHONY: install uninstall

# 默认目标：安装脚本
install:
	@mkdir -p $(INSTALL_DIR)
	@cp $(SCRIPT_NAME) $(INSTALL_DIR)
	@mv $(INSTALL_DIR)/$(SCRIPT_NAME) $(INSTALL_DIR)/$(INSTALLED_NAME)
	@chmod +x $(INSTALL_DIR)/$(INSTALLED_NAME)
	@echo "Installed $(INSTALLED_NAME) to $(INSTALL_DIR)"

# 卸载目标：删除脚本
uninstall:
	@if [ -f $(INSTALL_DIR)/$(INSTALLED_NAME) ]; then \
		rm $(INSTALL_DIR)/$(INSTALLED_NAME); \
		echo "Uninstalled $(INSTALLED_NAME) from $(INSTALL_DIR)"; \
	else \
		echo "$(INSTALLED_NAME) not found in $(INSTALL_DIR)"; \
	fi
